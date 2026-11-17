"""Three-seed paired location bootstrap; input values must already be paired."""

import numpy as np


def paired_intervals(seed_location_differences, resamples=2000, random_seed=3045):
    """Return fixed-seed and seed-by-location percentile intervals.

    Input is a (3, N) array of location-level paired differences, with identical
    location ordering across seeds and methods. A location may aggregate all its
    images and applicable corruptions. Equal location counts are required by the
    calling code when this is reported as a query-weighted mean.
    """
    values = np.asarray(seed_location_differences, dtype=np.float64)
    assert values.ndim == 2 and values.shape[0] == 3 and values.shape[1] > 0
    assert np.isfinite(values).all() and resamples > 0
    n = values.shape[1]

    fixed_rng = np.random.default_rng(random_seed)
    location_draws = fixed_rng.integers(0, n, size=(resamples, n))
    fixed_draws = values.mean(axis=0)[location_draws].mean(axis=1)

    hierarchical_rng = np.random.default_rng(random_seed)
    seed_draws = hierarchical_rng.integers(0, 3, size=(resamples, 3))
    hierarchical_locations = hierarchical_rng.integers(0, n, size=(resamples, n))
    hierarchical_draws = values[
        seed_draws[:, :, None], hierarchical_locations[:, None, :]
    ].mean(axis=(1, 2))

    fixed = np.quantile(fixed_draws, [0.025, 0.975])
    hierarchical = np.quantile(hierarchical_draws, [0.025, 0.975])
    per_seed = values.mean(axis=1)
    return {
        "point": float(per_seed.mean()),
        "seed_mean": per_seed.tolist(),
        "seed_sd_ddof1": float(per_seed.std(ddof=1)),
        "fixed_seed_location_ci": fixed.tolist(),
        "two_level_seed_location_ci": hierarchical.tolist(),
        "seeds": 3,
        "locations": n,
        "resamples": resamples,
        "random_seed": random_seed,
        "two_level_order": "sample three seeds with replacement, then sample locations once and share across sampled seeds",
    }
