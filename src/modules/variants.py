"""Hidden-layer variants with identical random weights and output alignment."""

from .qgin import network as reference_network, quantile as reference_quantile
import torch
import torch.nn.functional as F


@torch.no_grad()
def variant(x, param, mode, p, audit=False):
    assert mode in (
        "FixedZeroHinge",
        "MeanHinge",
        "Q50",
        "QuantNoStd",
        "MeanNoStd",
        "QGIN",
    )
    if mode == "FixedZeroHinge":
        return reference_network(x, param, None, audit)
    if mode == "QGIN":
        return reference_network(x, param, p, audit)
    assert x.ndim == 4 and x.shape[0] == 1 and x.shape[1] == 3
    z, layers, fallbacks = x.float(), [], 0
    maximum_pre, maximum_linear = 0.0, 0.0
    with torch.autocast(device_type=x.device.type, enabled=False):
        for layer, (weight, bias) in enumerate(param["layers"]):
            linear = F.conv2d(z, weight.to(z.device), None)
            original_bias = bias.to(z.device).reshape(1, -1, 1, 1)
            maximum_linear = max(maximum_linear, float(linear.abs().max()))
            if layer < 3:
                sigma = linear.std(dim=(-2, -1), correction=0, keepdim=True)
                bad = sigma < 1e-6
                if mode in ("MeanHinge", "MeanNoStd"):
                    threshold = linear.mean(dim=(-2, -1), keepdim=True)
                else:
                    probs = (
                        torch.full_like(p[layer], 0.5) if mode == "Q50" else p[layer]
                    )
                    threshold = reference_quantile(linear, probs)
                centered = linear - threshold
                normal = (
                    centered / (sigma + 1e-6)
                    if mode in ("MeanHinge", "Q50")
                    else centered
                )
                pre = torch.where(bad, linear + original_bias, normal)
                maximum_pre = max(maximum_pre, float(pre.abs().max()))
                fallbacks += int(bad.sum())
                z = F.leaky_relu(pre, 0.01)
                if audit:
                    for channel in range(z.shape[1]):
                        active = float((pre[0, channel] > 0).float().mean())
                        layers.append(
                            {
                                "layer": layer + 1,
                                "channel": channel,
                                "f_plus": active,
                                "hinge_miss": int(active > 0.99 or active < 0.01),
                                "active_hinge": int(0.20 <= active <= 0.80),
                                "linear_std": float(sigma[0, channel]),
                                "post_std": float(z[0, channel].std(correction=0)),
                                "threshold": float(threshold[0, channel]),
                                "fallback": int(bad[0, channel]),
                            }
                        )
            else:
                z = F.conv2d(z, weight.to(z.device), bias.to(z.device))
        raw = z
        yn = raw.norm()
        bad_output = (
            not bool(torch.isfinite(raw).all())
            or not bool(torch.isfinite(yn))
            or float(yn) < 1e-6
        )
        aligned = x if bad_output else raw * (x.norm() / yn.clamp_min(1e-6))
        premix = (1 - param["w"].to(x.device)) * x + param["w"].to(x.device) * aligned
        out = x if bad_output else premix.clamp(-1, 1)
        mu = raw.mean((-2, -1), keepdim=True)
        dc = float(
            x.shape[-1] * x.shape[-2] * mu.square().sum() / (raw.square().sum() + 1e-6)
        )
        record = {
            "channel_fallback": fallbacks,
            "identity_fallback": int(bad_output),
            "DC_share": dc,
            "AC_share": 1 - dc,
            "raw_norm": float(yn),
            "clip_fraction": float((premix.abs() > 1).float().mean()),
            "output_std": float(out.std(correction=0)),
            "max_abs_linear": maximum_linear,
            "max_abs_hidden_preactivation": maximum_pre,
            "output_finite": bool(torch.isfinite(out).all()),
        }
    return out, layers, record
