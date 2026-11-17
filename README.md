# QGIN: Quantile-Guided Intensity Network

QGIN is a training-time image augmentation for cross-view geo-localization. It anchors random pointwise intensity networks at spatial quantiles and scales hidden channels by their spatial standard deviation. **ConGeo-QView** applies QGIN to a ConGeo query view. Retrieval uses the same encoder and 768-dimensional representation.

The benchmark uses EVA-02 at 384×384, a shared 108-update warmup, 648 training updates and seeds 42, 43 and 44. The two-level paired bootstrap uses 2,000 resamples of training seeds and target locations. CorrMean6 averages six synthetic corruptions.

## ConGeo-QView results

CorrMean6 R@1 (%), mean ± sample standard deviation; gain in percentage points [95% CI]:

| Direction | ConGeo | ConGeo-QView | Difference, 95% CI |
| --- | --- | --- | --- |
| Dense→Dense | 82.32 ± 1.12 | 85.82 ± 0.98 | +3.50 [+2.62, +4.47] |
| SUES→SUES | 86.48 ± 1.32 | 92.39 ± 0.13 | +5.91 [+3.61, +8.44] |
| Dense→SUES | 70.86 ± 0.49 | 73.52 ± 0.24 | +2.66 [+1.34, +3.99] |
| SUES→Dense | 17.03 ± 0.92 | 21.80 ± 0.95 | +4.77 [+3.48, +6.12] |

For Snow R@1 the corresponding ConGeo→QView changes are 70.70→81.38, 65.46→83.18, 50.00→61.20 and 10.28→16.00 across the four directions. The full benchmark includes DAC, MEAN and four host pairs, plus controlled adapters based on SLAug, PASTA, AFA and RaffeSDG. [Tables and all confidence intervals](paper_assets/03_Main_Benchmark_Tables.md).

## QGIN across host objectives

CorrMean6 R@1 gain in pp [95% CI]:

| Host pair | Dense→Dense | SUES→SUES | Dense→SUES | SUES→Dense |
| --- | --- | --- | --- | --- |
| Base (EVA-02 + Label Smoothing) → Base + QGIN | +4.18 [+3.15, +5.22] | +8.19 [+5.45, +11.28] | +1.91 [+0.14, +3.70] | +6.22 [+4.62, +7.82] |
| Sample4Geo → S4G-QDual | +4.17 [+2.72, +5.44] | +5.07 [+3.27, +7.28] | -0.42 [-3.18, +2.27] | +4.15 [+2.16, +5.99] |
| ConGeo → ConGeo-QView | +3.50 [+2.62, +4.47] | +5.91 [+3.61, +8.44] | +2.66 [+1.34, +3.99] | +4.77 [+3.48, +6.12] |
| SinGeo → SinGeo-QView | +3.82 [+2.97, +4.69] | +5.39 [+2.26, +8.77] | +0.59 [-1.23, +2.33] | +4.83 [+3.02, +6.55] |

For Dense→SUES, Clean R@1 is 77.08→76.91 for ConGeo and 82.23→78.74 for Sample4Geo. Under the 18 unseen brightness conditions, the ConGeo-QView gains are reported alongside an adapter comparison and component ablations in [the ablation report](paper_assets/04_Ablation_and_Unseen_Eval.md).

## Contents

- [Motivation and Source128 diagnostics](paper_assets/01_Motivation_and_Diagnosis.md)
- [Formulation and timing](paper_assets/02_Method_Formulation.md)
- [Host and augmentation benchmark tables](paper_assets/03_Main_Benchmark_Tables.md)
- [Ablations and unseen brightness results](paper_assets/04_Ablation_and_Unseen_Eval.md)
- [Cases, spatial errors and efficiency](paper_assets/05_CTE_and_Efficiency.md)
- [Summary data and provenance](paper_assets/FILE_MANIFEST.md)
- [Adapter implementation contracts](configs_and_contracts/augmentation_adapters/PROTOCOL.md) and [third-party source information](THIRD_PARTY.md)

## Installation and use

Create an environment with the versions in `requirements.txt` and a CUDA-enabled PyTorch build. Then run:

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/fetch_official.py --help
```

QGIN accepts one normalized image in `[-1,1]` and explicitly sampled parameters:

```python
from src.modules.qgin import sample, network
parameters, quantiles = sample(seed=42, quantile_seed=43)
augmented, layer_diagnostics, output_diagnostics = network(image, parameters, quantiles)
```

Here `image` has shape `[1,3,H,W]`. Four hidden-layer variants are exposed in `src.modules.variants.variant`; the fixed-zero and QGIN paths use the same interface. Host training is configured through `configs_and_contracts/run.example.json` and launched with `python -m src.hosts.train --config PATH`. The adapters have their own [example](configs_and_contracts/augmentation_adapters/run.example.json).

Evaluation requires a user-provided query/gallery manifest and checkpoint: `python -m src.evaluation.retrieve --help`. Add `--include-unseen` for all six brightness families at three severities. Two-level intervals for aligned seed-by-location differences are available in `src.evaluation.paired_bootstrap.paired_intervals`. Data, source plans and model weights are supplied separately.

## Limitations

The evaluated weather and brightness changes are synthetic. SUES-200 lacks GPS coordinates for geographic distance metrics. The cross-domain operator comparisons are task-specific adapters, and some Dense→SUES host pairs trade Clean accuracy for robustness.
