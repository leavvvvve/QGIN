# QGIN: Quantile-Guided Intensity Network

QGIN is a training-time query-image augmentation. Let `z_l = W_l * h_(l-1)` be a pointwise convolution at one of three hidden layers. For each image, layer and channel, choose `p` uniformly in `[0.25, 0.75]` and set

$$t_l = Q_p(z_l),\qquad h_l = \operatorname{LeakyReLU}\left((z_l-t_l)/(\sigma_l+10^{-6})\right).$$

For a nearly constant channel (`sigma < 10^-6`), the implementation uses the original affine preactivation. The fourth pointwise layer produces `y`; its norm is aligned to the input norm, and the output is `(1-w)x + w y_aligned` clipped to `[-1,1]`, with `w` uniform in `[0.35,0.85]`. The hidden slope is 0.01. Invalid or nearly zero output falls back to the input.

1. **Hinge placement.** For finite samples without ties, the spatial quantile positions the zero hinge near the chosen order-statistic fraction; interpolation and ties determine the exact discrete fraction.
2. **Positive affine transformations.** For `z' = a z + b`, `a > 0`, quantile centering removes `b`; with the `10^-6` stabilizer the standardized value differs by the factor `(sigma + eps)/(sigma + eps/a)`. The expression becomes invariant when `eps` is negligible relative to channel scale. The constant-channel fallback is a separate case.

The encoder's inference graph is unchanged and retains its 768-dimensional descriptor. On the shared RTX 4090, CUDA-event timing for a full QGIN augmentation call on one 384×384 input, after 10 warmups and over 100 calls, was **12.81 ms median and 35.18 ms p95**. Training step timing is reported separately in [efficiency](05_CTE_and_Efficiency.md).

Implementation: [`src/modules/qgin.py`](../src/modules/qgin.py); component ablations: [`src/modules/variants.py`](../src/modules/variants.py).
