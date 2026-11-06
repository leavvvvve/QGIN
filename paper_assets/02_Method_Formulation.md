# QGIN and ConGeo-QView

## Retrieval under photometric degradation

For a query image $q$ and satellite gallery $\mathcal G=\{r_j\}$, retrieval selects $\arg\max_j f_\theta(T(q))^\top f_\theta(r_j)$. The source training set contains matched query–satellite pairs and place labels. The seven evaluation conditions apply fixed photometric transformations to queries while keeping the satellite gallery clean. QGIN adds a stochastic photometric view during source training.

The shared encoder is the EVA-family ViT-B/16 implemented by timm as `vit_base_patch16_rope_reg1_gap_256.sbb_in1k` (`timm.models.eva.Eva`, timm version `1.0.22`). At $384\times384$ resolution it has $24\times24=576$ spatial tokens and one register token. Its native global-average descriptor has dimension $768$; L2 normalization maps it to $\mathbb S^{767}$. We use **Base (EVA + Label Smoothing)** as the table label for this exact backbone and training objective.

## Quantile-guided intensity network

Let RGB input $u\in[0,1]^{3\times H\times W}$ and $x=2u-1$. Each image receives four spatially shared random $1\times1$ convolutions with channel widths $3\to2\to2\to2\to3$. We sample all weights and biases independently from $\mathcal N(0,1)$ and keep them fixed for that image's augmentation. For hidden layer $\ell\in\{1,2,3\}$, define

$$a_{\ell,c}(v)=\bigl(W_\ell*z_{\ell-1}\bigr)_c(v),\quad p_{\ell,c}\sim\mathcal U(0.25,0.75),\quad \tau_{\ell,c}=Q_{p_{\ell,c}}(a_{\ell,c}),$$

where $v$ indexes spatial position, $z_0=x$, and $Q_p$ is the exact spatial order-statistic quantile with linear interpolation. The population standard deviation is $\sigma_{\ell,c}=\operatorname{std}_{v}(a_{\ell,c}(v))$ with correction zero. With $\epsilon=10^{-6}$,

$$\tilde a_{\ell,c}(v)=\begin{cases}(a_{\ell,c}(v)-\tau_{\ell,c})/(\sigma_{\ell,c}+\epsilon),&\sigma_{\ell,c}\ge\epsilon,\\a_{\ell,c}(v)+b_{\ell,c},&\sigma_{\ell,c}<\epsilon,\end{cases}$$

$$z_{\ell,c}(v)=\max(\tilde a_{\ell,c}(v),0)+0.01\min(\tilde a_{\ell,c}(v),0).$$

The hidden bias is used in the constant-channel fallback. The fourth layer is linear: $y=W_4*z_3+b_4$. We align the **pure nonlinear output** to the input Frobenius norm, then interpolate exactly once:

$$\hat y=y\frac{\|x\|_F}{\max(\|y\|_F,\epsilon)},\quad w\sim\mathcal U(0.35,0.85),\quad \mathcal Q(x)=\operatorname{clip}_{[-1,1]}((1-w)x+w\hat y).$$

If $y$ or its norm is nonfinite, or $\|y\|_F<\epsilon$, the output is $x$. The entire operator runs in FP32 without autograd. Per-image frozen parameters allow deterministic replay without advancing the training RNG. Parameters are resampled across training image occurrences according to the cached source plan.

All spatial coordinates remain fixed. The same pointwise function acts at every pixel, while quantiles and scales depend on spatial order statistics. Thus the operator commutes with spatial permutations and introduces no resampling or geometric displacement. Its photometric response can be nonmonotonic and can mix RGB channels.

The **w/o Quantile Anchoring (Fixed Zero-Hinge)** control uses $z_\ell=\operatorname{LeakyReLU}(W_\ell*z_{\ell-1}+b_\ell)$ at the three hidden layers, followed by the same output normalization, interpolation and clipping. QGIN develops the randomized pointwise intensity-network construction with spatial quantile anchoring; the construction's source is credited in [THIRD_PARTY.md](../THIRD_PARTY.md).

## Host objectives

For normalized batch descriptors $A,B$, define symmetric smoothed contrastive cross-entropy

$$\mathcal L_s(A,B)=\frac{1}{2N}\sum_i\left[\operatorname{CE}_{\varepsilon}(sA_iB^\top,i)+\operatorname{CE}_{\varepsilon}(sB_iA^\top,i)\right].$$

For Sample4Geo, ConGeo and SinGeo, $\varepsilon=0.10$ and $s=\exp(t)$ with trainable $t$ initialized to $\log(1/0.07)$. Sample4Geo caps $s$ at $100$; ConGeo and SinGeo use the uncapped scale. All contrastive terms are evaluated over the complete logical batch.

**ConGeo-QView.** Four views are $(q_0,r_0,q_1,r_1)$. The second query is a different source image of the same place. The satellite views use independent standard transformations of the paired satellite image. QGIN transforms the standard secondary query view, giving $\tilde q_1=\mathcal Q(q_1)$. The objective is

$$\mathcal L_{\mathrm{ConGeo-QView}}=\mathcal L_s(q_0,r_0)+0.50\mathcal L_s(\tilde q_1,q_0)+0.50\mathcal L_s(r_1,r_0)+0.25\mathcal L_s(\tilde q_1,r_0).$$

Here image symbols inside $\mathcal L_s$ stand for their encoder descriptors. The ConGeo reference uses $q_1$ in place of $\tilde q_1$. Both arms share the place plan, same-place secondary query selection, host transforms and all loss coefficients. This is a nonpanoramic four-view implementation of [ConGeo](https://github.com/eceo-epfl/ConGeo).

**Base + QGIN.** The fixed scale is $1/0.07$ and smoothing is $0.092$. The target distribution is $0.908$ on the matched diagonal plus $0.092$ uniformly over allowed candidates. Other images of the same place are excluded from negatives. The augmented objective is $0.50\mathcal L(q_0,r_0)+0.50\mathcal L(\mathcal Q(q_0),r_0)$.

**S4G-QDual.** The same two-term objective uses the Sample4Geo smoothed contrastive loss and its learned capped temperature. S4G-StdDual replaces QGIN by scalar affine brightness and contrast augmentation, with contrast uniform in $[0.85,1.15]$ and brightness uniform in $[-0.15,0.15]$ in RGB $[0,1]$, followed by clipping.

**SinGeo-QView.** QGIN transforms $q_1$ and the objective is

$$\mathcal L_s(q_0,r_0)+0.50\mathcal L_s(\tilde q_1,q_0)+0.50\mathcal L_s(r_1,r_0)+0.25\left[\mathcal L_s(\tilde q_1,r_0)+\mathcal L_s(q_0,r_1)+\mathcal L_s(\tilde q_1,r_1)\right].$$

The secondary satellite rotation probability is $0.75t/648$ at update $t$, with rotations selected from $90$, $180$ and $270$ degrees. The reference and QGIN arm use identical coefficients and curriculum. These controlled settings are specified in the [SinGeo contract](../configs_and_contracts/SinGeo.json); the official University entry uses different cross-term weights and rotation scheduling.

## Optimization and inference

Each source domain and training seed supplies a common 108-update warmup encoder and optimizer state. Every formal arm runs 648 further updates and selects the final checkpoint. Shared Adam states are restored by parameter name and shape; new host parameters start at optimizer step zero. The learned host temperature is reset to the common initial value. DenseUAV uses six blocks of 105 batches of 64 and three batches of 16; SUES-200 uses 648 batches of 64. Each logical batch contains distinct places.

Base uses AdamW, weight decay $0.01$, cosine learning rate from $10^{-4}$ to $10^{-6}$, and global gradient norm clipping at $100$. The external AdamW hosts use $10^{-4}$ cosine decay with denominator 648 and gradient-value clipping at $100$. QDFL retains its frozen-backbone adapter/head SGD groups and warmup schedule. MRGeo uses fixed temperature and unsmoothed contrastive CE. [Contracts](../configs_and_contracts/protocol.json) specify each setting.

BF16 descriptor caching and RNG-restored chunk replay preserve full-batch contrastive interactions while reducing activation storage. QGIN is generated once per secondary view and reused through replay. Host heads operate on full-batch cached features; replay traverses the encoder and adds no BatchNorm head updates.

```text
for each source-only planned batch:
    construct paired host views using the shared image plan
    augment secondary query with FP32 QGIN using cached random parameters
    cache all view descriptors and RNG states
    compute the host objective on the full logical batch
    differentiate the objective with respect to cached descriptors
    replay encoder chunks with saved RNG states and descriptor gradients
    clip parameter gradients and take one optimizer step
```

At test time, Base, Sample4Geo, ConGeo and SinGeo and their QGIN variants use the same native $768$-dimensional encoder. QGIN has zero additional inference parameters and no inference call. The common evaluation protocol sums original and horizontally flipped descriptors before L2 normalization; the cost benchmark measures a single unflipped image. The external head baselines retain their own evaluated inference heads and dimensions.
