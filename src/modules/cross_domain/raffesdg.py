"""Taskbook's high-pass FreeAug-style two-view radial mixing adaptation."""

import math
import torch


def apply(x, gen):
    if x.ndim == 4:
        return torch.stack([apply(item, gen) for item in x])
    c, h, w = x.shape
    spectrum = torch.fft.fftshift(torch.fft.fft2(x, dim=(-2, -1)), dim=(-2, -1))
    yy = torch.arange(-(h // 2), h - (h // 2), device=x.device, dtype=torch.float32)[
        :, None
    ]
    xx = torch.arange(-(w // 2), w - (w // 2), device=x.device, dtype=torch.float32)[
        None, :
    ]
    dist = torch.sqrt(yy.square() + xx.square())
    rmax = math.sqrt((h / 2) ** 2 + (w / 2) ** 2)

    def filtered():
        d0 = torch.empty((c, 1, 1), device=x.device).uniform_(
            1e-4, 0.04 * rmax, generator=gen
        )
        order = torch.randint(1, 4, (c, 1, 1), device=x.device, generator=gen).float()
        eta = 1 / (1 + (d0 / (dist.unsqueeze(0) + 1e-6)) ** (2 * order))
        y = torch.fft.ifft2(
            torch.fft.ifftshift(spectrum * eta, dim=(-2, -1)), dim=(-2, -1)
        ).real
        ymin, ymax = y.amin((-2, -1), keepdim=True), y.amax((-2, -1), keepdim=True)
        return (y - ymin) / (ymax - ymin + 1e-6)

    a, b = filtered(), filtered()
    ch = torch.empty(1, device=x.device).uniform_(0, h, generator=gen)
    cw = torch.empty(1, device=x.device).uniform_(0, w, generator=gen)
    gy = torch.arange(h, device=x.device, dtype=torch.float32)[:, None]
    gx = torch.arange(w, device=x.device, dtype=torch.float32)[None, :]
    radial = torch.sqrt((gy - ch) ** 2 + (gx - cw) ** 2)
    mask = (radial / (radial.amax() + 1e-6)).unsqueeze(0)
    return (mask * a + (1 - mask) * b).clamp(0, 1)
