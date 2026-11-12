# EXP-003K: selected cross-domain augmentation comparison

This paper-ready selection compares four specified task-specific augmentation adapters with the historical ConGeo host and ConGeo-QView. Rankings below apply to this selected set.

## Protocol and measurement boundaries

Each adapter is applied to the secondary drone query view during training under the same ConGeo objective, 108-update warmup model and optimizer, six 108-update blocks, and seeds 42 and 43. The selected subset comprises 16 new models and 224 model–target–condition evaluations. ConGeo and ConGeo-QView are previously archived references; they were not retrained.

The four adapters follow the task-specific configurations described in [the operator contract](../../configs_and_contracts/exp003k/PROTOCOL.md). They are not full reproductions of the cited methods. All models use the same EVA-family backbone identifier and single-encoder retrieval interface. Synthetic Snow and Fog do not establish performance under real weather.

CorrMean6 equally averages Fog, Snow, Blur, Gamma, ExposureClip and Posterize4. R@1 and AP are percentages, Dis@1 is in metres and >200m is a percentage. SUES-200 has no GPS measurements, so both distance columns are unavailable for that target. Dense AP uses the historical trapezoidal multi-positive convention; SUES AP uses a single-positive convention. Two-seed averages do not measure training-seed uncertainty.

## Four-direction results (two-seed mean)

| Train → target | Method | Clean R@1 | Snow R@1 | Snow AP | CorrMean6 R@1 | CorrMean6 AP | CorrMean6 Dis@1 (m) | CorrMean6 >200m |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| dense → dense | ConGeo | 88.48 | 70.83 | 62.80 | 82.61 | 74.14 | 94.1 | 4.10 |
| dense → dense | SLAug* | 88.93 | 76.83 | 69.21 | 85.29 | 76.85 | 61.0 | 2.67 |
| dense → dense | PASTA* | 88.40 | 71.19 | 63.09 | 83.23 | 74.58 | 86.0 | 3.82 |
| dense → dense | AFA* | 88.48 | 71.75 | 63.42 | 83.10 | 74.63 | 92.9 | 4.00 |
| dense → dense | RaffeSDG* | 89.12 | 73.38 | 64.69 | 83.82 | 74.95 | 82.9 | 3.55 |
| dense → dense | ConGeo-QView | 89.06 | 81.38 | 73.10 | 85.73 | 77.39 | 52.7 | 2.20 |
| sues → sues | ConGeo | 94.03 | 67.91 | 77.32 | 87.24 | 91.63 | — | — |
| sues → sues | SLAug* | 94.85 | 78.86 | 86.08 | 90.85 | 94.32 | — | — |
| sues → sues | PASTA* | 94.55 | 67.06 | 76.33 | 87.71 | 91.91 | — | — |
| sues → sues | AFA* | 94.39 | 65.87 | 75.75 | 87.19 | 91.58 | — | — |
| sues → sues | RaffeSDG* | 94.16 | 68.53 | 78.16 | 87.07 | 91.69 | — | — |
| sues → sues | ConGeo-QView | 95.73 | 83.83 | 89.73 | 92.46 | 95.43 | — | — |
| dense → sues | ConGeo | 77.29 | 49.57 | 59.19 | 71.08 | 77.90 | — | — |
| dense → sues | SLAug* | 74.88 | 51.34 | 60.87 | 70.34 | 77.32 | — | — |
| dense → sues | PASTA* | 78.51 | 49.32 | 59.27 | 72.47 | 79.15 | — | — |
| dense → sues | AFA* | 77.87 | 49.35 | 59.13 | 71.74 | 78.48 | — | — |
| dense → sues | RaffeSDG* | 79.35 | 52.32 | 62.10 | 73.34 | 79.86 | — | — |
| dense → sues | ConGeo-QView | 77.09 | 60.18 | 68.66 | 73.49 | 79.90 | — | — |
| sues → dense | ConGeo | 20.85 | 10.47 | 7.83 | 17.52 | 12.07 | 760.5 | 34.24 |
| sues → dense | SLAug* | 22.99 | 12.46 | 9.83 | 20.56 | 14.89 | 762.5 | 31.35 |
| sues → dense | PASTA* | 21.45 | 11.58 | 8.33 | 18.75 | 12.94 | 697.7 | 32.19 |
| sues → dense | AFA* | 21.88 | 11.11 | 8.31 | 19.16 | 13.27 | 712.9 | 32.28 |
| sues → dense | RaffeSDG* | 20.51 | 10.08 | 7.46 | 17.81 | 12.01 | 769.4 | 34.52 |
| sues → dense | ConGeo-QView | 24.67 | 16.45 | 11.77 | 22.33 | 15.45 | 646.6 | 27.71 |

## R@1 by condition (two-seed mean)

| Train → target | Method | Clean | Fog | Snow | Blur | Gamma | ExposureClip | Posterize4 | CorrMean6 | NonSnowMean5 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| dense → dense | ConGeo | 88.48 | 81.08 | 70.83 | 87.82 | 87.92 | 79.69 | 88.31 | 82.61 | 84.96 |
| dense → dense | SLAug | 88.93 | 82.90 | 76.83 | 88.46 | 88.78 | 85.69 | 89.04 | 85.29 | 86.98 |
| dense → dense | PASTA | 88.40 | 82.56 | 71.19 | 88.03 | 88.31 | 80.63 | 88.65 | 83.23 | 85.64 |
| dense → dense | AFA | 88.48 | 82.26 | 71.75 | 88.29 | 87.99 | 80.03 | 88.27 | 83.10 | 85.37 |
| dense → dense | RaffeSDG | 89.12 | 82.43 | 73.38 | 88.61 | 89.00 | 80.74 | 88.78 | 83.82 | 85.91 |
| dense → dense | ConGeo-QView | 89.06 | 82.56 | 81.38 | 88.80 | 88.61 | 84.13 | 88.89 | 85.73 | 86.60 |
| sues → sues | ConGeo | 94.03 | 93.15 | 67.91 | 92.22 | 93.43 | 83.32 | 93.39 | 87.24 | 91.10 |
| sues → sues | SLAug | 94.85 | 94.08 | 78.86 | 93.19 | 94.51 | 90.02 | 94.44 | 90.85 | 93.25 |
| sues → sues | PASTA | 94.55 | 93.57 | 67.06 | 92.67 | 94.30 | 84.37 | 94.30 | 87.71 | 91.84 |
| sues → sues | AFA | 94.39 | 93.19 | 65.87 | 92.78 | 93.47 | 83.94 | 93.87 | 87.19 | 91.45 |
| sues → sues | RaffeSDG | 94.16 | 92.66 | 68.53 | 91.09 | 93.29 | 83.43 | 93.38 | 87.07 | 90.77 |
| sues → sues | ConGeo-QView | 95.73 | 94.84 | 83.83 | 93.89 | 95.38 | 91.48 | 95.36 | 92.46 | 94.19 |
| dense → sues | ConGeo | 77.29 | 78.31 | 49.57 | 78.12 | 76.27 | 67.40 | 76.84 | 71.08 | 75.39 |
| dense → sues | SLAug | 74.88 | 75.81 | 51.34 | 75.72 | 74.47 | 69.93 | 74.77 | 70.34 | 74.14 |
| dense → sues | PASTA | 78.51 | 79.63 | 49.32 | 79.92 | 78.17 | 69.47 | 78.34 | 72.47 | 77.11 |
| dense → sues | AFA | 77.87 | 79.06 | 49.35 | 79.04 | 77.39 | 68.02 | 77.57 | 71.74 | 76.22 |
| dense → sues | RaffeSDG | 79.35 | 80.02 | 52.32 | 79.88 | 78.63 | 70.18 | 78.98 | 73.34 | 77.54 |
| dense → sues | ConGeo-QView | 77.09 | 77.82 | 60.18 | 78.39 | 76.85 | 70.93 | 76.78 | 73.49 | 76.16 |
| sues → dense | ConGeo | 20.85 | 22.69 | 10.47 | 19.54 | 19.33 | 12.66 | 20.44 | 17.52 | 18.93 |
| sues → dense | SLAug | 22.99 | 25.27 | 12.46 | 22.65 | 22.89 | 16.99 | 23.12 | 20.56 | 22.18 |
| sues → dense | PASTA | 21.45 | 23.23 | 11.58 | 20.83 | 20.96 | 14.48 | 21.41 | 18.75 | 20.18 |
| sues → dense | AFA | 21.88 | 23.55 | 11.11 | 22.14 | 21.94 | 14.05 | 22.18 | 19.16 | 20.77 |
| sues → dense | RaffeSDG | 20.51 | 23.12 | 10.08 | 20.29 | 19.78 | 12.98 | 20.61 | 17.81 | 19.36 |
| sues → dense | ConGeo-QView | 24.67 | 25.44 | 16.45 | 24.56 | 24.58 | 17.61 | 25.35 | 22.33 | 23.51 |

## Four-direction macro-average (descriptive)

Each direction contributes equally; macro AP combines two different dataset-specific AP conventions.

| Method | Clean R@1 | Snow R@1 | CorrMean6 R@1 | CorrMean6 AP |
| --- | ---: | ---: | ---: | ---: |
| ConGeo | 70.16 | 49.69 | 64.61 | 63.94 |
| SLAug* | 70.41 | 54.87 | 66.76 | 65.85 |
| PASTA* | 70.73 | 49.79 | 65.54 | 64.65 |
| AFA* | 70.65 | 49.52 | 65.30 | 64.49 |
| RaffeSDG* | 70.78 | 51.08 | 65.51 | 64.63 |
| ConGeo-QView | 71.64 | 60.46 | 68.50 | 67.04 |

## Paired differences for R@1

QView minus each selected reference, in percentage points, with 2,000-draw paired 95% place-cluster bootstrap intervals. Both seeds use the same resampled test places; intervals condition on these trained models and do not cover retraining variability.

| Train → target | Reference | Snow Δ [95% CI] | CorrMean6 Δ [95% CI] |
| --- | --- | ---: | ---: |
| dense → dense | ConGeo | +10.55 [+9.31, +11.84] | +3.12 [+2.51, +3.71] |
| dense → dense | SLAug | +4.55 [+3.47, +5.68] | +0.44 [-0.22, +1.11] |
| dense → dense | PASTA | +10.19 [+8.94, +11.45] | +2.50 [+1.85, +3.14] |
| dense → dense | AFA | +9.63 [+8.43, +10.83] | +2.63 [+1.98, +3.25] |
| dense → dense | RaffeSDG | +8.00 [+6.80, +9.20] | +1.91 [+1.33, +2.47] |
| sues → sues | ConGeo | +15.93 [+11.63, +20.56] | +5.22 [+3.21, +7.45] |
| sues → sues | SLAug | +4.98 [+1.95, +8.35] | +1.61 [-0.05, +3.51] |
| sues → sues | PASTA | +16.77 [+12.32, +21.85] | +4.75 [+2.87, +6.80] |
| sues → sues | AFA | +17.97 [+13.35, +22.69] | +5.27 [+3.15, +7.67] |
| sues → sues | RaffeSDG | +15.30 [+11.31, +19.90] | +5.40 [+3.45, +7.48] |
| dense → sues | ConGeo | +10.61 [+8.29, +12.84] | +2.41 [+1.29, +3.45] |
| dense → sues | SLAug | +8.83 [+6.62, +10.96] | +3.15 [+2.16, +4.20] |
| dense → sues | PASTA | +10.86 [+8.40, +13.22] | +1.02 [-0.13, +2.06] |
| dense → sues | AFA | +10.83 [+8.33, +13.17] | +1.75 [+0.72, +2.76] |
| dense → sues | RaffeSDG | +7.86 [+5.07, +10.31] | +0.15 [-0.96, +1.18] |
| sues → dense | ConGeo | +5.98 [+4.57, +7.47] | +4.81 [+3.60, +5.95] |
| sues → dense | SLAug | +3.99 [+2.51, +5.45] | +1.77 [+0.54, +3.06] |
| sues → dense | PASTA | +4.87 [+3.52, +6.28] | +3.59 [+2.49, +4.70] |
| sues → dense | AFA | +5.34 [+3.90, +6.78] | +3.17 [+2.03, +4.34] |
| sues → dense | RaffeSDG | +6.37 [+4.93, +7.94] | +4.52 [+3.29, +5.82] |

A positive point estimate whose interval includes zero is not presented as a resolved advantage. These are exploratory comparisons without a multiple-testing correction.

## Source128 operator diagnostics

Thirty-two source images were sampled four times per operator. E1 and E2 are held-out RMS residuals after per-channel affine and full-channel affine fits, respectively. DC is squared spatial-mean perturbation energy; AC is all remaining spatial perturbation energy, not a high-frequency band. The edge statistic is the pixelwise RGB Sobel gradient cosine; pixels for which it is undefined are set to zero. These descriptive measurements do not establish a causal mechanism.

| Method | E1 | E2 | DC | AC | Edge cosine | Valid edge cosine | Valid fraction |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SLAug | 0.0365 | 0.0346 | 0.767 | 0.233 | 0.748 | 0.927 | 0.786 |
| PASTA | 0.0939 | 0.0938 | 0.289 | 0.711 | 0.450 | 0.455 | 0.988 |
| AFA | 0.0564 | 0.0564 | 0.009 | 0.991 | 0.596 | 0.604 | 0.988 |
| RaffeSDG | 0.0588 | 0.0570 | 0.407 | 0.593 | 0.932 | 0.943 | 0.988 |
| QGIN | 0.0582 | 0.0502 | 0.596 | 0.404 | 0.684 | 0.694 | 0.988 |

## Competitive takeover events: two reference anchors

A competitive takeover event (CTE) is a retrieval event, not an observed flight trajectory. For each reference anchor, Q0 comprises the reference model’s Clean-correct queries. Rescue and new-failure rates have different denominators; net gain is (rescued CTEs − new failures) / |Q0|. The table reports percentages, averaging per-seed rates; CorrMean6 also averages six condition-specific rates. Counts and denominators for each seed and condition are retained in the CTE CSV.

| Train → target | Anchor | Method | Condition | Rescue rate | New-failure rate | Net gain / Q0 |
| --- | --- | --- | --- | ---: | ---: | ---: |
| dense → dense | ConGeo_clean | ConGeo | Snow | 0.00 | 0.00 | 0.00 |
| dense → dense | ConGeo_clean | ConGeo | CorrMean6 | 0.00 | 0.00 | 0.00 |
| dense → dense | ConGeo_clean | SLAug | Snow | 46.83 | 4.59 | 1.47 |
| dense → dense | ConGeo_clean | SLAug | CorrMean6 | 54.53 | 3.54 | -1.42 |
| dense → dense | ConGeo_clean | PASTA | Snow | 23.21 | 6.21 | -2.33 |
| dense → dense | ConGeo_clean | PASTA | CorrMean6 | 27.23 | 3.39 | -2.15 |
| dense → dense | ConGeo_clean | AFA | Snow | 19.08 | 4.35 | -1.33 |
| dense → dense | ConGeo_clean | AFA | CorrMean6 | 26.88 | 2.58 | -1.56 |
| dense → dense | ConGeo_clean | RaffeSDG | Snow | 31.06 | 5.48 | -0.89 |
| dense → dense | ConGeo_clean | RaffeSDG | CorrMean6 | 33.10 | 3.50 | -2.06 |
| dense → dense | ConGeo_clean | ConGeo-QView | Snow | 69.10 | 3.12 | 4.98 |
| dense → dense | ConGeo_clean | ConGeo-QView | CorrMean6 | 55.63 | 3.19 | -0.89 |
| dense → dense | Base_clean | ConGeo | Snow | 54.45 | 15.63 | -4.02 |
| dense → dense | Base_clean | ConGeo | CorrMean6 | 72.48 | 9.42 | -5.57 |
| dense → dense | Base_clean | SLAug | Snow | 67.40 | 11.52 | 0.78 |
| dense → dense | Base_clean | SLAug | CorrMean6 | 84.48 | 7.68 | -3.59 |
| dense → dense | Base_clean | PASTA | Snow | 57.08 | 15.10 | -3.28 |
| dense → dense | Base_clean | PASTA | CorrMean6 | 73.66 | 8.95 | -5.05 |
| dense → dense | Base_clean | AFA | Snow | 55.71 | 14.94 | -3.33 |
| dense → dense | Base_clean | AFA | CorrMean6 | 74.58 | 9.06 | -5.19 |
| dense → dense | Base_clean | RaffeSDG | Snow | 59.80 | 13.53 | -1.74 |
| dense → dense | Base_clean | RaffeSDG | CorrMean6 | 74.15 | 8.37 | -4.52 |
| dense → dense | Base_clean | ConGeo-QView | Snow | 77.38 | 8.15 | 4.58 |
| dense → dense | Base_clean | ConGeo-QView | CorrMean6 | 80.32 | 7.15 | -3.09 |
| sues → sues | ConGeo_clean | ConGeo | Snow | 0.00 | 0.00 | 0.00 |
| sues → sues | ConGeo_clean | ConGeo | CorrMean6 | 0.00 | 0.00 | 0.00 |
| sues → sues | ConGeo_clean | SLAug | Snow | 54.65 | 4.22 | 4.54 |
| sues → sues | ConGeo_clean | SLAug | CorrMean6 | 64.15 | 2.57 | 0.05 |
| sues → sues | ConGeo_clean | PASTA | Snow | 19.69 | 7.70 | -2.78 |
| sues → sues | ConGeo_clean | PASTA | CorrMean6 | 48.20 | 3.02 | -1.47 |
| sues → sues | ConGeo_clean | AFA | Snow | 15.28 | 7.78 | -3.43 |
| sues → sues | ConGeo_clean | AFA | CorrMean6 | 44.10 | 2.72 | -1.36 |
| sues → sues | ConGeo_clean | RaffeSDG | Snow | 22.44 | 7.02 | -1.91 |
| sues → sues | ConGeo_clean | RaffeSDG | CorrMean6 | 34.35 | 3.30 | -1.93 |
| sues → sues | ConGeo_clean | ConGeo-QView | Snow | 69.18 | 2.96 | 7.42 |
| sues → sues | ConGeo_clean | ConGeo-QView | CorrMean6 | 65.66 | 2.07 | 0.81 |
| sues → sues | Base_clean | ConGeo | Snow | 45.72 | 15.36 | -3.34 |
| sues → sues | Base_clean | ConGeo | CorrMean6 | 71.61 | 5.73 | -1.99 |
| sues → sues | Base_clean | SLAug | Snow | 63.35 | 8.38 | 4.43 |
| sues → sues | Base_clean | SLAug | CorrMean6 | 81.07 | 3.60 | 0.50 |
| sues → sues | Base_clean | PASTA | Snow | 45.30 | 15.88 | -3.76 |
| sues → sues | Base_clean | PASTA | CorrMean6 | 75.86 | 5.64 | -1.74 |
| sues → sues | Base_clean | AFA | Snow | 43.23 | 16.99 | -4.88 |
| sues → sues | Base_clean | AFA | CorrMean6 | 73.82 | 5.87 | -2.03 |
| sues → sues | Base_clean | RaffeSDG | Snow | 47.24 | 15.72 | -3.33 |
| sues → sues | Base_clean | RaffeSDG | CorrMean6 | 71.77 | 6.19 | -2.37 |
| sues → sues | Base_clean | ConGeo-QView | Snow | 68.59 | 5.52 | 7.31 |
| sues → sues | Base_clean | ConGeo-QView | CorrMean6 | 84.28 | 2.81 | 1.30 |
| dense → sues | ConGeo_clean | ConGeo | Snow | 0.00 | 0.00 | 0.00 |
| dense → sues | ConGeo_clean | ConGeo | CorrMean6 | 0.00 | 0.00 | 0.00 |
| dense → sues | ConGeo_clean | SLAug | Snow | 31.01 | 9.93 | -0.74 |
| dense → sues | ConGeo_clean | SLAug | CorrMean6 | 34.36 | 5.82 | -3.38 |
| dense → sues | ConGeo_clean | PASTA | Snow | 16.41 | 7.97 | -2.08 |
| dense → sues | ConGeo_clean | PASTA | CorrMean6 | 42.45 | 3.12 | -1.45 |
| dense → sues | ConGeo_clean | AFA | Snow | 13.72 | 6.45 | -1.64 |
| dense → sues | ConGeo_clean | AFA | CorrMean6 | 40.15 | 2.65 | -1.25 |
| dense → sues | ConGeo_clean | RaffeSDG | Snow | 29.76 | 7.69 | 0.45 |
| dense → sues | ConGeo_clean | RaffeSDG | CorrMean6 | 45.28 | 3.14 | -1.07 |
| dense → sues | ConGeo_clean | ConGeo-QView | Snow | 57.91 | 4.48 | 7.31 |
| dense → sues | ConGeo_clean | ConGeo-QView | CorrMean6 | 49.71 | 3.76 | -0.95 |
| dense → sues | Base_clean | ConGeo | Snow | 37.47 | 22.17 | -9.74 |
| dense → sues | Base_clean | ConGeo | CorrMean6 | 43.67 | 11.04 | -8.06 |
| dense → sues | Base_clean | SLAug | Snow | 42.21 | 21.32 | -8.47 |
| dense → sues | Base_clean | SLAug | CorrMean6 | 53.45 | 11.93 | -8.73 |
| dense → sues | Base_clean | PASTA | Snow | 36.42 | 22.88 | -10.33 |
| dense → sues | Base_clean | PASTA | CorrMean6 | 44.34 | 10.19 | -7.24 |
| dense → sues | Base_clean | AFA | Snow | 36.36 | 22.70 | -10.20 |
| dense → sues | Base_clean | AFA | CorrMean6 | 44.43 | 10.65 | -7.67 |
| dense → sues | Base_clean | RaffeSDG | Snow | 43.12 | 19.93 | -7.44 |
| dense → sues | Base_clean | RaffeSDG | CorrMean6 | 48.66 | 9.49 | -6.55 |
| dense → sues | Base_clean | ConGeo-QView | Snow | 59.03 | 13.58 | -1.03 |
| dense → sues | Base_clean | ConGeo-QView | CorrMean6 | 59.74 | 9.23 | -6.21 |
| sues → dense | ConGeo_clean | ConGeo | Snow | 0.00 | 0.00 | 0.00 |
| sues → dense | ConGeo_clean | ConGeo | CorrMean6 | 0.00 | 0.00 | 0.00 |
| sues → dense | ConGeo_clean | SLAug | Snow | 16.42 | 44.54 | -6.48 |
| sues → dense | ConGeo_clean | SLAug | CorrMean6 | 35.40 | 39.02 | -17.48 |
| sues → dense | ConGeo_clean | PASTA | Snow | 13.46 | 33.23 | -4.41 |
| sues → dense | ConGeo_clean | PASTA | CorrMean6 | 26.87 | 29.43 | -13.32 |
| sues → dense | ConGeo_clean | AFA | Snow | 12.14 | 34.89 | -5.34 |
| sues → dense | ConGeo_clean | AFA | CorrMean6 | 27.68 | 26.75 | -11.29 |
| sues → dense | ConGeo_clean | RaffeSDG | Snow | 12.10 | 41.96 | -7.40 |
| sues → dense | ConGeo_clean | RaffeSDG | CorrMean6 | 22.70 | 34.43 | -16.72 |
| sues → dense | ConGeo_clean | ConGeo-QView | Snow | 27.81 | 35.70 | 0.34 |
| sues → dense | ConGeo_clean | ConGeo-QView | CorrMean6 | 38.75 | 34.69 | -14.45 |
| sues → dense | Base_clean | ConGeo | Snow | 15.97 | 65.74 | -13.32 |
| sues → dense | Base_clean | ConGeo | CorrMean6 | 30.90 | 55.05 | -27.82 |
| sues → dense | Base_clean | SLAug | Snow | 19.70 | 60.74 | -10.90 |
| sues → dense | Base_clean | SLAug | CorrMean6 | 37.07 | 50.41 | -23.89 |
| sues → dense | Base_clean | PASTA | Snow | 20.02 | 71.84 | -13.77 |
| sues → dense | Base_clean | PASTA | CorrMean6 | 35.73 | 55.40 | -27.09 |
| sues → dense | Base_clean | AFA | Snow | 18.52 | 66.40 | -12.51 |
| sues → dense | Base_clean | AFA | CorrMean6 | 31.33 | 52.45 | -25.67 |
| sues → dense | Base_clean | RaffeSDG | Snow | 12.15 | 66.38 | -15.14 |
| sues → dense | Base_clean | RaffeSDG | CorrMean6 | 31.87 | 54.70 | -27.45 |
| sues → dense | Base_clean | ConGeo-QView | Snow | 31.30 | 58.76 | -6.06 |
| sues → dense | Base_clean | ConGeo-QView | CorrMean6 | 40.08 | 50.65 | -23.66 |

## Suggested manuscript text

**English.** We compared four selected, task-specific cross-domain augmentation adapters under the same ConGeo host, warmup and update budget. In this selected comparison, ConGeo-QView achieved the highest two-seed point estimates for Snow R@1 and CorrMean6 R@1/AP in all four train–test directions. It also had the lowest CorrMean6 distance and >200 m error among these references in the two directions with DenseUAV as the target. Several paired CorrMean6 R@1 intervals include zero; we therefore report the intervals and avoid treating every point-estimate ranking as a resolved difference. The adapters are controlled implementations, not complete reproductions of the original methods.

**中文。** 我们在相同 ConGeo 宿主、warmup 和更新预算下，对四种选定的跨领域增强适配体进行受控比较。在这一选定对照集合中，ConGeo-QView 在四个训练—测试方向的 Snow R@1 和 CorrMean6 R@1/AP 双种子点估计最高；以 DenseUAV 为测试域的两个方向也具有最低的 CorrMean6 距离和大于 200 米错误率。部分 CorrMean6 R@1 配对区间跨零，因此同时报告区间，不能把每个点估计排序都解释为确定优势。各对照是受控适配体，并非原方法的完整复现。

## Evidence and interpretation

- Full per-condition and per-seed aggregates: [benchmark metrics](benchmark_metrics.csv).
- Paired intervals: [bootstrap CSV](paired_bootstrap_ci.csv).
- Competitive takeover event counts and rates: [CTE CSV](competitive_events.csv). CTE describes a retrieval competition event, not an observed flight trajectory; net gain must be interpreted with its reference anchor and denominator.
- Operator-level source observations: [summary](operator_diagnostics.csv), [per-pair values](operator_diagnostics_per_pair.csv), [exploratory paired intervals](operator_diagnostics_paired_ci.csv).
- [Training records](training_curves.csv), [checkpoint hashes](checkpoint_checksums.json), [evaluation hashes](evaluation_checksums.json), [smoke checks](smoke_verification.json), [operator equivalence checks](operator_code_equivalence.json), [data source verification](data_source_verification.json), and [selected protocol](selected_protocol.json).

Data, image features, original per-query outputs and model/optimizer binaries are not included; recorded hashes identify the archived files. The released training entry point is a portable refactoring and has not been used to retrain these archived results.
