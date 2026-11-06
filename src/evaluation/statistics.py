"""Place-cluster percentile bootstrap, retaining seed and height pairing."""
import numpy as np


def bootstrap_weights(n, draws=2000, seed=3045):
    rng = np.random.default_rng(seed)
    index = rng.integers(n, size=(draws, n))
    weights = np.zeros((draws, n), dtype=np.float64)
    for i, row in enumerate(index):
        weights[i] = np.bincount(row, minlength=n) / n
    return weights


def interval(samples):
    x = np.asarray(samples)
    if not np.isfinite(x).any():
        return np.nan, np.nan
    return tuple(np.nanquantile(x, [.025, .975], axis=0))


def summarize(values, weights):
    """values: [places, endpoints]; each place has equal mass."""
    values = np.asarray(values, dtype=np.float64)
    samples = weights @ values
    return values.mean(0), samples


def ratio_bootstrap(numerator, denominator, weights):
    numerator, denominator = np.asarray(numerator), np.asarray(denominator)
    den = weights @ denominator
    samples = np.divide(weights @ numerator, den,
                        out=np.full(den.shape, np.nan), where=den > 0)
    total = denominator.sum()
    return numerator.sum() / total if total else np.nan, samples
