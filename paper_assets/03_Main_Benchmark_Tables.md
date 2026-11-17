# Three-seed benchmark

All entries are R@1 percent, mean ± sample standard deviation across seeds 42/43/44. CorrMean6 averages Fog, Snow, Blur, Gamma, ExposureClip and Posterize4. All models use the shared EVA-02 backbone, 384×384 input and 648 training updates. Paired differences are in percentage points with 2,000-draw 95% seed-by-location percentile intervals. Four-direction means weight directions equally.

## Table 1. Hosts and controls

| Method | Dense→Dense Clean / Snow / CorrMean6 | SUES→SUES Clean / Snow / CorrMean6 | Dense→SUES Clean / Snow / CorrMean6 | SUES→Dense Clean / Snow / CorrMean6 | 4-dir CorrMean6 |
| --- | --- | --- | --- | --- | --- |
| DAC | 83.87 ± 0.63 / 64.02 ± 1.40 / 78.06 ± 1.00 | 94.02 ± 0.32 / 65.71 ± 1.62 / 87.14 ± 0.30 | 77.10 ± 1.43 / 49.75 ± 1.98 / 71.48 ± 1.00 | 20.23 ± 1.33 / 8.68 ± 1.09 / 17.32 ± 1.63 | 63.50 |
| MEAN | 85.17 ± 0.67 / 63.56 ± 2.53 / 78.97 ± 0.94 | 93.23 ± 0.63 / 64.59 ± 1.36 / 86.66 ± 0.52 | 77.70 ± 0.94 / 46.86 ± 1.79 / 71.40 ± 1.26 | 22.09 ± 1.89 / 10.32 ± 0.61 / 19.43 ± 1.86 | 64.11 |
| Base (EVA-02 + Label Smoothing) | 84.68 ± 0.76 / 66.22 ± 1.92 / 77.71 ± 0.87 | 89.96 ± 1.22 / 65.98 ± 2.50 / 82.67 ± 1.42 | 76.00 ± 1.55 / 52.08 ± 3.30 / 70.39 ± 1.49 | 13.83 ± 0.64 / 7.87 ± 1.16 / 12.32 ± 0.94 | 60.77 |
| Base + QGIN | 86.21 ± 0.77 / 78.08 ± 0.67 / 81.89 ± 0.63 | 94.15 ± 0.07 / 84.04 ± 1.31 / 90.86 ± 0.36 | 75.13 ± 1.19 / 62.98 ± 1.10 / 72.30 ± 0.78 | 19.55 ± 1.33 / 14.69 ± 1.35 / 18.54 ± 1.07 | 65.90 |
| Sample4Geo | 85.54 ± 1.68 / 64.59 ± 0.71 / 78.88 ± 1.45 | 95.21 ± 0.39 / 70.72 ± 3.26 / 88.75 ± 0.40 | 82.23 ± 1.54 / 52.96 ± 2.18 / 76.32 ± 1.70 | 22.31 ± 0.23 / 11.80 ± 0.26 / 19.05 ± 0.10 | 65.75 |
| S4G-QDual | 86.11 ± 0.39 / 79.55 ± 1.50 / 83.05 ± 0.90 | 96.30 ± 0.81 / 87.30 ± 1.30 / 93.82 ± 0.80 | 78.74 ± 1.16 / 65.03 ± 1.38 / 75.90 ± 0.88 | 26.08 ± 1.93 / 17.75 ± 1.11 / 23.20 ± 1.49 | 68.99 |
| ConGeo | 87.99 ± 1.35 / 70.70 ± 0.76 / 82.32 ± 1.12 | 93.77 ± 0.46 / 65.46 ± 4.35 / 86.48 ± 1.32 | 77.08 ± 0.50 / 50.00 ± 2.34 / 70.86 ± 0.49 | 19.91 ± 1.65 / 10.28 ± 1.00 / 17.03 ± 0.92 | 64.17 |
| ConGeo-QView | 89.00 ± 0.69 / 81.38 ± 0.73 / 85.82 ± 0.98 | 95.73 ± 0.02 / 83.18 ± 1.45 / 92.39 ± 0.13 | 76.91 ± 0.68 / 61.20 ± 1.96 / 73.52 ± 0.24 | 23.87 ± 1.40 / 16.00 ± 1.14 / 21.80 ± 0.95 | 68.38 |
| SinGeo | 89.33 ± 0.20 / 71.09 ± 0.90 / 83.26 ± 0.13 | 92.84 ± 1.72 / 63.41 ± 2.76 / 84.32 ± 1.61 | 73.23 ± 0.32 / 48.08 ± 2.64 / 67.62 ± 0.87 | 19.16 ± 2.25 / 9.67 ± 1.08 / 15.97 ± 2.02 | 62.79 |
| SinGeo-QView | 90.45 ± 0.58 / 82.91 ± 0.98 / 87.09 ± 0.49 | 93.75 ± 0.49 / 80.52 ± 0.75 / 89.71 ± 0.86 | 71.32 ± 1.00 / 57.36 ± 1.54 / 68.21 ± 0.39 | 23.21 ± 2.12 / 16.39 ± 0.60 / 20.79 ± 1.77 | 66.45 |

CorrMean6 paired gain, difference [95% CI] in percentage points:

| Host pair | Dense→Dense | SUES→SUES | Dense→SUES | SUES→Dense |
| --- | --- | --- | --- | --- |
| Base (EVA-02 + Label Smoothing) → Base + QGIN | +4.18 [+3.15, +5.22] | +8.19 [+5.45, +11.28] | +1.91 [+0.14, +3.70] | +6.22 [+4.62, +7.82] |
| Sample4Geo → S4G-QDual | +4.17 [+2.72, +5.44] | +5.07 [+3.27, +7.28] | -0.42 [-3.18, +2.27] | +4.15 [+2.16, +5.99] |
| ConGeo → ConGeo-QView | +3.50 [+2.62, +4.47] | +5.91 [+3.61, +8.44] | +2.66 [+1.34, +3.99] | +4.77 [+3.48, +6.12] |
| SinGeo → SinGeo-QView | +3.82 [+2.97, +4.69] | +5.39 [+2.26, +8.77] | +0.59 [-1.23, +2.33] | +4.83 [+3.02, +6.55] |

## Table 2. Adapted cross-domain operators

The operators are controlled adapters applied to ConGeo: the associated papers and implementation differences are documented in [the adapter contract](../configs_and_contracts/augmentation_adapters/PROTOCOL.md).

### CorrMean6 R@1 (%)

| Method | Dense→Dense | SUES→SUES | Dense→SUES | SUES→Dense | 4-direction mean |
| --- | --- | --- | --- | --- | --- |
| ConGeo | 82.32 ± 1.12 | 86.48 ± 1.32 | 70.86 ± 0.49 | 17.03 ± 0.92 | 64.17 |
| SLAug | 85.28 ± 1.27 | 90.66 ± 0.39 | 70.20 ± 0.68 | 20.28 ± 0.62 | 66.61 |
| PASTA | 82.96 ± 1.20 | 87.47 ± 0.58 | 72.47 ± 0.62 | 18.39 ± 0.68 | 65.32 |
| AFA | 82.88 ± 1.13 | 86.68 ± 0.88 | 71.37 ± 0.82 | 18.58 ± 1.00 | 64.88 |
| RaffeSDG | 83.27 ± 1.26 | 86.40 ± 1.22 | 73.30 ± 0.94 | 17.02 ± 1.39 | 65.00 |
| ConGeo-QView | 85.82 ± 0.98 | 92.39 ± 0.13 | 73.52 ± 0.24 | 21.80 ± 0.95 | 68.38 |

### Snow R@1 (%)

| Method | Dense→Dense | SUES→SUES | Dense→SUES | SUES→Dense | 4-direction mean |
| --- | --- | --- | --- | --- | --- |
| ConGeo | 70.70 ± 0.76 | 65.46 ± 4.35 | 50.00 ± 2.34 | 10.28 ± 1.00 | 49.11 |
| SLAug | 77.31 ± 1.60 | 76.56 ± 4.38 | 51.98 ± 1.10 | 12.44 ± 0.04 | 54.57 |
| PASTA | 70.80 ± 1.33 | 65.26 ± 3.74 | 49.99 ± 1.77 | 11.51 ± 0.36 | 49.39 |
| AFA | 71.13 ± 1.39 | 64.15 ± 3.05 | 48.93 ± 0.84 | 10.95 ± 0.58 | 48.79 |
| RaffeSDG | 73.26 ± 0.82 | 66.09 ± 4.44 | 53.11 ± 1.53 | 9.44 ± 1.13 | 50.47 |
| ConGeo-QView | 81.38 ± 0.73 | 83.18 ± 1.45 | 61.20 ± 1.96 | 16.00 ± 1.14 | 60.44 |

### CorrMean6 AP (%)

| Method | Dense→Dense | SUES→SUES | Dense→SUES | SUES→Dense | 4-direction mean |
| --- | --- | --- | --- | --- | --- |
| ConGeo | 73.73 ± 1.05 | 91.11 ± 0.91 | 77.75 ± 0.36 | 11.87 ± 0.58 | 63.61 |
| SLAug | 76.73 ± 1.06 | 94.23 ± 0.23 | 77.20 ± 0.59 | 14.67 ± 0.43 | 65.71 |
| PASTA | 74.22 ± 1.22 | 91.74 ± 0.44 | 79.16 ± 0.52 | 12.69 ± 0.48 | 64.45 |
| AFA | 74.26 ± 1.11 | 91.25 ± 0.57 | 78.22 ± 0.65 | 12.85 ± 0.82 | 64.14 |
| RaffeSDG | 74.55 ± 0.95 | 91.22 ± 0.87 | 79.81 ± 0.85 | 11.60 ± 0.75 | 64.29 |
| ConGeo-QView | 77.34 ± 0.76 | 95.38 ± 0.11 | 79.95 ± 0.17 | 14.86 ± 1.03 | 66.88 |

### QView minus adapter: CorrMean6 R@1 (pp), 95% CI

| Adapter | Dense→Dense | SUES→SUES | Dense→SUES | SUES→Dense |
| --- | --- | --- | --- | --- |
| SLAug | +0.54 [-0.19, +1.25] | +1.73 [+0.06, +3.52] | +3.32 [+2.10, +4.55] | +1.52 [+0.15, +2.93] |
| PASTA | +2.86 [+1.98, +3.87] | +4.92 [+2.92, +7.06] | +1.05 [-0.10, +2.21] | +3.40 [+2.26, +4.59] |
| AFA | +2.94 [+2.12, +3.84] | +5.71 [+3.40, +8.08] | +2.15 [+0.88, +3.55] | +3.22 [+1.97, +4.47] |
| RaffeSDG | +2.54 [+1.46, +3.82] | +5.99 [+3.87, +8.48] | +0.23 [-1.07, +1.43] | +4.78 [+3.39, +6.13] |

Across the 16 method-by-direction comparisons, all 16 Snow R@1 intervals favor QView, as do 13/16 CorrMean6 R@1 and 12/16 CorrMean6 AP intervals. These are individual, unadjusted 95% intervals. In Dense→SUES the RaffeSDG R@1 difference is +0.23 pp with a CI crossing zero.
