"""Taskbook's resolution-adjusted AFA-style planar-wave perturbation."""
import math
import torch


def apply(x, gen):
    if x.ndim == 4:
        return torch.stack([apply(item, gen) for item in x])
    c, h, w = x.shape
    v = torch.linspace(-.5, .5, h, device=x.device)[:, None]
    u = torch.linspace(-.5, .5, w, device=x.device)[None, :]
    freq = torch.empty((c, 1, 1), device=x.device).uniform_(1, float(h), generator=gen)
    theta = torch.empty((c, 1, 1), device=x.device).uniform_(0, math.pi, generator=gen)
    uniform = torch.empty((c, 1, 1), device=x.device).uniform_(1e-6, 1, generator=gen)
    strength = -.05*torch.log(uniform)
    waves = torch.sin(2*math.pi*freq*(u.unsqueeze(0)*theta.cos()+v.unsqueeze(0)*theta.sin())-math.pi/4)
    rms = torch.sqrt(waves.square().mean(dim=(-2, -1), keepdim=True)+1e-8)
    return (x + strength*waves/rms).clamp(0, 1)
