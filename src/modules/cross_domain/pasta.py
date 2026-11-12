"""Taskbook's PASTA-like clipped spectral magnitude perturbation."""
import torch


def apply(x, gen):
    if x.ndim == 4:
        return torch.stack([apply(item, gen) for item in x])
    _, h, w = x.shape
    f = torch.fft.fft2(x, dim=(-2, -1))
    amp = torch.fft.fftshift(f.abs(), dim=(-2, -1))
    yy = torch.arange(-(h//2), h-(h//2), device=x.device, dtype=torch.float32)[:, None]
    xx = torch.arange(-(w//2), w-(w//2), device=x.device, dtype=torch.float32)[None, :]
    radius = torch.sqrt((yy**2 + xx**2) / float(h*h+w*w))
    sigma = (6*radius)**2 + .25
    noise = torch.randn(amp.shape, generator=gen, device=x.device, dtype=torch.float32)
    amp = torch.fft.ifftshift(amp*(1+noise*sigma.unsqueeze(0)).clamp_min(0), dim=(-2, -1))
    out = torch.fft.ifft2(torch.polar(amp, f.angle()), dim=(-2, -1)).real
    return out.nan_to_num(nan=0, posinf=1, neginf=0).clamp(0, 1)
