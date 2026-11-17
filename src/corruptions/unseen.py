"""Deterministic pre-resize, query-only brightness corruptions."""

import hashlib
import math
import numpy as np

PROTOCOL_VERSION = "brightness-v1"
PARAMETERS = {
    "LowLight": ((0.5, 1.2, 0.01), (0.3, 1.5, 0.02), (0.15, 1.8, 0.03)),
    "ToneCurve": (5.0, 8.0, 12.0),
    "LogResponse": (10.0, 50.0, 200.0),
    "ShadowGradient": (0.6, 0.4, 0.2),
    "WhiteBalance": (0.15, 0.3, 0.45),
    "HazeLevels": (0.7, 0.5, 0.3),
}
LEVELS = ("S1", "S2", "S3")


def seed_hash(query_id, condition, level):
    """Historical SHA256 seed convention; independent of model and training seed."""
    assert isinstance(query_id, str) and query_id
    assert condition in PARAMETERS and level in LEVELS
    text = f"42:{query_id}:{condition}:{level}"
    return int(hashlib.sha256(text.encode("utf8")).hexdigest()[:8], 16)


def transform_rgb(image, query_id, condition, level):
    """Transform an HWC uint8 RGB image at its native resolution, before resize."""
    assert isinstance(image, np.ndarray) and image.dtype == np.uint8
    assert (
        image.ndim == 3
        and image.shape[2] == 3
        and image.shape[0] > 0
        and image.shape[1] > 0
    )
    index = LEVELS.index(level)
    param = PARAMETERS[condition][index]
    rng = np.random.default_rng(seed_hash(query_id, condition, level))
    x = image.astype(np.float32) / np.float32(255.0)
    if condition == "LowLight":
        gain, gamma, sigma = param
        noise = rng.normal(0.0, sigma, size=x.shape).astype(np.float32)
        y = gain * np.power(x, gamma) + noise
    elif condition == "ToneCurve":
        k = param
        low = 1.0 / (1.0 + math.exp(k / 2.0))
        high = 1.0 / (1.0 + math.exp(-k / 2.0))
        y = (1.0 / (1.0 + np.exp(-k * (x - 0.5))) - low) / (high - low)
    elif condition == "LogResponse":
        y = np.log1p(param * x) / math.log1p(param)
    elif condition == "ShadowGradient":
        h, w = x.shape[:2]
        theta = rng.uniform(0.0, 2.0 * math.pi)
        yy = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, None]
        xx = np.linspace(0.0, 1.0, w, dtype=np.float32)[None, :]
        projection = xx * math.cos(theta) + yy * math.sin(theta)
        spread = float(projection.max() - projection.min())
        t = (
            (projection - projection.min()) / spread
            if spread > 0.0
            else np.zeros_like(projection)
        )
        y = x * (1.0 - (1.0 - param) * t[..., None])
    elif condition == "WhiteBalance":
        direction = 1.0 if rng.random() < 0.5 else -1.0
        gains = np.asarray(
            (1.0 + direction * param, 1.0, 1.0 - direction * param), dtype=np.float32
        )
        y = x * gains.reshape(1, 1, 3)
    elif condition == "HazeLevels":
        y = x * param + 0.9 * (1.0 - param)
    else:
        raise ValueError(condition)
    return np.rint(np.clip(y, 0.0, 1.0) * 255.0).astype(np.uint8)
