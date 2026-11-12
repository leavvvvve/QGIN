# EXP-003K selected comparison contract

The released comparison contains the four specified augmentation adapters and the archived ConGeo and ConGeo-QView references. The adapters are project implementations configured for the fixed cross-view host; they are not the complete original systems.

## Common training and evaluation

- Four host views have order `[q0, r0, q1, r1]`. Only `q1` is replaced by the selected adapter; the other views and the host objective are unchanged.
- The actual historical objective is `NCE(q0,r0) + 0.5*NCE(q1,q0) + 0.5*NCE(r1,r0) + 0.25*NCE(q1,r0)`, with symmetric cross entropy and 0.1 label smoothing. The task specification displayed a different formula; the archived H/I objective was used in the completed experiment.
- Each domain and seed starts from its corresponding 108-update warmup model and optimizer. Each adapter is trained for 648 updates, in six blocks of 108, with seeds 42 and 43. The final checkpoint is selected by step, without tuning on target test data.
- RGB inputs are float32, in `[0,1]` for the adapter and normalized to `[-1,1]` for the host. Each sample uses a private `torch.Generator` seeded from SHA256 of seed, method, one-based step, and row index. Descriptor replay uses chunks of eight.
- Two train domains and two target domains are evaluated under Clean, Fog, Snow, Blur, Gamma, ExposureClip and Posterize4. Every evaluated checkpoint uses its own gallery. The four new adapters account for 16 checkpoints and 224 model–target–condition combinations.
- The two historical comparison arms use existing EXP-003H/I results. Synthetic conditions are fixed. Place-cluster bootstrap intervals use 2,000 draws and shared sampled target places across the two seeds. They do not quantify variability over new training seeds or datasets.
- Model binaries, original data and per-query tables are not bundled. Recorded model, optimizer, gallery and retrieval SHA256 values are provided under `paper_assets/exp003k/`.

## Adapter differences and source pins

| Adapter | Controlled implementation and limitation | Reference |
| --- | --- | --- |
| SLAug* | GLA-style monotone 1,024-point Bézier mapping with task-specific truncated scale and location distributions. It does not implement the original local saliency-balancing system. | [AAAI 2023 paper](https://ojs.aaai.org/index.php/AAAI/article/download/25332/25104), [source](https://github.com/Kaiseem/SLAug) |
| PASTA* | Frequency-proportional amplitude perturbation adapted to RGB, with nonnegative multiplier and output clipping specified by the task. The nonnegative clamp differs from the original Gaussian rule. | [ICCV 2023 paper](https://openaccess.thecvf.com/content/ICCV2023/html/Chattopadhyay_PASTA_Proportional_Amplitude_Spectrum_Training_Augmentation_for_Syn-to-Real_Domain_Generalization_ICCV_2023_paper.html), [source](https://github.com/prithv1/PASTA) |
| AFA* | Per-channel planar Fourier waves use task-specific continuous frequency/orientation sampling and pixel-RMS strength. The original discrete grid, scaling and auxiliary classification objective are not reproduced. | [CVPR 2024 paper](https://openaccess.thecvf.com/content/CVPR2024/html/Vaish_Fourier-basis_Functions_to_Bridge_Augmentation_Gap_Rethinking_Frequency_Augmentation_in_CVPR_2024_paper.html), [source](https://github.com/nis-research/afa-augment) |
| RaffeSDG/FreeAug* | Per-channel Butterworth filtering and radial mixing use task-specific continuous sampling. This is an adaptation of the augmentation component, not the full segmentation or structural-saliency framework. | [arXiv preprint, 2024](https://arxiv.org/abs/2405.01228), [source](https://github.com/liamheng/Non-IID_Medical_Image_Segmentation) |

Upstream commit and source-blob identifiers and the exact deviations are recorded in `paper_assets/exp003k/source_provenance.json`. The four operator module hashes agree with the frozen archived experiment; the package wrapper and training integration are a portable refactoring. The portable entry point has not been used to retrain the archived models.

## Running an adapter

Fetch the pinned official host sources as described in the root README, place the six source batch plans and warmup model/optimizer in your own directories, and edit `run.example.json`. Set `cross_domain_operator` to `SLAug`, `PASTA`, `AFA`, or `RaffeSDG`; use `host` and `method` both set to `ConGeo` and omit cached QGIN augmentation parameters.

```bash
python -m src.hosts.train --config configs_and_contracts/exp003k/run.example.json
```

The provided plans, source images, model weights and optimizer state remain external. Exact reproduction additionally requires the recorded data, software environment and GPU determinism conditions. The code validates the per-sample RNG interface but is not a claim of bitwise-identical end-to-end retraining.
