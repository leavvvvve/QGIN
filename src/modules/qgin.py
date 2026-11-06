"""QGIN: spatially shared random pointwise convolutions with quantile hinges.

network accepts one image and explicit frozen random parameters. Its FP32
arithmetic is preserved from the evaluated implementation. No learned state is
added to the retrieval encoder. Input/output range is [-1, 1].
"""
import torch
import torch.nn.functional as F

def sample(seed, quantile_seed=None):
    """Independent local CPU generators leave training RNG state unchanged."""
    g = torch.Generator(device='cpu').manual_seed(int(seed))
    layers = [(torch.randn(b,a,1,1,generator=g),torch.randn(b,generator=g))
              for a,b in zip([3,2,2,2],[2,2,2,3])]
    weight = .35 + .5 * torch.rand((),generator=g)
    q = torch.Generator(device='cpu').manual_seed(int((seed ^ 0x5F3759DF) if quantile_seed is None else quantile_seed))
    return dict(layers=layers,w=weight), .25 + .5*torch.rand(3,2,generator=q)

def quantile(z,p):
    # Exact sorted order statistics, torchvision/PyTorch linear interpolation convention.
    flat=z.flatten(2);v=flat.sort(-1).values;rank=p.to(z.device).reshape(1,-1,1)*(flat.shape[-1]-1);lo=rank.floor().long();hi=rank.ceil().long();a=v.gather(-1,lo);b=v.gather(-1,hi)
    return torch.lerp(a,b,rank-lo).reshape(1,z.shape[1],1,1)
@torch.no_grad()
def _network_fp32(x,param,p=None,audit=False):
    assert x.ndim == 4 and x.shape[0] == 1 and x.shape[1] == 3
    z=x.float();layers=[];fallback=0
    for layer,(w,b) in enumerate(param['layers']):
        linear=F.conv2d(z,w.to(z.device),None);bias=b.to(z.device).reshape(1,-1,1,1)
        if layer<3:
            sigma=linear.std(dim=(-2,-1),correction=0,keepdim=True)
            if p is not None:
                tau=quantile(linear,p[layer]);bad=sigma<1e-6;pre=torch.where(bad,linear+bias,(linear-tau)/(sigma+1e-6));fallback+=int(bad.sum())
            else:pre=F.conv2d(z,w.to(z.device),b.to(z.device));bad=torch.zeros_like(sigma,dtype=torch.bool);tau=torch.zeros_like(sigma)
            z=F.leaky_relu(pre,.01)
            if audit:
                for channel in range(z.shape[1]):
                    fplus=float((pre[0,channel]>0).float().mean());layers.append(dict(layer=layer+1,channel=channel,f_plus=fplus,hinge_miss=int(fplus>.99 or fplus<.01),active_hinge=int(.20<=fplus<=.80),linear_std=float(sigma[0,channel]),post_std=float(z[0,channel].std(correction=0)),threshold=float(tau[0,channel]),fallback=int(bad[0,channel])))
        else:z=F.conv2d(z,w.to(z.device),b.to(z.device))
    y=z;yn=y.norm();bad=not bool(torch.isfinite(y).all()) or not bool(torch.isfinite(yn)) or float(yn)<1e-6;yf=x if bad else y*(x.norm()/yn.clamp_min(1e-6));pre=(1-param['w'].to(x.device))*x+param['w'].to(x.device)*yf;out=x if bad else pre.clamp(-1,1)
    mu=y.mean((-2,-1),keepdim=True);dc=float(x.shape[-1]*x.shape[-2]*mu.square().sum()/(y.square().sum()+1e-6));rec=dict(channel_fallback=fallback,identity_fallback=int(bad),DC_share=dc,AC_share=1-dc,raw_norm=float(yn),clip_fraction=float((pre.abs()>1).float().mean()),output_std=float(out.std(correction=0)))
    return out,layers,rec

@torch.no_grad()
def augment_batch(x, parameters, quantiles):
    """Explicit per-image parameters support exact augmentation replay."""
    assert len(x) == len(parameters) == len(quantiles)
    with torch.autocast(device_type=x.device.type, enabled=False):
        return torch.cat([network(x[i:i+1].float(),p,q)[0]
                          for i,(p,q) in enumerate(zip(parameters,quantiles))])

@torch.no_grad()
def network(x, param, p=None, audit=False):
    """Disable ambient autocast before every nonlinear convolution and norm."""
    with torch.autocast(device_type=x.device.type, enabled=False):
        return _network_fp32(x.float(), param, p, audit)
