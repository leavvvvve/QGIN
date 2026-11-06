# Method and implementation sources

QGIN adds spatial quantile anchoring, constant-channel fallback, pure-output energy alignment and single interpolation to randomized pointwise intensity networks. The random intensity-network construction is related to [GIN source code](https://github.com/cheng-01037/Causality-Medical-Image-Domain-Generalization/tree/d4d5056ded88951fc3967f8f294f4a12420e13c6). The QGIN implementation in this repository is the project implementation specified by its equations and numerical tests.

The host objectives and transformations follow the pinned official sources below. DAC, MEAN and QDFL class bodies and loss utilities are loaded at runtime from separately fetched source trees. Those source files retain their original licenses; the fetch script places them under the ignored `external/` directory. This repository does not redistribute those upstream trees or grant a new license to their contents.

| Method | Primary source | Controlled implementation |
|---|---|---|
| Sample4Geo, ICCV 2023 | [Official repository](https://github.com/Skyy93/Sample4Geo) | Symmetric contrastive objective and University transforms |
| DAC, TCSVT 2024 | [Official repository](https://github.com/SummerpanKing/DAC) | Official alignment head/loss, shared EVA feature interface |
| ConGeo, ECCV 2024 | [Official repository](https://github.com/eceo-epfl/ConGeo) | Four-view contrastive objective, same-place nonpanoramic query pair |
| MEAN, TGRS 2025 | [Official repository](https://github.com/ISChenawei/MEAN) | Official multilevel head and alignment loss |
| QDFL, TGRS 2025 | [Official repository](https://github.com/Shuyu-Hu/QDFL) | Official query head/adapters with EVA token interface |
| SinGeo, CVPR 2026 | [Official repository](https://github.com/Yangchen-nudt/SinGeo) | Four-view objective with the specified cross weights and rotation curriculum |
| MRGeo, AAAI 2026 | [Author repository](https://github.com/WLHASH/MRGeo), [paper](https://arxiv.org/abs/2603.12587) | Paper reimplementation; implementation choices in the contract |
| EVA implementation | [timm](https://github.com/huggingface/pytorch-image-models) | Exact backbone identifier and runtime version in the protocol |

Commit pins and source entry points are in `configs_and_contracts/`. The released Python modules are a portable refactoring of the evaluated project code. Model and optimizer checkpoint identifiers are in `paper_assets/summary_csv/`; source file provenance is in `paper_assets/FILE_MANIFEST.md`.
