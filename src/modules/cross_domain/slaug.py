"""Taskbook's GLA-only Bezier and bounded truncated-normal adaptation."""

import torch


def apply(x, gen):
    if x.ndim == 4:
        return torch.stack([apply(item, gen) for item in x])
    assert x.ndim == 3 and x.shape[0] == 3
    lo, hi = x.amin(), x.amax()
    x = ((x - lo) / (hi - lo + 1e-6)).clamp(0, 1)
    p = torch.rand(4, generator=gen, device=x.device, dtype=torch.float32)
    x1, x2 = torch.minimum(p[0], p[1]), torch.maximum(p[0], p[1])
    y1, y2 = torch.minimum(p[2], p[3]), torch.maximum(p[2], p[3])
    t = torch.linspace(0, 1, 1024, device=x.device, dtype=torch.float32)
    z = 1 - t
    xl = 3 * z * z * t * x1 + 3 * z * t * t * x2 + t * t * t
    yl = 3 * z * z * t * y1 + 3 * z * t * t * y2 + t * t * t
    xl[0], xl[-1] = 0, 1
    yl[0], yl[-1] = 0, 1
    flat = x.reshape(-1).contiguous()
    i = torch.searchsorted(xl, flat).clamp(1, 1023)
    w = (flat - xl[i - 1]) / (xl[i] - xl[i - 1] + 1e-8)
    curve = (yl[i - 1] + w * (yl[i] - yl[i - 1])).reshape_as(x)
    a, b = torch.empty(1, device=x.device), torch.empty(1, device=x.device)
    torch.nn.init.trunc_normal_(a, mean=1.0, std=0.1, a=0.8, b=1.2, generator=gen)
    torch.nn.init.trunc_normal_(b, mean=0.0, std=0.5, a=-0.5, b=0.5, generator=gen)
    return (a * curve + b).clamp(0, 1)
