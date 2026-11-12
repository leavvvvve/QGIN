"""EXP-003K held-out affine residuals and pointwise RGB edge diagnostics."""
import cv2
import numpy as np
from src.modules.cross_domain import seed_for


def diagnostics(x, y, key, group):
    """Measure one pair of HWC float32 RGB images using the recorded pixel seed."""
    assert x.shape == y.shape and x.ndim == 3 and x.shape[2] == 3
    assert x.dtype == y.dtype == np.float32 and x.shape[0] * x.shape[1] >= 4096
    seed = seed_for(3005, 'fit-pixels', group, key)
    gen = np.random.default_rng(seed)
    ix = gen.choice(x.shape[0] * x.shape[1], 4096, replace=False)
    xf, yf = x.reshape(-1, 3)[ix[:2048]], y.reshape(-1, 3)[ix[:2048]]
    xe, ye = x.reshape(-1, 3)[ix[2048:]], y.reshape(-1, 3)[ix[2048:]]
    pred1 = np.empty_like(ye, dtype=np.float64)
    for ch in range(3):
        design = np.column_stack((xf[:, ch], np.ones(len(xf))))
        coef = np.linalg.lstsq(design, yf[:, ch], rcond=None)[0]
        pred1[:, ch] = np.column_stack((xe[:, ch], np.ones(len(xe)))) @ coef
    design = np.column_stack((xf, np.ones(len(xf))))
    coef = np.linalg.lstsq(design, yf, rcond=None)[0]
    pred2 = np.column_stack((xe, np.ones(len(xe)))) @ coef
    delta = y.astype(np.float64) - x.astype(np.float64)
    means = delta.mean(axis=(0, 1), keepdims=True)
    dc = float(delta.shape[0] * delta.shape[1] * np.square(means).sum())
    ac = float(np.square(delta - means).sum())
    energy = dc + ac
    gx = np.stack([cv2.Sobel(x, cv2.CV_32F, 1, 0), cv2.Sobel(x, cv2.CV_32F, 0, 1)], axis=-1).reshape(*x.shape[:2], 6)
    gy = np.stack([cv2.Sobel(y, cv2.CV_32F, 1, 0), cv2.Sobel(y, cv2.CV_32F, 0, 1)], axis=-1).reshape(*x.shape[:2], 6)
    nx, ny = np.linalg.norm(gx, axis=-1), np.linalg.norm(gy, axis=-1)
    valid = (nx > 1e-6) & (ny > 1e-6)
    cos = np.zeros_like(nx)
    cos[valid] = (gx[valid] * gy[valid]).sum(axis=-1) / (nx[valid] * ny[valid])
    return {'E1_delta': float(np.sqrt(np.mean((ye - pred1) ** 2))),
            'E2_delta': float(np.sqrt(np.mean((ye - pred2) ** 2))),
            'DC_share': dc / energy if energy > 1e-15 else np.nan,
            'AC_share': ac / energy if energy > 1e-15 else np.nan,
            'EdgeGrad_CosSim': float(cos.mean()),
            'EdgeGrad_CosSim_valid': float(cos[valid].mean()) if valid.any() else np.nan,
            'edge_valid_fraction': float(valid.mean()),
            'delta_rms': float(np.sqrt(np.mean(delta ** 2))),
            'clip_fraction': float(((y <= 0) | (y >= 1)).mean()), 'pixel_seed': seed}
