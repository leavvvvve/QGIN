import unittest
import numpy as np
from src.evaluation.paired_bootstrap import paired_intervals


class StatisticsTests(unittest.TestCase):
    def test_identity_and_reproducibility(self):
        data = np.zeros((3, 6))
        result = paired_intervals(data)
        self.assertEqual(result["point"], 0.0)
        self.assertEqual(result["fixed_seed_location_ci"], [0.0, 0.0])
        self.assertEqual(result["two_level_seed_location_ci"], [0.0, 0.0])
        self.assertEqual(result, paired_intervals(data))

    def test_seed_variability_is_in_two_level_interval(self):
        data = np.tile(np.array([-0.1, 0.0, 0.1])[:, None], (1, 7))
        result = paired_intervals(data)
        self.assertAlmostEqual(result["point"], 0.0)
        self.assertAlmostEqual(result["seed_sd_ddof1"], 0.1)
        self.assertEqual(result["fixed_seed_location_ci"], [0.0, 0.0])
        self.assertLess(result["two_level_seed_location_ci"][0], 0.0)
        self.assertGreater(result["two_level_seed_location_ci"][1], 0.0)

    def test_invalid_shapes_and_values_are_rejected(self):
        with self.assertRaises(AssertionError):
            paired_intervals(np.zeros((2, 5)))
        with self.assertRaises(AssertionError):
            paired_intervals(np.array([[0.0], [np.nan], [0.0]]))


if __name__ == "__main__":
    unittest.main()
