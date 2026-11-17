"""Synthetic-only checks; not an experiment evaluation or parameter search."""

import random
import unittest
import numpy as np
from src.corruptions.unseen import LEVELS, PARAMETERS, seed_hash, transform_rgb


class WeatherTests(unittest.TestCase):
    def test_all_conditions_are_deterministic_and_rng_isolated(self):
        x = np.random.default_rng(8).integers(0, 256, (33, 41, 3), dtype=np.uint8)
        before_np, before_py = np.random.get_state(), random.getstate()
        for condition in PARAMETERS:
            for level in LEVELS:
                with self.subTest(condition=condition, level=level):
                    a = transform_rgb(
                        x, "train-only-synthetic-fixture", condition, level
                    )
                    b = transform_rgb(
                        x, "train-only-synthetic-fixture", condition, level
                    )
                    self.assertTrue(np.array_equal(a, b))
                    self.assertEqual(a.dtype, np.uint8)
                    self.assertEqual(a.shape, x.shape)
                    self.assertGreaterEqual(int(a.min()), 0)
                    self.assertLessEqual(int(a.max()), 255)
        after_np = np.random.get_state()
        self.assertEqual(before_np[0], after_np[0])
        self.assertTrue(np.array_equal(before_np[1], after_np[1]))
        self.assertEqual(before_np[2:], after_np[2:])
        self.assertEqual(before_py, random.getstate())

    def test_tone_curve_preserves_endpoints_and_is_monotone(self):
        x = np.tile(np.arange(256, dtype=np.uint8).reshape(1, 256, 1), (2, 1, 3))
        for level in LEVELS:
            y = transform_rgb(x, "fixture", "ToneCurve", level)[0, :, 0].astype(int)
            self.assertEqual((int(y[0]), int(y[-1])), (0, 255))
            self.assertTrue((np.diff(y) >= 0).all())

    def test_seed_depends_on_query_condition_and_level(self):
        values = {
            seed_hash("query-a", "LowLight", "S1"),
            seed_hash("query-b", "LowLight", "S1"),
            seed_hash("query-a", "LowLight", "S2"),
            seed_hash("query-a", "ShadowGradient", "S1"),
        }
        self.assertEqual(len(values), 4)


if __name__ == "__main__":
    unittest.main()
