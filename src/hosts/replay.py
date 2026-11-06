"""Full-batch descriptor gradients with BF16 chunk replay (CUDA)."""
import torch
CHUNK=8
def rng():return (torch.get_rng_state(),torch.cuda.get_rng_state_all())
def setrng(s):torch.set_rng_state(s[0]);torch.cuda.set_rng_state_all(s[1])
def cached(m,x):
    outputs=[];states=[]
    with torch.no_grad():
        for z in x.split(CHUNK):
            states.append(rng())
            with torch.autocast('cuda',dtype=torch.bfloat16):y=m(img1=z.cuda())
            outputs.append(y.float())
    return torch.cat(outputs).detach().requires_grad_(),states
def replay(m,x,states,g):
    after=rng()
    try:
        for z,s,d in zip(x.split(CHUNK),states,g.split(CHUNK)):
            setrng(s)
            with torch.autocast('cuda',dtype=torch.bfloat16):h=m(img1=z.cuda())
            (h.float()*d).sum().backward()
    finally:setrng(after)
