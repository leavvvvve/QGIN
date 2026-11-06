"""Cached augmentation parameters and scalar affine controls."""
import torch
from .qgin import network


def unpack(rows):
    result = []
    for row in rows:
        layers, j = [], 0
        for a, b in zip([3, 2, 2, 2], [2, 2, 2, 3]):
            w = row[j:j+a*b].reshape(b, a, 1, 1); j += a*b
            bias = row[j:j+b]; j += b
            layers.append((w, bias))
        result.append(dict(layers=layers, w=row[j]))
    return result


@torch.no_grad()
def secondary(x, method, indices, parameters, device='cuda'):
    """parameters: packed [N,30], p [N,3,2], std [N,2], seeds [N]."""
    if 'StdDual' in method:
        p = parameters['std'][indices].float().reshape(-1, 2, 1, 1, 1)
        return (((x.float()+1)/2*p[:, 0]+p[:, 1]).clamp(0, 1)*2-1)
    if 'ColorJitter' in method or 'AugMix' in method:
        import torchvision.transforms as T
        transform = (T.ColorJitter(.4, .4, .4, .1) if 'ColorJitter' in method else
                     T.AugMix(severity=3, mixture_width=3, chain_depth=-1, alpha=1., all_ops=True,
                              interpolation=T.InterpolationMode.BILINEAR, fill=0))
        result = []
        for image, seed in zip(x, parameters['seeds'][indices]):
            with torch.random.fork_rng(devices=[]):
                torch.random.default_generator.manual_seed(int(seed))
                rgb = ((image.float()+1)/2).clamp(0, 1)
                y = transform(rgb) if 'ColorJitter' in method else transform(torch.round(rgb*255).to(torch.uint8)).float()/255
                result.append(y*2-1)
        return torch.stack(result)
    result = []
    for j, p in enumerate(unpack(parameters['packed'][indices])):
        quantiles = None if method == 'FixedZeroHinge' else parameters['p'][int(indices[j])]
        with torch.autocast(device_type=device, enabled=False):
            result.append(network(x[j:j+1].to(device).float(), p, quantiles)[0].cpu())
    return torch.cat(result)
