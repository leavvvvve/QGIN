"""Held-out normalized affine residuals used by the source-image diagnostics."""

import numpy as np


def affine_residuals(source, augmented, fit_indices, eval_indices):
    """Fit channel-wise and RGB affine maps; return normalized held-out SSE.

    Indices select disjoint flattened image pixels and can be restricted to
    unclipped locations. The source diagnostic uses 2,048 fit and 2,048
    evaluation pixels; near-constant shift energy returns NaN.
    """
    x, y = np.asarray(source, dtype=np.float64), np.asarray(augmented, dtype=np.float64)
    if x.shape != y.shape or x.ndim != 3 or x.shape[2] != 3:
        raise ValueError("Expected matching HWC RGB images")
    fit, evaluation = np.asarray(fit_indices, dtype=int), np.asarray(
        eval_indices, dtype=int
    )
    if not len(fit) or not len(evaluation) or len(np.intersect1d(fit, evaluation)):
        raise ValueError("Fit and evaluation indices must be nonempty and disjoint")
    xf, yf = x.reshape(-1, 3)[fit], y.reshape(-1, 3)[fit]
    xe, ye = x.reshape(-1, 3)[evaluation], y.reshape(-1, 3)[evaluation]
    channel_pred = np.empty_like(ye)
    for c in range(3):
        design = np.c_[xf[:, c], np.ones(len(xf))]
        coefficients = np.linalg.lstsq(design, yf[:, c], rcond=None)[0]
        channel_pred[:, c] = np.c_[xe[:, c], np.ones(len(xe))] @ coefficients
    rgb_coeff = np.linalg.lstsq(np.c_[xf, np.ones(len(xf))], yf, rcond=None)[0]
    rgb_pred = np.c_[xe, np.ones(len(xe))] @ rgb_coeff
    shift = np.square((ye - xe) - (yf - xf).mean(axis=0)).sum()
    near_constant = shift / len(evaluation) < 1e-6
    return {
        "channel_affine_residual": (
            float(np.square(ye - channel_pred).sum() / (shift + 1e-12))
            if not near_constant
            else np.nan
        ),
        "rgb_affine_residual": (
            float(np.square(ye - rgb_pred).sum() / (shift + 1e-12))
            if not near_constant
            else np.nan
        ),
        "near_constant_shift": bool(near_constant),
    }
