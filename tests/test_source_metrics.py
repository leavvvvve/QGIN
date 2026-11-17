import unittest
import numpy as np
from src.evaluation.source_metrics import affine_residuals


class SourceMetricTests(unittest.TestCase):
    def test_affine_fit_and_near_constant_shift(self):
        x = np.random.default_rng(5).uniform(0.1, 0.8, (64, 64, 3))
        fit, evaluation = np.arange(2048), np.arange(2048, 4096)
        y = 0.5 * x + 0.2
        result = affine_residuals(x, y, fit, evaluation)
        self.assertFalse(result["near_constant_shift"])
        self.assertLess(result["channel_affine_residual"], 1e-20)
        self.assertLess(result["rgb_affine_residual"], 1e-20)
        constant = affine_residuals(x, x + 0.01, fit, evaluation)
        self.assertTrue(constant["near_constant_shift"])
        self.assertTrue(np.isnan(constant["channel_affine_residual"]))


if __name__ == "__main__":
    unittest.main()
