import unittest
import torch
from src.modules.qgin import sample, network, network_variant
from src.modules.augmentations import secondary


class VariantTests(unittest.TestCase):
    def test_qgin_and_fixed_paths_match_main_operator(self):
        x = (
            torch.rand((1, 3, 16, 19), generator=torch.Generator().manual_seed(4)) * 2
            - 1
        )
        params, q = sample(7, 13)
        for mode, quantiles in [("QGIN", q), ("FixedZeroHinge", None)]:
            expected = network(x, params, quantiles, True)
            result = network_variant(x, params, mode, quantiles, True)
            self.assertTrue(torch.equal(result[0], expected[0]))
            self.assertEqual(result[1:], expected[1:])

    def test_all_variants_handle_random_and_constant_inputs(self):
        params, q = sample(8, 9)
        for x in (torch.zeros((1, 3, 16, 16)), torch.rand((1, 3, 16, 16)) * 2 - 1):
            for mode in ("MeanHinge", "Q50", "QuantNoStd", "MeanNoStd"):
                y, channels, info = network_variant(x, params, mode, q, True)
                self.assertTrue(torch.isfinite(y).all(), mode)
                self.assertEqual(y.shape, x.shape)
                self.assertEqual(len(channels), 6)
                self.assertLessEqual(float(y.abs().max()), 1.0)

    def test_named_variants_are_wired_into_cached_training_path(self):
        image = (
            torch.rand((1, 3, 13, 15), generator=torch.Generator().manual_seed(24)) * 2
            - 1
        )
        params, quantiles = sample(8, 9)
        pieces = []
        for weight, bias in params["layers"]:
            pieces.extend([weight.flatten(), bias.flatten()])
        pieces.append(params["w"].reshape(1))
        cache = {"packed": torch.cat(pieces).unsqueeze(0), "p": quantiles.unsqueeze(0)}
        for mode in (
            "FixedZeroHinge",
            "MeanHinge",
            "Q50",
            "QuantNoStd",
            "MeanNoStd",
            "QGIN",
        ):
            q = None if mode == "FixedZeroHinge" else quantiles
            expected = network_variant(image, params, mode, q)[0]
            actual = secondary(image, mode, torch.tensor([0]), cache, device="cpu")
            self.assertTrue(torch.equal(actual, expected), mode)

    def test_requires_quantiles(self):
        p, _ = sample(1)
        with self.assertRaises(ValueError):
            network_variant(torch.zeros((1, 3, 5, 5)), p, "MeanHinge")


if __name__ == "__main__":
    unittest.main()
