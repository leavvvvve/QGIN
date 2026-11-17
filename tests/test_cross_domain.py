import unittest
import numpy as np
import torch
from src.modules.cross_domain import OPERATORS, apply_normalized_batch, seed_for
from src.evaluation.operator_diagnostics import diagnostics


class CrossDomainTests(unittest.TestCase):
    def test_four_operators_are_reproducible_and_isolated(self):
        x = torch.rand((3, 64, 64), generator=torch.Generator().manual_seed(19))
        before = torch.get_rng_state().clone()
        self.assertEqual(set(OPERATORS), {"SLAug", "PASTA", "AFA", "RaffeSDG"})
        for name, fn in OPERATORS.items():
            with self.subTest(method=name):
                seed = seed_for(42, name, 1, 7)
                a = fn(x, torch.Generator().manual_seed(seed))
                b = fn(x, torch.Generator().manual_seed(seed))
                self.assertTrue(torch.equal(a, b))
                self.assertEqual(a.shape, x.shape)
                self.assertTrue(torch.isfinite(a).all())
                self.assertGreaterEqual(float(a.min()), 0.0)
                self.assertLessEqual(float(a.max()), 1.0)
                constant = fn(
                    torch.full_like(x, 0.5), torch.Generator().manual_seed(seed)
                )
                self.assertTrue(torch.isfinite(constant).all())
                self.assertTrue(torch.equal(before, torch.get_rng_state()))

    def test_normalized_batch_uses_per_sample_seeds(self):
        x = (
            torch.rand((2, 3, 64, 64), generator=torch.Generator().manual_seed(11)) * 2
            - 1
        )
        original = x.clone()
        before = torch.get_rng_state().clone()
        for name, fn in OPERATORS.items():
            with self.subTest(method=name):
                result = apply_normalized_batch(x, name, 42, 8, [13, 29], "cpu")
                expected = []
                for image, index in zip(x, (13, 29)):
                    g = torch.Generator().manual_seed(seed_for(42, name, 8, index))
                    expected.append(
                        fn(((image + 1) / 2).clamp(0, 1), g).clamp(0, 1) * 2 - 1
                    )
                self.assertTrue(torch.equal(result, torch.stack(expected)))
                self.assertTrue(torch.equal(before, torch.get_rng_state()))
                self.assertTrue(torch.equal(x, original))

    def test_diagnostics_recover_affine_mapping(self):
        x = np.random.default_rng(9).uniform(0.1, 0.8, (64, 64, 3)).astype(np.float32)
        y = (x * 0.7 + 0.1).astype(np.float32)
        result = diagnostics(x, y, 7, 2)
        self.assertLess(result["channel_affine_rmse"], 1e-6)
        self.assertLess(result["rgb_affine_rmse"], 1e-6)
        self.assertAlmostEqual(result["DC_share"] + result["AC_share"], 1.0)
        self.assertAlmostEqual(result["EdgeGrad_CosSim_valid"], 1.0, places=6)


if __name__ == "__main__":
    unittest.main()
