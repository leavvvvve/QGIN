# Evidence manifest

This file preserves the original experiment identifiers only as provenance keys. Published method names appear in all paper tables. Local paths are relative to `D:/科研工作流`; server paths identify the read-only evidence tree. SHA256 values identify the original bytes used for aggregation. Datasets, model binaries, feature caches and raw per-query CSVs are external inputs and are not included in this repository.

## Table lineage and statistics

| Asset | Input and row selection | Computation |
|---|---|---|
| Main benchmark | Evaluation mapping below; method/direction/seed keys | Query metrics → equal-place/height means; 2,000 place-cluster draws |
| Paired host gains | Same mapping; each QGIN variant and its host | Paired differences with common place indices; fixed two-seed average |
| CTE | Same mapping; Dense native Base additionally uses the competition-enhanced table listed below | Clean-correct reference membership, old-place/current margin signs, rescue/new failures, far-error counts |
| Motivation | Frozen competitor and moment-intervention query files; source hinge/energy/residual files | 777-place bootstrap or 32-source-image bootstrap, as specified in the document |
| Cost | Native-target inference_cost.json and available training_complete.json | Exact measured dimensions, parameters, median latency and device memory peaks |
| Checkpoints | Original checkpoint manifests and warmup origin files | Preserve recorded SHA256; do not redistribute model bytes |

The complete summary tables contain unrounded floating-point values (up to twelve significant digits). Documents show two decimal places. Every plotted quantity is read from these same aggregate tables. Bootstrap RNG is `numpy.default_rng(3045)`, with the same sampled place indices across matched models and seeds. CTE rates use resampled numerator/denominator sums and omit undefined zero-denominator draws; a missing seed point estimate has no seed-mean rate.

Dense AP is official trapezoidal AP; SUES AP is reciprocal rank for its single positive. Published Snow hardest-negative image switches are 77.43%–78.89%; place switches are 63.19%–63.62%. Residual ratios around 91× and 323× refer specifically to the unclipped pixel subset. Pixel-restoration R and shallow-feature restoration O_Snow are separate diagnostics.

## Evaluation input map

| Direction | Method | Seed | Local evidence path |
|---|---|---|---|
| dense_to_dense | Base | 42 | `code/output/route1_stagec/exp003c/eval_seed42_A6/retrieval.csv` |
| dense_to_dense | Base | 43 | `code/output/route1_stagec/exp003c/eval_seed43_A6/retrieval.csv` |
| dense_to_dense | Sample4Geo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_Sample4Geo/retrieval.csv` |
| dense_to_dense | Sample4Geo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_Sample4Geo/retrieval.csv` |
| dense_to_dense | DAC | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_DAC/retrieval.csv` |
| dense_to_dense | DAC | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_DAC/retrieval.csv` |
| dense_to_dense | ConGeo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_ConGeo/retrieval.csv` |
| dense_to_dense | ConGeo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_ConGeo/retrieval.csv` |
| dense_to_dense | MEAN | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_MEAN/retrieval.csv` |
| dense_to_dense | MEAN | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_MEAN/retrieval.csv` |
| dense_to_dense | QDFL | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_QDFL/retrieval.csv` |
| dense_to_dense | QDFL | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_QDFL/retrieval.csv` |
| dense_to_dense | SinGeo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_SinGeo/retrieval.csv` |
| dense_to_dense | SinGeo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_SinGeo/retrieval.csv` |
| dense_to_dense | MRGeo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_MRGeo/retrieval.csv` |
| dense_to_dense | MRGeo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_MRGeo/retrieval.csv` |
| dense_to_dense | Base + QGIN | 42 | `code/output/route1_stagec/exp003f/dense/seed42_QuantileGIN-Aug/retrieval.csv` |
| dense_to_dense | Base + QGIN | 43 | `code/output/route1_stagec/exp003f/dense/seed43_QuantileGIN-Aug/retrieval.csv` |
| dense_to_dense | S4G-QDual | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_S4G-QDual/retrieval.csv` |
| dense_to_dense | S4G-QDual | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_S4G-QDual/retrieval.csv` |
| dense_to_dense | ConGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_ConGeo-QView/retrieval.csv` |
| dense_to_dense | ConGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_ConGeo-QView/retrieval.csv` |
| dense_to_dense | SinGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_SinGeo-QView/retrieval.csv` |
| dense_to_dense | SinGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_SinGeo-QView/retrieval.csv` |
| dense_to_dense | S4G-StdDual | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_S4G-StdDual/retrieval.csv` |
| dense_to_dense | S4G-StdDual | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_S4G-StdDual/retrieval.csv` |
| dense_to_dense | Base + StdDual | 42 | `code/output/route1_stagec/exp003e/dense/seed42_StdDual/retrieval.csv` |
| dense_to_dense | Base + StdDual | 43 | `code/output/route1_stagec/exp003e/dense/seed43_StdDual/retrieval.csv` |
| dense_to_dense | Base + AugMix-Dual | 42 | `code/output/route1_stagec/exp003f/dense/seed42_AugMix-Dual/retrieval.csv` |
| dense_to_dense | Base + AugMix-Dual | 43 | `code/output/route1_stagec/exp003f/dense/seed43_AugMix-Dual/retrieval.csv` |
| dense_to_dense | w/o Quantile Anchoring (Fixed Zero-Hinge) | 42 | `code/output/route1_stagec/exp003c/eval_seed42_GIN-Aug/retrieval.csv` |
| dense_to_dense | w/o Quantile Anchoring (Fixed Zero-Hinge) | 43 | `code/output/route1_stagec/exp003c/eval_seed43_GIN-Aug/retrieval.csv` |
| dense_to_dense | Base + ColorJitter-Dual | 42 | `code/output/route1_stagec/exp003f/dense/seed42_ColorJitter-Dual/retrieval.csv` |
| dense_to_dense | Base + ColorJitter-Dual | 43 | `code/output/route1_stagec/exp003f/dense/seed43_ColorJitter-Dual/retrieval.csv` |
| sues_to_sues | Base | 42 | `code/output/route1_stagec/exp003d/final/seed42_Base648/retrieval.csv` |
| sues_to_sues | Base | 43 | `code/output/route1_stagec/exp003d/final/seed43_Base648/retrieval.csv` |
| sues_to_sues | Sample4Geo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_Sample4Geo/retrieval.csv` |
| sues_to_sues | Sample4Geo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_Sample4Geo/retrieval.csv` |
| sues_to_sues | DAC | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_DAC/retrieval.csv` |
| sues_to_sues | DAC | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_DAC/retrieval.csv` |
| sues_to_sues | ConGeo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_ConGeo/retrieval.csv` |
| sues_to_sues | ConGeo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_ConGeo/retrieval.csv` |
| sues_to_sues | MEAN | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_MEAN/retrieval.csv` |
| sues_to_sues | MEAN | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_MEAN/retrieval.csv` |
| sues_to_sues | QDFL | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_QDFL/retrieval.csv` |
| sues_to_sues | QDFL | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_QDFL/retrieval.csv` |
| sues_to_sues | SinGeo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_SinGeo/retrieval.csv` |
| sues_to_sues | SinGeo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_SinGeo/retrieval.csv` |
| sues_to_sues | MRGeo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_MRGeo/retrieval.csv` |
| sues_to_sues | MRGeo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_MRGeo/retrieval.csv` |
| sues_to_sues | Base + QGIN | 42 | `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed42_QuantileGIN-Aug/retrieval.csv` |
| sues_to_sues | Base + QGIN | 43 | `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed43_QuantileGIN-Aug/retrieval.csv` |
| sues_to_sues | S4G-QDual | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_S4G-QDual/retrieval.csv` |
| sues_to_sues | S4G-QDual | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_S4G-QDual/retrieval.csv` |
| sues_to_sues | ConGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_ConGeo-QView/retrieval.csv` |
| sues_to_sues | ConGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_ConGeo-QView/retrieval.csv` |
| sues_to_sues | SinGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_SinGeo-QView/retrieval.csv` |
| sues_to_sues | SinGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_SinGeo-QView/retrieval.csv` |
| sues_to_sues | S4G-StdDual | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_S4G-StdDual/retrieval.csv` |
| sues_to_sues | S4G-StdDual | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_S4G-StdDual/retrieval.csv` |
| sues_to_sues | Base + StdDual | 42 | `code/output/route1_stagec/exp003d/final/seed42_StdDual/retrieval.csv` |
| sues_to_sues | Base + StdDual | 43 | `code/output/route1_stagec/exp003d/final/seed43_StdDual/retrieval.csv` |
| sues_to_sues | Base + AugMix-Dual | 42 | `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed42_AugMix-Dual/retrieval.csv` |
| sues_to_sues | Base + AugMix-Dual | 43 | `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed43_AugMix-Dual/retrieval.csv` |
| sues_to_sues | w/o Quantile Anchoring (Fixed Zero-Hinge) | 42 | `code/output/route1_stagec/exp003d/final/seed42_GIN-Aug/retrieval.csv` |
| sues_to_sues | w/o Quantile Anchoring (Fixed Zero-Hinge) | 43 | `code/output/route1_stagec/exp003d/final/seed43_GIN-Aug/retrieval.csv` |
| dense_to_sues | Base | 42 | `code/output/route1_stagec/exp003e/zero_shot/seed42_A6/retrieval.csv` |
| dense_to_sues | Base | 43 | `code/output/route1_stagec/exp003e/zero_shot/seed43_A6/retrieval.csv` |
| dense_to_sues | Sample4Geo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_Sample4Geo/retrieval.csv` |
| dense_to_sues | Sample4Geo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_Sample4Geo/retrieval.csv` |
| dense_to_sues | DAC | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_DAC/retrieval.csv` |
| dense_to_sues | DAC | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_DAC/retrieval.csv` |
| dense_to_sues | ConGeo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_ConGeo/retrieval.csv` |
| dense_to_sues | ConGeo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_ConGeo/retrieval.csv` |
| dense_to_sues | MEAN | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_MEAN/retrieval.csv` |
| dense_to_sues | MEAN | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_MEAN/retrieval.csv` |
| dense_to_sues | QDFL | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_QDFL/retrieval.csv` |
| dense_to_sues | QDFL | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_QDFL/retrieval.csv` |
| dense_to_sues | SinGeo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_SinGeo/retrieval.csv` |
| dense_to_sues | SinGeo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_SinGeo/retrieval.csv` |
| dense_to_sues | MRGeo | 42 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_MRGeo/retrieval.csv` |
| dense_to_sues | MRGeo | 43 | `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_MRGeo/retrieval.csv` |
| dense_to_sues | Base + QGIN | 42 | `code/output/route1_stagec/exp003f/zero_shot/seed42_QuantileGIN-Aug/retrieval.csv` |
| dense_to_sues | Base + QGIN | 43 | `code/output/route1_stagec/exp003f/zero_shot/seed43_QuantileGIN-Aug/retrieval.csv` |
| dense_to_sues | S4G-QDual | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_S4G-QDual/retrieval.csv` |
| dense_to_sues | S4G-QDual | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_S4G-QDual/retrieval.csv` |
| dense_to_sues | ConGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_ConGeo-QView/retrieval.csv` |
| dense_to_sues | ConGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_ConGeo-QView/retrieval.csv` |
| dense_to_sues | SinGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_SinGeo-QView/retrieval.csv` |
| dense_to_sues | SinGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_SinGeo-QView/retrieval.csv` |
| dense_to_sues | S4G-StdDual | 42 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_S4G-StdDual/retrieval.csv` |
| dense_to_sues | S4G-StdDual | 43 | `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_S4G-StdDual/retrieval.csv` |
| sues_to_dense | Base | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_Base648/retrieval.csv` |
| sues_to_dense | Base | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_Base648/retrieval.csv` |
| sues_to_dense | Sample4Geo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_Sample4Geo/retrieval.csv` |
| sues_to_dense | Sample4Geo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_Sample4Geo/retrieval.csv` |
| sues_to_dense | DAC | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_DAC/retrieval.csv` |
| sues_to_dense | DAC | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_DAC/retrieval.csv` |
| sues_to_dense | ConGeo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_ConGeo/retrieval.csv` |
| sues_to_dense | ConGeo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_ConGeo/retrieval.csv` |
| sues_to_dense | MEAN | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_MEAN/retrieval.csv` |
| sues_to_dense | MEAN | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_MEAN/retrieval.csv` |
| sues_to_dense | QDFL | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_QDFL/retrieval.csv` |
| sues_to_dense | QDFL | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_QDFL/retrieval.csv` |
| sues_to_dense | SinGeo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_SinGeo/retrieval.csv` |
| sues_to_dense | SinGeo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_SinGeo/retrieval.csv` |
| sues_to_dense | MRGeo | 42 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_MRGeo/retrieval.csv` |
| sues_to_dense | MRGeo | 43 | `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_MRGeo/retrieval.csv` |
| sues_to_dense | Base + QGIN | 42 | `code/output/route1_stagec/exp003g/eval/sues_to_dense/seed42_QuantileGIN-Aug/retrieval.csv` |
| sues_to_dense | Base + QGIN | 43 | `code/output/route1_stagec/exp003g/eval/sues_to_dense/seed43_QuantileGIN-Aug/retrieval.csv` |
| sues_to_dense | S4G-QDual | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_S4G-QDual/retrieval.csv` |
| sues_to_dense | S4G-QDual | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_S4G-QDual/retrieval.csv` |
| sues_to_dense | ConGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_ConGeo-QView/retrieval.csv` |
| sues_to_dense | ConGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_ConGeo-QView/retrieval.csv` |
| sues_to_dense | SinGeo-QView | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_SinGeo-QView/retrieval.csv` |
| sues_to_dense | SinGeo-QView | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_SinGeo-QView/retrieval.csv` |
| sues_to_dense | S4G-StdDual | 42 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_S4G-StdDual/retrieval.csv` |
| sues_to_dense | S4G-StdDual | 43 | `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_S4G-StdDual/retrieval.csv` |

## Source files and SHA256

| Local evidence path | Server path | Bytes | SHA256 |
|---|---|---|---|
| `code/output/route1_stagec/exp003b/stage0_descriptive_ratios.csv` | `/home/life/route1-stagec/exp003b/output/stage0_descriptive_ratios.csv` | 447 | `50e2765895643e7264110840f58ce7b49021c3dcbc62782712342b4b5069316a` |
| `code/output/route1_stagec/exp003b/stage0_interventions.csv` | `/home/life/route1-stagec/exp003b/output/stage0_interventions.csv` | 4478 | `70cebe0a4ab64b71aa0b735860c1dd605988917d1fc501060267b374324050d3` |
| `code/output/route1_stagec/exp003b/stage0_per_query.csv` | `/home/life/route1-stagec/exp003b/output/stage0_per_query.csv` | 18225528 | `c7f6cdcfdaf6a6623b1c1dbf17ff41b9f16666f29aa581dcd9cf248494fbc68b` |
| `code/output/route1_stagec/exp003b/stage0_ratio_cluster_intervals.json` | `/home/life/route1-stagec/exp003b/output/stage0_ratio_cluster_intervals.json` | 605 | `7af4a6de98cc369c826c30c0009b82d3c460773a5c29f764f8b02dcd736463ad` |
| `code/output/route1_stagec/exp003c/checkpoint_manifest.json` | `/home/life/route1-stagec/exp003c_v2/output/checkpoint_manifest.json` | 2060 | `2b6594564cf03ede52474bb43f740da6a6f5a983cb5b42e7320d0a0ab73704de` |
| `code/output/route1_stagec/exp003c/eval_seed42_A6/retrieval.csv` | `/home/life/route1-stagec/exp003c_v2/output/eval_seed42_A6/retrieval.csv` | 13893604 | `1fbfb3525226ad5ad03d40ca9f8a08622e06312b566daea3c45ac7e3025aecbd` |
| `code/output/route1_stagec/exp003c/eval_seed42_GIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003c_v2/output/eval_seed42_GIN-Aug/retrieval.csv` | 13955839 | `d3a38720931163000045b36e16e407a6f5148266b6ad10297bdb6289cdd27f6e` |
| `code/output/route1_stagec/exp003c/eval_seed43_A6/retrieval.csv` | `/home/life/route1-stagec/exp003c_v2/output/eval_seed43_A6/retrieval.csv` | 13866422 | `bd9e6244cc123b6fb52a5eee61956e93c07df940ee2158d804f5ef1be66fe9ba` |
| `code/output/route1_stagec/exp003c/eval_seed43_GIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003c_v2/output/eval_seed43_GIN-Aug/retrieval.csv` | 13937195 | `7cc4b6868ce00f4bfde170f09faa3f90ebd95d5fa9d3f44e58389e39f33a473f` |
| `code/output/route1_stagec/exp003c/seed42/A6/training_complete.json` | `/home/life/route1-stagec/exp003c_v2/output/seed42/A6/training_complete.json` | 695 | `99296d6f5483b90592c2f2e251007215c243b4401cd23944421ee88517cc595e` |
| `code/output/route1_stagec/exp003c/seed43/A6/training_complete.json` | `/home/life/route1-stagec/exp003c_v2/output/seed43/A6/training_complete.json` | 694 | `7a863ac93f649b1688048578259fd9b5f00daf4c22de2c24eabc0fe12b8f6eac` |
| `code/output/route1_stagec/exp003c/stage0_cluster_intervals.csv` | `/home/life/route1-stagec/exp003c_v2/output/stage0_cluster_intervals.csv` | 10147 | `5c247ccbef7aa615bcfc27d68433b6b8a359937d460407e0af1112ba698045dc` |
| `code/output/route1_stagec/exp003c/stage0_per_query.csv` | `/home/life/route1-stagec/exp003c_v2/output/stage0_per_query.csv` | 15889911 | `0ed9df19b626a8e8773a98aa6bd29e089ee6c070cc4833269c5c500478b00346` |
| `code/output/route1_stagec/exp003c/stage0_summary.csv` | `/home/life/route1-stagec/exp003c_v2/output/stage0_summary.csv` | 2810 | `0b7e8f9b4a4d5358e081ba2a30242cb3a934ca2275abb724238a68ae1bc680a3` |
| `code/output/route1_stagec/exp003d/checkpoint_manifest.json` | `/home/life/route1-stagec/exp003d/output/checkpoint_manifest.json` | 2174 | `f181295f3cdf00caacc06e6298d13340bbc1a5f41eacd5b5f397a3cb5a974461` |
| `code/output/route1_stagec/exp003d/dense_competition_per_query.csv` | `/home/life/route1-stagec/exp003d/output/dense_competition_per_query.csv` | 116705549 | `9879569bcf5a97e4aedb58214c4245fda449e36006c7db11693ae43a33ead497` |
| `code/output/route1_stagec/exp003d/final/seed42_Base648/retrieval.csv` | `/home/life/route1-stagec/exp003d/output/final/seed42_Base648/retrieval.csv` | 24527159 | `3653d5494bed8b0f4b368ac483722f3c7dda4e43adc2e1034aac8ea7d563c8a2` |
| `code/output/route1_stagec/exp003d/final/seed42_GIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003d/output/final/seed42_GIN-Aug/retrieval.csv` | 24579332 | `beb27ccc06007a9912058104cce1c0ea4dd1750f0d2da54adb88248963bfb346` |
| `code/output/route1_stagec/exp003d/final/seed42_StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003d/output/final/seed42_StdDual/retrieval.csv` | 24457338 | `20e52326660b213cc9a0e8b71d01c015a6f78e9f643567edfc6886ef9256aa0a` |
| `code/output/route1_stagec/exp003d/final/seed43_Base648/retrieval.csv` | `/home/life/route1-stagec/exp003d/output/final/seed43_Base648/retrieval.csv` | 24522182 | `498cdf7e0d12f0c8e9e5c051d30691743237ae89f9a2f8b217955ce82b046210` |
| `code/output/route1_stagec/exp003d/final/seed43_GIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003d/output/final/seed43_GIN-Aug/retrieval.csv` | 24562885 | `efe70379dcaa35f0e0908ce63ecb98cc495b44121d4b242a9fe677af72367e41` |
| `code/output/route1_stagec/exp003d/final/seed43_StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003d/output/final/seed43_StdDual/retrieval.csv` | 24465219 | `b76b16fb01dcf4da2f5111bb7cd012c47c48221eb869e7a556938b9a06ce1ad7` |
| `code/output/route1_stagec/exp003d/seed42/Base648/training_complete.json` | `/home/life/route1-stagec/exp003d/output/seed42/Base648/training_complete.json` | 676 | `3035a9507e856f8efb4188dcce109fd53162b9157b507c5329cb8d1aa7b45ccb` |
| `code/output/route1_stagec/exp003d/seed43/Base648/training_complete.json` | `/home/life/route1-stagec/exp003d/output/seed43/Base648/training_complete.json` | 676 | `9585b14d16c29f8fa2d824b05ca7d12bbe333c21d696d261ffa8fa406f5fb278` |
| `code/output/route1_stagec/exp003e/checkpoint_manifest.json` | `/home/life/route1-stagec/exp003e/output/checkpoint_manifest.json` | 554 | `0e7abacdcf217d93c6f4f17da485c9834042400d6d4e17ef6cca5c578f8bbbec` |
| `code/output/route1_stagec/exp003e/dense/seed42_StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003e/output/dense/seed42_StdDual/retrieval.csv` | 15145212 | `f3b7ecd7a86e2743f348c2fa154bfaf9e1828f329bc704bc3d7780e71901e1ce` |
| `code/output/route1_stagec/exp003e/dense/seed43_StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003e/output/dense/seed43_StdDual/retrieval.csv` | 15125379 | `00ca83a48dd7aeb90622f497470569b6c6eead88fa7d42fde89e1dc6c345b550` |
| `code/output/route1_stagec/exp003e/zero_shot/seed42_A6/retrieval.csv` | `/home/life/route1-stagec/exp003e/output/zero_shot/seed42_A6/retrieval.csv` | 19087640 | `9774bebf0066784e01bfc1966928aa9c20f3fcafc4cafd1c8f3b7ed062d9de2e` |
| `code/output/route1_stagec/exp003e/zero_shot/seed43_A6/retrieval.csv` | `/home/life/route1-stagec/exp003e/output/zero_shot/seed43_A6/retrieval.csv` | 19175352 | `07c41c36e04e44eb5245383fcd3ff337d0e22c7f9cf5cb2cefa1e38e2ee37074` |
| `code/output/route1_stagec/exp003f/checkpoint_manifest.json` | `/home/life/route1-stagec/exp003f/output/checkpoint_manifest.json` | 1748 | `269c394080940e54042a06afdfcce058e899dcfb2053dae7774eb0836f2d7b00` |
| `code/output/route1_stagec/exp003f/dense/seed42_AugMix-Dual/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/dense/seed42_AugMix-Dual/retrieval.csv` | 15181784 | `7d23f9d62da6ab8c04b942e17aed3924f505e18637899aad95f5bc34001a1724` |
| `code/output/route1_stagec/exp003f/dense/seed42_ColorJitter-Dual/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/dense/seed42_ColorJitter-Dual/retrieval.csv` | 15282413 | `6c9b9dc66c741f13c196d11ffa91c2825897384216fbeca2a8777185d8120d43` |
| `code/output/route1_stagec/exp003f/dense/seed42_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/dense/seed42_QuantileGIN-Aug/retrieval.csv` | 15213866 | `c1bcc22d5ddeaf62a9260708e0e68107a22cb1dbf8fc2821dfc0ba0326cc6d82` |
| `code/output/route1_stagec/exp003f/dense/seed43_AugMix-Dual/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/dense/seed43_AugMix-Dual/retrieval.csv` | 15164508 | `cff48b87a402ce2443be649658d798450a14c752b248deb4dc9ef3c4e52acb0e` |
| `code/output/route1_stagec/exp003f/dense/seed43_ColorJitter-Dual/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/dense/seed43_ColorJitter-Dual/retrieval.csv` | 15264000 | `02a86146c0244ce9860ecf87adbb243bda693d8776e0f33a2a2e4c8d05150e55` |
| `code/output/route1_stagec/exp003f/dense/seed43_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/dense/seed43_QuantileGIN-Aug/retrieval.csv` | 15201154 | `67a8590193f08566a3cdd2fb7ba3c2634d495a8649af13dba782ce991a114ffa` |
| `code/output/route1_stagec/exp003f/seed42/QuantileGIN-Aug/training_complete.json` | `/home/life/route1-stagec/exp003f/output/seed42/QuantileGIN-Aug/training_complete.json` | 494 | `bc37d45ab84f16448e2d3d599ccaa9a1f3a5d6053dec705bb5cf6d5e14b96916` |
| `code/output/route1_stagec/exp003f/seed43/QuantileGIN-Aug/training_complete.json` | `/home/life/route1-stagec/exp003f/output/seed43/QuantileGIN-Aug/training_complete.json` | 493 | `d07903f47e9c2d52668ba8662c89eb0c4bd3c6534ff2d1a81618a4bca414428a` |
| `code/output/route1_stagec/exp003f/source_ac_dc_per_pair.csv` | `/home/life/route1-stagec/exp003f/output/source_ac_dc_per_pair.csv` | 35130 | `2d6568865be8c22621623198bf3de497021600f8f4296ee660c560f352b9f972` |
| `code/output/route1_stagec/exp003f/source_affine_rgb_per_pair.csv` | `/home/life/route1-stagec/exp003f/output/source_affine_rgb_per_pair.csv` | 300870 | `42b2db8fb0498d8580dcb622f0efbd85ece15b041910b66a384ec4f4fe45e48c` |
| `code/output/route1_stagec/exp003f/source_hinge_per_channel.csv` | `/home/life/route1-stagec/exp003f/output/source_hinge_per_channel.csv` | 185374 | `1998f19de340de97a317634c75ee1db2aeeb87074855599aec6dd4c31e6cccb1` |
| `code/output/route1_stagec/exp003f/source_hinge_summary.csv` | `/home/life/route1-stagec/exp003f/output/source_hinge_summary.csv` | 494 | `a4c2a3ed69de12e2578f80d8dec6e3f4945ef38a1318a0982a40c0ce94a25245` |
| `code/output/route1_stagec/exp003f/source_summary.csv` | `/home/life/route1-stagec/exp003f/output/source_summary.csv` | 7199 | `af1836519c47884cf61a39b197c811a699770f0fbabc9b27875c375f63564fca` |
| `code/output/route1_stagec/exp003f/zero_shot/seed42_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/zero_shot/seed42_QuantileGIN-Aug/retrieval.csv` | 16038945 | `fefacb7736bb229e37e061b9de343c3b069715330227085d952ea54c8b9419d4` |
| `code/output/route1_stagec/exp003f/zero_shot/seed43_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003f/output/zero_shot/seed43_QuantileGIN-Aug/retrieval.csv` | 16099052 | `b0fc32c97354aa0a152e3b60131c1725e65c54be92eeb65e7bc7f39d0038e97d` |
| `code/output/route1_stagec/exp003g/checkpoint_manifest.json` | `/home/life/route1-stagec/exp003g/output/checkpoint_manifest.json` | 1886 | `105f2b455d80906d337940f8383c84a4078baadadb8e8d4137cbbfb986f8909d` |
| `code/output/route1_stagec/exp003g/eval/sues_to_dense/seed42_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003g/output/eval/sues_to_dense/seed42_QuantileGIN-Aug/retrieval.csv` | 15987604 | `cca0b00d8f2bdb80efbcd9c28b53c8a628d291a65b0ffda8598f6be5c88a75d4` |
| `code/output/route1_stagec/exp003g/eval/sues_to_dense/seed43_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003g/output/eval/sues_to_dense/seed43_QuantileGIN-Aug/retrieval.csv` | 15965155 | `8dfa03482488c8b903e67e95342bc69ed1f4966b5254cf311ec7e593ede57124` |
| `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed42_AugMix-Dual/retrieval.csv` | `/home/life/route1-stagec/exp003g/output/eval/sues_to_sues/seed42_AugMix-Dual/retrieval.csv` | 24869812 | `e25043d674267492a8ff2cea2610556f5315166fe7411a57a2b5622aa627426a` |
| `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed42_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003g/output/eval/sues_to_sues/seed42_QuantileGIN-Aug/retrieval.csv` | 25225749 | `ae6adccf3f75ef48e3582741c6504b37cd122a5dfec1a794e2fc11c5c130ae59` |
| `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed43_AugMix-Dual/retrieval.csv` | `/home/life/route1-stagec/exp003g/output/eval/sues_to_sues/seed43_AugMix-Dual/retrieval.csv` | 24803394 | `29eb09d8cf66d6573ef3104f971bd9d791b3dd1ae38a19805e0dd034b51b04fc` |
| `code/output/route1_stagec/exp003g/eval/sues_to_sues/seed43_QuantileGIN-Aug/retrieval.csv` | `/home/life/route1-stagec/exp003g/output/eval/sues_to_sues/seed43_QuantileGIN-Aug/retrieval.csv` | 25165038 | `b0f0bd631ead90940f30b0a7f402566e9f86e50ca0399052752523494d9f9d25` |
| `code/output/route1_stagec/exp003g/train/sues/seed42/QuantileGIN-Aug/training_complete.json` | `/home/life/route1-stagec/exp003g/output/train/sues/seed42/QuantileGIN-Aug/training_complete.json` | 488 | `233a2eea408a8b294228ae1b2ff9daf788ff3350d00445957b712fc6a4e1a0a8` |
| `code/output/route1_stagec/exp003g/train/sues/seed43/QuantileGIN-Aug/training_complete.json` | `/home/life/route1-stagec/exp003g/output/train/sues/seed43/QuantileGIN-Aug/training_complete.json` | 487 | `2cc6e49e2a3e2d49677d48ed1bbc117fd9069f9d4d206693b4196adda13d2337` |
| `code/output/route1_stagec/exp003h/checkpoint_manifest.json` | `/home/life/route1-stagec/exp003h/output/checkpoint_manifest.json` | 7884 | `4c494b7cc1f16517b5564a18c7086ad4881c1e25151982e52977c26d6e68c923` |
| `code/output/route1_stagec/exp003h/cost/dense/seed42_A6/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/dense/seed42_A6/inference_cost.json` | 373 | `dfbcdf6cfd37bbbd3ca35479ea9aacc06be5161b82d3db5ce82219245ecb227c` |
| `code/output/route1_stagec/exp003h/cost/dense/seed42_QuantileGIN-Aug/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/dense/seed42_QuantileGIN-Aug/inference_cost.json` | 373 | `c5c4f4507811d9bb71b416a75d83ebf1e2ba40bd44168db84a213adde6dd5c80` |
| `code/output/route1_stagec/exp003h/cost/dense/seed43_A6/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/dense/seed43_A6/inference_cost.json` | 373 | `34026595b385b2d4402f47959ccb99eda50b0fd720ef96d172741b2d835a732a` |
| `code/output/route1_stagec/exp003h/cost/dense/seed43_QuantileGIN-Aug/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/dense/seed43_QuantileGIN-Aug/inference_cost.json` | 373 | `49ddee8d6da48b2a4e06f3cdfe8f8de5869fdfd8229e8b551ba997031011a660` |
| `code/output/route1_stagec/exp003h/cost/sues/seed42_Base648/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/sues/seed42_Base648/inference_cost.json` | 371 | `a369a88d7ee0400acfa9b83d458ecd4fcfd899a6d65bc82ce7cf1445601e8b60` |
| `code/output/route1_stagec/exp003h/cost/sues/seed42_QuantileGIN-Aug/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/sues/seed42_QuantileGIN-Aug/inference_cost.json` | 373 | `0fc40809ac6ee8f66475b8cb93c4ccad1233014f6907f913c8ec9e380859a5be` |
| `code/output/route1_stagec/exp003h/cost/sues/seed43_Base648/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/sues/seed43_Base648/inference_cost.json` | 372 | `1ee90dedbde6008da08f776e8ad1dab35d4fee7f68dd55824eec73102655997b` |
| `code/output/route1_stagec/exp003h/cost/sues/seed43_QuantileGIN-Aug/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/cost/sues/seed43_QuantileGIN-Aug/inference_cost.json` | 372 | `31f344c83dd471a40d468ba45784b0ad420af1ca85bd90bcb664b17e522eb5b5` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_ConGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_ConGeo/inference_cost.json` | 372 | `593fe3d4f00f654501cd18e67ae78eb75ee85b964604f8fc25a57010dbc795ba` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_ConGeo/retrieval.csv` | 15038399 | `615b6beea2b84f3fb36ecd67b1d6cbcf2fe0e5fb6c7d1fa3eb342ade67c5cbfc` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_DAC/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_DAC/inference_cost.json` | 379 | `a731129fbfe4287690bec4aab13a1b55950d25191a7e7414cc9c0ab8a336c33e` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_DAC/retrieval.csv` | 15023054 | `969febf22b7dac50a5f859add463e2ed3b36610a5e58af61946cd3785c0b7151` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_MEAN/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_MEAN/inference_cost.json` | 372 | `f29e5e51ac2f963a0cdba39d8e352634d6a06e268f8046792b88706f9b8d269f` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_MEAN/retrieval.csv` | 15062096 | `7932b6f958742bd7c027fbabc415718a7e2574233914bbc616681c5b8a58c12c` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_MRGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_MRGeo/inference_cost.json` | 381 | `2ab11579be59f5d9bdfc28650304f9da6146716c0308eb2f3cbd80ed83de1150` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_MRGeo/retrieval.csv` | 15201942 | `da00011fd390b23981b7366a911adb755ab7cc6d98ed3138fd3fcba13499c40b` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_QDFL/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_QDFL/inference_cost.json` | 384 | `eec358d0bc9d7f3baa8cf6a510f40645ec14f4fa868339f52f805450c475e710` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_QDFL/retrieval.csv` | 15524152 | `24a79b0a606db18b00979e6dbd01d3d0a660a62da77ec20a697b8619d0e13b94` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_Sample4Geo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_Sample4Geo/inference_cost.json` | 373 | `72cb5c1c885c84e523ba1f4fb45b434985d275b617b89ba01382c34553913c00` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_Sample4Geo/retrieval.csv` | 15150674 | `e43a1dc1d1e031f3cac4f4db435aaf6f4a8d1764c4ed176fe91067a4142e7902` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_SinGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_SinGeo/inference_cost.json` | 373 | `2748f9725a880cfcf1d142a9cf2699b799fccdac43bb7079958a47d5d41f7f91` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed42_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed42_SinGeo/retrieval.csv` | 15036926 | `35e37399bd9e3eb57d46b46606334c8ce04d383df6b78e5e59e96b752426ef57` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_ConGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_ConGeo/inference_cost.json` | 373 | `8fcfc165b154c0da4faf96dec48a053c7dcbacc5341f27a5fd9712aa3de8aca0` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_ConGeo/retrieval.csv` | 15056785 | `505df757abf97ef33b2db86d58cb71cdb74bbfbf5b4861ceffbfacfeeba5dabf` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_DAC/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_DAC/inference_cost.json` | 379 | `1bcbbf5af3693cb35b24eb54d54a110007aa865cd82fa48bf6bd7246445e4181` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_DAC/retrieval.csv` | 15046977 | `9b4b0740815b928f0df5991fe4dff22f44f25939208fcfabaedccd9f516418f2` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_MEAN/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_MEAN/inference_cost.json` | 373 | `c56c62aba8e8324e655da4b4ede388ea004bc9b27c35fe45529a2796b2974807` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_MEAN/retrieval.csv` | 15047131 | `8e186350585504ffff6f081cad198551afc8af8bbc873672dede80a0e052d4f9` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_MRGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_MRGeo/inference_cost.json` | 380 | `012aafa9cdbda7e9f4e43d84ad889d59d9ebf537d6ee0cccffc40ed8dd22f716` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_MRGeo/retrieval.csv` | 15200395 | `7f5b89e003de89238a367ebd652ef8b2b7ba5110ae1b232130e207d3afbb980d` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_QDFL/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_QDFL/inference_cost.json` | 383 | `6260e58ae1e4c3729ca017d35b9c1cb6f6638ba65a725ab4792df468762cef14` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_QDFL/retrieval.csv` | 15502539 | `facc270ce29680d58a20da05984240ce69dadba21ff028fddc2b10c90944bfa3` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_Sample4Geo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_Sample4Geo/inference_cost.json` | 372 | `fd0b1f5e0ae3cdb001190597414ec0d9e12d59635691275070738584e31faf32` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_Sample4Geo/retrieval.csv` | 15159596 | `c0216ff82a0b25d7a69e48abc48df45d75c7803223bc4dca8ad952292dedf649` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_SinGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_SinGeo/inference_cost.json` | 373 | `f10e07f773ae54ef3ba3d6463f1ccb2abaabc0259632e17ed9cd354f0c833996` |
| `code/output/route1_stagec/exp003h/eval/dense_to_dense/seed43_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_dense/seed43_SinGeo/retrieval.csv` | 15020979 | `f9998917a2431699164d781bbf9a9b92ddd0c75b507c2c8934a3386a925c9eae` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed42_ConGeo/retrieval.csv` | 24722278 | `052be62bc12a37783e1392b28e94ec0fcd1d3a56d8e380a452fb4d1a00e4cbef` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed42_DAC/retrieval.csv` | 24307791 | `e010a1049acd6ecaa9e6b40201a1deb174a368a45d15262556e997a282bbadac` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed42_MEAN/retrieval.csv` | 24427518 | `655c400145e1a4a78c7ed3dba6632d1bd51df5f7749157fac1fb7b6fa48bb11c` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed42_MRGeo/retrieval.csv` | 25008571 | `f2e33164c32b5348733ce376cfcb50a8d50a1e96178da1e412c30e3468056711` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed42_QDFL/retrieval.csv` | 24621309 | `6552ecbf8b4ec4c4bebaa43e3df71610d05f235508b0f66252808f3198058522` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed42_Sample4Geo/retrieval.csv` | 25025835 | `d1300537c941e17456c97d7a49fd0550f23d82346936731ac5a328b2d1e584c4` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed42_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed42_SinGeo/retrieval.csv` | 24846309 | `f4ad8559cd4faf9d17839629dc8f364cbebabde7a7bf356fc6cd57a6e4a3d628` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed43_ConGeo/retrieval.csv` | 24728459 | `c3b645b5a4c2d10a84c8d8f08d3993152ea3c516717465f99131d5b3bbe43d2f` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed43_DAC/retrieval.csv` | 24257684 | `e42f85a4db3c74fc08fb359af363096aabce404af9f38df8e4301cd812f21d70` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed43_MEAN/retrieval.csv` | 24367078 | `78412274accee793577605388afae4b92b54ce593cdeb82ef8ebdfccfcb86b07` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed43_MRGeo/retrieval.csv` | 24923707 | `41c8a145bb216b65eef216cc807c71b727dc0c4620ccf80cef626cda80f62b65` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed43_QDFL/retrieval.csv` | 24656285 | `3c48650fd803a7287d192c731d0ec17a87d6531c84b5539a636f1002a8c24938` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed43_Sample4Geo/retrieval.csv` | 24998553 | `ac79206b3d1f0003725aa96c5143dce983f908d9797fc044ca1915af1a19001b` |
| `code/output/route1_stagec/exp003h/eval/dense_to_sues/seed43_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/dense_to_sues/seed43_SinGeo/retrieval.csv` | 24799558 | `150e0136b4c20f9de5708206c715f888846b686873fbcf9961fcc8ae414ab1cf` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_Base648/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_Base648/retrieval.csv` | 15845736 | `1df5b9994d87bb51841405bea07a0fbcb5e1dcf9b4a54960c3c656815c6325a3` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_ConGeo/retrieval.csv` | 15795471 | `aa3266aad961999d4cae777884711ab4ae2ac4c7c0db8c9c1ffa0f3e53bab718` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_DAC/retrieval.csv` | 15742004 | `bbbd96278b38fbe4c9cff37e23ce755db64312b90061659274dd35aa272faeea` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_MEAN/retrieval.csv` | 15737410 | `11e553ad756f9fad6f367acf349205999e778b0532feef1b4b8fd39f34f3e1de` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_MRGeo/retrieval.csv` | 15727638 | `9c0cbb6c626ec933e10c8310339415d995712b0a1267cdb9de946779edea94dd` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_QDFL/retrieval.csv` | 15759002 | `336ab66425e8d4929fc77b363a2edcc92b6563b5f640430191b324971b002ff3` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_Sample4Geo/retrieval.csv` | 15845662 | `6b254e244e59f3c62ff680b8c78218d3b1fcd32fa08b74e23594e025827f114f` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed42_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed42_SinGeo/retrieval.csv` | 15779129 | `e9c71603134fb1cd7d1c60bb98ab5ee061cd8e852336ec79b1dcc487f6520055` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_Base648/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_Base648/retrieval.csv` | 15849307 | `4e733f74621d1a60b5ab3d76f6a82726d7d1ed25f9c50bd4312b45c0b27fc47e` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_ConGeo/retrieval.csv` | 15838116 | `ec8918ec9ec3eefc23d87fb14f652684edc39090a927b221b82c5cd2ad3e1ce4` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_DAC/retrieval.csv` | 15757606 | `37b4004fb8cc04d1e682ae4f864112eed94be58f9922be830573527dc5755abe` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_MEAN/retrieval.csv` | 15737607 | `24277ff2ffdb5b5d1271d0a43a3fa31cd24a42dbb97cc5bff9c7a8f0d72e5181` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_MRGeo/retrieval.csv` | 15754285 | `07084b7cb9f614efbeb297855b328091fe5cf920b3ae2eeeae862596dc5cd8dc` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_QDFL/retrieval.csv` | 15760071 | `2dddea2f38cec0b31ecb7d063cd5efb31f4c0241495c5155bccfecbec098a8bb` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_Sample4Geo/retrieval.csv` | 15858087 | `f67eda651166b96d525d0aa5e649cdcb55969b7072fdf875282dd3d99ef9b05b` |
| `code/output/route1_stagec/exp003h/eval/sues_to_dense/seed43_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_dense/seed43_SinGeo/retrieval.csv` | 15843285 | `d17371da35b22960d6368207d32070c8418e94baa6db796580f7e848cd45abc6` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_ConGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_ConGeo/inference_cost.json` | 373 | `0602d470aec467730ce7d5ee5b96a18e1d6cde120c595b14b9a9acf4d1e32bf8` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_ConGeo/retrieval.csv` | 24349771 | `ca388afe7a1f80d8f6295e7e70a147587ef262653a2a8dbf22bf1aea49bcb0e4` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_DAC/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_DAC/inference_cost.json` | 379 | `cb816d8f84f7ac7be743e34a0e72a977f256de815e487cc85399ef3949073ce1` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_DAC/retrieval.csv` | 23941729 | `8454c040583c3d137b14a7970cf7e58c780ad56c7648adedb517ddc3b6e643e4` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_MEAN/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_MEAN/inference_cost.json` | 374 | `20bac225d483d181342d210c3a516bd14455c9cbeb69656ca22dd04c830ad01a` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_MEAN/retrieval.csv` | 24141458 | `5eb8526a80529c1b648ba693dca5c55ec0320e3153612b68b0c2db3da4a6c4a3` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_MRGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_MRGeo/inference_cost.json` | 380 | `db3cfbb0ce67bf6c0739da01a3aa2dbec0fdea14a45fe3fb1330333886c2cca0` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_MRGeo/retrieval.csv` | 24325003 | `958706a0cccc8fb67de218eca6099bc5d24b0c613875d8d8c93922b3deba4ce8` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_QDFL/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_QDFL/inference_cost.json` | 384 | `85ab624763b3255ae5804e01eaac790b17ab1a7aa50d57f7f1c99d44cc20bb6a` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_QDFL/retrieval.csv` | 24261847 | `7a2dda8fcf3dcdd72265180da1b6e3a302dd7fbc6ad48e8d84f8ef9802990b7b` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_Sample4Geo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_Sample4Geo/inference_cost.json` | 373 | `92988f8f95f245eaa4744a23b0498f79129de94830558820332570e013ef7f86` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_Sample4Geo/retrieval.csv` | 24720785 | `61fa9b2aabe36731d538dfd14179c1e52ffec4f27bc37a7e82423a45347ce22c` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_SinGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_SinGeo/inference_cost.json` | 374 | `e93575933fdcb4dc8ef24e4dae87bd367d6f4c3f6020dbe1b18dda66c88192d1` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed42_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed42_SinGeo/retrieval.csv` | 24369135 | `d6a1c046a7ac113c1abcf06124319c37bc0bff8df4bb3a5dcf0d37f01fbd9430` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_ConGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_ConGeo/inference_cost.json` | 374 | `7d4d50fd46321dc298997b281cd9631f4b5b53ede347f3dbd8f9034214f5932b` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_ConGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_ConGeo/retrieval.csv` | 24341318 | `438bbb1c60d090cad12673a600860d554a98ec49ca4bf5515da214056cc136fd` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_DAC/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_DAC/inference_cost.json` | 377 | `6ffa3d23b09b409ae8a853ac058b05277147445b8e162a541f9175a0d92c1aed` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_DAC/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_DAC/retrieval.csv` | 23934218 | `945060e2362a5d49dd088c342635c8a6c0b87f67318d7d704fcee434c339bb9e` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_MEAN/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_MEAN/inference_cost.json` | 373 | `a5c3cdbbe4db9f5d78c034d4d98ff78cca6ffac1c648c706ce5b73245486ba4d` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_MEAN/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_MEAN/retrieval.csv` | 24126790 | `8915dd2b678b669b4b5246c4f9237c96cdfd4abbebf616d6782fcc99f20af4e5` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_MRGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_MRGeo/inference_cost.json` | 380 | `fc72857bd2c4e37c543828dedc163eb1a31a040877714fbc6ac27b0fd8c1d21b` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_MRGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_MRGeo/retrieval.csv` | 24338700 | `8cec563d8f6acc1553f7b0d14578edc6a3bd8c85abe3b71be4548b671586a70e` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_QDFL/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_QDFL/inference_cost.json` | 384 | `2dd162ec563ffa5d03d8b30c923a8fc9f91bf88072c6d953c0ba7d2ed19daa4f` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_QDFL/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_QDFL/retrieval.csv` | 24245366 | `135ce0921b70cfae7d2ccae25987f09b34ecdfe017d9eb4f67394d6adf5b4625` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_Sample4Geo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_Sample4Geo/inference_cost.json` | 374 | `e651f8f3eb64d7fca4420d1343e46a245c371b183df6da2ccf1da43f65b6c408` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_Sample4Geo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_Sample4Geo/retrieval.csv` | 24682068 | `224ab73f68092eb4c0d6829db2ef4899125cb73183f8f0a88ded1595cc9bb7c2` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_SinGeo/inference_cost.json` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_SinGeo/inference_cost.json` | 373 | `452c00ce4c58b876057788a6005bf0c676bc617b6e4479928c71e08875cb9f33` |
| `code/output/route1_stagec/exp003h/eval/sues_to_sues/seed43_SinGeo/retrieval.csv` | `/home/life/route1-stagec/exp003h/output/eval/sues_to_sues/seed43_SinGeo/retrieval.csv` | 24413156 | `ef7cd5b850f8678bc58f95950e6d73140f993d1ec3e4f8e7acb52d3c076766dd` |
| `code/output/route1_stagec/exp003i/checkpoint_manifest.json` | `/home/life/route1-stagec/exp003i/output/checkpoint_manifest.json` | 10858 | `9793b460404bba5895cd25166a46c0942ea8a2ed0b5867ac775bc71a925ef0a1` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_ConGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_ConGeo-QView/inference_cost.json` | 374 | `bd15598b15611822925380f4c4036c19c76f6e3416d926a82973b7da5219128c` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_ConGeo-QView/retrieval.csv` | 15088846 | `5c2b2b2a84603af68f6cba32a2d3e6f24b2c5615d4c041a8efa6d80d83a246f0` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_S4G-QDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_S4G-QDual/inference_cost.json` | 374 | `48a05c57dc1dca37b87639c8629e597cdaa8485716a9a6c54865ac5e966c4b5d` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_S4G-QDual/retrieval.csv` | 15096777 | `0b54bb65f90ff1d1a509b95cb8bead3063baff24bdc1cb53312f2df1150ab954` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_S4G-StdDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_S4G-StdDual/inference_cost.json` | 373 | `8dd5b3d10224aca8b2b558dadc88362c32e0eeb1c732da50daba8cb7ec5aede7` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_S4G-StdDual/retrieval.csv` | 15159422 | `b2c9331ede562858e71964f0a52f3a93f72e08b6008b5712dad44128d9f50d0f` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_SinGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_SinGeo-QView/inference_cost.json` | 374 | `cd8d0a25d6b39c5492dd7ae1d703e1271210a2171a3c8fc9693e638fc434005d` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed42_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed42_SinGeo-QView/retrieval.csv` | 15084668 | `bdcc75d67166dbf39eadac1f9c76019a72193328e6f9a8505c1af1032164d9fd` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_ConGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_ConGeo-QView/inference_cost.json` | 373 | `28b4eec158067821a15e47a61638c66e8aef90b4ac1ad4496923fa41933df28c` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_ConGeo-QView/retrieval.csv` | 15111826 | `e4b30af832ac34a10d65699786e54987a87dc7f36e74c1851f75d4aef27f1b0f` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_S4G-QDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_S4G-QDual/inference_cost.json` | 373 | `d76e67244c0f74dcd6e9d23dd14a1e6f92370079cc7360f16a4a5a7263dc240c` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_S4G-QDual/retrieval.csv` | 15075309 | `c8b0ee42f066a1206e128a986c6861aeee79cb01cd15fb91c4de44e16d65c7d1` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_S4G-StdDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_S4G-StdDual/inference_cost.json` | 373 | `645fce9d22ad1b05bb1ae084675a8959822ab9b40a9b021b74d3ba369eb9f898` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_S4G-StdDual/retrieval.csv` | 15174993 | `4ea32d3ac677d6650407fcc92d780284f297efcf1e5602c095b8651927adceeb` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_SinGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_SinGeo-QView/inference_cost.json` | 372 | `e17dfb0ed32ca7a803e19cbf693ee0b5159c53914c35c5aa38d15949963523fe` |
| `code/output/route1_stagec/exp003i/eval/dense_to_dense/seed43_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_dense/seed43_SinGeo-QView/retrieval.csv` | 15080517 | `8c4ffa1d745624c7d46b99654467e54c6f18f43d5a1bcd525fd701c262905876` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed42_ConGeo-QView/retrieval.csv` | 25310696 | `0d9f513e91e11e0837846a4871cac88e6be9a8d7eb59c8ce94e011cbeddd7947` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed42_S4G-QDual/retrieval.csv` | 24970433 | `e6130563f69bab8cad572533aff3162f65bfb0c47e997d2d2fd6356dd8137603` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed42_S4G-StdDual/retrieval.csv` | 25151291 | `997928cd1c35a00f76ef01486f02c8de8bc0bef132209c8fc7e7d0f83f9cb3dd` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed42_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed42_SinGeo-QView/retrieval.csv` | 25488171 | `8c97395c1bf508bd66848f8bd5ee711a811bda907c8b1bc2ef380e3f946afe06` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed43_ConGeo-QView/retrieval.csv` | 25320350 | `db5b1cfb85cbb446f43663ad3abd38b15db4502c672e215a57248360bebd53bb` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed43_S4G-QDual/retrieval.csv` | 24953291 | `8bbef47196eb828a9036efef46b0c1d5d3769f0e57bd13db2bc67f0ba4333e58` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed43_S4G-StdDual/retrieval.csv` | 25113552 | `d11d5251efd9c236a778e6755fc717f3eef2643935ddd1ce1df155f7579d23ac` |
| `code/output/route1_stagec/exp003i/eval/dense_to_sues/seed43_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/dense_to_sues/seed43_SinGeo-QView/retrieval.csv` | 25520220 | `b91a0deadd9c4c6577e9255bc5563fccd16707a644fa80b5401a54a8efdaad50` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed42_ConGeo-QView/retrieval.csv` | 15842722 | `087daab4e1e6c51ef655eb0c7bfee838babfbec8d03c9386d1240de5b4ba467c` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed42_S4G-QDual/retrieval.csv` | 15823333 | `f4602ff03328c71790c54e6c7efc7078cb1e9388297eca4c42b758252cdc0a96` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed42_S4G-StdDual/retrieval.csv` | 15861085 | `636c08807d712118846dd9212ee8d1606904dac77df130817bc05a31ec801ea3` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed42_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed42_SinGeo-QView/retrieval.csv` | 15848243 | `e6b7104c1ac60009bdc1479d8c16f45bb320f9eee80bbb965af5460189602751` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed43_ConGeo-QView/retrieval.csv` | 15870818 | `007cd68b01dbe722d12b4c79a30df2ab3b804fb2d01d738d2e3062e01738d188` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed43_S4G-QDual/retrieval.csv` | 15800867 | `326c494d4bb1a29c5f2abacb9e3ab943a0679e3ab03a133f80c013657f920d5f` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed43_S4G-StdDual/retrieval.csv` | 15869944 | `51620cb9ed8beea8a915cfe59c00546b9b6f87337cc840da5492dd15eff79940` |
| `code/output/route1_stagec/exp003i/eval/sues_to_dense/seed43_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_dense/seed43_SinGeo-QView/retrieval.csv` | 15874485 | `452872e91418b6a6e6c05080d40e864d3441c863cd1e95d6ede08210b9bd8eb6` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_ConGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_ConGeo-QView/inference_cost.json` | 373 | `66b534b629ab5b3b1fd67ec0e76cd4921f97760ec9f47182160fd8bb6a913d2f` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_ConGeo-QView/retrieval.csv` | 24908038 | `127e9666d5eb397c3fd2104edc7c8f29fd8bd4db76e5196ab861eead6ec25692` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_S4G-QDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_S4G-QDual/inference_cost.json` | 373 | `2b58a49bc1b146f7341d6fb0b1dc22052152ed8b3c2e6a13b19747f31614fbc4` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_S4G-QDual/retrieval.csv` | 24527063 | `e1b333d0983edb1ec1aec8d864c8d514d15153f2fa9941e75a088149d4657c46` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_S4G-StdDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_S4G-StdDual/inference_cost.json` | 374 | `c1602c837785c3ae07db099e6cf3f57f84b9fd3571c73b7b244433a6a0291b4b` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_S4G-StdDual/retrieval.csv` | 24832601 | `5cde20aa197a6a6d0a76e5c01daadb57c9040db97fbfd6ae57d626f9ed91e07e` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_SinGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_SinGeo-QView/inference_cost.json` | 374 | `ec4c47a2c814d214cb64b6d36927440bdfb9b07b6f6ebd3c01bf63912bcb56f5` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed42_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed42_SinGeo-QView/retrieval.csv` | 24968285 | `8dca6058aede1841cfbb3cbc07848f686675ac07015ecc0698ac1fc12a48b90d` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_ConGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_ConGeo-QView/inference_cost.json` | 372 | `8322f922d62300adba1691e7274b74085fa840847ab2d30146a6be33bb5e90be` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_ConGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_ConGeo-QView/retrieval.csv` | 24882399 | `a67f1b45c7c2f686f914a9c7b5752465e47712279e2d2ec87bfc51d550fe2400` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_S4G-QDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_S4G-QDual/inference_cost.json` | 374 | `c5fb14c9a02bd6422a42effbb9e5b1d64c297fdc61adfacaa1125a3056e5c250` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_S4G-QDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_S4G-QDual/retrieval.csv` | 24459922 | `170920cecc76693a707bf9e7cb48924cb75f36538b9b172277ea7d2c4d9b8f86` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_S4G-StdDual/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_S4G-StdDual/inference_cost.json` | 373 | `8580a8eb182ffb47c429701d781241270d34d951bacb02d5f27792a2988094a1` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_S4G-StdDual/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_S4G-StdDual/retrieval.csv` | 24765877 | `a14a9de36ca8fc20a7d065e70a3f01cf927cccfa272d82fb97a3ca1e217e11f1` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_SinGeo-QView/inference_cost.json` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_SinGeo-QView/inference_cost.json` | 374 | `7604a5746f60c829672b29566cd91ba00507f9aaf2036122f3fbfa3122fb687e` |
| `code/output/route1_stagec/exp003i/eval/sues_to_sues/seed43_SinGeo-QView/retrieval.csv` | `/home/life/route1-stagec/exp003i/output/eval/sues_to_sues/seed43_SinGeo-QView/retrieval.csv` | 24930706 | `5e3d22f9089b64ac223a806d0c688c48f8c7190f231aa333a2a6557f4736ab49` |
| `code/output/route1_stagec/exp003i/train/dense/seed42/ConGeo-QView/origin.json` | `/home/life/route1-stagec/exp003i/output/train/dense/seed42/ConGeo-QView/origin.json` | 2373 | `4c005b2af3004ad976a9a1fcfc7b54fa8991eebd63cafbf45f6ba5cf3f801e4a` |
| `code/output/route1_stagec/exp003i/train/dense/seed43/ConGeo-QView/origin.json` | `/home/life/route1-stagec/exp003i/output/train/dense/seed43/ConGeo-QView/origin.json` | 2373 | `fc4dfcf6cbe91f14c11695cb6b602e31cdd4d96c511a949110cac73b5c65a679` |
| `code/output/route1_stagec/exp003i/train/sues/seed42/ConGeo-QView/origin.json` | `/home/life/route1-stagec/exp003i/output/train/sues/seed42/ConGeo-QView/origin.json` | 2372 | `6ca344b2ef6ed8969cc54d93753bfc611e0d43c3e2834d90b81b310e43874d0c` |
| `code/output/route1_stagec/exp003i/train/sues/seed43/ConGeo-QView/origin.json` | `/home/life/route1-stagec/exp003i/output/train/sues/seed43/ConGeo-QView/origin.json` | 2372 | `db8b4bc3b8a6f70d6089f8b8419eb9f29922a42877fc150860fcba64962ffa7c` |
| `code/route1_stagec/common.py` | `/home/life/route1-stagec/exp003a/code/common.py` | 5250 | `70c0955f25a0b533db0a3549ebfe9c3d4062aa772497d5ae14d2646dc9a900d6` |
| `code/route1_stagec/exp003c/eval_c.py` | `/home/life/route1-stagec/exp003c_v2/code/eval_c.py` | 7534 | `e2296f0de849ce63bf4fe108e3a1365cbda89a0b5eadfadd8d32edfc27ea3d09` |
| `code/route1_stagec/exp003c/operators.py` | `/home/life/route1-stagec/exp003c_v2/code/operators.py` | 2473 | `8ba1e3380c9e1f2f9dbd81f9f73e8b2db0e330896a15efacefe9bf43ec57b18e` |
| `code/route1_stagec/exp003c/train_branch.py` | `/home/life/route1-stagec/exp003c_v2/code/train_branch.py` | 7755 | `1d8be4fe3cb30a524a57f111968f4b7f770b3c31d64f1b5a556ff296cbe43068` |
| `code/route1_stagec/exp003f/operators_f.py` | `/home/life/route1-stagec/exp003f/code/operators_f.py` | 3650 | `017b236031f291898f44806873fec246d88007caaf0fc89dd912ff950e58fe02` |
| `code/route1_stagec/exp003g/train_g.py` | `/home/life/route1-stagec/exp003g/code/train_g.py` | 6267 | `cd13e3f49759d198cd166c1b0c7c47b6b901932337b8d8c47ddb899a98bcb3af` |
| `code/route1_stagec/exp003h/contracts/ConGeo.yaml` | `/home/life/route1-stagec/exp003h/code/contracts/ConGeo.yaml` | 1648 | `86c7dc016de28ede5a401292718ec51a69086ab1b0548c8d98b0b147984e3eac` |
| `code/route1_stagec/exp003h/contracts/DAC.yaml` | `/home/life/route1-stagec/exp003h/code/contracts/DAC.yaml` | 2745 | `1d317944e9dbc8647e72d3db275f1296da30aa1f2277abc9d63531cb1b71c683` |
| `code/route1_stagec/exp003h/contracts/MEAN.yaml` | `/home/life/route1-stagec/exp003h/code/contracts/MEAN.yaml` | 2494 | `635eba068d503b8ee30b16c3f8c7628d1d9ae4aba3ee1ecf66e47f931865ef84` |
| `code/route1_stagec/exp003h/contracts/MRGeo.yaml` | `/home/life/route1-stagec/exp003h/code/contracts/MRGeo.yaml` | 2457 | `771adba65ac967cb6b953ab7566f96dc46f8a4832effcc0e33b98ef160d9061f` |
| `code/route1_stagec/exp003h/contracts/QDFL.yaml` | `/home/life/route1-stagec/exp003h/code/contracts/QDFL.yaml` | 3018 | `ea4b2cfd3c7b42734a290b59e822eb1268d3f651b3f95cb554b19ce92d1e3e92` |
| `code/route1_stagec/exp003h/contracts/Sample4Geo.yaml` | `/home/life/route1-stagec/exp003h/code/contracts/Sample4Geo.yaml` | 1893 | `8f2c3e7f6b7ec2376e356796b316889996432687031379048c2a3a61162c5e82` |
| `code/route1_stagec/exp003h/contracts/SinGeo.yaml` | `/home/life/route1-stagec/exp003h/code/contracts/SinGeo.yaml` | 2094 | `92e10a19d6e6e4ca0198f3d0663ab3ce1264d417d087d44e4f563849218538d4` |
| `code/route1_stagec/exp003h/data_h.py` | `/home/life/route1-stagec/exp003h/code/data_h.py` | 2967 | `6ebbeb15f49ac821d7449f2e08b929211424e803aacf817e834f23a5902437e5` |
| `code/route1_stagec/exp003h/heads_h.py` | `/home/life/route1-stagec/exp003h/code/heads_h.py` | 1050 | `7d459f31fdcdcf6510cf348661af0fbfed38b3db3929e1c798e810a1701436ee` |
| `code/route1_stagec/exp003h/model_h.py` | `/home/life/route1-stagec/exp003h/code/model_h.py` | 3856 | `2b3458d06d6c08680d3241c3a47aca2be25f6e1a49224dd6ab43edad064ce9d9` |
| `code/route1_stagec/exp003h/mrgeo_h.py` | `/home/life/route1-stagec/exp003h/code/mrgeo_h.py` | 1398 | `5dcbcd2847eda068420651d1149ade87ab15601e8f6932f6e958d893c748817d` |
| `code/route1_stagec/exp003h/qdfl_h.py` | `/home/life/route1-stagec/exp003h/code/qdfl_h.py` | 2875 | `ff18816b67a34fd02f9056b989ed0eac337849309dbc181bae4e2f4f674b23fa` |
| `code/route1_stagec/exp003h/train_h.py` | `/home/life/route1-stagec/exp003h/code/train_h.py` | 9407 | `58f34bfddd3fccb65c81b405389ff87a2abc6a2ceb5223bc1b65152f3f96187c` |
| `code/route1_stagec/exp003i/data_i.py` | `/home/life/route1-stagec/exp003i/code/data_i.py` | 913 | `169149312d5cc00b0082831c791201ea07eb0f27b57f7ef11fb11c8a1e78a313` |
| `code/route1_stagec/exp003i/objectives_i.py` | `/home/life/route1-stagec/exp003i/code/objectives_i.py` | 3341 | `cc05248a24250c2c825c5d0e7e56a1c0a0d0c59fa65e16b4ba5c19e7e692355a` |
| `code/route1_stagec/exp003i/train_i.py` | `/home/life/route1-stagec/exp003i/code/train_i.py` | 6932 | `8cbba784079fc4d7c8239f3120fb3dd607b5a8638dac43a7fa92a342e4139b65` |
| `code/route1_stagec/metrics.py` | `/home/life/route1-stagec/exp003a/code/metrics.py` | 2129 | `079cb94947b410baef65bdb629be318d471a1a18039b524cecec49be75725749` |
| `code/route1_stagec/soft_objective.py` | `/home/life/route1-stagec/exp003a/code/soft_objective.py` | 1234 | `4a6fe187e0c9910728189b1cbbbf810ed6039ff60bc3e23d5bee74c7d0b3c93e` |

## Evaluated model paths

| Training domain | Method | Seed | Server checkpoint | SHA256 |
|---|---|---|---|---|
| dense | Base | 42 | `/home/life/route1-stagec/exp003c_v2/output/seed42/A6/checkpoints/A6_epoch6.pth` | `55aef370b488d40a157b87c5a14333dd0136252cd9c17d6ee1dc94bbadb04754` |
| dense | w/o Quantile Anchoring (Fixed Zero-Hinge) | 42 | `/home/life/route1-stagec/exp003c_v2/output/seed42/GIN-Aug/checkpoints/GIN-Aug_epoch6.pth` | `527a336c1d22eff8ac299a5b207e90987874f4593d5f8cf92c154579a6a39dd8` |
| dense | Base | 43 | `/home/life/route1-stagec/exp003c_v2/output/seed43/A6/checkpoints/A6_epoch6.pth` | `e481fd87356f76e45ed6374859a8ee23d8999711849a8c89976e6cfce03e17fa` |
| dense | w/o Quantile Anchoring (Fixed Zero-Hinge) | 43 | `/home/life/route1-stagec/exp003c_v2/output/seed43/GIN-Aug/checkpoints/GIN-Aug_epoch6.pth` | `5069f174d53ccb3accd0e980e39639d04b120c029a523e0065163ed5a2ab618f` |
| sues | Base | 42 | `/home/life/route1-stagec/exp003d/output/seed42/Base648/checkpoints/step648.pth` | `216f8ecb2b3bbed86352ec13a5a7384af5b94c1be764632457a4ed222154f341` |
| sues | Base + StdDual | 42 | `/home/life/route1-stagec/exp003d/output/seed42/StdDual/checkpoints/step648.pth` | `051373e7ebe71682acb159ea1506b0fe8b212dcf191f4986d8d968df27d7d6ad` |
| sues | w/o Quantile Anchoring (Fixed Zero-Hinge) | 42 | `/home/life/route1-stagec/exp003d/output/seed42/GIN-Aug/checkpoints/step648.pth` | `8785bd08ce1b1736416e5ead2121d0f19efaffe4f5f9259125d8e81570b385b2` |
| sues | Base | 43 | `/home/life/route1-stagec/exp003d/output/seed43/Base648/checkpoints/step648.pth` | `0d72da51e95ee1885db4bedf51f7b59ebc81ec5fde50cb8db5edd04908fbd0bf` |
| sues | Base + StdDual | 43 | `/home/life/route1-stagec/exp003d/output/seed43/StdDual/checkpoints/step648.pth` | `16994fd747cd1b7b09a2270dd1ad4c6ce8e8d187eabe82dd131b4bc7fe6650d1` |
| sues | w/o Quantile Anchoring (Fixed Zero-Hinge) | 43 | `/home/life/route1-stagec/exp003d/output/seed43/GIN-Aug/checkpoints/step648.pth` | `9271cbd18a5a4fe5a84af7eadd4e74ffa4365a128172f89bb00cc196ba0b9ae6` |
| dense | Base + StdDual | 42 | `/home/life/route1-stagec/exp003e/output/seed42/StdDual/checkpoints/StdDual_epoch6.pth` | `3bc1a5cc71fc306b2cf3472d62ada9c614acd48e2638c371106f6c8c5255aebd` |
| dense | Base + StdDual | 43 | `/home/life/route1-stagec/exp003e/output/seed43/StdDual/checkpoints/StdDual_epoch6.pth` | `6b6dc4baf2536f34e9f024b0549798073c5a541d311742d731824008316555ee` |
| dense | Base + ColorJitter-Dual | 42 | `/home/life/route1-stagec/exp003f/output/seed42/ColorJitter-Dual/checkpoints/ColorJitter-Dual_epoch6.pth` | `97b5346cf2c9e7e2463e285f67a16a4a0e25909ac7f71ab07de934b2a4384ac3` |
| dense | Base + AugMix-Dual | 42 | `/home/life/route1-stagec/exp003f/output/seed42/AugMix-Dual/checkpoints/AugMix-Dual_epoch6.pth` | `c5c4b55ec2190df57d33264894a186868bb8b27de914e4a14fd1ab586254022b` |
| dense | Base + QGIN | 42 | `/home/life/route1-stagec/exp003f/output/seed42/QuantileGIN-Aug/checkpoints/QuantileGIN-Aug_epoch6.pth` | `12de5a75cc3594f7743a7bab41279c0198e90ccde496c5ab4c7b5291f85a8f1c` |
| dense | Base + ColorJitter-Dual | 43 | `/home/life/route1-stagec/exp003f/output/seed43/ColorJitter-Dual/checkpoints/ColorJitter-Dual_epoch6.pth` | `000025db408809c4fd17006c1b0e3c0e4f16ebe063a7210732693af634950f02` |
| dense | Base + AugMix-Dual | 43 | `/home/life/route1-stagec/exp003f/output/seed43/AugMix-Dual/checkpoints/AugMix-Dual_epoch6.pth` | `ce3205e65ca52475121a23cc4d462c81b00e248c281058b697545f4dc2726073` |
| dense | Base + QGIN | 43 | `/home/life/route1-stagec/exp003f/output/seed43/QuantileGIN-Aug/checkpoints/QuantileGIN-Aug_epoch6.pth` | `4ac1c4bbdc5ef5c9310cd6eebfddd9edd4ab8bf93aa37d1d525b222e4e1c4ec1` |
| sues | Base + QGIN | 42 | `/home/life/route1-stagec/exp003g/output/train/sues/seed42/QuantileGIN-Aug/checkpoints/step648.pth` | `5e3cd7fe1fdd7a59e3291a4c305d979f98697275668cbd75596f23bbfe52befe` |
| sues | Base + AugMix-Dual | 42 | `/home/life/route1-stagec/exp003g/output/train/sues/seed42/AugMix-Dual/checkpoints/step648.pth` | `4e19ac3216d0531acdd56029fad125f81cf76de76a6ddaba4a71aebd04640b6d` |
| sues | Base + QGIN | 43 | `/home/life/route1-stagec/exp003g/output/train/sues/seed43/QuantileGIN-Aug/checkpoints/step648.pth` | `e1b46ad6a6bceef087bad655f44dd010fe79d03ccc56a8c5e2b131802b87fadf` |
| sues | Base + AugMix-Dual | 43 | `/home/life/route1-stagec/exp003g/output/train/sues/seed43/AugMix-Dual/checkpoints/step648.pth` | `cbb7491efabc42bf9643233ce9e0195ebd0ce52a25184abb047a8642e3892b35` |
| dense | Sample4Geo | 42 | `/home/life/route1-stagec/exp003h/output/train/dense/seed42/Sample4Geo/step648.pth` | `21d847cf1f3a482fc3f6424ee245100262cfb837701ab52035ba28526603b4f5` |
| dense | Sample4Geo | 43 | `/home/life/route1-stagec/exp003h/output/train/dense/seed43/Sample4Geo/step648.pth` | `8a7c66a54bf412555d31576453ad35ba5e2e3c8904a180a6750f3effbdc4df95` |
| sues | Sample4Geo | 42 | `/home/life/route1-stagec/exp003h/output/train/sues/seed42/Sample4Geo/step648.pth` | `68a0c004fa92669d30ae602da44f6479c0021e32396561aed313980823fc2f77` |
| sues | Sample4Geo | 43 | `/home/life/route1-stagec/exp003h/output/train/sues/seed43/Sample4Geo/step648.pth` | `0ccf8a962736c0737f25fecd001ef355ae4d0aed753dc3e29d49e4e0747585d9` |
| dense | DAC | 42 | `/home/life/route1-stagec/exp003h/output/train/dense/seed42/DAC/step648.pth` | `c4db1e589f00dd4e7aa5a03127240150928f291e28af8df9c9279fd0cb2b732b` |
| dense | DAC | 43 | `/home/life/route1-stagec/exp003h/output/train/dense/seed43/DAC/step648.pth` | `ab6b6d453121583786fbf4fc7cd95e185cf8bd902739400e16ba1ef01d49a03b` |
| sues | DAC | 42 | `/home/life/route1-stagec/exp003h/output/train/sues/seed42/DAC/step648.pth` | `3348e71116a9e024e722019764f0e895fb002a7f3774d953907f5d220a735ad5` |
| sues | DAC | 43 | `/home/life/route1-stagec/exp003h/output/train/sues/seed43/DAC/step648.pth` | `7d77138feac467fe3486584e2d16a2f0a184d0f757c8d4ed594539961dfac383` |
| dense | ConGeo | 42 | `/home/life/route1-stagec/exp003h/output/train/dense/seed42/ConGeo/step648.pth` | `2564554a99d9466665762b89544b5f3aed74b49c97beedfa23e4b4840a69ef2c` |
| dense | ConGeo | 43 | `/home/life/route1-stagec/exp003h/output/train/dense/seed43/ConGeo/step648.pth` | `f24633e2079dc24511904e66e0825fc7225dad9f14cdb440bcc6bd8a7467a62b` |
| sues | ConGeo | 42 | `/home/life/route1-stagec/exp003h/output/train/sues/seed42/ConGeo/step648.pth` | `96f0af2b81e7cc67dd42222acc22776f9a38cffd5ae61271ad6e5093a0e2aac4` |
| sues | ConGeo | 43 | `/home/life/route1-stagec/exp003h/output/train/sues/seed43/ConGeo/step648.pth` | `586534e177947eff22a1b34ae9398d07a80d729a00e94cf85b550cb5c4035a77` |
| dense | SinGeo | 42 | `/home/life/route1-stagec/exp003h/output/train/dense/seed42/SinGeo/step648.pth` | `aaddd8c4ef1306dd137e6115a69bedbcd9f08880afb91c02d9aaca012558cb04` |
| dense | SinGeo | 43 | `/home/life/route1-stagec/exp003h/output/train/dense/seed43/SinGeo/step648.pth` | `aab0a9d7c02716385facade06c971279f99a3f47fefa68965e49ef76e59385da` |
| sues | SinGeo | 42 | `/home/life/route1-stagec/exp003h/output/train/sues/seed42/SinGeo/step648.pth` | `0dafb51c36fe3e4b4bd1abe0ac2a90f07f05a870edee9f556112e622f4252921` |
| sues | SinGeo | 43 | `/home/life/route1-stagec/exp003h/output/train/sues/seed43/SinGeo/step648.pth` | `3d1226251b50a6add4206ee226dab74d729c6da42bf1af77478906e2fbef3a0a` |
| dense | MEAN | 42 | `/home/life/route1-stagec/exp003h/output/train/dense/seed42/MEAN/step648.pth` | `084c4d63dadc7fe868abed54964cd2507dbe359c70aea7562f6d26fe7f4b986c` |
| dense | MEAN | 43 | `/home/life/route1-stagec/exp003h/output/train/dense/seed43/MEAN/step648.pth` | `e4172a01688cb2c64d4437429f244196bd910a7eec54987e6c03702b4d5af29b` |
| sues | MEAN | 42 | `/home/life/route1-stagec/exp003h/output/train/sues/seed42/MEAN/step648.pth` | `fa9368b1436d9758eab78358d799fd483701d31e5b131c27df262a7b6d715d6c` |
| sues | MEAN | 43 | `/home/life/route1-stagec/exp003h/output/train/sues/seed43/MEAN/step648.pth` | `b3fc9eebf46ee7a141c80e36a05c9ac5555d0b579fa8bbe236e7f9e4ae039cb7` |
| dense | QDFL | 42 | `/home/life/route1-stagec/exp003h/output/train/dense/seed42/QDFL/step648.pth` | `c22c64c97d8eccee9cd64f2eeddfe8b4f37254ff51919b1bae647fef19d04087` |
| dense | QDFL | 43 | `/home/life/route1-stagec/exp003h/output/train/dense/seed43/QDFL/step648.pth` | `a2426bff4e57b09a6bc824d5d89341a45d462813ee5eb766fcc494037850d914` |
| sues | QDFL | 42 | `/home/life/route1-stagec/exp003h/output/train/sues/seed42/QDFL/step648.pth` | `f5070a26207fa96535831c4909e6204f5e4b68e2227d11687123d5774a7052a8` |
| sues | QDFL | 43 | `/home/life/route1-stagec/exp003h/output/train/sues/seed43/QDFL/step648.pth` | `e083d4764ad0b1f09d6f17e491f5331f8d77a4625faf971436e77c209a441c0a` |
| dense | MRGeo | 42 | `/home/life/route1-stagec/exp003h/output/train/dense/seed42/MRGeo/step648.pth` | `a9e08314defb4cb0f684858290f20182f30775c0016f4639b2e4c372402ddad3` |
| dense | MRGeo | 43 | `/home/life/route1-stagec/exp003h/output/train/dense/seed43/MRGeo/step648.pth` | `a3833662d374f716501428aef8a0b73d6263f69802f68ab31cf4136852b544fc` |
| sues | MRGeo | 42 | `/home/life/route1-stagec/exp003h/output/train/sues/seed42/MRGeo/step648.pth` | `e6a741c00ec08d054c67c10709ac8cb5e0144748da9f9405703f4fe6691c7858` |
| sues | MRGeo | 43 | `/home/life/route1-stagec/exp003h/output/train/sues/seed43/MRGeo/step648.pth` | `22696687376bee407200075d4e7cfb1d9648913b8e5842ba9d188813ef62f125` |
| dense | S4G-StdDual | 42 | `/home/life/route1-stagec/exp003i/output/train/dense/seed42/S4G-StdDual/step648.pth` | `b9565640b6d9c0f77f75f27554a490cddc912511f0853926a2760517c2da14f4` |
| dense | S4G-QDual | 42 | `/home/life/route1-stagec/exp003i/output/train/dense/seed42/S4G-QDual/step648.pth` | `4d3edcde046ef7593e64668f4fa2866f1093545c27156a72759a554802fd4fd2` |
| dense | SinGeo-QView | 42 | `/home/life/route1-stagec/exp003i/output/train/dense/seed42/SinGeo-QView/step648.pth` | `b623d389fd13b0f8158a0c106c44a3a01eac49b5cc7a0a0c7f5fc2cb3de0b570` |
| dense | ConGeo-QView | 42 | `/home/life/route1-stagec/exp003i/output/train/dense/seed42/ConGeo-QView/step648.pth` | `251838006aefd3ef24e7a31d195d0f7bbf5ddbfd5dd7b713ab5c5f401be1baa7` |
| dense | S4G-StdDual | 43 | `/home/life/route1-stagec/exp003i/output/train/dense/seed43/S4G-StdDual/step648.pth` | `ef5dda3ebeed97391bebe62433a085cde53cc2e4d8c2e3aafdf12c6c906e407c` |
| dense | S4G-QDual | 43 | `/home/life/route1-stagec/exp003i/output/train/dense/seed43/S4G-QDual/step648.pth` | `6e73964db86ed5207c96c2322dd423cc485c6fba095609b08493717316d8fb38` |
| dense | SinGeo-QView | 43 | `/home/life/route1-stagec/exp003i/output/train/dense/seed43/SinGeo-QView/step648.pth` | `f71e819f9c2291385a1ea8aa0e83bd7381040daa2d13a843daba699039f5fe8b` |
| dense | ConGeo-QView | 43 | `/home/life/route1-stagec/exp003i/output/train/dense/seed43/ConGeo-QView/step648.pth` | `6ecd4d53de3749a191c8d8a40486f8ab55452d7aef314de9c63b97b00f49d756` |
| sues | S4G-StdDual | 42 | `/home/life/route1-stagec/exp003i/output/train/sues/seed42/S4G-StdDual/step648.pth` | `5669a8100d04a5084d82c561e214b3a7cc961171f3d268bb58a15a81f9e9360b` |
| sues | S4G-QDual | 42 | `/home/life/route1-stagec/exp003i/output/train/sues/seed42/S4G-QDual/step648.pth` | `16560f5821da24c13a1f52afe05f509974a182ec5f7623b9802d4a43e5c8395a` |
| sues | SinGeo-QView | 42 | `/home/life/route1-stagec/exp003i/output/train/sues/seed42/SinGeo-QView/step648.pth` | `42dbce678df8b0cfd968c35f79b85baec63432d99157497c0336ede6df0b245b` |
| sues | ConGeo-QView | 42 | `/home/life/route1-stagec/exp003i/output/train/sues/seed42/ConGeo-QView/step648.pth` | `251bceb01be8d3bb3e7ffe8106011cde9bcdc253b7fa2b94bd8846118ac83efe` |
| sues | S4G-StdDual | 43 | `/home/life/route1-stagec/exp003i/output/train/sues/seed43/S4G-StdDual/step648.pth` | `b48ff0897efa4e69cbe20792776cbd79f2defdd75d0b8f994ee7ec5df415bbc5` |
| sues | S4G-QDual | 43 | `/home/life/route1-stagec/exp003i/output/train/sues/seed43/S4G-QDual/step648.pth` | `c86bde8b28c158563044c30d476d28b4ec07925769e34bab81548f2f52f5c0b0` |
| sues | SinGeo-QView | 43 | `/home/life/route1-stagec/exp003i/output/train/sues/seed43/SinGeo-QView/step648.pth` | `bee0f84e75ca1ef1c74b304baa4ef80cb60daf0559199aa33e1e61abdb1c27d4` |
| sues | ConGeo-QView | 43 | `/home/life/route1-stagec/exp003i/output/train/sues/seed43/ConGeo-QView/step648.pth` | `f2494c84670c7a9b902058a1a000d7ab308183041550c9b0e328ef86361d2314` |

## Aggregate output hashes

| File | SHA256 |
|---|---|
| `paper_assets/summary_csv/affine_stage0_descriptive_ratios.csv` | `a0ef68c86526c87fbf3fcdd1ac5c6253e891946b738c970de98997f46803fc3b` |
| `paper_assets/summary_csv/affine_stage0_interventions.csv` | `5d6badd61c4b162be4149047f2bc1c9a3f6a6040f031f91b118175f73f79800c` |
| `paper_assets/summary_csv/affine_stage0_ratio_cluster_intervals.json` | `7af4a6de98cc369c826c30c0009b82d3c460773a5c29f764f8b02dcd736463ad` |
| `paper_assets/summary_csv/benchmark_all.csv` | `4e1b1feca48daf2c25d53f9dba93c10a00af6850ede57d126e03b013d2741b86` |
| `paper_assets/summary_csv/checkpoint_sha256.csv` | `6f25dbc586b9f35d0b3bcd46d7098311432943154a12f1c5831e80f528be3dae` |
| `paper_assets/summary_csv/competition_stage0_cluster_intervals.csv` | `76bd886ba4ae5a88bf7dabd1524a0bb958ad122076061aac5714b3a9a46a6f8b` |
| `paper_assets/summary_csv/competition_stage0_summary.csv` | `adc2e254dd5c8a6ad154b6a6b6d82b3200b3f93aa47147a8077c4752381fe486` |
| `paper_assets/summary_csv/cte_paired.csv` | `3240efd38826e8814d2438735c8069b59711ad3c954bffbfee7832a37cf66803` |
| `paper_assets/summary_csv/diagnostic_intervals.csv` | `33ffef4732e0458e33966d78541f4869a5aba84e90b59cfcc03365e4823bfa13` |
| `paper_assets/summary_csv/inference_cost.csv` | `f59592922d73157de7610d9ae6bb93c98a023974e42cbd4b08834c4e48a410f9` |
| `paper_assets/summary_csv/nonlinear_energy_summary.csv` | `59dcd421776f4f4ae019f41fe285d75ae9471dda076b3a7c93232427784b5aa2` |
| `paper_assets/summary_csv/nonlinear_source_hinge_summary.csv` | `4de865ba80982c72aee76b90937c31f5a834758c340927805536053589d29ff4` |
| `paper_assets/summary_csv/nonlinear_source_summary.csv` | `8f589cd2a272c2ed3b864226879e0fc83d6690a68247e054b709347c3fd5d4db` |
| `paper_assets/summary_csv/paired_host_gains.csv` | `60abba6e31e6ecb767a666609796f4f4b5f950b90d944c93bed342b25d8b4b06` |
| `paper_assets/summary_csv/source_operator_intervals.csv` | `66933907909423cd588df0237027dcc95782e7aaef39e545f527c76264d7de7a` |
| `paper_assets/summary_csv/warmup_sha256.csv` | `23940419cd2aa1e0f674e5c4360b647060d4e446d2fce8d328deb55ab106afe1` |

| `paper_assets/summary_csv/release_validation.json` | `d500cfa14db090d14be5176dc2cc1b57b4c8687b4819452fb4765b4d13d355b4` |

## Runtime validation

QGIN was compared against the historical implementation on CPU for three parameter seeds with and without quantile anchoring: output tensors and diagnostic records matched exactly (maximum output error 0.00). Four core tests cover RNG preservation/spatial permutation, constant/identity fallback, Base loss and gradient equivalence, and bootstrap/geographic/AP checks. On the CUDA server, all seven external baseline checkpoints loaded strictly and produced finite descriptors with the recorded dimensions: Sample4Geo/ConGeo/SinGeo/MEAN 768, DAC 1024, QDFL 2048, MRGeo 3072. The portable refactoring has not been used to retrain the benchmark; the tables describe the archived completed runs.

The final validation independently checked 5,868 finite raw-metric cells, 420 native CTE rate cells and all 226 input SHA256 values. The maximum CSV round-trip discrepancy was 4.84 × 10⁻⁹ in the displayed metric units.
