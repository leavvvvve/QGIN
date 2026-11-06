# Competitive takeovers, spatial errors and ablations

## A. Competitive-takeover trajectories

For a reference encoder, let $Q_0$ be queries retrieved correctly in Clean. Under each degraded condition, $m_{\rm old,loc}$ compares the best positive with the best image of the clean hardest-negative place, and $m_{\rm all}$ compares the best positive with the current hardest negative. A competitive takeover event (CTE) satisfies $m_{\rm old,loc}>10^{-6}$ and $m_{\rm all}<-10^{-6}$ within $Q_0$.

Rescue rate counts CTE queries whose candidate margin exceeds $10^{-6}$, divided by all reference CTE queries. New-failure rate counts candidate R@1 failures among the reference's still-correct degraded queries ($m_{\rm all}>10^{-6}$), divided by that still-correct set. Far-error removal counts reference CTE queries with Dis@1 > 200 m whose candidate error is ≤ 200 m, divided by reference CTE queries beyond 200 m. A zero denominator is shown as —. Exact numerators, denominators and Clean-correct set sizes for each seed are included in [cte_paired.csv](summary_csv/cte_paired.csv).

The primary frame uses each model's original host as reference. The common frame uses Base for all candidates. Both frames use the reference's Clean-correct set and degraded margins consistently. Seed-mean rates are the arithmetic mean of the two seed-specific rates; their confidence intervals use the same place resampling indices. A rate with a missing seed denominator has no two-seed mean.

### Dense → Dense

#### Primary host reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 5.53 [4.38, 6.81] | — |
| Base + QGIN | Clean | 43 | — | 5.33 [4.26, 6.47] | — |
| Base + QGIN | Clean | mean | — | 5.43 [4.53, 6.34] | — |
| Base + QGIN | Fog | 42 | 39.84 [30.60, 48.49] | 9.06 [7.41, 10.81] | 41.03 [23.68, 57.14] |
| Base + QGIN | Fog | 43 | 44.80 [35.91, 54.20] | 9.44 [7.77, 11.12] | 52.63 [37.50, 68.58] |
| Base + QGIN | Fog | mean | 42.32 [35.92, 49.28] | 9.25 [7.94, 10.62] | 46.83 [35.05, 58.86] |
| Base + QGIN | Snow | 42 | 66.19 [59.78, 72.45] | 4.99 [3.80, 6.32] | 78.45 [72.02, 84.73] |
| Base + QGIN | Snow | 43 | 64.86 [58.13, 71.43] | 5.46 [4.31, 6.68] | 72.84 [65.29, 80.25] |
| Base + QGIN | Snow | mean | 65.53 [60.54, 70.26] | 5.22 [4.33, 6.15] | 75.65 [70.13, 80.66] |
| Base + QGIN | Blur | 42 | 100.00 [100.00, 100.00] | 4.62 [3.52, 5.73] | 100.00 [100.00, 100.00] |
| Base + QGIN | Blur | 43 | 46.67 [16.67, 72.74] | 4.78 [3.64, 6.07] | 42.86 [0.00, 83.33] |
| Base + QGIN | Blur | mean | 73.33 [58.33, 86.37] | 4.70 [3.85, 5.63] | 71.43 [50.00, 91.67] |
| Base + QGIN | Gamma | 42 | 28.57 [0.00, 62.92] | 4.62 [3.46, 5.86] | 100.00 [100.00, 100.00] |
| Base + QGIN | Gamma | 43 | 50.00 [0.00, 100.00] | 4.76 [3.71, 5.92] | 40.00 [0.00, 100.00] |
| Base + QGIN | Gamma | mean | 39.29 [12.05, 68.79] | 4.69 [3.82, 5.58] | 70.00 [50.00, 100.00] |
| Base + QGIN | ExposureClip | 42 | 59.52 [48.86, 70.51] | 5.45 [4.27, 6.71] | 65.31 [50.94, 80.36] |
| Base + QGIN | ExposureClip | 43 | 57.89 [47.14, 68.13] | 5.53 [4.35, 6.75] | 61.67 [49.02, 73.85] |
| Base + QGIN | ExposureClip | mean | 58.71 [50.45, 67.16] | 5.49 [4.56, 6.46] | 63.49 [53.05, 73.91] |
| Base + QGIN | Posterize4 | 42 | 0.00 [0.00, 0.00] | 5.34 [4.18, 6.65] | 100.00 [100.00, 100.00] |
| Base + QGIN | Posterize4 | 43 | — | 4.94 [3.88, 6.10] | — |
| Base + QGIN | Posterize4 | mean | — | 5.14 [4.27, 6.06] | — |
| S4G-QDual | Clean | 42 | — | 6.14 [5.05, 7.42] | — |
| S4G-QDual | Clean | 43 | — | 5.03 [3.97, 6.23] | — |
| S4G-QDual | Clean | mean | — | 5.58 [4.74, 6.55] | — |
| S4G-QDual | Fog | 42 | 43.40 [29.41, 58.00] | 6.60 [5.31, 8.04] | 46.15 [16.67, 75.00] |
| S4G-QDual | Fog | 43 | 58.33 [47.54, 69.01] | 6.22 [4.99, 7.53] | 73.08 [54.17, 90.91] |
| S4G-QDual | Fog | mean | 50.86 [42.39, 59.45] | 6.41 [5.52, 7.43] | 59.62 [41.67, 77.78] |
| S4G-QDual | Snow | 42 | 77.64 [72.58, 82.74] | 5.06 [3.87, 6.33] | 88.78 [84.02, 93.00] |
| S4G-QDual | Snow | 43 | 74.91 [69.83, 79.86] | 5.12 [3.90, 6.36] | 88.59 [83.85, 93.01] |
| S4G-QDual | Snow | mean | 76.28 [72.75, 79.92] | 5.09 [4.16, 6.02] | 88.68 [85.00, 91.98] |
| S4G-QDual | Blur | 42 | 50.00 [16.67, 85.71] | 5.44 [4.38, 6.62] | 50.00 [0.00, 100.00] |
| S4G-QDual | Blur | 43 | 50.00 [0.00, 100.00] | 4.49 [3.53, 5.53] | 100.00 [100.00, 100.00] |
| S4G-QDual | Blur | mean | 50.00 [16.67, 83.33] | 4.96 [4.19, 5.80] | 75.00 [50.00, 100.00] |
| S4G-QDual | Gamma | 42 | 80.00 [33.33, 100.00] | 5.81 [4.70, 7.03] | 75.00 [0.00, 100.00] |
| S4G-QDual | Gamma | 43 | 100.00 [100.00, 100.00] | 4.59 [3.53, 5.74] | — |
| S4G-QDual | Gamma | mean | 90.00 [66.67, 100.00] | 5.20 [4.35, 6.17] | — |
| S4G-QDual | ExposureClip | 42 | 58.73 [50.00, 67.39] | 6.03 [4.83, 7.41] | 71.08 [60.67, 80.56] |
| S4G-QDual | ExposureClip | 43 | 64.71 [55.65, 73.02] | 4.84 [3.71, 6.08] | 67.95 [56.16, 77.78] |
| S4G-QDual | ExposureClip | mean | 61.72 [54.58, 68.21] | 5.43 [4.50, 6.49] | 69.52 [61.66, 76.60] |
| S4G-QDual | Posterize4 | 42 | — | 5.84 [4.77, 7.01] | — |
| S4G-QDual | Posterize4 | 43 | — | 4.55 [3.58, 5.66] | — |
| S4G-QDual | Posterize4 | mean | — | 5.19 [4.38, 6.12] | — |
| ConGeo-QView | Clean | 42 | — | 3.26 [2.43, 4.12] | — |
| ConGeo-QView | Clean | 43 | — | 3.14 [2.31, 4.09] | — |
| ConGeo-QView | Clean | mean | — | 3.20 [2.57, 3.86] | — |
| ConGeo-QView | Fog | 42 | 49.06 [36.36, 61.71] | 3.91 [2.98, 4.99] | 62.50 [41.37, 84.62] |
| ConGeo-QView | Fog | 43 | 43.94 [31.48, 56.25] | 4.11 [3.11, 5.15] | 65.38 [46.15, 83.33] |
| ConGeo-QView | Fog | mean | 46.50 [37.82, 54.93] | 4.01 [3.31, 4.82] | 63.94 [49.55, 77.50] |
| ConGeo-QView | Snow | 42 | 69.19 [61.86, 76.21] | 2.74 [1.84, 3.67] | 71.54 [63.26, 80.00] |
| ConGeo-QView | Snow | 43 | 69.01 [62.92, 75.00] | 3.51 [2.60, 4.46] | 80.98 [75.00, 87.23] |
| ConGeo-QView | Snow | mean | 69.10 [64.43, 74.10] | 3.12 [2.44, 3.84] | 76.26 [71.02, 81.82] |
| ConGeo-QView | Blur | 42 | 62.50 [25.00, 100.00] | 2.71 [1.96, 3.53] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Blur | 43 | 50.00 [12.50, 85.76] | 2.89 [2.07, 3.80] | — |
| ConGeo-QView | Blur | mean | 56.25 [30.00, 81.25] | 2.80 [2.25, 3.46] | — |
| ConGeo-QView | Gamma | 42 | 25.00 [0.00, 80.00] | 2.70 [1.92, 3.59] | 33.33 [0.00, 100.00] |
| ConGeo-QView | Gamma | 43 | 66.67 [0.00, 100.00] | 2.75 [1.99, 3.56] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Gamma | mean | 45.83 [0.00, 83.33] | 2.73 [2.16, 3.34] | 66.67 [50.00, 100.00] |
| ConGeo-QView | ExposureClip | 42 | 62.24 [52.47, 72.17] | 3.34 [2.49, 4.29] | 67.24 [54.24, 80.00] |
| ConGeo-QView | ExposureClip | 43 | 58.72 [50.00, 67.50] | 3.15 [2.28, 4.07] | 61.90 [51.39, 71.62] |
| ConGeo-QView | ExposureClip | mean | 60.48 [53.58, 67.63] | 3.24 [2.60, 3.94] | 64.57 [55.93, 73.27] |
| ConGeo-QView | Posterize4 | 42 | — | 3.14 [2.31, 4.01] | — |
| ConGeo-QView | Posterize4 | 43 | — | 3.32 [2.40, 4.35] | — |
| ConGeo-QView | Posterize4 | mean | — | 3.23 [2.59, 3.93] | — |
| SinGeo-QView | Clean | 42 | — | 2.70 [1.95, 3.53] | — |
| SinGeo-QView | Clean | 43 | — | 3.07 [2.25, 4.05] | — |
| SinGeo-QView | Clean | mean | — | 2.88 [2.26, 3.59] | — |
| SinGeo-QView | Fog | 42 | 61.36 [46.67, 76.19] | 5.70 [4.55, 6.94] | 65.00 [45.83, 84.62] |
| SinGeo-QView | Fog | 43 | 39.66 [26.31, 52.50] | 4.93 [3.92, 6.03] | 56.25 [30.42, 80.95] |
| SinGeo-QView | Fog | mean | 50.51 [40.47, 59.82] | 5.32 [4.47, 6.26] | 60.62 [44.14, 76.19] |
| SinGeo-QView | Snow | 42 | 70.71 [64.73, 76.80] | 3.12 [2.17, 4.20] | 86.49 [80.43, 92.16] |
| SinGeo-QView | Snow | 43 | 75.00 [69.35, 80.36] | 3.35 [2.42, 4.34] | 78.81 [72.15, 84.77] |
| SinGeo-QView | Snow | mean | 72.86 [68.43, 77.24] | 3.24 [2.54, 3.96] | 82.65 [77.87, 87.15] |
| SinGeo-QView | Blur | 42 | 0.00 [0.00, 0.00] | 2.88 [2.08, 3.75] | — |
| SinGeo-QView | Blur | 43 | 66.67 [0.00, 100.00] | 2.75 [1.99, 3.58] | 66.67 [0.00, 100.00] |
| SinGeo-QView | Blur | mean | 33.33 [0.00, 50.00] | 2.82 [2.22, 3.46] | — |
| SinGeo-QView | Gamma | 42 | 50.00 [0.00, 100.00] | 2.19 [1.53, 2.89] | 0.00 [0.00, 0.00] |
| SinGeo-QView | Gamma | 43 | 50.00 [0.00, 100.00] | 2.37 [1.68, 3.16] | 50.00 [0.00, 100.00] |
| SinGeo-QView | Gamma | mean | 50.00 [12.50, 90.00] | 2.28 [1.76, 2.86] | 25.00 [0.00, 50.00] |
| SinGeo-QView | ExposureClip | 42 | 64.29 [55.10, 73.12] | 3.25 [2.43, 4.18] | 76.81 [66.67, 86.44] |
| SinGeo-QView | ExposureClip | 43 | 64.65 [54.95, 73.56] | 3.00 [2.14, 3.90] | 66.67 [55.43, 76.47] |
| SinGeo-QView | ExposureClip | mean | 64.47 [57.49, 71.55] | 3.13 [2.49, 3.80] | 71.74 [63.81, 78.87] |
| SinGeo-QView | Posterize4 | 42 | — | 2.62 [1.88, 3.49] | — |
| SinGeo-QView | Posterize4 | 43 | 100.00 [100.00, 100.00] | 3.05 [2.20, 4.01] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Posterize4 | mean | — | 2.84 [2.20, 3.53] | — |


#### Common Base reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 5.53 [4.38, 6.81] | — |
| Base + QGIN | Clean | 43 | — | 5.33 [4.26, 6.47] | — |
| Base + QGIN | Clean | mean | — | 5.43 [4.53, 6.34] | — |
| Base + QGIN | Fog | 42 | 39.84 [30.60, 48.49] | 9.06 [7.41, 10.81] | 41.03 [23.68, 57.14] |
| Base + QGIN | Fog | 43 | 44.80 [35.91, 54.20] | 9.44 [7.77, 11.12] | 52.63 [37.50, 68.58] |
| Base + QGIN | Fog | mean | 42.32 [35.92, 49.28] | 9.25 [7.94, 10.62] | 46.83 [35.05, 58.86] |
| Base + QGIN | Snow | 42 | 66.19 [59.78, 72.45] | 4.99 [3.80, 6.32] | 78.45 [72.02, 84.73] |
| Base + QGIN | Snow | 43 | 64.86 [58.13, 71.43] | 5.46 [4.31, 6.68] | 72.84 [65.29, 80.25] |
| Base + QGIN | Snow | mean | 65.53 [60.54, 70.26] | 5.22 [4.33, 6.15] | 75.65 [70.13, 80.66] |
| Base + QGIN | Blur | 42 | 100.00 [100.00, 100.00] | 4.62 [3.52, 5.73] | 100.00 [100.00, 100.00] |
| Base + QGIN | Blur | 43 | 46.67 [16.67, 72.74] | 4.78 [3.64, 6.07] | 42.86 [0.00, 83.33] |
| Base + QGIN | Blur | mean | 73.33 [58.33, 86.37] | 4.70 [3.85, 5.63] | 71.43 [50.00, 91.67] |
| Base + QGIN | Gamma | 42 | 28.57 [0.00, 62.92] | 4.62 [3.46, 5.86] | 100.00 [100.00, 100.00] |
| Base + QGIN | Gamma | 43 | 50.00 [0.00, 100.00] | 4.76 [3.71, 5.92] | 40.00 [0.00, 100.00] |
| Base + QGIN | Gamma | mean | 39.29 [12.05, 68.79] | 4.69 [3.82, 5.58] | 70.00 [50.00, 100.00] |
| Base + QGIN | ExposureClip | 42 | 59.52 [48.86, 70.51] | 5.45 [4.27, 6.71] | 65.31 [50.94, 80.36] |
| Base + QGIN | ExposureClip | 43 | 57.89 [47.14, 68.13] | 5.53 [4.35, 6.75] | 61.67 [49.02, 73.85] |
| Base + QGIN | ExposureClip | mean | 58.71 [50.45, 67.16] | 5.49 [4.56, 6.46] | 63.49 [53.05, 73.91] |
| Base + QGIN | Posterize4 | 42 | 0.00 [0.00, 0.00] | 5.34 [4.18, 6.65] | 100.00 [100.00, 100.00] |
| Base + QGIN | Posterize4 | 43 | — | 4.94 [3.88, 6.10] | — |
| Base + QGIN | Posterize4 | mean | — | 5.14 [4.27, 6.06] | — |
| S4G-QDual | Clean | 42 | — | 8.45 [6.94, 10.07] | — |
| S4G-QDual | Clean | 43 | — | 7.90 [6.48, 9.41] | — |
| S4G-QDual | Clean | mean | — | 8.17 [7.00, 9.38] | — |
| S4G-QDual | Fog | 42 | 63.41 [54.69, 71.63] | 10.49 [8.68, 12.44] | 87.18 [76.47, 96.88] |
| S4G-QDual | Fog | 43 | 69.60 [60.92, 77.69] | 10.87 [9.07, 12.80] | 84.21 [71.79, 94.59] |
| S4G-QDual | Fog | mean | 66.51 [60.10, 72.58] | 10.68 [9.21, 12.26] | 85.70 [76.71, 94.19] |
| S4G-QDual | Snow | 42 | 75.54 [69.50, 80.97] | 8.83 [7.24, 10.54] | 89.50 [84.57, 93.92] |
| S4G-QDual | Snow | 43 | 74.52 [69.10, 79.85] | 9.51 [7.80, 11.26] | 88.27 [83.22, 92.86] |
| S4G-QDual | Snow | mean | 75.03 [70.68, 79.14] | 9.17 [7.91, 10.54] | 88.89 [85.28, 92.14] |
| S4G-QDual | Blur | 42 | 50.00 [0.00, 100.00] | 7.29 [5.84, 8.79] | 50.00 [0.00, 100.00] |
| S4G-QDual | Blur | 43 | 86.67 [66.67, 100.00] | 8.02 [6.56, 9.64] | 85.71 [50.00, 100.00] |
| S4G-QDual | Blur | mean | 68.33 [38.88, 100.00] | 7.66 [6.47, 8.89] | 67.86 [30.00, 100.00] |
| S4G-QDual | Gamma | 42 | 71.43 [40.00, 100.00] | 8.39 [6.88, 10.01] | 100.00 [100.00, 100.00] |
| S4G-QDual | Gamma | 43 | 66.67 [20.00, 100.00] | 7.76 [6.34, 9.26] | 80.00 [33.33, 100.00] |
| S4G-QDual | Gamma | mean | 69.05 [37.50, 100.00] | 8.08 [6.88, 9.42] | 90.00 [66.67, 100.00] |
| S4G-QDual | ExposureClip | 42 | 60.71 [50.55, 70.83] | 9.97 [8.25, 11.78] | 75.51 [64.10, 86.84] |
| S4G-QDual | ExposureClip | 43 | 68.42 [58.62, 78.50] | 8.91 [7.36, 10.60] | 80.00 [69.09, 90.00] |
| S4G-QDual | ExposureClip | mean | 64.57 [57.35, 72.16] | 9.44 [8.15, 10.79] | 77.76 [70.45, 85.26] |
| S4G-QDual | Posterize4 | 42 | 0.00 [0.00, 0.00] | 8.35 [6.90, 9.96] | 100.00 [100.00, 100.00] |
| S4G-QDual | Posterize4 | 43 | — | 7.70 [6.19, 9.17] | — |
| S4G-QDual | Posterize4 | mean | — | 8.02 [6.84, 9.24] | — |
| ConGeo-QView | Clean | 42 | — | 5.27 [4.11, 6.61] | — |
| ConGeo-QView | Clean | 43 | — | 6.84 [5.47, 8.30] | — |
| ConGeo-QView | Clean | mean | — | 6.06 [5.01, 7.21] | — |
| ConGeo-QView | Fog | 42 | 72.36 [63.49, 80.45] | 8.31 [6.78, 10.04] | 89.74 [79.54, 97.83] |
| ConGeo-QView | Fog | 43 | 73.60 [65.14, 81.60] | 9.94 [8.13, 11.81] | 89.47 [76.19, 100.00] |
| ConGeo-QView | Fog | mean | 72.98 [66.53, 78.88] | 9.12 [7.77, 10.62] | 89.61 [79.79, 97.37] |
| ConGeo-QView | Snow | 42 | 79.86 [74.44, 84.85] | 7.12 [5.39, 8.96] | 90.06 [85.28, 94.66] |
| ConGeo-QView | Snow | 43 | 74.90 [69.29, 80.49] | 9.17 [7.38, 10.93] | 87.04 [81.22, 92.21] |
| ConGeo-QView | Snow | mean | 77.38 [73.33, 81.33] | 8.15 [6.82, 9.47] | 88.55 [84.70, 92.26] |
| ConGeo-QView | Blur | 42 | 100.00 [100.00, 100.00] | 4.68 [3.56, 5.99] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Blur | 43 | 86.67 [66.67, 100.00] | 6.27 [4.88, 7.73] | 85.71 [50.00, 100.00] |
| ConGeo-QView | Blur | mean | 93.33 [83.33, 100.00] | 5.47 [4.39, 6.66] | 92.86 [75.00, 100.00] |
| ConGeo-QView | Gamma | 42 | 85.71 [50.00, 100.00] | 5.58 [4.33, 6.96] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Gamma | 43 | 83.33 [50.00, 100.00] | 6.99 [5.64, 8.47] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Gamma | mean | 84.52 [58.33, 100.00] | 6.28 [5.20, 7.48] | 100.00 [100.00, 100.00] |
| ConGeo-QView | ExposureClip | 42 | 66.67 [55.55, 77.50] | 8.04 [6.56, 9.69] | 67.35 [53.49, 80.39] |
| ConGeo-QView | ExposureClip | 43 | 64.21 [53.92, 74.19] | 7.63 [6.11, 9.14] | 73.33 [61.22, 84.78] |
| ConGeo-QView | ExposureClip | mean | 65.44 [56.31, 74.21] | 7.83 [6.58, 9.21] | 70.34 [59.97, 80.30] |
| ConGeo-QView | Posterize4 | 42 | 100.00 [100.00, 100.00] | 5.34 [4.13, 6.69] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Posterize4 | 43 | — | 6.73 [5.37, 8.19] | — |
| ConGeo-QView | Posterize4 | mean | — | 6.04 [4.99, 7.19] | — |
| SinGeo-QView | Clean | 42 | — | 4.25 [3.19, 5.39] | — |
| SinGeo-QView | Clean | 43 | — | 4.83 [3.75, 6.03] | — |
| SinGeo-QView | Clean | mean | — | 4.54 [3.69, 5.51] | — |
| SinGeo-QView | Fog | 42 | 79.67 [71.54, 86.99] | 7.37 [5.95, 8.93] | 92.31 [82.93, 100.00] |
| SinGeo-QView | Fog | 43 | 72.00 [63.64, 79.68] | 8.45 [6.95, 10.18] | 84.21 [72.09, 94.74] |
| SinGeo-QView | Fog | mean | 75.84 [69.65, 81.52] | 7.91 [6.76, 9.25] | 88.26 [80.95, 94.83] |
| SinGeo-QView | Snow | 42 | 74.46 [68.80, 80.00] | 6.77 [5.21, 8.27] | 91.16 [86.34, 95.57] |
| SinGeo-QView | Snow | 43 | 74.90 [69.14, 80.39] | 5.80 [4.48, 7.21] | 87.65 [81.72, 92.90] |
| SinGeo-QView | Snow | mean | 74.68 [70.34, 78.91] | 6.28 [5.18, 7.46] | 89.41 [85.47, 93.10] |
| SinGeo-QView | Blur | 42 | 100.00 [100.00, 100.00] | 4.19 [3.12, 5.38] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Blur | 43 | 93.33 [78.57, 100.00] | 4.89 [3.74, 6.16] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Blur | mean | 96.67 [89.29, 100.00] | 4.54 [3.65, 5.54] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Gamma | 42 | 100.00 [100.00, 100.00] | 4.14 [3.17, 5.19] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Gamma | 43 | 66.67 [25.00, 100.00] | 4.92 [3.85, 6.06] | 60.00 [0.00, 100.00] |
| SinGeo-QView | Gamma | mean | 83.33 [62.50, 100.00] | 4.53 [3.68, 5.45] | 80.00 [50.00, 100.00] |
| SinGeo-QView | ExposureClip | 42 | 67.86 [58.44, 76.92] | 6.22 [4.95, 7.50] | 71.43 [60.00, 82.93] |
| SinGeo-QView | ExposureClip | 43 | 63.16 [53.76, 72.48] | 5.77 [4.51, 7.07] | 76.67 [66.07, 87.04] |
| SinGeo-QView | ExposureClip | mean | 65.51 [58.34, 73.04] | 5.99 [5.01, 7.07] | 74.05 [65.81, 82.69] |
| SinGeo-QView | Posterize4 | 42 | 100.00 [100.00, 100.00] | 4.20 [3.20, 5.27] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Posterize4 | 43 | — | 4.74 [3.68, 5.91] | — |
| SinGeo-QView | Posterize4 | mean | — | 4.47 [3.64, 5.43] | — |


### SUES → SUES

#### Primary host reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 2.09 [1.10, 3.30] | — |
| Base + QGIN | Clean | 43 | — | 1.85 [0.66, 3.63] | — |
| Base + QGIN | Clean | mean | — | 1.97 [0.96, 3.31] | — |
| Base + QGIN | Fog | 42 | 85.36 [74.82, 93.02] | 1.94 [1.05, 3.06] | — |
| Base + QGIN | Fog | 43 | 79.27 [69.78, 88.31] | 1.74 [0.68, 3.36] | — |
| Base + QGIN | Fog | mean | 82.31 [76.38, 88.06] | 1.84 [0.99, 3.07] | — |
| Base + QGIN | Snow | 42 | 67.53 [56.74, 78.55] | 4.52 [2.62, 6.71] | — |
| Base + QGIN | Snow | 43 | 74.95 [64.96, 84.00] | 2.13 [1.13, 3.38] | — |
| Base + QGIN | Snow | mean | 71.24 [62.53, 80.06] | 3.32 [2.01, 4.89] | — |
| Base + QGIN | Blur | 42 | 69.50 [56.97, 84.21] | 3.48 [1.54, 5.95] | — |
| Base + QGIN | Blur | 43 | 80.80 [71.22, 88.73] | 2.60 [1.17, 4.51] | — |
| Base + QGIN | Blur | mean | 75.15 [67.70, 83.84] | 3.04 [1.50, 4.90] | — |
| Base + QGIN | Gamma | 42 | 92.86 [78.95, 100.00] | 1.94 [0.98, 3.12] | — |
| Base + QGIN | Gamma | 43 | 80.00 [60.00, 96.43] | 1.74 [0.56, 3.49] | — |
| Base + QGIN | Gamma | mean | 86.43 [73.03, 95.83] | 1.84 [0.87, 3.14] | — |
| Base + QGIN | ExposureClip | 42 | 78.38 [70.27, 85.80] | 2.71 [1.58, 4.03] | — |
| Base + QGIN | ExposureClip | 43 | 67.74 [52.39, 83.68] | 2.88 [1.18, 5.35] | — |
| Base + QGIN | ExposureClip | mean | 73.06 [63.24, 82.95] | 2.79 [1.58, 4.41] | — |
| Base + QGIN | Posterize4 | 42 | 90.91 [75.00, 100.00] | 1.91 [1.06, 2.90] | — |
| Base + QGIN | Posterize4 | 43 | 92.31 [57.14, 100.00] | 1.75 [0.66, 3.43] | — |
| Base + QGIN | Posterize4 | mean | 91.61 [77.78, 100.00] | 1.83 [0.92, 3.05] | — |
| S4G-QDual | Clean | 42 | — | 2.14 [0.98, 3.92] | — |
| S4G-QDual | Clean | 43 | — | 0.60 [0.28, 1.03] | — |
| S4G-QDual | Clean | mean | — | 1.37 [0.67, 2.40] | — |
| S4G-QDual | Fog | 42 | 77.65 [40.38, 94.92] | 1.90 [0.86, 3.36] | — |
| S4G-QDual | Fog | 43 | 61.54 [30.00, 88.57] | 0.72 [0.34, 1.24] | — |
| S4G-QDual | Fog | mean | 69.59 [41.93, 88.08] | 1.31 [0.65, 2.27] | — |
| S4G-QDual | Snow | 42 | 75.46 [63.97, 84.39] | 3.05 [1.45, 5.22] | — |
| S4G-QDual | Snow | 43 | 78.69 [67.30, 87.34] | 2.53 [1.21, 4.37] | — |
| S4G-QDual | Snow | mean | 77.08 [66.81, 85.33] | 2.79 [1.39, 4.67] | — |
| S4G-QDual | Blur | 42 | 68.66 [35.89, 89.59] | 1.22 [0.62, 2.08] | — |
| S4G-QDual | Blur | 43 | 67.57 [49.06, 83.33] | 0.95 [0.47, 1.59] | — |
| S4G-QDual | Blur | mean | 68.11 [48.60, 82.86] | 1.09 [0.58, 1.81] | — |
| S4G-QDual | Gamma | 42 | 34.78 [6.63, 100.00] | 1.99 [1.03, 3.36] | — |
| S4G-QDual | Gamma | 43 | 87.50 [61.54, 100.00] | 0.62 [0.32, 1.03] | — |
| S4G-QDual | Gamma | mean | 61.14 [40.93, 96.15] | 1.31 [0.73, 2.11] | — |
| S4G-QDual | ExposureClip | 42 | 65.62 [51.55, 79.07] | 2.19 [1.13, 3.78] | — |
| S4G-QDual | ExposureClip | 43 | 78.43 [65.35, 88.24] | 1.66 [0.70, 3.06] | — |
| S4G-QDual | ExposureClip | mean | 72.02 [59.79, 82.43] | 1.93 [1.02, 3.14] | — |
| S4G-QDual | Posterize4 | 42 | 18.18 [0.00, 100.00] | 1.90 [0.91, 3.39] | — |
| S4G-QDual | Posterize4 | 43 | 66.67 [0.00, 100.00] | 0.67 [0.32, 1.12] | — |
| S4G-QDual | Posterize4 | mean | 42.42 [12.96, 83.33] | 1.29 [0.69, 2.14] | — |
| ConGeo-QView | Clean | 42 | — | 1.69 [0.70, 3.37] | — |
| ConGeo-QView | Clean | 43 | — | 1.36 [0.72, 2.22] | — |
| ConGeo-QView | Clean | mean | — | 1.53 [0.78, 2.67] | — |
| ConGeo-QView | Fog | 42 | 68.42 [40.00, 92.86] | 2.07 [0.94, 3.81] | — |
| ConGeo-QView | Fog | 43 | 56.14 [35.29, 77.78] | 1.47 [0.73, 2.41] | — |
| ConGeo-QView | Fog | mean | 62.28 [41.81, 80.11] | 1.77 [0.90, 3.01] | — |
| ConGeo-QView | Snow | 42 | 70.53 [60.26, 80.25] | 2.92 [1.71, 4.41] | — |
| ConGeo-QView | Snow | 43 | 67.82 [55.77, 78.64] | 3.00 [1.66, 4.54] | — |
| ConGeo-QView | Snow | mean | 69.18 [60.69, 78.11] | 2.96 [1.81, 4.31] | — |
| ConGeo-QView | Blur | 42 | 56.79 [43.33, 71.43] | 2.92 [1.72, 4.46] | — |
| ConGeo-QView | Blur | 43 | 53.92 [35.85, 70.95] | 1.88 [0.91, 3.27] | — |
| ConGeo-QView | Blur | mean | 55.36 [44.73, 66.87] | 2.40 [1.45, 3.65] | — |
| ConGeo-QView | Gamma | 42 | 64.29 [30.00, 92.86] | 1.95 [0.82, 3.75] | — |
| ConGeo-QView | Gamma | 43 | 59.09 [35.29, 92.31] | 1.35 [0.73, 2.13] | — |
| ConGeo-QView | Gamma | mean | 61.69 [38.89, 85.03] | 1.65 [0.86, 2.75] | — |
| ConGeo-QView | ExposureClip | 42 | 71.63 [56.53, 83.95] | 2.87 [1.45, 5.10] | — |
| ConGeo-QView | ExposureClip | 43 | 80.55 [70.56, 87.20] | 1.29 [0.79, 1.91] | — |
| ConGeo-QView | ExposureClip | mean | 76.09 [65.98, 83.87] | 2.08 [1.23, 3.41] | — |
| ConGeo-QView | Posterize4 | 42 | 93.33 [77.78, 100.00] | 1.73 [0.75, 3.24] | — |
| ConGeo-QView | Posterize4 | 43 | 45.45 [10.00, 87.50] | 1.40 [0.72, 2.22] | — |
| ConGeo-QView | Posterize4 | mean | 69.39 [51.19, 91.12] | 1.57 [0.82, 2.58] | — |
| SinGeo-QView | Clean | 42 | — | 3.57 [1.96, 5.75] | — |
| SinGeo-QView | Clean | 43 | — | 1.85 [1.08, 2.81] | — |
| SinGeo-QView | Clean | mean | — | 2.71 [1.65, 4.16] | — |
| SinGeo-QView | Fog | 42 | 60.76 [35.29, 77.78] | 3.37 [1.94, 5.28] | — |
| SinGeo-QView | Fog | 43 | 80.60 [60.00, 95.39] | 1.95 [1.19, 2.87] | — |
| SinGeo-QView | Fog | mean | 70.68 [52.43, 83.49] | 2.66 [1.70, 3.95] | — |
| SinGeo-QView | Snow | 42 | 68.18 [56.21, 79.05] | 6.51 [4.12, 9.32] | — |
| SinGeo-QView | Snow | 43 | 65.37 [52.91, 76.04] | 4.60 [2.76, 7.18] | — |
| SinGeo-QView | Snow | mean | 66.77 [56.39, 76.18] | 5.56 [3.71, 7.93] | — |
| SinGeo-QView | Blur | 42 | 45.91 [28.91, 64.05] | 5.20 [3.42, 7.39] | — |
| SinGeo-QView | Blur | 43 | 63.64 [47.34, 76.58] | 2.08 [1.27, 3.06] | — |
| SinGeo-QView | Blur | mean | 54.77 [42.07, 67.67] | 3.64 [2.46, 5.04] | — |
| SinGeo-QView | Gamma | 42 | 48.15 [22.73, 75.00] | 4.05 [2.28, 6.22] | — |
| SinGeo-QView | Gamma | 43 | 80.65 [60.00, 94.29] | 1.90 [1.07, 3.02] | — |
| SinGeo-QView | Gamma | mean | 64.40 [47.74, 80.51] | 2.97 [1.86, 4.36] | — |
| SinGeo-QView | ExposureClip | 42 | 65.21 [56.30, 73.50] | 6.00 [3.63, 9.01] | — |
| SinGeo-QView | ExposureClip | 43 | 73.34 [60.05, 84.37] | 2.92 [1.82, 4.43] | — |
| SinGeo-QView | ExposureClip | mean | 69.28 [60.30, 76.85] | 4.46 [2.88, 6.50] | — |
| SinGeo-QView | Posterize4 | 42 | 37.50 [0.00, 70.59] | 3.31 [1.86, 5.33] | — |
| SinGeo-QView | Posterize4 | 43 | 30.00 [0.00, 66.67] | 1.76 [1.03, 2.62] | — |
| SinGeo-QView | Posterize4 | mean | 33.75 [10.00, 61.27] | 2.53 [1.57, 3.86] | — |


#### Common Base reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 2.09 [1.10, 3.30] | — |
| Base + QGIN | Clean | 43 | — | 1.85 [0.66, 3.63] | — |
| Base + QGIN | Clean | mean | — | 1.97 [0.96, 3.31] | — |
| Base + QGIN | Fog | 42 | 85.36 [74.82, 93.02] | 1.94 [1.05, 3.06] | — |
| Base + QGIN | Fog | 43 | 79.27 [69.78, 88.31] | 1.74 [0.68, 3.36] | — |
| Base + QGIN | Fog | mean | 82.31 [76.38, 88.06] | 1.84 [0.99, 3.07] | — |
| Base + QGIN | Snow | 42 | 67.53 [56.74, 78.55] | 4.52 [2.62, 6.71] | — |
| Base + QGIN | Snow | 43 | 74.95 [64.96, 84.00] | 2.13 [1.13, 3.38] | — |
| Base + QGIN | Snow | mean | 71.24 [62.53, 80.06] | 3.32 [2.01, 4.89] | — |
| Base + QGIN | Blur | 42 | 69.50 [56.97, 84.21] | 3.48 [1.54, 5.95] | — |
| Base + QGIN | Blur | 43 | 80.80 [71.22, 88.73] | 2.60 [1.17, 4.51] | — |
| Base + QGIN | Blur | mean | 75.15 [67.70, 83.84] | 3.04 [1.50, 4.90] | — |
| Base + QGIN | Gamma | 42 | 92.86 [78.95, 100.00] | 1.94 [0.98, 3.12] | — |
| Base + QGIN | Gamma | 43 | 80.00 [60.00, 96.43] | 1.74 [0.56, 3.49] | — |
| Base + QGIN | Gamma | mean | 86.43 [73.03, 95.83] | 1.84 [0.87, 3.14] | — |
| Base + QGIN | ExposureClip | 42 | 78.38 [70.27, 85.80] | 2.71 [1.58, 4.03] | — |
| Base + QGIN | ExposureClip | 43 | 67.74 [52.39, 83.68] | 2.88 [1.18, 5.35] | — |
| Base + QGIN | ExposureClip | mean | 73.06 [63.24, 82.95] | 2.79 [1.58, 4.41] | — |
| Base + QGIN | Posterize4 | 42 | 90.91 [75.00, 100.00] | 1.91 [1.06, 2.90] | — |
| Base + QGIN | Posterize4 | 43 | 92.31 [57.14, 100.00] | 1.75 [0.66, 3.43] | — |
| Base + QGIN | Posterize4 | mean | 91.61 [77.78, 100.00] | 1.83 [0.92, 3.05] | — |
| S4G-QDual | Clean | 42 | — | 1.29 [0.67, 2.11] | — |
| S4G-QDual | Clean | 43 | — | 1.20 [0.33, 2.62] | — |
| S4G-QDual | Clean | mean | — | 1.25 [0.55, 2.36] | — |
| S4G-QDual | Fog | 42 | 90.79 [80.28, 98.68] | 1.33 [0.68, 2.14] | — |
| S4G-QDual | Fog | 43 | 91.46 [84.96, 97.06] | 1.22 [0.31, 2.72] | — |
| S4G-QDual | Fog | mean | 91.13 [84.08, 96.57] | 1.28 [0.55, 2.40] | — |
| S4G-QDual | Snow | 42 | 75.70 [65.05, 85.53] | 3.96 [2.22, 6.02] | — |
| S4G-QDual | Snow | 43 | 78.51 [66.82, 87.60] | 3.08 [0.83, 7.16] | — |
| S4G-QDual | Snow | mean | 77.11 [66.93, 85.62] | 3.52 [1.64, 6.23] | — |
| S4G-QDual | Blur | 42 | 96.19 [92.10, 98.40] | 1.51 [0.75, 2.52] | — |
| S4G-QDual | Blur | 43 | 86.93 [77.78, 94.67] | 1.47 [0.63, 2.63] | — |
| S4G-QDual | Blur | mean | 91.56 [86.30, 95.99] | 1.49 [0.71, 2.54] | — |
| S4G-QDual | Gamma | 42 | 92.86 [79.16, 100.00] | 1.24 [0.68, 1.98] | — |
| S4G-QDual | Gamma | 43 | 73.33 [50.00, 96.15] | 1.25 [0.33, 2.81] | — |
| S4G-QDual | Gamma | mean | 83.10 [70.28, 95.65] | 1.25 [0.54, 2.36] | — |
| S4G-QDual | ExposureClip | 42 | 85.74 [78.80, 92.15] | 2.73 [1.21, 4.77] | — |
| S4G-QDual | ExposureClip | 43 | 87.70 [81.64, 92.47] | 2.05 [0.73, 4.09] | — |
| S4G-QDual | ExposureClip | mean | 86.72 [81.14, 91.71] | 2.39 [1.14, 3.99] | — |
| S4G-QDual | Posterize4 | 42 | 81.82 [50.00, 100.00] | 1.42 [0.73, 2.28] | — |
| S4G-QDual | Posterize4 | 43 | 100.00 [100.00, 100.00] | 1.28 [0.39, 2.67] | — |
| S4G-QDual | Posterize4 | mean | 90.91 [75.00, 100.00] | 1.35 [0.60, 2.43] | — |
| ConGeo-QView | Clean | 42 | — | 1.32 [0.68, 2.15] | — |
| ConGeo-QView | Clean | 43 | — | 2.02 [0.90, 3.50] | — |
| ConGeo-QView | Clean | mean | — | 1.67 [0.85, 2.75] | — |
| ConGeo-QView | Fog | 42 | 92.05 [84.10, 97.39] | 1.39 [0.56, 2.56] | — |
| ConGeo-QView | Fog | 43 | 72.56 [52.80, 89.77] | 1.95 [0.97, 3.31] | — |
| ConGeo-QView | Fog | mean | 82.31 [70.75, 92.24] | 1.67 [0.83, 2.93] | — |
| ConGeo-QView | Snow | 42 | 71.37 [61.03, 82.32] | 5.16 [2.35, 8.81] | — |
| ConGeo-QView | Snow | 43 | 65.80 [53.88, 78.35] | 5.87 [2.98, 9.53] | — |
| ConGeo-QView | Snow | mean | 68.59 [59.10, 78.90] | 5.52 [2.76, 9.11] | — |
| ConGeo-QView | Blur | 42 | 92.20 [87.16, 96.40] | 2.70 [1.39, 4.23] | — |
| ConGeo-QView | Blur | 43 | 82.93 [70.65, 93.77] | 3.04 [1.61, 4.73] | — |
| ConGeo-QView | Blur | mean | 87.57 [80.84, 93.92] | 2.87 [1.62, 4.34] | — |
| ConGeo-QView | Gamma | 42 | 92.86 [79.16, 100.00] | 1.56 [0.74, 2.67] | — |
| ConGeo-QView | Gamma | 43 | 80.00 [60.00, 96.55] | 2.22 [0.98, 3.84] | — |
| ConGeo-QView | Gamma | mean | 86.43 [74.41, 96.03] | 1.89 [0.96, 3.18] | — |
| ConGeo-QView | ExposureClip | 42 | 83.92 [75.88, 90.76] | 3.28 [2.03, 4.73] | — |
| ConGeo-QView | ExposureClip | 43 | 85.38 [78.86, 90.86] | 2.81 [1.49, 4.57] | — |
| ConGeo-QView | ExposureClip | mean | 84.65 [78.57, 89.91] | 3.05 [1.89, 4.42] | — |
| ConGeo-QView | Posterize4 | 42 | 100.00 [100.00, 100.00] | 1.44 [0.73, 2.45] | — |
| ConGeo-QView | Posterize4 | 43 | 92.31 [62.50, 100.00] | 2.35 [1.09, 4.00] | — |
| ConGeo-QView | Posterize4 | mean | 96.15 [81.25, 100.00] | 1.90 [0.99, 3.16] | — |
| SinGeo-QView | Clean | 42 | — | 3.18 [1.86, 4.82] | — |
| SinGeo-QView | Clean | 43 | — | 2.72 [1.53, 4.28] | — |
| SinGeo-QView | Clean | mean | — | 2.95 [1.83, 4.26] | — |
| SinGeo-QView | Fog | 42 | 79.92 [66.24, 91.21] | 3.16 [1.89, 4.63] | — |
| SinGeo-QView | Fog | 43 | 73.78 [55.47, 90.51] | 2.79 [1.55, 4.38] | — |
| SinGeo-QView | Fog | mean | 76.85 [64.02, 88.28] | 2.98 [1.87, 4.30] | — |
| SinGeo-QView | Snow | 42 | 63.59 [51.51, 76.03] | 9.25 [5.87, 12.95] | — |
| SinGeo-QView | Snow | 43 | 64.46 [51.38, 77.16] | 6.22 [3.57, 9.49] | — |
| SinGeo-QView | Snow | mean | 64.02 [53.32, 75.41] | 7.73 [5.05, 10.79] | — |
| SinGeo-QView | Blur | 42 | 83.36 [73.29, 91.94] | 5.55 [3.59, 7.70] | — |
| SinGeo-QView | Blur | 43 | 81.33 [73.33, 89.07] | 3.10 [1.79, 4.69] | — |
| SinGeo-QView | Blur | mean | 82.35 [75.63, 88.93] | 4.32 [2.80, 6.00] | — |
| SinGeo-QView | Gamma | 42 | 85.71 [64.29, 97.06] | 3.92 [2.21, 5.86] | — |
| SinGeo-QView | Gamma | 43 | 63.33 [31.58, 90.91] | 2.78 [1.44, 4.46] | — |
| SinGeo-QView | Gamma | mean | 74.52 [50.51, 93.07] | 3.35 [2.05, 4.88] | — |
| SinGeo-QView | ExposureClip | 42 | 77.11 [67.00, 86.08] | 7.51 [4.82, 10.52] | — |
| SinGeo-QView | ExposureClip | 43 | 72.37 [56.57, 85.32] | 4.96 [3.18, 6.97] | — |
| SinGeo-QView | ExposureClip | mean | 74.74 [62.42, 84.73] | 6.24 [4.32, 8.37] | — |
| SinGeo-QView | Posterize4 | 42 | 81.82 [52.57, 100.00] | 3.34 [1.99, 5.08] | — |
| SinGeo-QView | Posterize4 | 43 | 92.31 [62.50, 100.00] | 2.75 [1.53, 4.33] | — |
| SinGeo-QView | Posterize4 | mean | 87.06 [66.67, 100.00] | 3.04 [1.87, 4.42] | — |


### Dense → SUES

#### Primary host reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 7.17 [5.48, 9.16] | — |
| Base + QGIN | Clean | 43 | — | 7.47 [5.40, 9.86] | — |
| Base + QGIN | Clean | mean | — | 7.32 [5.62, 9.18] | — |
| Base + QGIN | Fog | 42 | — | 5.51 [4.03, 7.21] | — |
| Base + QGIN | Fog | 43 | — | 5.14 [3.65, 6.87] | — |
| Base + QGIN | Fog | mean | — | 5.32 [3.99, 6.76] | — |
| Base + QGIN | Snow | 42 | 55.30 [48.18, 62.00] | 6.23 [4.37, 8.31] | — |
| Base + QGIN | Snow | 43 | 64.24 [57.03, 70.80] | 4.44 [2.86, 6.72] | — |
| Base + QGIN | Snow | mean | 59.77 [54.36, 64.78] | 5.33 [3.82, 7.17] | — |
| Base + QGIN | Blur | 42 | — | 5.67 [4.07, 7.50] | — |
| Base + QGIN | Blur | 43 | — | 4.21 [2.93, 5.73] | — |
| Base + QGIN | Blur | mean | — | 4.94 [3.68, 6.38] | — |
| Base + QGIN | Gamma | 42 | — | 5.94 [4.46, 7.69] | — |
| Base + QGIN | Gamma | 43 | — | 7.14 [5.17, 9.41] | — |
| Base + QGIN | Gamma | mean | — | 6.54 [5.02, 8.22] | — |
| Base + QGIN | ExposureClip | 42 | 44.93 [32.27, 57.86] | 5.89 [4.37, 7.46] | — |
| Base + QGIN | ExposureClip | 43 | 50.00 [37.61, 62.73] | 6.59 [4.77, 8.58] | — |
| Base + QGIN | ExposureClip | mean | 47.47 [35.60, 58.93] | 6.24 [4.79, 7.78] | — |
| Base + QGIN | Posterize4 | 42 | — | 6.87 [5.21, 8.84] | — |
| Base + QGIN | Posterize4 | 43 | — | 7.09 [5.12, 9.40] | — |
| Base + QGIN | Posterize4 | mean | — | 6.98 [5.34, 8.78] | — |
| S4G-QDual | Clean | 42 | — | 7.36 [5.44, 9.44] | — |
| S4G-QDual | Clean | 43 | — | 9.95 [7.54, 12.57] | — |
| S4G-QDual | Clean | mean | — | 8.65 [6.70, 10.79] | — |
| S4G-QDual | Fog | 42 | 33.90 [22.00, 47.17] | 5.79 [4.33, 7.52] | — |
| S4G-QDual | Fog | 43 | 25.88 [12.99, 42.27] | 8.18 [6.12, 10.43] | — |
| S4G-QDual | Fog | mean | 29.89 [21.30, 40.63] | 6.99 [5.41, 8.75] | — |
| S4G-QDual | Snow | 42 | 59.98 [52.96, 66.40] | 4.57 [3.03, 6.30] | — |
| S4G-QDual | Snow | 43 | 55.37 [48.57, 62.01] | 6.36 [4.57, 8.34] | — |
| S4G-QDual | Snow | mean | 57.67 [51.89, 63.18] | 5.46 [4.16, 6.88] | — |
| S4G-QDual | Blur | 42 | 32.62 [18.79, 45.86] | 5.62 [3.76, 7.88] | — |
| S4G-QDual | Blur | 43 | 25.75 [14.67, 38.15] | 7.25 [5.38, 9.21] | — |
| S4G-QDual | Blur | mean | 29.19 [19.77, 38.07] | 6.43 [4.84, 8.17] | — |
| S4G-QDual | Gamma | 42 | 25.00 [8.70, 42.11] | 6.70 [4.82, 8.81] | — |
| S4G-QDual | Gamma | 43 | 31.82 [11.11, 53.85] | 9.00 [6.70, 11.69] | — |
| S4G-QDual | Gamma | mean | 28.41 [15.35, 42.17] | 7.85 [6.01, 9.96] | — |
| S4G-QDual | ExposureClip | 42 | 34.05 [23.27, 46.63] | 6.22 [4.28, 8.49] | — |
| S4G-QDual | ExposureClip | 43 | 34.92 [24.44, 47.51] | 7.55 [5.52, 9.80] | — |
| S4G-QDual | ExposureClip | mean | 34.48 [24.87, 45.74] | 6.89 [5.25, 8.82] | — |
| S4G-QDual | Posterize4 | 42 | 25.00 [0.00, 60.00] | 6.90 [5.14, 8.85] | — |
| S4G-QDual | Posterize4 | 43 | 40.00 [0.00, 66.67] | 9.07 [6.85, 11.55] | — |
| S4G-QDual | Posterize4 | mean | 32.50 [8.33, 53.57] | 7.99 [6.20, 9.95] | — |
| ConGeo-QView | Clean | 42 | — | 3.94 [2.88, 5.16] | — |
| ConGeo-QView | Clean | 43 | — | 5.33 [4.15, 6.71] | — |
| ConGeo-QView | Clean | mean | — | 4.63 [3.65, 5.74] | — |
| ConGeo-QView | Fog | 42 | 45.74 [33.94, 57.58] | 2.71 [1.94, 3.61] | — |
| ConGeo-QView | Fog | 43 | 42.11 [28.71, 57.45] | 4.05 [3.00, 5.25] | — |
| ConGeo-QView | Fog | mean | 43.92 [36.42, 52.19] | 3.38 [2.60, 4.28] | — |
| ConGeo-QView | Snow | 42 | 60.42 [55.58, 64.93] | 4.23 [2.70, 6.01] | — |
| ConGeo-QView | Snow | 43 | 55.40 [49.79, 60.88] | 4.73 [3.24, 6.43] | — |
| ConGeo-QView | Snow | mean | 57.91 [53.84, 61.80] | 4.48 [3.26, 5.83] | — |
| ConGeo-QView | Blur | 42 | 47.16 [36.73, 57.23] | 2.45 [1.75, 3.28] | — |
| ConGeo-QView | Blur | 43 | 42.92 [31.80, 53.96] | 3.57 [2.44, 4.88] | — |
| ConGeo-QView | Blur | mean | 45.04 [37.57, 52.87] | 3.01 [2.21, 3.91] | — |
| ConGeo-QView | Gamma | 42 | 71.43 [59.62, 83.67] | 3.24 [2.31, 4.32] | — |
| ConGeo-QView | Gamma | 43 | 41.67 [21.74, 64.29] | 4.35 [3.27, 5.62] | — |
| ConGeo-QView | Gamma | mean | 56.55 [44.98, 68.39] | 3.79 [2.94, 4.79] | — |
| ConGeo-QView | ExposureClip | 42 | 52.36 [42.46, 63.16] | 2.91 [2.14, 3.78] | — |
| ConGeo-QView | ExposureClip | 43 | 49.28 [39.29, 58.86] | 4.32 [3.16, 5.66] | — |
| ConGeo-QView | ExposureClip | mean | 50.82 [41.70, 59.92] | 3.62 [2.83, 4.48] | — |
| ConGeo-QView | Posterize4 | 42 | 38.10 [16.64, 63.17] | 3.70 [2.72, 4.88] | — |
| ConGeo-QView | Posterize4 | 43 | 50.00 [16.67, 85.71] | 4.87 [3.69, 6.22] | — |
| ConGeo-QView | Posterize4 | mean | 44.05 [26.39, 63.33] | 4.28 [3.33, 5.39] | — |
| SinGeo-QView | Clean | 42 | — | 6.80 [5.14, 8.64] | — |
| SinGeo-QView | Clean | 43 | — | 9.04 [6.99, 11.40] | — |
| SinGeo-QView | Clean | mean | — | 7.92 [6.30, 9.72] | — |
| SinGeo-QView | Fog | 42 | 37.74 [23.52, 52.94] | 5.16 [3.88, 6.62] | — |
| SinGeo-QView | Fog | 43 | 30.67 [19.72, 41.10] | 6.83 [4.98, 9.04] | — |
| SinGeo-QView | Fog | mean | 34.20 [24.68, 43.30] | 5.99 [4.64, 7.59] | — |
| SinGeo-QView | Snow | 42 | 57.72 [51.81, 63.03] | 5.48 [3.74, 7.46] | — |
| SinGeo-QView | Snow | 43 | 53.62 [47.05, 59.83] | 5.93 [4.23, 7.68] | — |
| SinGeo-QView | Snow | mean | 55.67 [50.92, 60.00] | 5.71 [4.30, 7.28] | — |
| SinGeo-QView | Blur | 42 | 27.35 [18.52, 38.59] | 5.47 [4.22, 6.95] | — |
| SinGeo-QView | Blur | 43 | 28.88 [20.08, 38.38] | 6.43 [4.59, 8.63] | — |
| SinGeo-QView | Blur | mean | 28.12 [20.95, 36.04] | 5.95 [4.56, 7.58] | — |
| SinGeo-QView | Gamma | 42 | 34.69 [19.51, 50.88] | 5.72 [4.24, 7.38] | — |
| SinGeo-QView | Gamma | 43 | 48.28 [24.00, 67.65] | 7.42 [5.64, 9.57] | — |
| SinGeo-QView | Gamma | mean | 41.48 [28.12, 53.93] | 6.57 [5.18, 8.22] | — |
| SinGeo-QView | ExposureClip | 42 | 44.00 [33.69, 54.91] | 5.47 [4.07, 7.09] | — |
| SinGeo-QView | ExposureClip | 43 | 37.27 [27.91, 48.45] | 6.77 [4.96, 8.80] | — |
| SinGeo-QView | ExposureClip | mean | 40.63 [32.65, 49.57] | 6.12 [4.77, 7.71] | — |
| SinGeo-QView | Posterize4 | 42 | 45.00 [15.79, 69.24] | 6.28 [4.71, 8.09] | — |
| SinGeo-QView | Posterize4 | 43 | 25.00 [5.88, 50.00] | 8.68 [6.64, 11.06] | — |
| SinGeo-QView | Posterize4 | mean | 35.00 [15.53, 52.86] | 7.48 [5.92, 9.25] | — |


#### Common Base reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 7.17 [5.48, 9.16] | — |
| Base + QGIN | Clean | 43 | — | 7.47 [5.40, 9.86] | — |
| Base + QGIN | Clean | mean | — | 7.32 [5.62, 9.18] | — |
| Base + QGIN | Fog | 42 | — | 5.51 [4.03, 7.21] | — |
| Base + QGIN | Fog | 43 | — | 5.14 [3.65, 6.87] | — |
| Base + QGIN | Fog | mean | — | 5.32 [3.99, 6.76] | — |
| Base + QGIN | Snow | 42 | 55.30 [48.18, 62.00] | 6.23 [4.37, 8.31] | — |
| Base + QGIN | Snow | 43 | 64.24 [57.03, 70.80] | 4.44 [2.86, 6.72] | — |
| Base + QGIN | Snow | mean | 59.77 [54.36, 64.78] | 5.33 [3.82, 7.17] | — |
| Base + QGIN | Blur | 42 | — | 5.67 [4.07, 7.50] | — |
| Base + QGIN | Blur | 43 | — | 4.21 [2.93, 5.73] | — |
| Base + QGIN | Blur | mean | — | 4.94 [3.68, 6.38] | — |
| Base + QGIN | Gamma | 42 | — | 5.94 [4.46, 7.69] | — |
| Base + QGIN | Gamma | 43 | — | 7.14 [5.17, 9.41] | — |
| Base + QGIN | Gamma | mean | — | 6.54 [5.02, 8.22] | — |
| Base + QGIN | ExposureClip | 42 | 44.93 [32.27, 57.86] | 5.89 [4.37, 7.46] | — |
| Base + QGIN | ExposureClip | 43 | 50.00 [37.61, 62.73] | 6.59 [4.77, 8.58] | — |
| Base + QGIN | ExposureClip | mean | 47.47 [35.60, 58.93] | 6.24 [4.79, 7.78] | — |
| Base + QGIN | Posterize4 | 42 | — | 6.87 [5.21, 8.84] | — |
| Base + QGIN | Posterize4 | 43 | — | 7.09 [5.12, 9.40] | — |
| Base + QGIN | Posterize4 | mean | — | 6.98 [5.34, 8.78] | — |
| S4G-QDual | Clean | 42 | — | 7.59 [5.64, 9.75] | — |
| S4G-QDual | Clean | 43 | — | 7.70 [5.46, 10.02] | — |
| S4G-QDual | Clean | mean | — | 7.65 [5.82, 9.69] | — |
| S4G-QDual | Fog | 42 | — | 6.05 [4.40, 7.92] | — |
| S4G-QDual | Fog | 43 | — | 6.44 [4.61, 8.49] | — |
| S4G-QDual | Fog | mean | — | 6.25 [4.71, 8.02] | — |
| S4G-QDual | Snow | 42 | 61.71 [54.18, 69.16] | 10.43 [7.68, 13.33] | — |
| S4G-QDual | Snow | 43 | 66.67 [59.14, 74.01] | 7.83 [5.45, 10.41] | — |
| S4G-QDual | Snow | mean | 64.19 [57.82, 70.37] | 9.13 [6.70, 11.63] | — |
| S4G-QDual | Blur | 42 | — | 5.45 [3.73, 7.35] | — |
| S4G-QDual | Blur | 43 | — | 5.24 [3.66, 6.96] | — |
| S4G-QDual | Blur | mean | — | 5.35 [3.88, 6.98] | — |
| S4G-QDual | Gamma | 42 | — | 7.44 [5.46, 9.61] | — |
| S4G-QDual | Gamma | 43 | — | 6.95 [4.88, 9.22] | — |
| S4G-QDual | Gamma | mean | — | 7.20 [5.38, 9.25] | — |
| S4G-QDual | ExposureClip | 42 | 55.77 [39.37, 70.59] | 8.12 [5.88, 10.62] | — |
| S4G-QDual | ExposureClip | 43 | 65.95 [50.35, 79.09] | 7.02 [5.06, 9.43] | — |
| S4G-QDual | ExposureClip | mean | 60.86 [45.48, 74.16] | 7.57 [5.61, 9.82] | — |
| S4G-QDual | Posterize4 | 42 | — | 7.18 [5.41, 9.12] | — |
| S4G-QDual | Posterize4 | 43 | — | 7.05 [5.08, 9.25] | — |
| S4G-QDual | Posterize4 | mean | — | 7.12 [5.43, 9.00] | — |
| ConGeo-QView | Clean | 42 | — | 8.96 [7.15, 10.90] | — |
| ConGeo-QView | Clean | 43 | — | 9.02 [6.90, 11.29] | — |
| ConGeo-QView | Clean | mean | — | 8.99 [7.16, 10.89] | — |
| ConGeo-QView | Fog | 42 | — | 7.81 [6.09, 9.71] | — |
| ConGeo-QView | Fog | 43 | — | 7.10 [5.31, 9.18] | — |
| ConGeo-QView | Fog | mean | — | 7.45 [5.91, 9.18] | — |
| ConGeo-QView | Snow | 42 | 57.02 [49.86, 63.99] | 15.79 [12.56, 19.12] | — |
| ConGeo-QView | Snow | 43 | 61.05 [54.50, 67.66] | 11.37 [8.23, 14.42] | — |
| ConGeo-QView | Snow | mean | 59.03 [53.29, 64.75] | 13.58 [10.61, 16.45] | — |
| ConGeo-QView | Blur | 42 | — | 7.16 [5.47, 8.96] | — |
| ConGeo-QView | Blur | 43 | — | 6.47 [4.73, 8.46] | — |
| ConGeo-QView | Blur | mean | — | 6.82 [5.26, 8.47] | — |
| ConGeo-QView | Gamma | 42 | — | 8.99 [7.12, 10.91] | — |
| ConGeo-QView | Gamma | 43 | — | 8.15 [6.13, 10.50] | — |
| ConGeo-QView | Gamma | mean | — | 8.57 [6.76, 10.41] | — |
| ConGeo-QView | ExposureClip | 42 | 55.77 [43.06, 69.56] | 10.89 [8.44, 13.41] | — |
| ConGeo-QView | ExposureClip | 43 | 65.13 [53.32, 75.22] | 9.47 [7.25, 12.05] | — |
| ConGeo-QView | ExposureClip | mean | 60.45 [49.10, 71.04] | 10.18 [8.08, 12.49] | — |
| ConGeo-QView | Posterize4 | 42 | — | 8.96 [7.12, 10.81] | — |
| ConGeo-QView | Posterize4 | 43 | — | 8.63 [6.59, 10.77] | — |
| ConGeo-QView | Posterize4 | mean | — | 8.80 [7.00, 10.60] | — |
| SinGeo-QView | Clean | 42 | — | 14.45 [11.72, 17.34] | — |
| SinGeo-QView | Clean | 43 | — | 13.95 [10.82, 17.33] | — |
| SinGeo-QView | Clean | mean | — | 14.20 [11.36, 17.05] | — |
| SinGeo-QView | Fog | 42 | — | 11.79 [9.39, 14.36] | — |
| SinGeo-QView | Fog | 43 | — | 12.40 [9.38, 15.74] | — |
| SinGeo-QView | Fog | mean | — | 12.10 [9.67, 14.64] | — |
| SinGeo-QView | Snow | 42 | 44.83 [37.49, 52.43] | 17.99 [14.07, 22.06] | — |
| SinGeo-QView | Snow | 43 | 57.58 [50.03, 64.76] | 13.48 [9.76, 17.76] | — |
| SinGeo-QView | Snow | mean | 51.20 [45.28, 57.45] | 15.73 [12.10, 19.71] | — |
| SinGeo-QView | Blur | 42 | — | 12.33 [9.90, 15.02] | — |
| SinGeo-QView | Blur | 43 | — | 11.37 [8.32, 14.80] | — |
| SinGeo-QView | Blur | mean | — | 11.85 [9.38, 14.55] | — |
| SinGeo-QView | Gamma | 42 | — | 13.94 [11.22, 16.82] | — |
| SinGeo-QView | Gamma | 43 | — | 12.87 [9.75, 16.23] | — |
| SinGeo-QView | Gamma | mean | — | 13.41 [10.75, 16.17] | — |
| SinGeo-QView | ExposureClip | 42 | 46.15 [31.16, 62.34] | 15.00 [12.14, 18.06] | — |
| SinGeo-QView | ExposureClip | 43 | 55.92 [44.90, 65.87] | 13.87 [10.57, 17.66] | — |
| SinGeo-QView | ExposureClip | mean | 51.04 [39.16, 62.88] | 14.44 [11.53, 17.59] | — |
| SinGeo-QView | Posterize4 | 42 | — | 14.05 [11.38, 16.89] | — |
| SinGeo-QView | Posterize4 | 43 | — | 13.68 [10.60, 16.96] | — |
| SinGeo-QView | Posterize4 | mean | — | 13.87 [11.20, 16.63] | — |


### SUES → Dense

#### Primary host reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 44.30 [37.74, 51.11] | — |
| Base + QGIN | Clean | 43 | — | 40.25 [33.86, 46.65] | — |
| Base + QGIN | Clean | mean | — | 42.27 [37.01, 47.35] | — |
| Base + QGIN | Fog | 42 | 46.15 [33.33, 59.68] | 36.63 [28.92, 45.40] | 79.17 [61.11, 95.24] |
| Base + QGIN | Fog | 43 | 46.91 [36.36, 57.66] | 36.48 [28.66, 44.96] | 65.00 [43.75, 85.71] |
| Base + QGIN | Fog | mean | 46.53 [37.94, 55.65] | 36.55 [30.36, 43.23] | 72.08 [57.50, 86.19] |
| Base + QGIN | Snow | 42 | 29.51 [21.43, 37.68] | 44.74 [32.89, 56.25] | 59.09 [45.71, 71.43] |
| Base + QGIN | Snow | 43 | 36.00 [25.74, 46.81] | 41.28 [31.37, 52.13] | 71.11 [58.33, 83.03] |
| Base + QGIN | Snow | mean | 32.75 [25.93, 39.84] | 43.01 [34.59, 51.45] | 65.10 [54.33, 75.01] |
| Base + QGIN | Blur | 42 | 42.31 [21.73, 62.50] | 44.09 [36.32, 51.72] | 81.82 [57.14, 100.00] |
| Base + QGIN | Blur | 43 | 33.33 [15.38, 51.72] | 41.15 [33.80, 49.19] | 66.67 [33.33, 93.75] |
| Base + QGIN | Blur | mean | 37.82 [23.69, 52.42] | 42.62 [36.59, 48.74] | 74.24 [55.59, 92.31] |
| Base + QGIN | Gamma | 42 | 53.85 [33.33, 72.01] | 40.64 [33.76, 48.21] | 71.43 [33.33, 100.00] |
| Base + QGIN | Gamma | 43 | 68.75 [44.44, 91.67] | 36.84 [30.00, 43.48] | 100.00 [100.00, 100.00] |
| Base + QGIN | Gamma | mean | 61.30 [43.56, 77.08] | 38.74 [33.12, 44.20] | 85.71 [66.67, 100.00] |
| Base + QGIN | ExposureClip | 42 | 29.21 [19.23, 39.71] | 40.16 [31.21, 49.21] | 54.35 [39.53, 68.63] |
| Base + QGIN | ExposureClip | 43 | 41.11 [31.03, 51.85] | 33.82 [24.30, 43.14] | 78.57 [64.10, 92.31] |
| Base + QGIN | ExposureClip | mean | 35.16 [27.50, 43.17] | 36.99 [29.51, 44.27] | 66.46 [56.57, 76.52] |
| Base + QGIN | Posterize4 | 42 | 20.00 [0.00, 50.00] | 43.77 [37.07, 50.84] | 100.00 [100.00, 100.00] |
| Base + QGIN | Posterize4 | 43 | 44.44 [12.50, 80.00] | 34.63 [28.41, 40.97] | 100.00 [100.00, 100.00] |
| Base + QGIN | Posterize4 | mean | 32.22 [11.11, 55.13] | 39.20 [33.94, 44.70] | 100.00 [100.00, 100.00] |
| S4G-QDual | Clean | 42 | — | 38.80 [34.16, 43.65] | — |
| S4G-QDual | Clean | 43 | — | 37.26 [32.60, 42.12] | — |
| S4G-QDual | Clean | mean | — | 38.03 [34.55, 41.91] | — |
| S4G-QDual | Fog | 42 | 29.17 [20.41, 38.30] | 32.52 [26.94, 38.16] | 51.16 [34.69, 68.00] |
| S4G-QDual | Fog | 43 | 31.76 [21.52, 43.01] | 29.01 [23.81, 34.27] | 45.16 [25.62, 64.71] |
| S4G-QDual | Fog | mean | 30.47 [23.29, 38.31] | 30.76 [27.01, 34.91] | 48.16 [34.77, 61.34] |
| S4G-QDual | Snow | 42 | 31.94 [25.68, 38.56] | 34.76 [26.84, 42.97] | 54.55 [41.93, 67.05] |
| S4G-QDual | Snow | 43 | 31.05 [24.02, 38.27] | 36.05 [27.50, 44.67] | 58.54 [46.97, 68.66] |
| S4G-QDual | Snow | mean | 31.49 [26.34, 36.81] | 35.41 [29.35, 41.69] | 56.54 [47.29, 64.89] |
| S4G-QDual | Blur | 42 | 35.59 [24.14, 48.08] | 30.42 [25.13, 35.92] | 57.14 [37.50, 76.48] |
| S4G-QDual | Blur | 43 | 34.09 [20.83, 47.62] | 37.57 [32.17, 42.74] | 64.29 [37.50, 90.00] |
| S4G-QDual | Blur | mean | 34.84 [25.22, 44.68] | 34.00 [30.06, 38.06] | 60.71 [44.95, 75.95] |
| S4G-QDual | Gamma | 42 | 29.73 [15.56, 45.16] | 35.13 [30.00, 40.38] | 66.67 [39.96, 92.86] |
| S4G-QDual | Gamma | 43 | 43.33 [29.69, 56.86] | 32.80 [27.72, 38.04] | 78.26 [60.00, 94.74] |
| S4G-QDual | Gamma | mean | 36.53 [25.76, 47.36] | 33.96 [30.07, 38.01] | 72.46 [55.02, 89.15] |
| S4G-QDual | ExposureClip | 42 | 29.66 [21.82, 37.50] | 33.96 [27.41, 40.73] | 44.93 [33.33, 57.58] |
| S4G-QDual | ExposureClip | 43 | 23.61 [16.79, 31.29] | 33.04 [26.57, 39.83] | 47.06 [34.78, 59.46] |
| S4G-QDual | ExposureClip | mean | 26.63 [21.10, 32.05] | 33.50 [28.43, 39.02] | 45.99 [37.39, 54.75] |
| S4G-QDual | Posterize4 | 42 | 40.00 [6.96, 75.00] | 33.19 [28.65, 37.93] | 66.67 [20.00, 100.00] |
| S4G-QDual | Posterize4 | 43 | 100.00 [100.00, 100.00] | 33.68 [28.98, 38.85] | 100.00 [100.00, 100.00] |
| S4G-QDual | Posterize4 | mean | 70.00 [51.43, 87.17] | 33.44 [30.05, 37.38] | 83.33 [60.00, 100.00] |
| ConGeo-QView | Clean | 42 | — | 38.25 [33.26, 43.30] | — |
| ConGeo-QView | Clean | 43 | — | 38.09 [33.19, 42.86] | — |
| ConGeo-QView | Clean | mean | — | 38.17 [34.50, 41.89] | — |
| ConGeo-QView | Fog | 42 | 31.58 [21.21, 42.47] | 31.35 [25.76, 37.39] | 56.25 [40.54, 71.80] |
| ConGeo-QView | Fog | 43 | 38.46 [27.78, 49.40] | 34.18 [28.35, 40.49] | 56.00 [35.29, 78.57] |
| ConGeo-QView | Fog | mean | 35.02 [27.47, 42.90] | 32.77 [28.36, 37.25] | 56.12 [42.83, 70.84] |
| ConGeo-QView | Snow | 42 | 29.83 [22.35, 37.37] | 30.30 [22.03, 39.54] | 63.73 [53.53, 73.33] |
| ConGeo-QView | Snow | 43 | 25.79 [19.44, 32.35] | 41.10 [32.89, 49.64] | 50.00 [39.51, 60.26] |
| ConGeo-QView | Snow | mean | 27.81 [22.58, 32.96] | 35.70 [29.56, 42.63] | 56.86 [49.52, 63.93] |
| ConGeo-QView | Blur | 42 | 50.00 [35.82, 63.16] | 34.27 [29.19, 39.88] | 84.21 [64.29, 100.00] |
| ConGeo-QView | Blur | 43 | 34.55 [21.05, 48.94] | 30.65 [25.23, 36.18] | 58.33 [36.84, 80.02] |
| ConGeo-QView | Blur | mean | 42.27 [32.69, 51.67] | 32.46 [28.33, 36.69] | 71.27 [57.42, 84.46] |
| ConGeo-QView | Gamma | 42 | 61.40 [47.83, 74.51] | 37.16 [31.03, 43.33] | 92.86 [75.00, 100.00] |
| ConGeo-QView | Gamma | 43 | 35.71 [24.07, 48.15] | 30.72 [25.34, 36.29] | 59.09 [36.35, 80.77] |
| ConGeo-QView | Gamma | mean | 48.56 [39.12, 57.79] | 33.94 [29.64, 38.72] | 75.97 [62.14, 88.46] |
| ConGeo-QView | ExposureClip | 42 | 25.69 [18.38, 33.33] | 40.62 [32.98, 48.30] | 42.67 [30.55, 54.32] |
| ConGeo-QView | ExposureClip | 43 | 28.15 [20.15, 36.43] | 38.31 [31.68, 45.37] | 36.36 [21.57, 51.35] |
| ConGeo-QView | ExposureClip | mean | 26.92 [21.18, 32.88] | 39.47 [34.03, 45.35] | 39.52 [29.91, 49.85] |
| ConGeo-QView | Posterize4 | 42 | 53.85 [25.00, 83.33] | 36.11 [31.13, 41.53] | 75.00 [0.00, 100.00] |
| ConGeo-QView | Posterize4 | 43 | 50.00 [10.00, 85.71] | 31.49 [26.50, 36.28] | 60.00 [0.00, 100.00] |
| ConGeo-QView | Posterize4 | mean | 51.92 [27.78, 75.00] | 33.80 [30.08, 37.46] | 67.50 [29.17, 100.00] |
| SinGeo-QView | Clean | 42 | — | 41.12 [36.10, 46.35] | — |
| SinGeo-QView | Clean | 43 | — | 37.61 [32.57, 42.66] | — |
| SinGeo-QView | Clean | mean | — | 39.36 [35.65, 43.25] | — |
| SinGeo-QView | Fog | 42 | 33.70 [24.24, 43.59] | 30.15 [24.17, 35.97] | 51.43 [36.00, 67.74] |
| SinGeo-QView | Fog | 43 | 28.12 [18.81, 37.64] | 31.02 [24.81, 37.78] | 57.14 [40.54, 72.73] |
| SinGeo-QView | Fog | mean | 30.91 [24.41, 37.93] | 30.58 [26.10, 35.44] | 54.29 [42.86, 65.92] |
| SinGeo-QView | Snow | 42 | 33.50 [26.00, 41.75] | 38.76 [30.53, 47.41] | 51.35 [41.12, 60.78] |
| SinGeo-QView | Snow | 43 | 28.98 [21.76, 36.17] | 43.59 [33.91, 53.92] | 46.75 [34.48, 59.21] |
| SinGeo-QView | Snow | mean | 31.24 [25.83, 36.93] | 41.17 [34.37, 48.53] | 49.05 [40.45, 57.14] |
| SinGeo-QView | Blur | 42 | 31.15 [20.34, 42.55] | 36.10 [30.06, 42.71] | 61.11 [38.10, 85.71] |
| SinGeo-QView | Blur | 43 | 38.60 [25.00, 52.54] | 35.02 [29.27, 41.37] | 80.00 [57.14, 100.00] |
| SinGeo-QView | Blur | mean | 34.87 [25.46, 43.86] | 35.56 [31.14, 40.46] | 70.56 [54.60, 86.67] |
| SinGeo-QView | Gamma | 42 | 37.78 [23.68, 52.94] | 38.97 [33.43, 44.60] | 61.90 [40.00, 81.82] |
| SinGeo-QView | Gamma | 43 | 26.67 [14.29, 40.44] | 34.53 [28.97, 40.61] | 47.06 [23.08, 75.00] |
| SinGeo-QView | Gamma | mean | 32.22 [23.11, 41.95] | 36.75 [32.51, 41.31] | 54.48 [38.69, 71.50] |
| SinGeo-QView | ExposureClip | 42 | 24.64 [17.22, 32.28] | 40.93 [33.01, 48.92] | 45.21 [33.33, 56.06] |
| SinGeo-QView | ExposureClip | 43 | 31.39 [24.11, 39.70] | 33.16 [25.64, 41.15] | 50.65 [38.57, 62.69] |
| SinGeo-QView | ExposureClip | mean | 28.01 [22.54, 33.77] | 37.04 [31.06, 43.43] | 47.93 [39.10, 57.07] |
| SinGeo-QView | Posterize4 | 42 | 42.86 [0.00, 85.71] | 40.80 [35.71, 46.17] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Posterize4 | 43 | 33.33 [0.00, 80.00] | 37.08 [32.01, 42.58] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Posterize4 | mean | 38.10 [10.00, 70.02] | 38.94 [35.06, 43.37] | 100.00 [100.00, 100.00] |


#### Common Base reference

| Method | Condition | Seed | Rescue % [CI] | New failure % [CI] | Far-error removal % [CI] |
| --- | --- | --- | --- | --- | --- |
| Base + QGIN | Clean | 42 | — | 44.30 [37.74, 51.11] | — |
| Base + QGIN | Clean | 43 | — | 40.25 [33.86, 46.65] | — |
| Base + QGIN | Clean | mean | — | 42.27 [37.01, 47.35] | — |
| Base + QGIN | Fog | 42 | 46.15 [33.33, 59.68] | 36.63 [28.92, 45.40] | 79.17 [61.11, 95.24] |
| Base + QGIN | Fog | 43 | 46.91 [36.36, 57.66] | 36.48 [28.66, 44.96] | 65.00 [43.75, 85.71] |
| Base + QGIN | Fog | mean | 46.53 [37.94, 55.65] | 36.55 [30.36, 43.23] | 72.08 [57.50, 86.19] |
| Base + QGIN | Snow | 42 | 29.51 [21.43, 37.68] | 44.74 [32.89, 56.25] | 59.09 [45.71, 71.43] |
| Base + QGIN | Snow | 43 | 36.00 [25.74, 46.81] | 41.28 [31.37, 52.13] | 71.11 [58.33, 83.03] |
| Base + QGIN | Snow | mean | 32.75 [25.93, 39.84] | 43.01 [34.59, 51.45] | 65.10 [54.33, 75.01] |
| Base + QGIN | Blur | 42 | 42.31 [21.73, 62.50] | 44.09 [36.32, 51.72] | 81.82 [57.14, 100.00] |
| Base + QGIN | Blur | 43 | 33.33 [15.38, 51.72] | 41.15 [33.80, 49.19] | 66.67 [33.33, 93.75] |
| Base + QGIN | Blur | mean | 37.82 [23.69, 52.42] | 42.62 [36.59, 48.74] | 74.24 [55.59, 92.31] |
| Base + QGIN | Gamma | 42 | 53.85 [33.33, 72.01] | 40.64 [33.76, 48.21] | 71.43 [33.33, 100.00] |
| Base + QGIN | Gamma | 43 | 68.75 [44.44, 91.67] | 36.84 [30.00, 43.48] | 100.00 [100.00, 100.00] |
| Base + QGIN | Gamma | mean | 61.30 [43.56, 77.08] | 38.74 [33.12, 44.20] | 85.71 [66.67, 100.00] |
| Base + QGIN | ExposureClip | 42 | 29.21 [19.23, 39.71] | 40.16 [31.21, 49.21] | 54.35 [39.53, 68.63] |
| Base + QGIN | ExposureClip | 43 | 41.11 [31.03, 51.85] | 33.82 [24.30, 43.14] | 78.57 [64.10, 92.31] |
| Base + QGIN | ExposureClip | mean | 35.16 [27.50, 43.17] | 36.99 [29.51, 44.27] | 66.46 [56.57, 76.52] |
| Base + QGIN | Posterize4 | 42 | 20.00 [0.00, 50.00] | 43.77 [37.07, 50.84] | 100.00 [100.00, 100.00] |
| Base + QGIN | Posterize4 | 43 | 44.44 [12.50, 80.00] | 34.63 [28.41, 40.97] | 100.00 [100.00, 100.00] |
| Base + QGIN | Posterize4 | mean | 32.22 [11.11, 55.13] | 39.20 [33.94, 44.70] | 100.00 [100.00, 100.00] |
| S4G-QDual | Clean | 42 | — | 45.60 [39.02, 52.33] | — |
| S4G-QDual | Clean | 43 | — | 45.51 [39.22, 52.05] | — |
| S4G-QDual | Clean | mean | — | 45.56 [40.52, 50.64] | — |
| S4G-QDual | Fog | 42 | 43.08 [31.58, 54.67] | 38.37 [30.43, 47.16] | 83.33 [66.67, 96.30] |
| S4G-QDual | Fog | 43 | 41.98 [30.77, 54.29] | 40.88 [32.54, 49.65] | 80.00 [61.53, 95.45] |
| S4G-QDual | Fog | mean | 42.53 [34.18, 51.00] | 39.63 [33.54, 46.51] | 81.67 [68.57, 93.33] |
| S4G-QDual | Snow | 42 | 33.61 [24.44, 42.72] | 50.00 [37.50, 62.30] | 71.21 [58.00, 83.08] |
| S4G-QDual | Snow | 43 | 42.00 [32.00, 52.00] | 40.37 [30.51, 50.45] | 75.56 [62.00, 87.50] |
| S4G-QDual | Snow | mean | 37.80 [30.32, 45.26] | 45.18 [36.70, 54.14] | 73.38 [63.09, 83.07] |
| S4G-QDual | Blur | 42 | 53.85 [33.33, 73.08] | 43.64 [36.25, 51.31] | 100.00 [100.00, 100.00] |
| S4G-QDual | Blur | 43 | 50.00 [31.24, 67.86] | 46.46 [39.33, 53.85] | 91.67 [71.43, 100.00] |
| S4G-QDual | Blur | mean | 51.92 [38.17, 64.57] | 45.05 [39.09, 51.23] | 95.83 [85.71, 100.00] |
| S4G-QDual | Gamma | 42 | 50.00 [30.00, 69.58] | 43.84 [36.19, 51.57] | 71.43 [33.33, 100.00] |
| S4G-QDual | Gamma | 43 | 50.00 [22.22, 75.00] | 42.51 [35.48, 50.01] | 50.00 [0.00, 100.00] |
| S4G-QDual | Gamma | mean | 50.00 [33.39, 66.27] | 43.17 [37.48, 49.18] | 60.71 [21.43, 100.00] |
| S4G-QDual | ExposureClip | 42 | 30.34 [20.22, 41.24] | 46.46 [36.47, 55.93] | 60.87 [46.15, 75.56] |
| S4G-QDual | ExposureClip | 43 | 30.00 [20.62, 40.21] | 44.12 [35.17, 54.17] | 76.19 [62.74, 89.47] |
| S4G-QDual | ExposureClip | mean | 30.17 [23.00, 38.43] | 45.29 [37.80, 53.17] | 68.53 [57.54, 79.03] |
| S4G-QDual | Posterize4 | 42 | 60.00 [25.00, 90.91] | 46.79 [39.91, 53.90] | 100.00 [100.00, 100.00] |
| S4G-QDual | Posterize4 | 43 | 33.33 [0.00, 66.67] | 44.88 [38.33, 51.80] | 100.00 [100.00, 100.00] |
| S4G-QDual | Posterize4 | mean | 46.67 [22.92, 69.64] | 45.83 [40.50, 50.98] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Clean | 42 | — | 48.86 [42.30, 55.48] | — |
| ConGeo-QView | Clean | 43 | — | 52.63 [45.91, 59.26] | — |
| ConGeo-QView | Clean | mean | — | 50.75 [45.29, 56.06] | — |
| ConGeo-QView | Fog | 42 | 38.46 [26.23, 50.85] | 44.77 [36.26, 53.59] | 75.00 [56.00, 91.30] |
| ConGeo-QView | Fog | 43 | 34.57 [24.49, 45.31] | 40.25 [31.47, 49.41] | 65.00 [42.09, 85.00] |
| ConGeo-QView | Fog | mean | 36.51 [27.78, 45.13] | 42.51 [35.87, 49.43] | 70.00 [57.17, 81.85] |
| ConGeo-QView | Snow | 42 | 33.61 [24.43, 42.59] | 57.89 [46.15, 70.15] | 68.18 [55.00, 80.00] |
| ConGeo-QView | Snow | 43 | 29.00 [20.83, 38.05] | 59.63 [48.48, 70.94] | 64.44 [51.06, 77.27] |
| ConGeo-QView | Snow | mean | 31.30 [24.63, 38.29] | 58.76 [50.07, 68.02] | 66.31 [56.88, 75.49] |
| ConGeo-QView | Blur | 42 | 53.85 [33.31, 73.68] | 53.64 [45.75, 61.47] | 81.82 [54.55, 100.00] |
| ConGeo-QView | Blur | 43 | 33.33 [16.67, 50.00] | 50.44 [43.25, 57.79] | 91.67 [75.00, 100.00] |
| ConGeo-QView | Blur | mean | 43.59 [30.29, 56.28] | 52.04 [46.15, 58.17] | 86.74 [72.12, 100.00] |
| ConGeo-QView | Gamma | 42 | 53.85 [33.33, 73.08] | 45.21 [37.81, 53.07] | 85.71 [50.00, 100.00] |
| ConGeo-QView | Gamma | 43 | 56.25 [28.57, 80.00] | 51.42 [43.39, 59.25] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Gamma | mean | 55.05 [37.01, 71.71] | 48.31 [42.25, 54.65] | 92.86 [75.00, 100.00] |
| ConGeo-QView | ExposureClip | 42 | 19.10 [10.52, 28.40] | 56.69 [47.62, 65.35] | 50.00 [34.69, 65.00] |
| ConGeo-QView | ExposureClip | 43 | 24.44 [15.28, 34.21] | 51.47 [41.48, 62.02] | 66.67 [52.27, 81.14] |
| ConGeo-QView | ExposureClip | mean | 21.77 [15.20, 29.12] | 54.08 [46.42, 62.17] | 58.33 [47.00, 69.74] |
| ConGeo-QView | Posterize4 | 42 | 60.00 [25.00, 90.00] | 49.06 [42.52, 56.25] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Posterize4 | 43 | 44.44 [12.50, 80.00] | 47.35 [40.48, 54.14] | 100.00 [100.00, 100.00] |
| ConGeo-QView | Posterize4 | mean | 52.22 [27.78, 75.25] | 48.20 [42.79, 53.71] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Clean | 42 | — | 53.75 [47.20, 60.44] | — |
| SinGeo-QView | Clean | 43 | — | 46.13 [39.82, 52.71] | — |
| SinGeo-QView | Clean | mean | — | 49.94 [44.77, 55.20] | — |
| SinGeo-QView | Fog | 42 | 49.23 [36.92, 61.34] | 45.35 [36.60, 53.71] | 75.00 [56.67, 91.31] |
| SinGeo-QView | Fog | 43 | 39.51 [28.05, 51.22] | 46.54 [38.00, 55.79] | 70.00 [46.67, 90.00] |
| SinGeo-QView | Fog | mean | 44.37 [35.87, 53.05] | 45.94 [39.19, 53.07] | 72.50 [57.69, 85.67] |
| SinGeo-QView | Snow | 42 | 27.87 [18.75, 36.74] | 57.89 [45.33, 70.89] | 66.67 [53.85, 77.97] |
| SinGeo-QView | Snow | 43 | 31.00 [21.70, 40.17] | 56.88 [46.34, 68.14] | 60.00 [44.74, 75.00] |
| SinGeo-QView | Snow | mean | 29.43 [22.34, 36.42] | 57.39 [47.95, 67.16] | 63.33 [53.53, 72.60] |
| SinGeo-QView | Blur | 42 | 38.46 [17.39, 58.62] | 51.82 [44.27, 59.66] | 72.73 [42.86, 100.00] |
| SinGeo-QView | Blur | 43 | 30.00 [14.29, 47.38] | 46.46 [38.86, 54.38] | 91.67 [71.43, 100.00] |
| SinGeo-QView | Blur | mean | 34.23 [21.12, 46.80] | 49.14 [42.97, 55.35] | 82.20 [65.58, 96.67] |
| SinGeo-QView | Gamma | 42 | 42.31 [23.52, 61.30] | 52.97 [45.36, 60.09] | 85.71 [50.00, 100.00] |
| SinGeo-QView | Gamma | 43 | 50.00 [25.00, 75.00] | 44.13 [36.49, 51.43] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Gamma | mean | 46.15 [30.30, 61.66] | 48.55 [42.30, 54.48] | 92.86 [75.00, 100.00] |
| SinGeo-QView | ExposureClip | 42 | 15.73 [7.69, 25.00] | 59.84 [49.59, 69.72] | 41.30 [26.66, 55.56] |
| SinGeo-QView | ExposureClip | 43 | 24.44 [15.38, 34.15] | 46.32 [36.94, 56.10] | 66.67 [51.28, 81.08] |
| SinGeo-QView | ExposureClip | mean | 20.09 [13.52, 27.39] | 53.08 [44.64, 61.42] | 53.99 [42.02, 65.42] |
| SinGeo-QView | Posterize4 | 42 | 30.00 [0.00, 61.12] | 53.58 [46.30, 60.64] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Posterize4 | 43 | 44.44 [11.11, 80.05] | 43.11 [36.23, 50.00] | 100.00 [100.00, 100.00] |
| SinGeo-QView | Posterize4 | mean | 37.22 [13.64, 61.11] | 48.35 [42.64, 53.88] | 100.00 [100.00, 100.00] |


## B. Photometric operator ablations

StdDual uses scalar contrast/brightness; ColorJitter-Dual uses brightness/contrast/saturation 0.40 and hue 0.10; AugMix-Dual uses severity 3, width 3, stochastic depth and alpha 1.00. The Fixed Zero-Hinge control has the same sampled pointwise architecture, normalization and single mix as QGIN. SUES-trained ColorJitter-Dual was not evaluated and is shown as —.

### Dense → Dense

#### Two-seed mean

#### Clean

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 84.53 [82.63, 86.40] | 96.18 [95.15, 97.15] | 74.95 [73.38, 76.60] | 86.17 [84.72, 87.69] | 68.12 [47.62, 91.30] | 2.49 [1.76, 3.33] | 84.04 [81.53, 85.59] |
| Base + StdDual | 83.91 [82.00, 85.82] | 96.07 [95.07, 97.02] | 74.56 [72.97, 76.20] | 85.71 [84.26, 87.25] | 71.10 [50.08, 94.94] | 2.70 [1.93, 3.54] | 83.08 [80.57, 84.75] |
| Base + ColorJitter-Dual | 84.28 [82.41, 86.27] | 95.86 [94.89, 96.83] | 74.69 [73.15, 76.36] | 85.99 [84.61, 87.48] | 68.73 [47.80, 91.90] | 2.49 [1.76, 3.32] | 83.91 [81.34, 85.46] |
| Base + AugMix-Dual | 85.31 [83.50, 87.11] | 96.37 [95.43, 97.23] | 75.62 [74.08, 77.26] | 86.85 [85.45, 88.26] | 61.55 [42.29, 82.10] | 2.36 [1.65, 3.13] | 84.62 [82.18, 86.16] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 84.45 [82.56, 86.40] | 95.84 [94.83, 96.83] | 75.19 [73.61, 76.89] | 86.02 [84.56, 87.57] | 68.57 [47.95, 92.29] | 2.62 [1.80, 3.50] | 83.66 [81.08, 85.39] |
| Base + QGIN (Ours) | 86.01 [84.23, 87.75] | 96.46 [95.54, 97.32] | 77.19 [75.57, 78.84] | 87.30 [85.92, 88.71] | 64.39 [45.46, 86.54] | 2.64 [1.93, 3.45] | 84.56 [82.37, 86.49] |
| Sample4Geo† [ICCV 2023] | 86.34 [84.58, 88.10] | 97.04 [96.16, 97.88] | 76.22 [74.65, 77.80] | 87.97 [86.69, 89.21] | 38.82 [26.08, 53.61] | 1.74 [1.14, 2.38] | 85.39 [83.20, 87.13] |
| S4G-StdDual | 85.63 [83.87, 87.45] | 97.47 [96.70, 98.20] | 75.93 [74.38, 77.52] | 87.51 [86.21, 88.83] | 38.70 [25.47, 52.97] | 1.72 [1.12, 2.36] | 84.04 [81.79, 85.97] |
| S4G-QDual (Ours) | 86.29 [84.58, 87.92] | 97.90 [97.19, 98.52] | 77.69 [76.17, 79.22] | 88.30 [87.08, 89.50] | 42.48 [28.56, 58.63] | 1.72 [1.14, 2.34] | 85.59 [83.33, 87.07] |


#### Fog

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 72.99 [70.76, 75.31] | 91.83 [90.48, 93.14] | 63.54 [61.84, 65.31] | 76.91 [75.21, 78.60] | 132.24 [104.56, 160.06] | 5.21 [4.18, 6.29] | 65.25 [62.36, 68.21] |
| Base + StdDual | 72.24 [70.01, 74.50] | 91.72 [90.37, 93.03] | 63.11 [61.39, 64.93] | 76.39 [74.74, 78.08] | 140.92 [112.71, 169.73] | 5.73 [4.65, 6.89] | 64.74 [61.84, 67.63] |
| Base + ColorJitter-Dual | 71.69 [69.46, 73.98] | 91.36 [89.98, 92.69] | 62.42 [60.78, 64.20] | 75.57 [73.88, 77.26] | 140.05 [110.70, 169.63] | 5.51 [4.44, 6.67] | 63.06 [60.10, 66.09] |
| Base + AugMix-Dual | 73.14 [70.98, 75.38] | 92.43 [91.12, 93.69] | 64.00 [62.27, 65.81] | 77.25 [75.65, 78.88] | 122.22 [95.65, 149.98] | 4.80 [3.80, 5.90] | 66.15 [63.45, 69.11] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 71.99 [69.67, 74.30] | 91.89 [90.54, 93.22] | 64.21 [62.44, 66.08] | 76.65 [74.96, 78.47] | 131.08 [100.57, 160.48] | 5.30 [4.14, 6.46] | 65.19 [62.10, 68.28] |
| Base + QGIN (Ours) | 74.41 [72.31, 76.56] | 92.77 [91.51, 93.97] | 65.71 [64.10, 67.56] | 78.01 [76.39, 79.69] | 119.15 [92.72, 148.35] | 5.02 [4.03, 6.13] | 66.99 [64.09, 69.88] |
| Sample4Geo† [ICCV 2023] | 77.76 [75.72, 79.86] | 94.42 [93.39, 95.45] | 67.41 [65.70, 69.11] | 81.50 [80.06, 83.00] | 68.98 [50.92, 89.17] | 2.92 [2.19, 3.73] | 72.46 [69.82, 75.10] |
| S4G-StdDual | 77.24 [75.18, 79.39] | 94.34 [93.29, 95.35] | 67.17 [65.45, 68.88] | 81.31 [79.82, 82.86] | 62.89 [46.25, 80.85] | 2.64 [1.95, 3.47] | 70.98 [68.21, 73.68] |
| S4G-QDual (Ours) | 80.33 [78.34, 82.22] | 95.37 [94.40, 96.31] | 70.48 [68.78, 72.14] | 83.37 [81.91, 84.80] | 60.82 [44.16, 79.26] | 2.55 [1.84, 3.35] | 75.16 [72.52, 77.67] |


#### Snow

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 66.02 [63.71, 68.32] | 84.56 [82.80, 86.31] | 55.96 [54.11, 57.88] | 68.32 [66.41, 70.28] | 386.84 [340.73, 432.41] | 14.48 [12.89, 16.17] | 59.65 [56.50, 62.74] |
| Base + StdDual | 65.85 [63.43, 68.17] | 84.56 [82.80, 86.38] | 56.49 [54.62, 58.35] | 68.83 [66.89, 70.79] | 387.25 [341.15, 435.74] | 14.67 [13.06, 16.35] | 58.75 [55.73, 61.84] |
| Base + ColorJitter-Dual | 66.71 [64.39, 68.96] | 85.74 [84.04, 87.39] | 57.25 [55.48, 59.14] | 69.50 [67.63, 71.38] | 365.12 [321.07, 410.17] | 13.77 [12.25, 15.34] | 60.42 [57.40, 63.38] |
| Base + AugMix-Dual | 70.66 [68.47, 72.87] | 88.37 [86.91, 89.83] | 61.20 [59.43, 63.02] | 73.33 [71.52, 75.12] | 292.60 [251.87, 334.48] | 11.07 [9.63, 12.46] | 65.57 [62.68, 68.47] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 70.23 [68.04, 72.42] | 87.54 [85.95, 89.10] | 60.79 [59.01, 62.66] | 72.99 [71.24, 74.83] | 280.20 [241.46, 318.75] | 11.05 [9.63, 12.46] | 64.67 [61.84, 67.63] |
| Base + QGIN (Ours) | 77.89 [75.87, 79.90] | 92.88 [91.68, 94.08] | 69.23 [67.59, 71.03] | 79.99 [78.36, 81.71] | 165.08 [134.65, 197.21] | 6.37 [5.30, 7.53] | 74.39 [71.81, 76.96] |
| Sample4Geo† [ICCV 2023] | 64.69 [62.42, 66.99] | 85.16 [83.53, 86.77] | 55.88 [54.04, 57.70] | 67.89 [66.03, 69.72] | 380.03 [336.33, 421.63] | 15.06 [13.45, 16.69] | 59.97 [57.08, 62.81] |
| S4G-StdDual | 66.07 [63.71, 68.28] | 86.04 [84.45, 87.58] | 56.58 [54.75, 58.38] | 68.98 [67.01, 70.81] | 347.10 [304.86, 390.25] | 13.64 [12.10, 15.19] | 63.06 [60.17, 65.83] |
| S4G-QDual (Ours) | 80.39 [78.59, 82.28] | 95.37 [94.42, 96.22] | 70.91 [69.27, 72.53] | 82.64 [81.23, 84.05] | 108.10 [84.71, 131.97] | 4.12 [3.22, 5.08] | 78.57 [76.00, 80.76] |


#### Blur

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 82.58 [80.65, 84.62] | 95.35 [94.23, 96.40] | 73.52 [71.82, 75.29] | 84.98 [83.49, 86.58] | 85.23 [63.03, 110.20] | 3.26 [2.40, 4.18] | 81.47 [78.96, 83.46] |
| Base + StdDual | 82.48 [80.52, 84.47] | 95.11 [93.97, 96.25] | 73.26 [71.56, 74.99] | 84.91 [83.42, 86.47] | 88.25 [65.54, 114.04] | 3.41 [2.55, 4.31] | 80.95 [78.51, 82.95] |
| Base + ColorJitter-Dual | 83.12 [81.15, 85.14] | 94.77 [93.67, 95.82] | 73.33 [71.71, 75.03] | 84.78 [83.25, 86.32] | 82.31 [59.11, 107.40] | 3.26 [2.40, 4.20] | 81.85 [79.47, 83.91] |
| Base + AugMix-Dual | 83.63 [81.70, 85.52] | 95.67 [94.59, 96.65] | 74.35 [72.72, 76.06] | 85.88 [84.36, 87.41] | 74.44 [53.48, 96.51] | 2.98 [2.15, 3.90] | 82.82 [80.31, 84.56] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 82.78 [80.87, 84.79] | 94.51 [93.37, 95.65] | 73.38 [71.64, 75.21] | 84.44 [82.90, 86.06] | 90.34 [67.79, 114.06] | 3.84 [2.90, 4.78] | 80.57 [77.99, 83.01] |
| Base + QGIN (Ours) | 84.96 [83.05, 86.74] | 95.41 [94.36, 96.42] | 75.35 [73.72, 77.06] | 86.00 [84.47, 87.52] | 79.45 [57.86, 104.31] | 3.28 [2.45, 4.25] | 83.08 [80.69, 85.27] |
| Sample4Geo† [ICCV 2023] | 85.84 [84.10, 87.67] | 97.02 [96.16, 97.81] | 75.55 [73.99, 77.12] | 87.41 [86.14, 88.71] | 43.82 [29.64, 59.84] | 1.87 [1.24, 2.53] | 84.36 [82.18, 86.36] |
| S4G-StdDual | 85.65 [83.83, 87.49] | 97.23 [96.42, 98.01] | 75.55 [73.95, 77.10] | 87.25 [85.98, 88.57] | 38.51 [26.75, 52.37] | 1.76 [1.16, 2.42] | 84.11 [81.92, 86.23] |
| S4G-QDual (Ours) | 86.25 [84.60, 87.90] | 97.47 [96.70, 98.18] | 76.89 [75.30, 78.41] | 87.84 [86.57, 89.10] | 44.90 [30.06, 62.58] | 1.87 [1.24, 2.55] | 83.78 [81.53, 85.91] |


#### Gamma

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 83.70 [81.83, 85.63] | 95.67 [94.57, 96.70] | 74.08 [72.46, 75.79] | 85.43 [84.00, 86.98] | 82.23 [60.13, 107.17] | 3.22 [2.38, 4.12] | 82.69 [80.24, 84.49] |
| Base + StdDual | 83.20 [81.30, 85.14] | 95.54 [94.47, 96.57] | 73.74 [72.15, 75.42] | 85.28 [83.83, 86.81] | 88.93 [65.94, 114.45] | 3.43 [2.60, 4.35] | 82.18 [79.60, 83.85] |
| Base + ColorJitter-Dual | 83.81 [81.96, 85.76] | 95.67 [94.70, 96.61] | 74.07 [72.51, 75.73] | 85.37 [83.91, 86.88] | 75.66 [54.20, 98.96] | 3.07 [2.25, 3.97] | 82.95 [80.50, 84.62] |
| Base + AugMix-Dual | 84.60 [82.73, 86.47] | 95.67 [94.62, 96.65] | 74.64 [73.02, 76.33] | 86.13 [84.72, 87.55] | 76.64 [56.57, 99.32] | 2.96 [2.17, 3.84] | 83.72 [81.21, 85.33] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 83.81 [81.90, 85.71] | 95.75 [94.72, 96.76] | 74.74 [73.12, 76.47] | 85.59 [84.09, 87.15] | 72.66 [53.14, 94.46] | 2.92 [2.12, 3.78] | 83.08 [80.50, 84.75] |
| Base + QGIN (Ours) | 85.78 [84.04, 87.56] | 96.29 [95.35, 97.19] | 76.69 [75.05, 78.34] | 86.96 [85.54, 88.41] | 69.53 [49.72, 92.33] | 3.05 [2.25, 3.93] | 84.81 [82.56, 86.55] |
| Sample4Geo† [ICCV 2023] | 85.82 [83.93, 87.60] | 97.06 [96.20, 97.85] | 75.40 [73.81, 76.97] | 87.26 [85.93, 88.51] | 47.38 [32.65, 63.70] | 2.04 [1.39, 2.72] | 84.88 [82.69, 86.55] |
| S4G-StdDual | 85.48 [83.74, 87.24] | 97.51 [96.76, 98.20] | 75.39 [73.80, 76.98] | 87.17 [85.88, 88.48] | 52.27 [35.72, 70.31] | 2.23 [1.54, 3.00] | 84.23 [82.18, 86.10] |
| S4G-QDual (Ours) | 86.10 [84.34, 87.75] | 97.79 [97.08, 98.43] | 77.32 [75.76, 78.83] | 88.08 [86.86, 89.31] | 44.70 [29.97, 61.39] | 1.76 [1.20, 2.38] | 85.71 [83.20, 87.07] |


#### ExposureClip

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 76.34 [74.35, 78.40] | 91.42 [90.07, 92.71] | 66.77 [65.10, 68.57] | 78.75 [77.07, 80.41] | 173.60 [145.14, 205.16] | 7.34 [6.22, 8.60] | 75.16 [72.46, 77.28] |
| Base + StdDual | 76.45 [74.39, 78.46] | 91.46 [90.09, 92.77] | 66.65 [64.98, 68.46] | 78.63 [76.94, 80.31] | 188.53 [155.73, 223.10] | 7.64 [6.41, 8.92] | 74.90 [72.26, 77.16] |
| Base + ColorJitter-Dual | 78.51 [76.51, 80.42] | 92.43 [91.10, 93.72] | 68.53 [66.85, 70.36] | 80.45 [78.85, 82.05] | 150.16 [121.24, 183.21] | 6.46 [5.38, 7.68] | 77.09 [74.52, 79.15] |
| Base + AugMix-Dual | 78.04 [76.10, 79.94] | 92.77 [91.57, 93.93] | 68.44 [66.72, 70.25] | 80.24 [78.62, 81.84] | 159.10 [130.38, 189.98] | 6.63 [5.47, 7.83] | 77.41 [74.65, 79.02] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 78.01 [76.00, 79.99] | 92.45 [91.18, 93.69] | 68.39 [66.69, 70.21] | 80.18 [78.51, 81.84] | 151.62 [123.56, 181.84] | 6.31 [5.23, 7.44] | 76.58 [74.00, 78.76] |
| Base + QGIN (Ours) | 81.02 [79.06, 82.90] | 93.99 [92.79, 95.17] | 72.04 [70.34, 73.77] | 82.98 [81.43, 84.53] | 129.50 [104.32, 158.23] | 5.53 [4.53, 6.65] | 79.09 [76.58, 81.27] |
| Sample4Geo† [ICCV 2023] | 76.83 [74.77, 79.02] | 92.17 [90.93, 93.39] | 66.71 [64.97, 68.53] | 79.18 [77.57, 80.84] | 171.26 [140.30, 203.38] | 7.36 [6.13, 8.62] | 76.32 [73.49, 77.99] |
| S4G-StdDual | 77.39 [75.40, 79.52] | 92.73 [91.55, 93.91] | 67.43 [65.74, 69.22] | 79.72 [78.16, 81.33] | 162.22 [132.37, 193.07] | 6.89 [5.75, 8.11] | 75.93 [73.29, 78.12] |
| S4G-QDual (Ours) | 81.85 [79.94, 83.74] | 95.65 [94.77, 96.50] | 72.30 [70.68, 73.92] | 83.80 [82.38, 85.23] | 104.75 [80.79, 130.32] | 4.16 [3.28, 5.08] | 81.21 [78.64, 82.82] |


#### Posterize4

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 84.43 [82.52, 86.36] | 95.92 [94.87, 96.93] | 74.87 [73.32, 76.52] | 86.15 [84.72, 87.65] | 70.86 [50.31, 94.20] | 2.51 [1.78, 3.35] | 83.66 [81.21, 85.39] |
| Base + StdDual | 83.78 [81.81, 85.69] | 96.10 [95.09, 97.06] | 74.54 [72.97, 76.21] | 85.80 [84.33, 87.32] | 70.91 [50.94, 93.09] | 2.77 [1.99, 3.60] | 82.63 [80.24, 84.56] |
| Base + ColorJitter-Dual | 84.45 [82.58, 86.34] | 95.97 [95.02, 96.93] | 74.73 [73.19, 76.38] | 85.90 [84.50, 87.37] | 68.83 [48.87, 90.73] | 2.62 [1.87, 3.45] | 83.66 [81.21, 85.52] |
| Base + AugMix-Dual | 85.18 [83.33, 87.00] | 96.29 [95.32, 97.17] | 75.66 [74.12, 77.27] | 86.90 [85.51, 88.30] | 62.69 [43.61, 83.42] | 2.38 [1.67, 3.17] | 84.11 [81.79, 85.91] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 84.45 [82.54, 86.38] | 96.03 [95.00, 97.02] | 75.21 [73.62, 76.95] | 86.02 [84.58, 87.56] | 66.76 [46.53, 89.94] | 2.64 [1.84, 3.48] | 83.53 [81.02, 85.39] |
| Base + QGIN (Ours) | 85.74 [83.91, 87.52] | 96.53 [95.58, 97.38] | 77.18 [75.57, 78.81] | 87.28 [85.86, 88.68] | 66.18 [46.34, 89.00] | 2.60 [1.89, 3.41] | 83.98 [81.66, 86.04] |
| Sample4Geo† [ICCV 2023] | 86.72 [84.92, 88.50] | 97.13 [96.29, 97.94] | 76.19 [74.61, 77.75] | 87.95 [86.65, 89.20] | 36.81 [23.99, 51.20] | 1.61 [1.03, 2.25] | 85.14 [83.01, 87.19] |
| S4G-StdDual | 85.76 [83.96, 87.56] | 97.47 [96.72, 98.20] | 75.86 [74.30, 77.46] | 87.44 [86.13, 88.74] | 37.00 [25.37, 50.15] | 1.67 [1.12, 2.30] | 84.17 [81.79, 86.10] |
| S4G-QDual (Ours) | 86.42 [84.77, 88.01] | 97.88 [97.17, 98.52] | 77.67 [76.13, 79.19] | 88.36 [87.14, 89.57] | 40.39 [25.85, 56.91] | 1.61 [1.05, 2.25] | 85.39 [83.20, 86.94] |


#### CorrMean6

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 77.68 [75.93, 79.49] | 92.46 [91.40, 93.49] | 68.12 [66.60, 69.74] | 80.09 [78.72, 81.53] | 155.17 [133.10, 178.33] | 6.00 [5.18, 6.87] | 74.95 [73.02, 76.96] |
| Base + StdDual | 77.33 [75.54, 79.09] | 92.41 [91.38, 93.48] | 67.96 [66.42, 69.59] | 79.97 [78.58, 81.43] | 160.80 [138.70, 184.91] | 6.27 [5.44, 7.18] | 74.38 [72.38, 76.42] |
| Base + ColorJitter-Dual | 78.05 [76.33, 79.87] | 92.65 [91.62, 93.68] | 68.39 [66.88, 69.98] | 80.26 [78.87, 81.70] | 147.02 [124.95, 170.77] | 5.78 [4.96, 6.67] | 75.15 [73.25, 77.05] |
| Base + AugMix-Dual | 79.21 [77.47, 80.92] | 93.53 [92.54, 94.47] | 69.72 [68.16, 71.32] | 81.62 [80.26, 83.00] | 131.28 [111.01, 152.69] | 5.14 [4.32, 6.00] | 76.75 [74.83, 78.72] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 78.54 [76.76, 80.37] | 93.03 [92.02, 94.07] | 69.45 [67.92, 71.11] | 80.98 [79.56, 82.47] | 132.11 [110.57, 155.19] | 5.34 [4.51, 6.20] | 76.10 [74.10, 78.15] |
| Base + QGIN (Ours) | 81.63 [79.91, 83.33] | 94.64 [93.67, 95.55] | 72.70 [71.14, 74.30] | 83.54 [82.15, 84.97] | 104.82 [84.32, 127.03] | 4.31 [3.52, 5.17] | 79.12 [77.12, 81.02] |
| Sample4Geo† [ICCV 2023] | 79.61 [77.97, 81.24] | 93.83 [93.01, 94.66] | 69.52 [68.02, 71.06] | 81.87 [80.61, 83.13] | 124.71 [107.83, 142.71] | 5.14 [4.43, 5.90] | 77.75 [75.82, 79.61] |
| S4G-StdDual | 79.60 [77.92, 81.31] | 94.22 [93.46, 94.99] | 69.66 [68.13, 71.19] | 81.98 [80.72, 83.24] | 116.67 [99.61, 134.25] | 4.80 [4.11, 5.58] | 77.72 [75.78, 79.56] |
| S4G-QDual (Ours) | 83.56 [81.96, 85.09] | 96.59 [95.90, 97.23] | 74.26 [72.75, 75.73] | 85.68 [84.51, 86.85] | 67.28 [52.51, 83.46] | 2.68 [2.08, 3.31] | 82.31 [80.37, 83.99] |


#### NonSnowMean5

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 80.01 [78.24, 81.82] | 94.04 [92.96, 95.03] | 70.56 [68.99, 72.17] | 82.44 [81.03, 83.95] | 108.84 [88.94, 131.03] | 4.31 [3.53, 5.16] | 78.01 [75.93, 80.06] |
| Base + StdDual | 79.63 [77.82, 81.43] | 93.99 [92.94, 95.02] | 70.26 [68.69, 71.90] | 82.20 [80.82, 83.69] | 115.51 [94.37, 138.43] | 4.59 [3.78, 5.47] | 77.50 [75.35, 79.58] |
| Base + ColorJitter-Dual | 80.31 [78.54, 82.12] | 94.04 [93.02, 95.05] | 70.61 [69.09, 72.25] | 82.41 [81.00, 83.88] | 103.40 [82.83, 126.71] | 4.18 [3.41, 5.08] | 78.10 [76.06, 80.08] |
| Base + AugMix-Dual | 80.92 [79.16, 82.67] | 94.56 [93.60, 95.47] | 71.42 [69.86, 73.03] | 83.28 [81.90, 84.66] | 99.02 [80.40, 118.98] | 3.95 [3.20, 4.79] | 78.98 [76.95, 80.99] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 80.21 [78.36, 82.09] | 94.13 [93.12, 95.12] | 71.19 [69.63, 72.87] | 82.58 [81.14, 84.08] | 102.49 [82.10, 124.59] | 4.20 [3.39, 5.06] | 78.39 [76.31, 80.49] |
| Base + QGIN (Ours) | 82.38 [80.67, 84.07] | 95.00 [94.02, 95.89] | 73.39 [71.82, 74.97] | 84.25 [82.83, 85.66] | 92.77 [73.35, 114.45] | 3.90 [3.14, 4.74] | 80.06 [78.02, 82.02] |
| Sample4Geo† [ICCV 2023] | 82.60 [80.91, 84.29] | 95.56 [94.71, 96.37] | 72.25 [70.68, 73.78] | 84.66 [83.39, 85.92] | 73.65 [58.78, 89.85] | 3.16 [2.52, 3.87] | 81.30 [79.32, 83.11] |
| S4G-StdDual | 82.30 [80.61, 84.05] | 95.86 [95.11, 96.58] | 72.28 [70.74, 73.80] | 84.58 [83.31, 85.88] | 70.58 [55.78, 86.40] | 3.04 [2.42, 3.75] | 80.66 [78.55, 82.50] |
| S4G-QDual (Ours) | 84.19 [82.62, 85.77] | 96.83 [96.13, 97.47] | 74.93 [73.40, 76.41] | 86.29 [85.14, 87.50] | 59.11 [44.58, 74.91] | 2.39 [1.82, 3.01] | 83.06 [81.08, 84.72] |


#### Seed 42

#### Clean

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 83.78 [81.68, 85.76] | 96.27 [95.15, 97.34] | 74.38 [72.63, 76.15] | 85.70 [84.11, 87.33] | 75.90 [50.31, 104.42] | 2.53 [1.67, 3.52] | 83.40 [80.44, 85.07] |
| Base + StdDual | 83.44 [81.34, 85.50] | 96.27 [95.15, 97.34] | 73.86 [72.13, 75.64] | 85.26 [83.65, 86.85] | 78.24 [49.96, 109.27] | 2.79 [1.84, 3.82] | 81.98 [79.28, 84.04] |
| Base + ColorJitter-Dual | 83.53 [81.47, 85.63] | 95.80 [94.68, 96.87] | 74.14 [72.44, 75.91] | 85.67 [84.14, 87.23] | 85.27 [55.04, 117.42] | 2.62 [1.76, 3.56] | 82.88 [79.92, 84.94] |
| Base + AugMix-Dual | 85.37 [83.27, 87.30] | 96.70 [95.67, 97.64] | 75.70 [74.05, 77.40] | 87.12 [85.59, 88.61] | 64.48 [40.46, 91.88] | 2.23 [1.46, 3.13] | 84.30 [81.60, 86.36] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 83.96 [81.81, 86.06] | 95.75 [94.59, 96.83] | 74.43 [72.78, 76.21] | 85.51 [83.87, 87.15] | 70.32 [45.16, 99.38] | 2.53 [1.67, 3.47] | 83.53 [80.57, 85.33] |
| Base + QGIN (Ours) | 85.33 [83.35, 87.34] | 96.57 [95.58, 97.55] | 76.79 [75.06, 78.45] | 86.77 [85.26, 88.34] | 67.12 [43.63, 93.01] | 2.83 [1.93, 3.78] | 84.04 [81.34, 86.23] |
| Sample4Geo† [ICCV 2023] | 87.30 [85.50, 89.19] | 97.17 [96.22, 98.11] | 76.49 [75.00, 78.09] | 88.20 [86.80, 89.56] | 37.89 [22.53, 55.97] | 1.67 [1.03, 2.40] | 87.00 [84.30, 88.55] |
| S4G-StdDual | 86.62 [84.68, 88.46] | 97.47 [96.61, 98.28] | 76.39 [74.82, 78.01] | 87.92 [86.55, 89.32] | 45.80 [26.49, 67.66] | 1.84 [1.12, 2.62] | 85.71 [83.14, 87.77] |
| S4G-QDual (Ours) | 86.06 [84.00, 87.95] | 97.81 [96.95, 98.58] | 77.04 [75.35, 78.63] | 88.12 [86.75, 89.44] | 48.06 [30.01, 68.92] | 1.84 [1.12, 2.62] | 85.71 [82.88, 87.39] |


#### Fog

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 73.19 [70.74, 75.72] | 92.06 [90.56, 93.56] | 64.23 [62.37, 66.21] | 77.05 [75.21, 78.92] | 134.95 [103.63, 168.23] | 4.98 [3.86, 6.18] | 65.64 [62.29, 69.11] |
| Base + StdDual | 72.16 [69.71, 74.78] | 91.85 [90.30, 93.35] | 63.40 [61.51, 65.37] | 76.58 [74.81, 78.50] | 135.16 [104.68, 166.81] | 5.19 [4.03, 6.39] | 64.74 [61.26, 68.08] |
| Base + ColorJitter-Dual | 71.86 [69.37, 74.43] | 91.25 [89.70, 92.84] | 63.17 [61.33, 65.12] | 76.05 [74.21, 78.02] | 145.33 [111.51, 181.25] | 5.19 [3.99, 6.44] | 63.96 [60.49, 67.44] |
| Base + AugMix-Dual | 73.70 [71.34, 76.23] | 92.92 [91.59, 94.25] | 64.41 [62.58, 66.35] | 77.54 [75.76, 79.41] | 117.38 [87.42, 148.40] | 4.33 [3.26, 5.49] | 66.54 [63.32, 69.88] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 71.86 [69.15, 74.43] | 91.25 [89.70, 92.88] | 63.83 [61.93, 65.90] | 76.61 [74.75, 78.62] | 130.14 [96.05, 165.68] | 4.85 [3.60, 6.05] | 64.74 [61.26, 68.34] |
| Base + QGIN (Ours) | 74.17 [71.77, 76.62] | 93.01 [91.59, 94.38] | 65.74 [63.96, 67.65] | 77.85 [76.05, 79.70] | 121.24 [91.59, 154.28] | 5.15 [4.03, 6.35] | 66.28 [62.93, 69.63] |
| Sample4Geo† [ICCV 2023] | 79.75 [77.56, 81.98] | 95.62 [94.55, 96.70] | 69.16 [67.40, 70.88] | 83.14 [81.58, 84.63] | 60.89 [40.36, 83.11] | 2.62 [1.80, 3.52] | 75.68 [72.59, 78.76] |
| S4G-StdDual | 79.28 [77.01, 81.47] | 95.15 [94.08, 96.18] | 68.89 [67.10, 70.64] | 83.07 [81.44, 84.61] | 57.70 [39.15, 78.63] | 2.36 [1.59, 3.22] | 74.65 [71.43, 77.61] |
| S4G-QDual (Ours) | 80.48 [78.25, 82.63] | 95.71 [94.64, 96.74] | 70.62 [68.84, 72.39] | 83.63 [82.06, 85.10] | 60.40 [41.25, 82.79] | 2.40 [1.67, 3.26] | 75.93 [72.72, 78.76] |


#### Snow

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 64.14 [61.52, 66.75] | 83.70 [81.72, 85.67] | 54.57 [52.51, 56.62] | 66.82 [64.64, 69.00] | 442.43 [380.83, 500.02] | 15.62 [13.69, 17.59] | 59.33 [55.73, 63.06] |
| Base + StdDual | 64.09 [61.35, 66.67] | 83.61 [81.64, 85.71] | 54.87 [52.90, 56.83] | 67.32 [65.15, 69.38] | 435.69 [376.84, 495.75] | 15.70 [13.94, 17.72] | 58.30 [54.95, 61.78] |
| Base + ColorJitter-Dual | 65.25 [62.63, 67.82] | 84.98 [83.10, 86.87] | 55.75 [53.83, 57.69] | 68.37 [66.33, 70.45] | 407.56 [352.06, 464.75] | 14.54 [12.66, 16.34] | 60.10 [56.75, 63.71] |
| Base + AugMix-Dual | 69.46 [66.92, 71.99] | 87.47 [85.76, 89.15] | 59.85 [57.89, 61.87] | 72.05 [70.00, 74.04] | 336.87 [284.07, 390.85] | 12.14 [10.42, 13.86] | 65.25 [61.90, 68.73] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 68.90 [66.41, 71.34] | 86.79 [84.86, 88.63] | 59.30 [57.44, 61.26] | 71.74 [69.79, 73.79] | 299.08 [250.39, 349.87] | 11.33 [9.65, 13.04] | 64.22 [60.88, 67.70] |
| Base + QGIN (Ours) | 77.31 [74.99, 79.62] | 92.11 [90.65, 93.56] | 68.69 [66.87, 70.66] | 79.41 [77.56, 81.32] | 172.84 [137.54, 211.21] | 6.91 [5.66, 8.24] | 74.52 [71.56, 77.35] |
| Sample4Geo† [ICCV 2023] | 64.01 [61.35, 66.58] | 84.73 [82.80, 86.62] | 55.22 [53.22, 57.12] | 67.09 [64.94, 69.10] | 414.22 [360.08, 468.01] | 15.92 [13.99, 17.76] | 59.59 [56.11, 63.06] |
| S4G-StdDual | 65.51 [62.81, 68.04] | 85.89 [84.04, 87.69] | 56.18 [54.18, 58.06] | 68.50 [66.30, 70.51] | 365.05 [312.37, 418.45] | 13.99 [12.23, 15.79] | 62.68 [59.20, 66.02] |
| S4G-QDual (Ours) | 80.05 [78.03, 82.15] | 95.11 [93.99, 96.14] | 70.27 [68.55, 71.99] | 82.21 [80.60, 83.76] | 115.39 [86.86, 146.30] | 4.42 [3.39, 5.53] | 77.86 [74.77, 80.57] |


#### Blur

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 81.64 [79.36, 83.91] | 95.50 [94.29, 96.65] | 72.91 [71.04, 74.79] | 84.39 [82.62, 86.10] | 91.09 [61.43, 121.52] | 3.26 [2.27, 4.33] | 80.18 [77.22, 82.63] |
| Base + StdDual | 82.02 [79.75, 84.21] | 95.24 [93.95, 96.48] | 72.58 [70.75, 74.43] | 84.38 [82.66, 86.09] | 87.17 [59.43, 117.79] | 3.17 [2.19, 4.20] | 80.69 [77.73, 82.88] |
| Base + ColorJitter-Dual | 82.33 [80.05, 84.60] | 95.02 [93.82, 96.18] | 72.65 [70.86, 74.46] | 84.24 [82.55, 85.93] | 86.26 [58.27, 115.48] | 3.00 [2.02, 3.99] | 81.21 [78.38, 83.53] |
| Base + AugMix-Dual | 83.61 [81.34, 85.71] | 95.80 [94.64, 96.87] | 74.41 [72.62, 76.21] | 85.91 [84.18, 87.52] | 74.73 [49.80, 101.99] | 2.70 [1.80, 3.69] | 82.63 [79.67, 84.56] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 82.15 [79.88, 84.47] | 94.38 [93.13, 95.71] | 72.64 [70.79, 74.55] | 83.90 [82.16, 85.71] | 91.74 [64.28, 121.44] | 3.69 [2.66, 4.80] | 79.92 [76.96, 82.63] |
| Base + QGIN (Ours) | 84.34 [82.20, 86.53] | 95.28 [94.12, 96.44] | 74.93 [73.11, 76.77] | 85.40 [83.70, 87.10] | 90.76 [62.53, 120.87] | 3.47 [2.45, 4.59] | 82.75 [80.05, 85.20] |
| Sample4Geo† [ICCV 2023] | 86.10 [84.08, 88.07] | 97.08 [96.18, 97.94] | 75.51 [73.90, 77.16] | 87.27 [85.81, 88.63] | 44.15 [29.01, 61.67] | 1.93 [1.24, 2.66] | 84.17 [81.60, 86.74] |
| S4G-StdDual | 86.14 [84.21, 88.16] | 97.04 [96.10, 97.94] | 75.75 [74.11, 77.40] | 87.29 [85.86, 88.72] | 39.34 [24.89, 55.96] | 1.76 [1.12, 2.49] | 84.30 [81.72, 86.87] |
| S4G-QDual (Ours) | 85.71 [83.66, 87.64] | 97.47 [96.57, 98.28] | 76.11 [74.38, 77.78] | 87.40 [85.98, 88.73] | 45.06 [29.16, 63.11] | 2.06 [1.33, 2.87] | 84.43 [81.85, 86.62] |


#### Gamma

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 82.33 [80.09, 84.39] | 95.58 [94.38, 96.70] | 73.26 [71.53, 75.10] | 84.54 [82.94, 86.20] | 103.49 [72.62, 136.99] | 3.47 [2.53, 4.50] | 80.82 [77.99, 83.14] |
| Base + StdDual | 82.41 [80.27, 84.56] | 95.50 [94.25, 96.61] | 72.88 [71.16, 74.69] | 84.56 [82.96, 86.24] | 104.18 [72.37, 138.63] | 3.56 [2.53, 4.63] | 81.08 [78.12, 83.14] |
| Base + ColorJitter-Dual | 83.10 [80.95, 85.24] | 95.84 [94.72, 96.87] | 73.42 [71.75, 75.17] | 84.88 [83.31, 86.52] | 90.48 [61.07, 122.53] | 3.22 [2.27, 4.25] | 82.24 [79.28, 83.91] |
| Base + AugMix-Dual | 84.34 [82.20, 86.32] | 95.88 [94.64, 96.95] | 74.43 [72.71, 76.18] | 86.12 [84.52, 87.63] | 78.83 [52.68, 106.18] | 2.83 [1.97, 3.78] | 82.88 [80.05, 85.07] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 82.93 [80.78, 85.07] | 95.75 [94.59, 96.87] | 73.81 [72.16, 75.62] | 84.91 [83.27, 86.62] | 72.14 [48.58, 98.23] | 2.83 [1.93, 3.78] | 82.37 [79.41, 84.30] |
| Base + QGIN (Ours) | 85.37 [83.35, 87.26] | 96.40 [95.41, 97.38] | 76.33 [74.57, 78.01] | 86.53 [85.06, 88.08] | 67.16 [44.45, 91.79] | 3.13 [2.14, 4.16] | 84.30 [81.72, 86.36] |
| Sample4Geo† [ICCV 2023] | 86.83 [84.73, 88.72] | 97.25 [96.31, 98.11] | 75.96 [74.40, 77.58] | 87.62 [86.18, 88.96] | 55.36 [37.03, 77.03] | 2.32 [1.59, 3.13] | 86.36 [83.66, 88.03] |
| S4G-StdDual | 86.27 [84.30, 88.16] | 97.51 [96.65, 98.28] | 75.91 [74.27, 77.56] | 87.60 [86.23, 88.98] | 58.24 [37.27, 82.47] | 2.40 [1.59, 3.30] | 85.07 [82.50, 87.26] |
| S4G-QDual (Ours) | 85.76 [83.74, 87.69] | 97.68 [96.83, 98.46] | 76.64 [74.99, 78.23] | 87.82 [86.43, 89.16] | 51.03 [32.00, 72.17] | 1.93 [1.20, 2.70] | 85.59 [82.75, 87.13] |


#### ExposureClip

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 76.10 [73.83, 78.38] | 91.21 [89.66, 92.66] | 66.55 [64.79, 68.41] | 78.63 [76.81, 80.38] | 188.91 [153.03, 228.92] | 7.34 [6.09, 8.71] | 75.42 [72.33, 77.48] |
| Base + StdDual | 75.98 [73.57, 78.16] | 91.51 [89.92, 92.92] | 66.02 [64.26, 67.84] | 78.23 [76.43, 80.01] | 194.66 [156.34, 233.47] | 7.59 [6.26, 9.01] | 74.65 [71.43, 76.97] |
| Base + ColorJitter-Dual | 78.08 [75.80, 80.27] | 92.45 [91.03, 93.82] | 68.14 [66.42, 69.99] | 80.27 [78.54, 81.95] | 157.56 [122.59, 196.99] | 6.44 [5.23, 7.76] | 76.71 [73.75, 79.15] |
| Base + AugMix-Dual | 78.04 [75.85, 80.18] | 92.66 [91.25, 93.99] | 68.49 [66.70, 70.32] | 80.38 [78.62, 82.10] | 163.66 [129.79, 201.49] | 6.65 [5.45, 8.07] | 77.61 [74.26, 79.41] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 77.91 [75.68, 80.09] | 92.45 [90.99, 93.82] | 67.76 [66.02, 69.57] | 80.00 [78.32, 81.70] | 152.87 [121.37, 187.38] | 5.96 [4.80, 7.21] | 76.32 [73.23, 78.89] |
| Base + QGIN (Ours) | 80.87 [78.76, 82.97] | 93.87 [92.58, 95.15] | 71.86 [70.03, 73.66] | 82.87 [81.13, 84.52] | 129.73 [101.19, 161.54] | 5.66 [4.55, 6.86] | 79.54 [76.83, 82.11] |
| Sample4Geo† [ICCV 2023] | 77.78 [75.59, 79.97] | 93.18 [91.85, 94.42] | 67.29 [65.55, 69.09] | 79.74 [78.01, 81.37] | 172.35 [137.30, 209.57] | 7.29 [5.92, 8.67] | 77.35 [74.13, 79.15] |
| S4G-StdDual | 78.46 [76.19, 80.74] | 94.17 [93.01, 95.28] | 68.32 [66.55, 70.14] | 80.74 [79.08, 82.40] | 160.32 [126.12, 195.19] | 6.48 [5.23, 7.81] | 77.61 [74.39, 79.92] |
| S4G-QDual (Ours) | 81.77 [79.62, 83.74] | 95.62 [94.59, 96.65] | 71.79 [70.10, 73.50] | 83.75 [82.20, 85.29] | 112.36 [84.11, 143.32] | 4.29 [3.26, 5.32] | 80.82 [77.86, 83.01] |


#### Posterize4

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 83.48 [81.30, 85.54] | 95.92 [94.72, 97.04] | 74.28 [72.51, 76.04] | 85.60 [84.02, 87.21] | 81.63 [54.45, 111.09] | 2.70 [1.84, 3.69] | 82.88 [79.92, 84.81] |
| Base + StdDual | 83.48 [81.34, 85.59] | 96.22 [95.07, 97.30] | 73.86 [72.15, 75.61] | 85.37 [83.75, 86.98] | 75.70 [48.57, 106.83] | 2.70 [1.80, 3.69] | 82.37 [79.54, 84.30] |
| Base + ColorJitter-Dual | 83.53 [81.42, 85.67] | 95.80 [94.68, 96.87] | 74.06 [72.38, 75.82] | 85.41 [83.89, 86.99] | 81.46 [52.45, 113.33] | 2.70 [1.80, 3.69] | 82.37 [79.66, 84.68] |
| Base + AugMix-Dual | 85.20 [83.05, 87.09] | 96.53 [95.45, 97.47] | 75.71 [74.05, 77.38] | 87.05 [85.49, 88.50] | 64.78 [41.82, 91.28] | 2.32 [1.54, 3.22] | 83.78 [81.08, 86.10] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 84.08 [81.98, 86.14] | 95.97 [94.85, 97.08] | 74.46 [72.78, 76.26] | 85.45 [83.82, 87.09] | 66.06 [41.26, 94.28] | 2.53 [1.67, 3.43] | 83.53 [80.57, 85.46] |
| Base + QGIN (Ours) | 85.11 [83.01, 87.13] | 96.74 [95.75, 97.68] | 76.73 [74.98, 78.40] | 86.73 [85.22, 88.26] | 71.10 [46.53, 97.88] | 2.87 [1.97, 3.82] | 82.88 [80.18, 85.46] |
| Sample4Geo† [ICCV 2023] | 87.47 [85.58, 89.36] | 97.30 [96.35, 98.20] | 76.42 [74.90, 78.04] | 88.07 [86.70, 89.42] | 40.39 [24.14, 58.85] | 1.59 [0.94, 2.27] | 86.49 [83.91, 88.55] |
| S4G-StdDual | 86.57 [84.68, 88.46] | 97.51 [96.65, 98.33] | 76.36 [74.80, 78.00] | 87.88 [86.51, 89.28] | 41.05 [24.63, 59.65] | 1.72 [1.07, 2.45] | 85.97 [83.27, 87.90] |
| S4G-QDual (Ours) | 86.19 [84.25, 88.07] | 97.94 [97.13, 98.67] | 77.07 [75.44, 78.66] | 88.23 [86.83, 89.54] | 40.92 [23.92, 61.95] | 1.54 [0.86, 2.32] | 85.84 [83.14, 87.39] |


#### CorrMean6

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 76.81 [74.85, 78.72] | 92.33 [91.21, 93.44] | 67.63 [65.98, 69.37] | 79.50 [77.98, 81.04] | 173.75 [146.88, 202.79] | 6.23 [5.32, 7.21] | 74.30 [72.05, 76.56] |
| Base + StdDual | 76.69 [74.71, 78.59] | 92.32 [91.23, 93.44] | 67.27 [65.61, 69.00] | 79.41 [77.86, 80.99] | 172.09 [145.46, 201.49] | 6.32 [5.40, 7.31] | 73.81 [71.54, 76.08] |
| Base + ColorJitter-Dual | 77.36 [75.42, 79.26] | 92.56 [91.48, 93.69] | 67.86 [66.26, 69.58] | 79.87 [78.38, 81.42] | 161.44 [134.31, 191.57] | 5.85 [4.94, 6.82] | 74.62 [72.31, 76.77] |
| Base + AugMix-Dual | 79.06 [77.16, 80.87] | 93.54 [92.48, 94.57] | 69.55 [67.91, 71.25] | 81.51 [80.02, 83.00] | 139.38 [115.05, 165.20] | 5.16 [4.30, 6.08] | 76.45 [74.22, 78.70] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 77.97 [76.06, 79.92] | 92.76 [91.66, 93.91] | 68.63 [66.99, 70.39] | 80.43 [78.92, 82.05] | 135.34 [109.63, 163.04] | 5.20 [4.28, 6.18] | 75.61 [73.40, 77.86] |
| Base + QGIN (Ours) | 81.20 [79.30, 83.04] | 94.57 [93.57, 95.56] | 72.38 [70.69, 74.05] | 83.13 [81.64, 84.66] | 108.81 [85.27, 133.53] | 4.53 [3.62, 5.48] | 78.68 [76.53, 80.89] |
| Sample4Geo† [ICCV 2023] | 80.32 [78.60, 82.00] | 94.19 [93.29, 95.05] | 69.93 [68.39, 71.46] | 82.16 [80.84, 83.44] | 131.23 [112.27, 152.12] | 5.28 [4.54, 6.07] | 79.13 [77.05, 81.06] |
| S4G-StdDual | 80.37 [78.60, 82.09] | 94.54 [93.69, 95.37] | 70.24 [68.67, 71.81] | 82.51 [81.15, 83.86] | 120.28 [100.16, 141.56] | 4.78 [4.00, 5.58] | 79.34 [77.24, 81.19] |
| S4G-QDual (Ours) | 83.33 [81.57, 84.97] | 96.59 [95.84, 97.30] | 73.75 [72.13, 75.34] | 85.51 [84.21, 86.76] | 70.86 [53.78, 90.64] | 2.77 [2.12, 3.47] | 82.09 [79.88, 83.98] |


#### NonSnowMean5

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 79.35 [77.35, 81.29] | 94.05 [92.93, 95.12] | 70.25 [68.57, 72.05] | 82.04 [80.50, 83.61] | 120.01 [94.61, 147.77] | 4.35 [3.49, 5.30] | 77.30 [74.95, 79.64] |
| Base + StdDual | 79.21 [77.15, 81.14] | 94.06 [92.96, 95.16] | 69.75 [68.06, 71.51] | 81.83 [80.34, 83.44] | 119.37 [94.36, 147.79] | 4.44 [3.55, 5.41] | 76.91 [74.47, 79.25] |
| Base + ColorJitter-Dual | 79.78 [77.82, 81.76] | 94.07 [93.00, 95.14] | 70.29 [68.64, 72.01] | 82.17 [80.67, 83.75] | 112.22 [86.12, 140.55] | 4.11 [3.24, 5.08] | 77.53 [75.16, 79.79] |
| Base + AugMix-Dual | 80.98 [79.03, 82.78] | 94.76 [93.74, 95.72] | 71.49 [69.82, 73.19] | 83.40 [81.89, 84.85] | 99.88 [78.47, 124.28] | 3.77 [2.97, 4.64] | 78.69 [76.32, 80.90] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 79.79 [77.81, 81.78] | 93.96 [92.89, 95.09] | 70.50 [68.84, 72.29] | 82.17 [80.61, 83.80] | 102.59 [78.86, 128.41] | 3.97 [3.07, 4.92] | 77.89 [75.60, 80.21] |
| Base + QGIN (Ours) | 81.97 [79.98, 83.83] | 95.06 [94.09, 96.04] | 73.12 [71.43, 74.80] | 83.87 [82.34, 85.42] | 96.00 [72.79, 120.45] | 4.06 [3.15, 5.00] | 79.51 [77.30, 81.78] |
| Sample4Geo† [ICCV 2023] | 83.59 [81.80, 85.30] | 96.09 [95.24, 96.92] | 72.87 [71.32, 74.43] | 85.17 [83.85, 86.46] | 74.63 [57.80, 93.81] | 3.15 [2.48, 3.87] | 83.04 [80.72, 84.76] |
| S4G-StdDual | 83.35 [81.57, 85.07] | 96.28 [95.49, 97.05] | 73.05 [71.47, 74.63] | 85.31 [83.97, 86.63] | 71.33 [53.50, 90.54] | 2.94 [2.27, 3.70] | 82.68 [80.44, 84.50] |
| S4G-QDual (Ours) | 83.98 [82.16, 85.69] | 96.89 [96.13, 97.62] | 74.45 [72.79, 76.01] | 86.17 [84.85, 87.44] | 61.95 [44.97, 81.80] | 2.45 [1.79, 3.14] | 82.93 [80.69, 84.81] |


#### Seed 43

#### Clean

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 85.29 [83.27, 87.30] | 96.10 [94.89, 97.21] | 75.53 [73.89, 77.26] | 86.64 [85.17, 88.18] | 60.34 [38.12, 87.04] | 2.45 [1.63, 3.39] | 84.68 [81.98, 86.62] |
| Base + StdDual | 84.38 [82.24, 86.57] | 95.88 [94.68, 97.04] | 75.26 [73.55, 76.97] | 86.16 [84.55, 87.79] | 63.96 [41.22, 90.46] | 2.62 [1.80, 3.56] | 84.17 [81.21, 86.10] |
| Base + ColorJitter-Dual | 85.03 [82.88, 87.17] | 95.92 [94.81, 97.08] | 75.23 [73.59, 76.92] | 86.30 [84.78, 87.84] | 52.20 [33.28, 74.65] | 2.36 [1.59, 3.26] | 84.94 [81.98, 86.49] |
| Base + AugMix-Dual | 85.24 [83.23, 87.26] | 96.05 [94.94, 97.08] | 75.55 [73.89, 77.31] | 86.58 [85.06, 88.08] | 58.62 [39.31, 81.04] | 2.49 [1.67, 3.39] | 84.94 [82.11, 86.62] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 84.94 [82.88, 87.04] | 95.92 [94.81, 97.08] | 75.95 [74.27, 77.69] | 86.53 [84.92, 88.11] | 66.83 [45.52, 92.24] | 2.70 [1.80, 3.69] | 83.78 [80.95, 85.84] |
| Base + QGIN (Ours) | 86.70 [84.68, 88.59] | 96.35 [95.28, 97.34] | 77.59 [76.04, 79.23] | 87.83 [86.30, 89.30] | 61.66 [40.89, 87.51] | 2.45 [1.67, 3.35] | 85.07 [82.50, 87.39] |
| Sample4Geo† [ICCV 2023] | 85.37 [83.40, 87.43] | 96.91 [95.88, 97.85] | 75.95 [74.28, 77.63] | 87.73 [86.28, 89.18] | 39.74 [24.93, 56.51] | 1.80 [1.16, 2.53] | 83.78 [81.21, 86.23] |
| S4G-StdDual | 84.64 [82.54, 86.79] | 97.47 [96.57, 98.28] | 75.48 [73.84, 77.17] | 87.09 [85.64, 88.53] | 31.60 [20.27, 43.77] | 1.59 [0.99, 2.23] | 82.37 [79.67, 84.94] |
| S4G-QDual (Ours) | 86.53 [84.60, 88.37] | 97.98 [97.25, 98.71] | 78.35 [76.82, 79.97] | 88.47 [87.17, 89.80] | 36.90 [21.24, 54.50] | 1.59 [0.99, 2.27] | 85.46 [82.88, 87.39] |


#### Fog

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 72.80 [70.31, 75.33] | 91.59 [90.00, 93.09] | 62.85 [61.01, 64.68] | 76.77 [74.94, 78.60] | 129.54 [98.63, 161.71] | 5.45 [4.29, 6.69] | 64.86 [61.52, 68.34] |
| Base + StdDual | 72.33 [69.80, 74.78] | 91.59 [90.05, 93.14] | 62.81 [60.99, 64.69] | 76.20 [74.34, 78.08] | 146.69 [112.60, 182.79] | 6.26 [4.93, 7.64] | 64.74 [61.52, 68.21] |
| Base + ColorJitter-Dual | 71.51 [68.94, 74.13] | 91.46 [89.96, 92.97] | 61.67 [59.88, 63.58] | 75.08 [73.23, 76.99] | 134.77 [102.46, 168.80] | 5.83 [4.55, 7.21] | 62.16 [58.82, 65.51] |
| Base + AugMix-Dual | 72.59 [70.06, 75.12] | 91.93 [90.39, 93.39] | 63.58 [61.78, 65.50] | 76.97 [75.13, 78.83] | 127.07 [94.75, 162.64] | 5.28 [4.03, 6.56] | 65.77 [62.42, 69.11] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 72.11 [69.67, 74.65] | 92.54 [90.99, 93.99] | 64.59 [62.72, 66.49] | 76.68 [74.84, 78.55] | 132.02 [99.60, 167.48] | 5.75 [4.50, 7.08] | 65.64 [62.29, 69.11] |
| Base + QGIN (Ours) | 74.65 [72.29, 77.09] | 92.54 [90.99, 93.95] | 65.68 [64.00, 67.55] | 78.17 [76.40, 79.99] | 117.06 [86.91, 150.92] | 4.89 [3.77, 6.09] | 67.70 [64.35, 71.04] |
| Sample4Geo† [ICCV 2023] | 75.76 [73.36, 78.16] | 93.22 [91.89, 94.51] | 65.67 [63.74, 67.60] | 79.86 [78.18, 81.63] | 77.08 [53.43, 104.20] | 3.22 [2.32, 4.16] | 69.24 [65.89, 72.59] |
| S4G-StdDual | 75.20 [72.72, 77.73] | 93.52 [92.19, 94.81] | 65.44 [63.60, 67.30] | 79.56 [77.89, 81.29] | 68.07 [46.55, 92.43] | 2.92 [2.06, 3.95] | 67.31 [63.96, 70.66] |
| S4G-QDual (Ours) | 80.18 [78.04, 82.54] | 95.02 [93.91, 96.14] | 70.34 [68.55, 72.09] | 83.12 [81.54, 84.78] | 61.24 [42.31, 82.04] | 2.70 [1.89, 3.56] | 74.39 [71.30, 77.35] |


#### Snow

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 67.91 [65.38, 70.36] | 85.41 [83.53, 87.30] | 57.35 [55.43, 59.37] | 69.82 [67.81, 71.83] | 331.25 [285.76, 378.86] | 13.34 [11.63, 15.10] | 59.97 [56.50, 63.45] |
| Base + StdDual | 67.61 [64.99, 70.18] | 85.50 [83.61, 87.35] | 58.12 [56.19, 60.09] | 70.33 [68.22, 72.47] | 338.81 [294.21, 387.04] | 13.64 [11.93, 15.45] | 59.20 [55.60, 62.55] |
| Base + ColorJitter-Dual | 68.17 [65.64, 70.61] | 86.49 [84.64, 88.37] | 58.76 [56.85, 60.68] | 70.62 [68.52, 72.64] | 322.68 [278.33, 369.98] | 13.00 [11.37, 14.71] | 60.75 [57.27, 64.22] |
| Base + AugMix-Dual | 71.86 [69.46, 74.35] | 89.27 [87.60, 90.82] | 62.55 [60.68, 64.44] | 74.62 [72.70, 76.55] | 248.32 [208.58, 290.05] | 10.00 [8.49, 11.54] | 65.89 [62.42, 69.37] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 71.56 [69.07, 74.13] | 88.29 [86.66, 89.96] | 62.27 [60.41, 64.28] | 74.24 [72.30, 76.25] | 261.32 [219.21, 301.43] | 10.77 [9.22, 12.23] | 65.12 [61.65, 68.47] |
| Base + QGIN (Ours) | 78.46 [76.19, 80.78] | 93.65 [92.36, 94.89] | 69.78 [68.07, 71.65] | 80.57 [78.76, 82.34] | 157.31 [122.41, 196.06] | 5.83 [4.68, 7.04] | 74.26 [71.30, 77.22] |
| Sample4Geo† [ICCV 2023] | 65.38 [62.85, 67.87] | 85.59 [83.78, 87.30] | 56.54 [54.64, 58.51] | 68.70 [66.65, 70.73] | 345.84 [299.09, 393.31] | 14.20 [12.53, 16.00] | 60.36 [56.88, 63.71] |
| S4G-StdDual | 66.62 [64.18, 69.03] | 86.19 [84.47, 87.86] | 56.98 [55.10, 58.91] | 69.45 [67.50, 71.35] | 329.16 [284.51, 377.06] | 13.30 [11.67, 15.06] | 63.45 [59.97, 66.54] |
| S4G-QDual (Ours) | 80.74 [78.64, 82.76] | 95.62 [94.59, 96.61] | 71.54 [69.87, 73.24] | 83.07 [81.55, 84.66] | 100.82 [76.63, 127.28] | 3.82 [2.83, 4.85] | 79.28 [76.32, 81.72] |


#### Blur

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 83.53 [81.47, 85.67] | 95.20 [93.91, 96.40] | 74.14 [72.42, 75.93] | 85.56 [83.99, 87.17] | 79.38 [54.57, 107.01] | 3.26 [2.32, 4.29] | 82.75 [79.92, 84.68] |
| Base + StdDual | 82.93 [80.69, 85.11] | 94.98 [93.69, 96.18] | 73.93 [72.20, 75.72] | 85.44 [83.81, 87.05] | 89.34 [63.42, 118.62] | 3.65 [2.70, 4.68] | 81.21 [78.38, 83.66] |
| Base + ColorJitter-Dual | 83.91 [81.81, 86.01] | 94.51 [93.22, 95.80] | 74.01 [72.29, 75.77] | 85.32 [83.72, 86.96] | 78.36 [53.52, 106.29] | 3.52 [2.53, 4.59] | 82.50 [79.79, 84.81] |
| Base + AugMix-Dual | 83.66 [81.55, 85.76] | 95.54 [94.29, 96.70] | 74.29 [72.59, 76.12] | 85.85 [84.22, 87.47] | 74.15 [51.56, 97.99] | 3.26 [2.32, 4.29] | 83.01 [80.18, 85.07] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 83.40 [81.30, 85.59] | 94.64 [93.39, 95.88] | 74.13 [72.37, 75.98] | 84.99 [83.38, 86.66] | 88.94 [65.03, 115.88] | 3.99 [2.96, 5.11] | 81.21 [78.25, 83.91] |
| Base + QGIN (Ours) | 85.59 [83.53, 87.60] | 95.54 [94.38, 96.70] | 75.76 [74.10, 77.45] | 86.60 [84.97, 88.16] | 68.14 [46.42, 94.53] | 3.09 [2.19, 4.12] | 83.40 [80.69, 85.97] |
| Sample4Geo† [ICCV 2023] | 85.59 [83.57, 87.52] | 96.95 [95.97, 97.85] | 75.59 [73.94, 77.26] | 87.55 [86.12, 88.98] | 43.50 [27.29, 63.31] | 1.80 [1.16, 2.53] | 84.56 [81.98, 86.74] |
| S4G-StdDual | 85.16 [83.18, 87.17] | 97.43 [96.48, 98.24] | 75.34 [73.68, 77.00] | 87.21 [85.80, 88.61] | 37.68 [24.27, 53.09] | 1.76 [1.12, 2.53] | 83.91 [81.21, 86.23] |
| S4G-QDual (Ours) | 86.79 [84.94, 88.59] | 97.47 [96.61, 98.28] | 77.66 [76.07, 79.25] | 88.28 [86.96, 89.62] | 44.75 [26.54, 67.58] | 1.67 [1.03, 2.40] | 83.14 [80.44, 85.84] |


#### Gamma

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 85.07 [83.01, 87.05] | 95.75 [94.51, 96.91] | 74.90 [73.23, 76.64] | 86.32 [84.82, 87.89] | 60.97 [40.41, 85.36] | 2.96 [2.02, 3.95] | 84.56 [81.85, 86.49] |
| Base + StdDual | 84.00 [81.85, 86.10] | 95.58 [94.34, 96.78] | 74.59 [72.89, 76.29] | 85.99 [84.41, 87.63] | 73.68 [49.29, 101.70] | 3.30 [2.36, 4.38] | 83.27 [80.44, 85.20] |
| Base + ColorJitter-Dual | 84.51 [82.41, 86.66] | 95.50 [94.34, 96.65] | 74.72 [73.03, 76.41] | 85.85 [84.31, 87.42] | 60.84 [39.08, 85.24] | 2.92 [2.02, 3.95] | 83.66 [80.82, 85.84] |
| Base + AugMix-Dual | 84.86 [82.75, 86.92] | 95.45 [94.25, 96.65] | 74.86 [73.16, 76.58] | 86.14 [84.58, 87.67] | 74.44 [51.13, 100.96] | 3.09 [2.15, 4.16] | 84.56 [81.60, 86.23] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 84.68 [82.63, 86.66] | 95.75 [94.55, 96.91] | 75.68 [73.98, 77.43] | 86.27 [84.71, 87.87] | 73.18 [52.28, 98.60] | 3.00 [2.15, 3.99] | 83.78 [80.82, 85.71] |
| Base + QGIN (Ours) | 86.19 [84.30, 88.16] | 96.18 [95.02, 97.25] | 77.04 [75.43, 78.71] | 87.39 [85.83, 88.92] | 71.91 [48.62, 97.75] | 2.96 [2.15, 3.95] | 85.33 [82.75, 87.39] |
| Sample4Geo† [ICCV 2023] | 84.81 [82.75, 86.92] | 96.87 [95.92, 97.77] | 74.84 [73.17, 76.55] | 86.91 [85.41, 88.37] | 39.40 [23.03, 58.96] | 1.76 [1.07, 2.53] | 83.40 [80.82, 85.84] |
| S4G-StdDual | 84.68 [82.71, 86.74] | 97.51 [96.70, 98.28] | 74.87 [73.28, 76.55] | 86.75 [85.28, 88.20] | 46.30 [28.72, 66.89] | 2.06 [1.33, 2.87] | 83.40 [80.69, 85.71] |
| S4G-QDual (Ours) | 86.44 [84.60, 88.29] | 97.90 [97.13, 98.63] | 77.99 [76.47, 79.62] | 88.35 [87.04, 89.69] | 38.37 [23.92, 54.22] | 1.59 [0.99, 2.23] | 85.84 [83.14, 87.52] |


#### ExposureClip

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 76.58 [74.30, 78.94] | 91.63 [90.13, 93.09] | 66.99 [65.23, 68.84] | 78.87 [77.07, 80.64] | 158.30 [129.89, 191.81] | 7.34 [6.05, 8.75] | 74.90 [71.81, 77.86] |
| Base + StdDual | 76.92 [74.65, 79.19] | 91.42 [89.88, 92.92] | 67.27 [65.48, 69.15] | 79.04 [77.19, 80.85] | 182.41 [148.56, 219.33] | 7.68 [6.35, 9.05] | 75.16 [72.20, 77.86] |
| Base + ColorJitter-Dual | 78.94 [76.58, 81.12] | 92.41 [90.99, 93.87] | 68.92 [67.12, 70.84] | 80.63 [78.85, 82.40] | 142.76 [114.06, 176.62] | 6.48 [5.28, 7.81] | 77.48 [74.52, 79.92] |
| Base + AugMix-Dual | 78.04 [75.85, 80.14] | 92.88 [91.51, 94.21] | 68.39 [66.64, 70.25] | 80.10 [78.31, 81.87] | 154.54 [124.34, 187.80] | 6.61 [5.32, 7.94] | 77.22 [74.26, 79.28] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 78.12 [75.80, 80.40] | 92.45 [91.12, 93.74] | 69.02 [67.21, 70.93] | 80.36 [78.54, 82.19] | 150.37 [118.94, 185.52] | 6.65 [5.40, 8.02] | 76.83 [73.87, 79.28] |
| Base + QGIN (Ours) | 81.17 [79.02, 83.31] | 94.12 [92.84, 95.37] | 72.22 [70.52, 74.00] | 83.10 [81.42, 84.79] | 129.27 [101.45, 160.17] | 5.41 [4.33, 6.61] | 78.64 [75.68, 81.34] |
| Sample4Geo† [ICCV 2023] | 75.89 [73.62, 78.38] | 91.16 [89.70, 92.66] | 66.12 [64.26, 68.05] | 78.62 [76.78, 80.58] | 170.18 [135.72, 205.69] | 7.42 [6.01, 8.79] | 75.29 [72.07, 77.48] |
| S4G-StdDual | 76.32 [74.00, 78.77] | 91.29 [89.75, 92.84] | 66.54 [64.68, 68.46] | 78.70 [76.92, 80.56] | 164.13 [130.43, 199.09] | 7.29 [5.92, 8.71] | 74.26 [71.17, 77.22] |
| S4G-QDual (Ours) | 81.94 [79.88, 84.00] | 95.67 [94.59, 96.70] | 72.80 [71.17, 74.57] | 83.84 [82.27, 85.42] | 97.13 [71.34, 123.28] | 4.03 [3.09, 5.02] | 81.60 [78.64, 83.27] |


#### Posterize4

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 85.37 [83.31, 87.34] | 95.92 [94.77, 97.08] | 75.46 [73.85, 77.16] | 86.71 [85.24, 88.25] | 60.10 [37.77, 85.70] | 2.32 [1.50, 3.22] | 84.43 [81.85, 86.62] |
| Base + StdDual | 84.08 [81.90, 86.23] | 95.97 [94.77, 97.08] | 75.22 [73.54, 76.94] | 86.23 [84.65, 87.83] | 66.11 [42.36, 93.25] | 2.83 [1.97, 3.78] | 82.88 [80.18, 85.46] |
| Base + ColorJitter-Dual | 85.37 [83.35, 87.39] | 96.14 [95.02, 97.25] | 75.40 [73.73, 77.09] | 86.39 [84.89, 87.93] | 56.19 [35.93, 79.73] | 2.53 [1.72, 3.39] | 84.94 [82.24, 86.87] |
| Base + AugMix-Dual | 85.16 [83.14, 87.22] | 96.05 [94.94, 97.13] | 75.62 [73.98, 77.35] | 86.75 [85.23, 88.23] | 60.59 [40.06, 84.71] | 2.45 [1.63, 3.35] | 84.43 [81.72, 86.36] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 84.81 [82.71, 86.87] | 96.10 [94.98, 97.21] | 75.96 [74.29, 77.67] | 86.60 [85.00, 88.15] | 67.46 [45.99, 92.05] | 2.75 [1.89, 3.69] | 83.53 [80.69, 85.72] |
| Base + QGIN (Ours) | 86.36 [84.34, 88.20] | 96.31 [95.24, 97.38] | 77.63 [76.03, 79.27] | 87.83 [86.25, 89.32] | 61.27 [41.07, 84.64] | 2.32 [1.59, 3.17] | 85.07 [82.50, 87.26] |
| Sample4Geo† [ICCV 2023] | 85.97 [83.87, 88.03] | 96.95 [95.97, 97.90] | 75.95 [74.28, 77.66] | 87.82 [86.38, 89.30] | 33.23 [19.88, 48.23] | 1.63 [0.99, 2.36] | 83.78 [81.21, 86.36] |
| S4G-StdDual | 84.94 [82.84, 87.13] | 97.43 [96.53, 98.24] | 75.36 [73.72, 77.07] | 86.99 [85.53, 88.43] | 32.96 [21.44, 45.45] | 1.63 [1.03, 2.27] | 82.37 [79.67, 84.94] |
| S4G-QDual (Ours) | 86.66 [84.77, 88.46] | 97.81 [97.04, 98.54] | 78.27 [76.72, 79.88] | 88.50 [87.16, 89.84] | 39.86 [23.39, 58.03] | 1.67 [1.03, 2.40] | 84.94 [82.49, 87.26] |


#### CorrMean6

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 78.54 [76.73, 80.40] | 92.59 [91.41, 93.69] | 68.61 [67.04, 70.22] | 80.68 [79.19, 82.14] | 136.59 [115.83, 159.20] | 5.78 [4.90, 6.73] | 75.59 [73.47, 77.69] |
| Base + StdDual | 77.98 [76.04, 79.87] | 92.51 [91.33, 93.68] | 68.66 [67.06, 70.30] | 80.54 [79.01, 82.06] | 149.51 [125.44, 176.98] | 6.23 [5.30, 7.20] | 74.95 [72.82, 77.11] |
| Base + ColorJitter-Dual | 78.74 [76.95, 80.58] | 92.75 [91.61, 93.89] | 68.91 [67.32, 70.56] | 80.65 [79.15, 82.12] | 132.60 [110.94, 155.55] | 5.71 [4.84, 6.66] | 75.68 [73.57, 77.78] |
| Base + AugMix-Dual | 79.36 [77.46, 81.22] | 93.52 [92.43, 94.58] | 69.88 [68.27, 71.52] | 81.74 [80.26, 83.25] | 123.19 [101.66, 147.10] | 5.11 [4.22, 6.10] | 77.05 [74.97, 79.19] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 79.11 [77.20, 81.01] | 93.29 [92.22, 94.39] | 70.27 [68.66, 71.93] | 81.52 [80.08, 83.08] | 128.88 [107.21, 152.71] | 5.48 [4.60, 6.44] | 76.60 [74.32, 78.83] |
| Base + QGIN (Ours) | 82.07 [80.23, 83.89] | 94.72 [93.69, 95.72] | 73.02 [71.50, 74.64] | 83.94 [82.49, 85.40] | 100.83 [79.85, 125.66] | 4.08 [3.30, 4.99] | 79.56 [77.37, 81.68] |
| Sample4Geo† [ICCV 2023] | 78.90 [77.10, 80.76] | 93.46 [92.53, 94.40] | 69.12 [67.55, 70.80] | 81.58 [80.21, 83.00] | 118.20 [100.38, 136.59] | 5.01 [4.23, 5.82] | 76.36 [74.22, 78.61] |
| S4G-StdDual | 78.82 [77.08, 80.71] | 93.89 [93.04, 94.76] | 69.09 [67.52, 70.75] | 81.45 [80.09, 82.85] | 113.05 [96.02, 131.08] | 4.83 [4.08, 5.61] | 76.10 [73.92, 78.27] |
| S4G-QDual (Ours) | 83.79 [82.11, 85.47] | 96.58 [95.82, 97.30] | 74.77 [73.27, 76.33] | 85.86 [84.63, 87.16] | 63.69 [48.87, 80.17] | 2.58 [1.98, 3.23] | 82.54 [80.44, 84.41] |


#### NonSnowMean5

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 80.67 [78.76, 82.54] | 94.02 [92.87, 95.14] | 70.87 [69.26, 72.52] | 82.85 [81.37, 84.32] | 97.66 [77.77, 120.25] | 4.26 [3.44, 5.17] | 78.71 [76.47, 80.98] |
| Base + StdDual | 80.05 [78.12, 81.99] | 93.91 [92.76, 95.03] | 70.76 [69.17, 72.41] | 82.58 [81.07, 84.11] | 111.65 [88.35, 137.08] | 4.74 [3.85, 5.67] | 78.10 [75.88, 80.39] |
| Base + ColorJitter-Dual | 80.85 [78.95, 82.73] | 94.00 [92.86, 95.14] | 70.94 [69.31, 72.59] | 82.65 [81.17, 84.15] | 94.58 [74.39, 117.30] | 4.26 [3.43, 5.19] | 78.66 [76.47, 80.82] |
| Base + AugMix-Dual | 80.86 [78.93, 82.75] | 94.37 [93.28, 95.44] | 71.35 [69.74, 73.05] | 83.16 [81.65, 84.64] | 98.16 [77.35, 120.80] | 4.14 [3.27, 5.10] | 79.28 [77.12, 81.44] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 80.63 [78.71, 82.51] | 94.29 [93.21, 95.39] | 71.88 [70.22, 73.58] | 82.98 [81.49, 84.50] | 102.40 [81.58, 126.04] | 4.43 [3.55, 5.40] | 78.89 [76.60, 81.18] |
| Base + QGIN (Ours) | 82.79 [80.99, 84.62] | 94.94 [93.87, 95.98] | 73.67 [72.11, 75.29] | 84.62 [83.11, 86.10] | 89.53 [69.04, 112.88] | 3.73 [2.94, 4.64] | 80.62 [78.40, 82.78] |
| Sample4Geo† [ICCV 2023] | 81.60 [79.77, 83.51] | 95.03 [94.08, 95.96] | 71.63 [70.03, 73.30] | 84.15 [82.75, 85.56] | 72.68 [56.85, 89.68] | 3.17 [2.49, 3.91] | 79.56 [77.27, 81.90] |
| S4G-StdDual | 81.26 [79.39, 83.17] | 95.44 [94.54, 96.29] | 71.51 [69.94, 73.18] | 83.84 [82.47, 85.28] | 69.83 [54.93, 86.11] | 3.13 [2.46, 3.89] | 78.64 [76.37, 80.93] |
| S4G-QDual (Ours) | 84.40 [82.68, 86.14] | 96.77 [96.01, 97.49] | 75.41 [73.88, 76.97] | 86.42 [85.18, 87.75] | 56.27 [41.58, 71.95] | 2.33 [1.74, 2.99] | 83.19 [81.03, 85.07] |


### SUES → SUES

#### Two-seed mean

#### Clean

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 89.52 [84.92, 93.23] | 97.96 [96.02, 99.40] | 93.22 [89.92, 95.82] | — | — | — | 83.62 [77.84, 88.70] |
| Base + StdDual | 91.83 [87.83, 94.91] | 98.12 [95.61, 99.65] | 94.66 [91.55, 96.94] | — | — | — | 84.61 [78.97, 89.51] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.69 [87.46, 94.92] | 98.72 [97.19, 99.73] | 94.73 [91.78, 96.92] | — | — | — | 85.78 [80.09, 90.48] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 91.87 [88.01, 94.92] | 97.91 [95.50, 99.42] | 94.62 [91.63, 96.89] | — | — | — | 86.11 [80.79, 90.66] |
| Base + QGIN (Ours) | 94.14 [90.74, 96.69] | 99.12 [98.03, 99.79] | 96.43 [94.13, 98.09] | — | — | — | 89.36 [84.72, 93.16] |
| Sample4Geo† [ICCV 2023] | 95.12 [91.88, 97.62] | 99.40 [98.43, 99.99] | 97.03 [94.84, 98.63] | — | — | — | 92.01 [87.84, 95.30] |
| S4G-StdDual | 95.13 [91.88, 97.60] | 99.46 [98.53, 99.98] | 97.06 [94.90, 98.63] | — | — | — | 92.14 [88.02, 95.40] |
| S4G-QDual (Ours) | 96.29 [93.97, 98.08] | 99.63 [99.09, 99.95] | 97.82 [96.36, 98.93] | — | — | — | 93.14 [89.79, 95.95] |


#### Fog

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 88.16 [83.35, 92.08] | 97.69 [95.84, 99.02] | 92.38 [88.99, 95.04] | — | — | — | 80.75 [74.81, 85.89] |
| Base + StdDual | 89.96 [85.68, 93.32] | 97.81 [95.23, 99.46] | 93.53 [90.26, 95.96] | — | — | — | 81.88 [75.80, 87.15] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 90.49 [86.29, 93.67] | 98.51 [97.23, 99.45] | 94.01 [91.26, 96.11] | — | — | — | 84.33 [78.87, 88.81] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 90.49 [86.60, 93.63] | 97.69 [95.48, 99.23] | 93.74 [90.71, 96.03] | — | — | — | 83.66 [77.76, 88.64] |
| Base + QGIN (Ours) | 93.51 [90.26, 95.95] | 99.06 [98.09, 99.70] | 96.03 [93.83, 97.61] | — | — | — | 87.91 [83.30, 91.83] |
| Sample4Geo† [ICCV 2023] | 93.78 [90.09, 96.66] | 99.17 [97.87, 99.94] | 96.20 [93.69, 98.06] | — | — | — | 90.10 [85.56, 93.75] |
| S4G-StdDual | 93.71 [90.03, 96.63] | 99.19 [97.92, 99.93] | 96.13 [93.59, 98.03] | — | — | — | 89.71 [84.97, 93.55] |
| S4G-QDual (Ours) | 95.73 [93.03, 97.78] | 99.53 [98.79, 99.93] | 97.46 [95.70, 98.72] | — | — | — | 92.03 [88.21, 95.11] |


#### Snow

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 64.62 [57.33, 71.53] | 86.18 [80.33, 91.17] | 74.37 [68.25, 79.95] | — | — | — | 60.61 [52.54, 68.08] |
| Base + StdDual | 70.40 [63.38, 76.91] | 89.04 [83.34, 93.60] | 78.81 [72.90, 84.09] | — | — | — | 66.05 [58.61, 72.94] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 73.27 [66.33, 79.47] | 90.38 [85.59, 94.39] | 81.00 [75.46, 86.02] | — | — | — | 67.56 [60.40, 74.38] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 74.05 [67.21, 80.24] | 91.24 [86.29, 95.22] | 81.81 [76.38, 86.70] | — | — | — | 70.31 [63.00, 77.01] |
| Base + QGIN (Ours) | 83.90 [78.26, 88.65] | 95.63 [92.52, 98.08] | 89.12 [84.87, 92.63] | — | — | — | 78.12 [71.12, 84.11] |
| Sample4Geo† [ICCV 2023] | 72.12 [65.17, 78.46] | 90.94 [86.03, 94.97] | 80.68 [75.08, 85.71] | — | — | — | 67.12 [59.52, 73.99] |
| S4G-StdDual | 73.62 [67.31, 79.81] | 91.87 [87.22, 95.55] | 81.90 [76.64, 86.65] | — | — | — | 68.31 [60.80, 75.06] |
| S4G-QDual (Ours) | 87.00 [82.28, 91.18] | 97.66 [95.90, 98.98] | 91.78 [88.57, 94.56] | — | — | — | 81.56 [76.15, 86.67] |


#### Blur

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 86.25 [81.82, 89.91] | 97.60 [95.46, 98.98] | 91.19 [87.99, 93.78] | — | — | — | 80.61 [74.67, 85.79] |
| Base + StdDual | 88.43 [83.95, 92.02] | 97.68 [95.38, 99.30] | 92.61 [89.40, 95.18] | — | — | — | 82.54 [76.54, 87.46] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 89.30 [85.24, 92.80] | 98.59 [97.66, 99.31] | 93.39 [90.77, 95.62] | — | — | — | 83.84 [78.36, 88.36] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 89.34 [85.78, 92.55] | 97.90 [96.20, 99.13] | 93.27 [90.67, 95.47] | — | — | — | 84.21 [78.94, 88.61] |
| Base + QGIN (Ours) | 92.11 [88.77, 95.00] | 98.88 [98.01, 99.52] | 95.11 [93.00, 96.91] | — | — | — | 87.72 [82.59, 91.75] |
| Sample4Geo† [ICCV 2023] | 92.33 [88.67, 95.27] | 99.15 [98.14, 99.79] | 95.36 [92.96, 97.26] | — | — | — | 87.54 [82.55, 91.61] |
| S4G-StdDual | 92.56 [88.98, 95.42] | 99.03 [97.90, 99.76] | 95.46 [93.01, 97.33] | — | — | — | 87.75 [82.83, 91.64] |
| S4G-QDual (Ours) | 95.48 [93.09, 97.37] | 99.51 [98.76, 99.92] | 97.31 [95.75, 98.47] | — | — | — | 92.08 [88.40, 95.04] |


#### Gamma

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 88.65 [83.90, 92.49] | 97.73 [95.76, 99.21] | 92.60 [89.12, 95.38] | — | — | — | 82.39 [76.56, 87.33] |
| Base + StdDual | 91.08 [86.92, 94.29] | 98.09 [95.55, 99.60] | 94.20 [90.98, 96.52] | — | — | — | 83.59 [78.04, 88.51] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.60 [87.38, 94.97] | 98.55 [96.87, 99.65] | 94.61 [91.63, 96.94] | — | — | — | 86.33 [81.05, 90.81] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 92.02 [88.26, 94.97] | 98.13 [95.87, 99.52] | 94.74 [91.84, 96.94] | — | — | — | 86.22 [81.11, 90.55] |
| Base + QGIN (Ours) | 94.12 [90.69, 96.66] | 99.15 [98.05, 99.81] | 96.41 [94.07, 98.06] | — | — | — | 89.28 [84.57, 93.11] |
| Sample4Geo† [ICCV 2023] | 94.50 [91.29, 97.05] | 99.52 [98.83, 99.96] | 96.68 [94.60, 98.30] | — | — | — | 90.86 [86.69, 94.41] |
| S4G-StdDual | 94.25 [90.81, 97.03] | 99.45 [98.62, 99.96] | 96.52 [94.29, 98.28] | — | — | — | 90.51 [86.15, 94.24] |
| S4G-QDual (Ours) | 95.96 [93.57, 97.79] | 99.64 [99.08, 99.95] | 97.62 [96.17, 98.74] | — | — | — | 92.79 [89.41, 95.54] |


#### ExposureClip

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 76.04 [69.32, 82.07] | 93.79 [89.70, 96.91] | 83.90 [78.61, 88.31] | — | — | — | 67.95 [60.57, 74.69] |
| Base + StdDual | 81.25 [75.18, 86.44] | 95.36 [91.56, 98.13] | 87.61 [82.75, 91.50] | — | — | — | 71.97 [64.90, 78.08] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 82.53 [76.37, 87.82] | 96.09 [92.85, 98.53] | 88.70 [84.28, 92.48] | — | — | — | 75.72 [68.94, 81.58] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 82.41 [76.92, 86.94] | 95.91 [92.35, 98.52] | 88.46 [84.09, 91.88] | — | — | — | 74.85 [68.48, 80.41] |
| Base + QGIN (Ours) | 87.78 [82.94, 91.84] | 97.42 [94.87, 99.26] | 92.21 [88.58, 95.08] | — | — | — | 81.62 [75.67, 86.75] |
| Sample4Geo† [ICCV 2023] | 85.48 [80.57, 90.07] | 98.12 [96.58, 99.23] | 91.07 [87.75, 94.02] | — | — | — | 79.92 [73.99, 85.30] |
| S4G-StdDual | 87.34 [82.64, 91.54] | 98.32 [96.78, 99.42] | 92.14 [88.89, 94.95] | — | — | — | 81.49 [75.84, 86.71] |
| S4G-QDual (Ours) | 92.09 [88.67, 94.99] | 99.17 [98.43, 99.71] | 95.25 [93.14, 97.01] | — | — | — | 87.09 [82.49, 91.24] |


#### Posterize4

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 89.04 [84.48, 92.84] | 97.74 [95.52, 99.33] | 92.88 [89.54, 95.57] | — | — | — | 83.41 [77.54, 88.54] |
| Base + StdDual | 91.51 [87.51, 94.63] | 97.87 [95.10, 99.54] | 94.38 [91.18, 96.70] | — | — | — | 84.36 [78.49, 89.35] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.41 [87.01, 94.75] | 98.65 [97.09, 99.70] | 94.53 [91.50, 96.81] | — | — | — | 85.56 [79.95, 90.41] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 91.55 [87.75, 94.61] | 97.74 [95.49, 99.26] | 94.36 [91.36, 96.65] | — | — | — | 85.65 [80.31, 90.25] |
| Base + QGIN (Ours) | 93.88 [90.36, 96.49] | 99.04 [97.91, 99.76] | 96.24 [93.85, 97.96] | — | — | — | 89.03 [84.40, 92.86] |
| Sample4Geo† [ICCV 2023] | 94.53 [91.17, 97.19] | 99.27 [98.22, 99.97] | 96.67 [94.42, 98.39] | — | — | — | 91.16 [86.88, 94.66] |
| S4G-StdDual | 94.40 [91.03, 97.13] | 99.35 [98.28, 99.96] | 96.63 [94.38, 98.35] | — | — | — | 91.35 [87.08, 94.85] |
| S4G-QDual (Ours) | 96.10 [93.85, 97.90] | 99.62 [99.10, 99.94] | 97.70 [96.24, 98.81] | — | — | — | 92.91 [89.61, 95.64] |


#### CorrMean6

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 82.13 [77.46, 86.03] | 95.12 [92.64, 97.09] | 87.89 [84.33, 90.81] | — | — | — | 75.95 [70.27, 80.89] |
| Base + StdDual | 85.44 [81.02, 88.91] | 95.97 [93.04, 98.01] | 90.19 [86.71, 92.89] | — | — | — | 78.40 [72.75, 83.19] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 86.43 [82.08, 89.84] | 96.79 [94.89, 98.28] | 91.04 [87.81, 93.53] | — | — | — | 80.56 [75.46, 84.87] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 86.64 [82.78, 89.75] | 96.44 [93.95, 98.20] | 91.06 [87.99, 93.46] | — | — | — | 80.82 [75.47, 85.51] |
| Base + QGIN (Ours) | 90.88 [87.49, 93.58] | 98.20 [96.79, 99.18] | 94.19 [91.75, 96.07] | — | — | — | 85.61 [80.92, 89.55] |
| Sample4Geo† [ICCV 2023] | 88.79 [85.23, 91.71] | 97.69 [96.20, 98.83] | 92.78 [90.25, 94.79] | — | — | — | 84.45 [79.98, 88.22] |
| S4G-StdDual | 89.31 [85.62, 92.28] | 97.87 [96.31, 98.99] | 93.13 [90.50, 95.18] | — | — | — | 84.85 [80.33, 88.71] |
| S4G-QDual (Ours) | 93.73 [91.12, 95.88] | 99.19 [98.48, 99.67] | 96.19 [94.50, 97.55] | — | — | — | 89.74 [86.18, 92.82] |


#### NonSnowMean5

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 85.63 [81.08, 89.40] | 96.91 [94.85, 98.48] | 90.59 [87.24, 93.23] | — | — | — | 79.02 [73.48, 83.84] |
| Base + StdDual | 88.45 [84.17, 91.78] | 97.36 [94.79, 99.06] | 92.46 [89.20, 94.91] | — | — | — | 80.87 [75.19, 85.69] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 89.07 [84.93, 92.34] | 98.08 [96.54, 99.21] | 93.05 [90.18, 95.34] | — | — | — | 83.16 [77.90, 87.41] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 89.16 [85.49, 92.10] | 97.47 [95.28, 98.96] | 92.92 [90.05, 95.12] | — | — | — | 82.92 [77.63, 87.31] |
| Base + QGIN (Ours) | 92.28 [88.94, 94.85] | 98.71 [97.52, 99.51] | 95.20 [92.87, 96.90] | — | — | — | 87.11 [82.49, 90.94] |
| Sample4Geo† [ICCV 2023] | 92.12 [88.78, 94.93] | 99.04 [98.01, 99.70] | 95.20 [92.91, 97.03] | — | — | — | 87.92 [83.60, 91.54] |
| S4G-StdDual | 92.45 [88.97, 95.26] | 99.07 [97.95, 99.77] | 95.38 [92.95, 97.22] | — | — | — | 88.16 [83.81, 91.79] |
| S4G-QDual (Ours) | 95.07 [92.62, 97.00] | 99.49 [98.84, 99.85] | 97.07 [95.50, 98.26] | — | — | — | 91.38 [88.02, 94.24] |


#### Seed 42

#### Clean

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 89.36 [84.90, 93.00] | 98.37 [96.34, 99.57] | 93.25 [89.94, 95.80] | — | — | — | 82.65 [76.77, 87.95] |
| Base + StdDual | 92.36 [88.61, 95.33] | 98.38 [96.11, 99.67] | 95.03 [92.14, 97.19] | — | — | — | 84.60 [79.10, 89.60] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.65 [87.51, 95.01] | 98.46 [96.22, 99.74] | 94.69 [91.56, 97.02] | — | — | — | 85.12 [79.00, 90.53] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 92.08 [88.34, 95.12] | 97.97 [95.31, 99.49] | 94.81 [91.82, 97.04] | — | — | — | 86.12 [80.50, 90.88] |
| Base + QGIN (Ours) | 94.08 [90.69, 96.77] | 99.11 [98.03, 99.78] | 96.38 [94.05, 98.12] | — | — | — | 88.88 [84.07, 93.10] |
| Sample4Geo† [ICCV 2023] | 95.47 [92.17, 97.96] | 99.33 [98.26, 99.99] | 97.22 [94.94, 98.88] | — | — | — | 92.15 [87.75, 95.58] |
| S4G-StdDual | 95.22 [91.88, 97.74] | 99.34 [98.23, 99.98] | 97.07 [94.79, 98.75] | — | — | — | 92.05 [87.70, 95.43] |
| S4G-QDual (Ours) | 95.48 [92.76, 97.62] | 99.44 [98.61, 99.92] | 97.26 [95.44, 98.64] | — | — | — | 91.83 [87.82, 95.10] |


#### Fog

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 87.67 [82.86, 91.59] | 98.22 [96.58, 99.27] | 92.24 [89.03, 94.86] | — | — | — | 79.35 [73.15, 84.65] |
| Base + StdDual | 90.88 [86.90, 94.04] | 97.96 [95.37, 99.48] | 94.09 [90.99, 96.39] | — | — | — | 82.92 [77.17, 88.20] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 90.22 [86.06, 93.65] | 98.17 [95.99, 99.56] | 93.86 [90.93, 96.20] | — | — | — | 82.85 [77.30, 87.93] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 90.83 [86.99, 93.97] | 97.91 [95.72, 99.33] | 93.98 [91.07, 96.25] | — | — | — | 83.65 [77.45, 88.72] |
| Base + QGIN (Ours) | 93.30 [90.01, 95.94] | 99.04 [98.01, 99.71] | 95.90 [93.71, 97.60] | — | — | — | 86.95 [81.82, 91.28] |
| Sample4Geo† [ICCV 2023] | 93.99 [90.30, 96.91] | 99.12 [97.77, 99.92] | 96.33 [93.87, 98.21] | — | — | — | 90.00 [85.03, 93.93] |
| S4G-StdDual | 93.76 [89.96, 96.76] | 99.03 [97.58, 99.93] | 96.15 [93.49, 98.13] | — | — | — | 89.62 [84.60, 93.78] |
| S4G-QDual (Ours) | 95.09 [92.14, 97.39] | 99.34 [98.31, 99.91] | 97.00 [94.96, 98.47] | — | — | — | 91.15 [86.77, 94.70] |


#### Snow

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 65.17 [58.09, 72.09] | 86.71 [80.92, 91.79] | 74.99 [68.96, 80.60] | — | — | — | 60.90 [52.87, 68.38] |
| Base + StdDual | 72.05 [65.16, 78.26] | 89.74 [84.05, 94.52] | 80.21 [74.44, 85.44] | — | — | — | 68.08 [60.55, 74.60] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 71.85 [65.03, 78.34] | 90.72 [85.82, 94.87] | 80.39 [75.01, 85.39] | — | — | — | 65.50 [57.87, 72.75] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 75.39 [69.05, 81.48] | 91.75 [86.87, 95.62] | 82.78 [77.55, 87.55] | — | — | — | 71.00 [63.57, 77.73] |
| Base + QGIN (Ours) | 82.61 [76.69, 87.55] | 95.42 [92.32, 97.78] | 88.23 [83.81, 91.95] | — | — | — | 76.47 [68.80, 83.15] |
| Sample4Geo† [ICCV 2023] | 69.96 [62.79, 76.79] | 90.36 [85.43, 94.54] | 79.12 [73.33, 84.39] | — | — | — | 65.97 [58.20, 73.13] |
| S4G-StdDual | 71.10 [63.87, 77.80] | 91.38 [86.83, 95.14] | 80.21 [74.68, 85.25] | — | — | — | 66.50 [58.65, 73.88] |
| S4G-QDual (Ours) | 85.81 [80.59, 90.25] | 97.17 [95.06, 98.76] | 90.89 [87.28, 93.91] | — | — | — | 79.75 [73.57, 85.35] |


#### Blur

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 85.13 [80.24, 89.38] | 97.61 [96.17, 98.77] | 90.53 [87.14, 93.44] | — | — | — | 79.55 [73.42, 84.80] |
| Base + StdDual | 89.31 [84.86, 93.07] | 97.81 [95.32, 99.36] | 93.17 [90.04, 95.71] | — | — | — | 83.83 [77.85, 88.85] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 87.12 [82.11, 91.44] | 98.12 [96.66, 99.19] | 91.98 [88.71, 94.78] | — | — | — | 81.42 [74.95, 86.95] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 90.03 [86.37, 93.18] | 98.11 [96.31, 99.28] | 93.69 [91.06, 95.88] | — | — | — | 84.88 [79.67, 89.30] |
| Base + QGIN (Ours) | 91.34 [87.38, 94.74] | 98.75 [97.64, 99.59] | 94.65 [92.06, 96.85] | — | — | — | 86.38 [80.60, 91.18] |
| Sample4Geo† [ICCV 2023] | 92.09 [88.12, 95.36] | 99.04 [97.97, 99.78] | 95.20 [92.60, 97.29] | — | — | — | 87.10 [81.65, 91.65] |
| S4G-StdDual | 92.03 [87.97, 95.29] | 98.86 [97.59, 99.76] | 95.09 [92.33, 97.20] | — | — | — | 87.12 [81.65, 91.65] |
| S4G-QDual (Ours) | 95.22 [92.64, 97.26] | 99.33 [98.34, 99.88] | 97.05 [95.18, 98.41] | — | — | — | 91.40 [87.12, 94.85] |


#### Gamma

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 88.31 [83.76, 92.10] | 98.20 [96.34, 99.47] | 92.59 [89.37, 95.22] | — | — | — | 80.97 [74.92, 86.40] |
| Base + StdDual | 91.64 [87.66, 94.68] | 98.41 [96.25, 99.62] | 94.56 [91.51, 96.76] | — | — | — | 83.90 [78.50, 88.75] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.53 [87.37, 94.93] | 98.16 [95.55, 99.66] | 94.58 [91.36, 96.99] | — | — | — | 86.10 [80.42, 90.90] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 92.32 [88.66, 95.28] | 98.23 [95.70, 99.64] | 94.97 [92.03, 97.17] | — | — | — | 86.17 [80.78, 90.75] |
| Base + QGIN (Ours) | 94.08 [90.69, 96.70] | 99.11 [97.94, 99.80] | 96.36 [93.99, 98.10] | — | — | — | 88.55 [83.60, 92.85] |
| Sample4Geo† [ICCV 2023] | 94.80 [91.67, 97.24] | 99.46 [98.54, 99.99] | 96.90 [94.88, 98.45] | — | — | — | 91.25 [86.72, 94.92] |
| S4G-StdDual | 94.24 [90.68, 97.05] | 99.39 [98.32, 99.98] | 96.54 [94.26, 98.31] | — | — | — | 90.60 [85.90, 94.42] |
| S4G-QDual (Ours) | 95.10 [92.28, 97.33] | 99.44 [98.59, 99.92] | 97.03 [95.19, 98.45] | — | — | — | 91.53 [87.45, 94.78] |


#### ExposureClip

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 75.37 [68.62, 81.26] | 93.45 [89.09, 96.94] | 83.48 [78.32, 87.87] | — | — | — | 66.60 [59.05, 73.58] |
| Base + StdDual | 82.10 [76.11, 87.26] | 95.47 [91.79, 98.26] | 88.13 [83.44, 92.06] | — | — | — | 72.25 [64.87, 78.83] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 81.90 [75.72, 87.22] | 95.75 [91.91, 98.52] | 88.31 [83.64, 92.16] | — | — | — | 75.10 [68.15, 81.35] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 82.86 [77.47, 87.33] | 95.98 [92.29, 98.72] | 88.75 [84.51, 92.18] | — | — | — | 75.15 [68.15, 81.10] |
| Base + QGIN (Ours) | 88.00 [83.32, 91.76] | 97.71 [95.27, 99.41] | 92.45 [88.96, 95.14] | — | — | — | 81.40 [75.40, 86.58] |
| Sample4Geo† [ICCV 2023] | 84.75 [79.28, 89.72] | 97.79 [96.11, 99.09] | 90.53 [86.88, 93.83] | — | — | — | 78.75 [72.15, 84.83] |
| S4G-StdDual | 86.06 [80.80, 90.77] | 97.86 [95.91, 99.28] | 91.24 [87.56, 94.47] | — | — | — | 79.83 [73.67, 85.63] |
| S4G-QDual (Ours) | 91.22 [87.29, 94.51] | 98.85 [97.72, 99.62] | 94.60 [92.09, 96.76] | — | — | — | 85.60 [80.25, 90.40] |


#### Posterize4

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 88.69 [84.11, 92.49] | 98.09 [95.68, 99.49] | 92.79 [89.42, 95.43] | — | — | — | 82.70 [76.62, 87.95] |
| Base + StdDual | 92.22 [88.46, 95.23] | 98.04 [95.32, 99.56] | 94.86 [91.86, 97.06] | — | — | — | 84.70 [79.05, 89.63] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.30 [86.94, 94.76] | 98.43 [96.17, 99.73] | 94.47 [91.28, 96.86] | — | — | — | 85.00 [78.85, 90.38] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 91.64 [87.87, 94.83] | 97.80 [95.25, 99.39] | 94.47 [91.46, 96.79] | — | — | — | 85.47 [79.70, 90.33] |
| Base + QGIN (Ours) | 93.84 [90.36, 96.58] | 99.03 [97.91, 99.74] | 96.20 [93.80, 97.98] | — | — | — | 88.62 [83.85, 92.72] |
| Sample4Geo† [ICCV 2023] | 94.79 [91.54, 97.36] | 99.22 [98.09, 99.95] | 96.81 [94.56, 98.51] | — | — | — | 91.35 [86.83, 94.98] |
| S4G-StdDual | 94.34 [90.84, 97.13] | 99.26 [98.11, 99.93] | 96.54 [94.20, 98.36] | — | — | — | 91.35 [86.92, 94.90] |
| S4G-QDual (Ours) | 95.24 [92.56, 97.38] | 99.41 [98.62, 99.89] | 97.11 [95.29, 98.49] | — | — | — | 91.60 [87.67, 94.85] |


#### CorrMean6

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 81.72 [77.12, 85.63] | 95.38 [93.09, 97.26] | 87.77 [84.23, 90.68] | — | — | — | 75.01 [69.36, 80.19] |
| Base + StdDual | 86.37 [82.25, 89.72] | 96.24 [93.45, 98.18] | 90.83 [87.44, 93.41] | — | — | — | 79.28 [73.95, 84.18] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 85.66 [81.12, 89.34] | 96.56 [93.99, 98.30] | 90.60 [87.33, 93.26] | — | — | — | 79.33 [73.94, 83.96] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 87.18 [83.52, 90.36] | 96.63 [94.00, 98.35] | 91.44 [88.44, 93.87] | — | — | — | 81.05 [75.50, 85.83] |
| Base + QGIN (Ours) | 90.53 [87.12, 93.28] | 98.18 [96.73, 99.15] | 93.97 [91.46, 95.84] | — | — | — | 84.73 [79.67, 88.94] |
| Sample4Geo† [ICCV 2023] | 88.40 [84.79, 91.33] | 97.50 [95.86, 98.69] | 92.48 [89.82, 94.54] | — | — | — | 84.07 [79.40, 88.05] |
| S4G-StdDual | 88.59 [84.71, 91.62] | 97.63 [95.89, 98.82] | 92.63 [89.82, 94.76] | — | — | — | 84.17 [79.35, 88.17] |
| S4G-QDual (Ours) | 92.95 [89.98, 95.37] | 98.92 [97.99, 99.57] | 95.61 [93.57, 97.19] | — | — | — | 88.50 [84.28, 91.98] |


#### NonSnowMean5

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 85.03 [80.50, 88.86] | 97.11 [95.23, 98.60] | 90.33 [86.99, 93.03] | — | — | — | 77.83 [72.11, 82.84] |
| Base + StdDual | 89.23 [85.28, 92.48] | 97.54 [95.05, 99.10] | 92.96 [89.86, 95.34] | — | — | — | 81.52 [76.33, 86.33] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 88.42 [84.15, 91.92] | 97.73 [95.44, 99.18] | 92.64 [89.55, 95.10] | — | — | — | 82.09 [76.59, 86.79] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 89.53 [85.91, 92.53] | 97.61 [95.21, 99.11] | 93.17 [90.31, 95.40] | — | — | — | 83.06 [77.65, 87.75] |
| Base + QGIN (Ours) | 92.11 [88.77, 94.79] | 98.73 [97.52, 99.54] | 95.11 [92.76, 96.87] | — | — | — | 86.38 [81.51, 90.45] |
| Sample4Geo† [ICCV 2023] | 92.08 [88.65, 94.88] | 98.93 [97.80, 99.65] | 95.15 [92.79, 96.98] | — | — | — | 87.69 [83.07, 91.58] |
| S4G-StdDual | 92.09 [88.44, 95.03] | 98.88 [97.56, 99.69] | 95.11 [92.50, 97.05] | — | — | — | 87.70 [83.18, 91.66] |
| S4G-QDual (Ours) | 94.38 [91.60, 96.53] | 99.27 [98.34, 99.80] | 96.56 [94.64, 97.97] | — | — | — | 90.25 [86.21, 93.59] |


#### Seed 43

#### Clean

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 89.69 [84.84, 93.56] | 97.56 [94.89, 99.38] | 93.18 [89.60, 96.02] | — | — | — | 84.60 [78.67, 89.95] |
| Base + StdDual | 91.31 [86.75, 94.74] | 97.86 [95.11, 99.69] | 94.29 [90.81, 96.82] | — | — | — | 84.62 [78.55, 89.85] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.73 [87.27, 95.14] | 98.99 [97.87, 99.83] | 94.77 [91.80, 97.02] | — | — | — | 86.42 [80.97, 91.20] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 91.66 [87.19, 95.02] | 97.84 [95.46, 99.53] | 94.44 [91.09, 96.94] | — | — | — | 86.10 [80.70, 90.70] |
| Base + QGIN (Ours) | 94.20 [90.61, 96.84] | 99.14 [97.94, 99.88] | 96.48 [94.03, 98.21] | — | — | — | 89.85 [84.92, 93.88] |
| Sample4Geo† [ICCV 2023] | 94.76 [91.30, 97.50] | 99.47 [98.60, 99.99] | 96.83 [94.57, 98.56] | — | — | — | 91.88 [87.53, 95.42] |
| S4G-StdDual | 95.04 [91.79, 97.66] | 99.58 [98.83, 99.98] | 97.06 [94.95, 98.67] | — | — | — | 92.22 [87.85, 95.70] |
| S4G-QDual (Ours) | 97.11 [95.11, 98.69] | 99.83 [99.57, 99.98] | 98.38 [97.23, 99.28] | — | — | — | 94.45 [91.27, 97.05] |


#### Fog

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 88.64 [83.62, 92.70] | 97.16 [94.52, 98.99] | 92.53 [88.80, 95.41] | — | — | — | 82.15 [75.90, 87.62] |
| Base + StdDual | 89.03 [84.27, 92.88] | 97.66 [94.92, 99.54] | 92.97 [89.40, 95.67] | — | — | — | 80.83 [74.15, 86.58] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 90.76 [86.39, 94.25] | 98.84 [97.98, 99.50] | 94.16 [91.28, 96.42] | — | — | — | 85.80 [80.27, 90.40] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 90.15 [85.61, 93.48] | 97.47 [95.04, 99.31] | 93.49 [90.07, 95.98] | — | — | — | 83.67 [77.72, 88.60] |
| Base + QGIN (Ours) | 93.72 [90.27, 96.34] | 99.09 [98.15, 99.72] | 96.15 [93.91, 97.80] | — | — | — | 88.88 [84.30, 92.70] |
| Sample4Geo† [ICCV 2023] | 93.57 [89.67, 96.64] | 99.21 [97.97, 99.96] | 96.08 [93.47, 98.09] | — | — | — | 90.20 [85.47, 94.12] |
| S4G-StdDual | 93.65 [89.77, 96.73] | 99.35 [98.24, 99.97] | 96.11 [93.54, 98.11] | — | — | — | 89.80 [84.85, 93.85] |
| S4G-QDual (Ours) | 96.37 [93.79, 98.31] | 99.71 [99.27, 99.96] | 97.91 [96.37, 99.03] | — | — | — | 92.90 [89.35, 95.78] |


#### Snow

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 64.06 [56.41, 71.23] | 85.66 [79.45, 90.85] | 73.76 [67.23, 79.73] | — | — | — | 60.33 [51.97, 67.98] |
| Base + StdDual | 68.75 [61.04, 75.63] | 88.33 [82.45, 93.01] | 77.42 [70.94, 83.05] | — | — | — | 64.03 [55.82, 71.70] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 74.68 [67.37, 81.09] | 90.03 [84.81, 94.47] | 81.61 [75.51, 86.85] | — | — | — | 69.62 [62.07, 76.40] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 72.70 [65.30, 79.34] | 90.73 [85.56, 94.97] | 80.85 [74.92, 85.96] | — | — | — | 69.62 [61.92, 76.70] |
| Base + QGIN (Ours) | 85.19 [79.50, 90.12] | 95.84 [92.34, 98.53] | 90.01 [85.66, 93.62] | — | — | — | 79.78 [72.90, 85.90] |
| Sample4Geo† [ICCV 2023] | 74.29 [67.43, 80.73] | 91.51 [86.46, 95.68] | 82.23 [76.63, 87.09] | — | — | — | 68.28 [60.52, 75.30] |
| S4G-StdDual | 76.14 [69.74, 82.15] | 92.36 [87.65, 96.20] | 83.60 [78.22, 88.20] | — | — | — | 70.12 [62.85, 76.93] |
| S4G-QDual (Ours) | 88.19 [83.63, 92.48] | 98.14 [96.62, 99.29] | 92.67 [89.66, 95.39] | — | — | — | 83.38 [77.80, 88.40] |


#### Blur

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 87.37 [82.94, 90.98] | 97.59 [94.57, 99.27] | 91.86 [88.33, 94.49] | — | — | — | 81.67 [75.05, 87.13] |
| Base + StdDual | 87.55 [82.42, 91.78] | 97.56 [94.87, 99.39] | 92.04 [88.33, 95.01] | — | — | — | 81.25 [74.32, 86.67] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.48 [87.79, 94.46] | 99.06 [98.33, 99.59] | 94.80 [92.50, 96.68] | — | — | — | 86.25 [80.82, 90.65] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 88.66 [84.59, 92.24] | 97.69 [95.69, 99.15] | 92.85 [89.87, 95.29] | — | — | — | 83.55 [77.90, 88.30] |
| Base + QGIN (Ours) | 92.88 [89.66, 95.63] | 99.01 [98.25, 99.58] | 95.57 [93.43, 97.30] | — | — | — | 89.08 [84.40, 92.93] |
| Sample4Geo† [ICCV 2023] | 92.56 [88.88, 95.52] | 99.26 [98.33, 99.84] | 95.52 [93.03, 97.43] | — | — | — | 87.97 [82.90, 92.05] |
| S4G-StdDual | 93.09 [89.68, 95.85] | 99.21 [98.16, 99.84] | 95.83 [93.51, 97.60] | — | — | — | 88.38 [83.70, 92.33] |
| S4G-QDual (Ours) | 95.74 [93.39, 97.55] | 99.69 [99.19, 99.96] | 97.57 [96.20, 98.64] | — | — | — | 92.75 [89.20, 95.58] |


#### Gamma

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 88.99 [83.75, 93.15] | 97.26 [94.66, 99.13] | 92.60 [88.76, 95.65] | — | — | — | 83.80 [77.55, 89.10] |
| Base + StdDual | 90.53 [85.92, 94.11] | 97.78 [94.92, 99.66] | 93.83 [90.26, 96.42] | — | — | — | 83.28 [76.90, 88.67] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.67 [87.08, 95.18] | 98.94 [97.83, 99.74] | 94.63 [91.57, 97.03] | — | — | — | 86.55 [81.40, 91.05] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 91.71 [87.40, 94.96] | 98.03 [95.84, 99.58] | 94.52 [91.26, 96.91] | — | — | — | 86.28 [81.10, 90.78] |
| Base + QGIN (Ours) | 94.16 [90.59, 96.78] | 99.19 [98.06, 99.89] | 96.46 [94.02, 98.18] | — | — | — | 90.00 [85.22, 93.85] |
| Sample4Geo† [ICCV 2023] | 94.20 [90.62, 97.05] | 99.58 [99.05, 99.96] | 96.47 [94.26, 98.27] | — | — | — | 90.47 [85.70, 94.35] |
| S4G-StdDual | 94.25 [90.62, 97.16] | 99.51 [98.86, 99.97] | 96.49 [94.23, 98.32] | — | — | — | 90.42 [85.67, 94.40] |
| S4G-QDual (Ours) | 96.83 [94.73, 98.45] | 99.84 [99.57, 99.99] | 98.21 [97.03, 99.12] | — | — | — | 94.05 [90.95, 96.58] |


#### ExposureClip

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 76.71 [69.71, 82.99] | 94.12 [90.22, 97.10] | 84.32 [79.03, 88.93] | — | — | — | 69.30 [61.55, 76.43] |
| Base + StdDual | 80.41 [74.01, 85.86] | 95.24 [91.24, 98.13] | 87.10 [82.16, 91.10] | — | — | — | 71.70 [64.28, 78.03] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 83.17 [76.84, 88.53] | 96.44 [93.57, 98.72] | 89.09 [84.62, 92.90] | — | — | — | 76.35 [69.42, 82.43] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 81.96 [76.05, 86.93] | 95.84 [92.31, 98.46] | 88.16 [83.61, 91.82] | — | — | — | 74.55 [67.78, 80.50] |
| Base + QGIN (Ours) | 87.56 [82.04, 92.08] | 97.14 [94.42, 99.16] | 91.97 [88.05, 95.23] | — | — | — | 81.85 [75.50, 87.45] |
| Sample4Geo† [ICCV 2023] | 86.22 [81.19, 90.71] | 98.44 [96.85, 99.49] | 91.61 [88.28, 94.45] | — | — | — | 81.10 [75.55, 86.38] |
| S4G-StdDual | 88.62 [83.96, 92.69] | 98.79 [97.32, 99.74] | 93.05 [89.99, 95.65] | — | — | — | 83.15 [77.77, 88.15] |
| S4G-QDual (Ours) | 92.96 [89.78, 95.63] | 99.49 [98.95, 99.88] | 95.91 [94.04, 97.49] | — | — | — | 88.58 [84.40, 92.38] |


#### Posterize4

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 89.39 [84.68, 93.26] | 97.39 [94.58, 99.31] | 92.97 [89.40, 95.82] | — | — | — | 84.12 [78.20, 89.38] |
| Base + StdDual | 90.79 [86.39, 94.28] | 97.69 [94.89, 99.60] | 93.90 [90.34, 96.49] | — | — | — | 84.03 [77.87, 89.35] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 91.53 [87.05, 94.98] | 98.86 [97.55, 99.80] | 94.60 [91.51, 96.93] | — | — | — | 86.12 [80.58, 90.97] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 91.46 [87.11, 94.83] | 97.68 [95.29, 99.39] | 94.26 [90.93, 96.76] | — | — | — | 85.83 [80.32, 90.38] |
| Base + QGIN (Ours) | 93.92 [90.23, 96.64] | 99.06 [97.86, 99.85] | 96.27 [93.75, 98.09] | — | — | — | 89.42 [84.40, 93.55] |
| Sample4Geo† [ICCV 2023] | 94.28 [90.62, 97.18] | 99.31 [98.26, 99.99] | 96.53 [94.13, 98.38] | — | — | — | 90.97 [86.28, 94.75] |
| S4G-StdDual | 94.47 [90.92, 97.33] | 99.44 [98.44, 99.99] | 96.73 [94.44, 98.49] | — | — | — | 91.35 [86.67, 95.12] |
| S4G-QDual (Ours) | 96.96 [95.02, 98.52] | 99.84 [99.56, 99.99] | 98.30 [97.17, 99.17] | — | — | — | 94.22 [91.15, 96.78] |


#### CorrMean6

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 82.53 [77.62, 86.61] | 94.87 [91.91, 97.07] | 88.01 [84.18, 91.05] | — | — | — | 76.90 [70.99, 81.98] |
| Base + StdDual | 84.51 [79.78, 88.26] | 95.71 [92.61, 97.95] | 89.55 [85.74, 92.49] | — | — | — | 77.52 [71.28, 82.72] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 87.21 [82.74, 90.74] | 97.03 [95.36, 98.40] | 91.48 [88.33, 94.02] | — | — | — | 81.78 [76.51, 86.20] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 86.11 [81.73, 89.60] | 96.24 [93.69, 98.14] | 90.69 [87.32, 93.27] | — | — | — | 80.58 [75.23, 85.09] |
| Base + QGIN (Ours) | 91.24 [87.55, 94.16] | 98.22 [96.76, 99.30] | 94.41 [91.82, 96.47] | — | — | — | 86.50 [81.62, 90.68] |
| Sample4Geo† [ICCV 2023] | 89.19 [85.43, 92.28] | 97.89 [96.43, 99.00] | 93.07 [90.50, 95.13] | — | — | — | 84.83 [80.24, 88.80] |
| S4G-StdDual | 90.04 [86.34, 93.11] | 98.11 [96.69, 99.18] | 93.63 [91.13, 95.72] | — | — | — | 85.54 [80.93, 89.37] |
| S4G-QDual (Ours) | 94.51 [92.10, 96.46] | 99.45 [98.96, 99.80] | 96.76 [95.29, 97.94] | — | — | — | 90.98 [87.76, 93.80] |


#### NonSnowMean5

| Method | R@1 ↑ | R@5 ↑ | AP ↑ | SDM@3 ↑ | Dis@1 (m) ↓ | >200 m (%) ↓ | Worst-height R@1 ↑ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 86.22 [81.35, 90.11] | 96.71 [94.13, 98.57] | 90.86 [87.20, 93.69] | — | — | — | 80.21 [74.31, 85.22] |
| Base + StdDual | 87.66 [83.00, 91.32] | 97.19 [94.41, 99.13] | 91.97 [88.40, 94.66] | — | — | — | 80.22 [73.97, 85.50] |
| Base + ColorJitter-Dual | — | — | — | — | — | — | — |
| Base + AugMix-Dual | 89.72 [85.51, 93.03] | 98.43 [97.29, 99.34] | 93.46 [90.57, 95.70] | — | — | — | 84.22 [79.00, 88.53] |
| w/o Quantile Anchoring (Fixed Zero-Hinge) | 88.79 [84.63, 92.08] | 97.34 [95.05, 98.99] | 92.66 [89.47, 95.09] | — | — | — | 82.78 [77.43, 87.18] |
| Base + QGIN (Ours) | 92.45 [88.92, 95.23] | 98.70 [97.47, 99.55] | 95.28 [92.86, 97.13] | — | — | — | 87.84 [83.02, 91.79] |
| Sample4Geo† [ICCV 2023] | 92.17 [88.67, 95.07] | 99.16 [98.23, 99.79] | 95.24 [92.92, 97.11] | — | — | — | 88.14 [83.61, 91.89] |
| S4G-StdDual | 92.82 [89.27, 95.70] | 99.26 [98.33, 99.89] | 95.64 [93.29, 97.50] | — | — | — | 88.62 [84.15, 92.30] |
| S4G-QDual (Ours) | 95.77 [93.50, 97.53] | 99.71 [99.34, 99.93] | 97.58 [96.26, 98.60] | — | — | — | 92.50 [89.37, 95.11] |


## C. Complexity and inference cost

Latency is the measured median of 30 single-image FP16 inference repetitions after 10 warmup repetitions on an RTX 4090, without flip augmentation or input I/O. Extra parameters are relative to the shared Base inference encoder. QGIN adds no learned or inference parameters. Training memory reports the maximum allocated memory on any one device during the recorded training process; the CSV retains each device peak and execution scope. A dash denotes an unrecorded training-memory measurement. Latency and memory means average the two runs; these device measurements have no place-bootstrap CI.

### Dense training

| Method | Seed | Dim | Extra params (M) | Single image (ms) | Training peak (GiB) |
| --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 42 | 768.00 | 0.00 | 5.95 | 1.96 |
| Base (EVA + Label Smoothing) | 43 | 768.00 | 0.00 | 5.93 | 1.96 |
| Base (EVA + Label Smoothing) | mean | 768.00 | 0.00 | 5.94 | 1.96 |
| Sample4Geo† [ICCV 2023] | 42 | 768.00 | 0.00 | 6.15 | — |
| Sample4Geo† [ICCV 2023] | 43 | 768.00 | 0.00 | 6.10 | — |
| Sample4Geo† [ICCV 2023] | mean | 768.00 | 0.00 | 6.13 | — |
| DAC† [TCSVT 2024] | 42 | 1024.00 | 0.79 | 6.21 | — |
| DAC† [TCSVT 2024] | 43 | 1024.00 | 0.79 | 6.27 | — |
| DAC† [TCSVT 2024] | mean | 1024.00 | 0.79 | 6.24 | — |
| ConGeo† [ECCV 2024] | 42 | 768.00 | 0.00 | 6.07 | — |
| ConGeo† [ECCV 2024] | 43 | 768.00 | 0.00 | 6.13 | — |
| ConGeo† [ECCV 2024] | mean | 768.00 | 0.00 | 6.10 | — |
| MEAN† [TGRS 2025] | 42 | 768.00 | 0.00 | 6.19 | — |
| MEAN† [TGRS 2025] | 43 | 768.00 | 0.00 | 6.12 | — |
| MEAN† [TGRS 2025] | mean | 768.00 | 0.00 | 6.16 | — |
| QDFL† [TGRS 2025] | 42 | 2048.00 | 20.85 | 10.54 | — |
| QDFL† [TGRS 2025] | 43 | 2048.00 | 20.85 | 12.15 | — |
| QDFL† [TGRS 2025] | mean | 2048.00 | 20.85 | 11.34 | — |
| SinGeo† [CVPR 2026] | 42 | 768.00 | 0.00 | 6.87 | — |
| SinGeo† [CVPR 2026] | 43 | 768.00 | 0.00 | 6.02 | — |
| SinGeo† [CVPR 2026] | mean | 768.00 | 0.00 | 6.44 | — |
| MRGeo‡ [AAAI 2026] | 42 | 3072.00 | 5.90 | 6.65 | — |
| MRGeo‡ [AAAI 2026] | 43 | 3072.00 | 5.90 | 6.40 | — |
| MRGeo‡ [AAAI 2026] | mean | 3072.00 | 5.90 | 6.52 | — |
| Base + QGIN (Ours) | 42 | 768.00 | 0.00 | 5.95 | 1.96 |
| Base + QGIN (Ours) | 43 | 768.00 | 0.00 | 5.92 | 1.96 |
| Base + QGIN (Ours) | mean | 768.00 | 0.00 | 5.94 | 1.96 |
| S4G-QDual (Ours) | 42 | 768.00 | 0.00 | 6.17 | — |
| S4G-QDual (Ours) | 43 | 768.00 | 0.00 | 6.14 | — |
| S4G-QDual (Ours) | mean | 768.00 | 0.00 | 6.16 | — |
| ConGeo-QView (Ours) | 42 | 768.00 | 0.00 | 6.02 | — |
| ConGeo-QView (Ours) | 43 | 768.00 | 0.00 | 5.96 | — |
| ConGeo-QView (Ours) | mean | 768.00 | 0.00 | 5.99 | — |
| SinGeo-QView (Ours) | 42 | 768.00 | 0.00 | 6.02 | — |
| SinGeo-QView (Ours) | 43 | 768.00 | 0.00 | 7.47 | — |
| SinGeo-QView (Ours) | mean | 768.00 | 0.00 | 6.75 | — |
| S4G-StdDual | 42 | 768.00 | 0.00 | 6.06 | — |
| S4G-StdDual | 43 | 768.00 | 0.00 | 6.05 | — |
| S4G-StdDual | mean | 768.00 | 0.00 | 6.05 | — |


### Sues training

| Method | Seed | Dim | Extra params (M) | Single image (ms) | Training peak (GiB) |
| --- | --- | --- | --- | --- | --- |
| Base (EVA + Label Smoothing) | 42 | 768.00 | 0.00 | 6.02 | 1.96 |
| Base (EVA + Label Smoothing) | 43 | 768.00 | 0.00 | 5.95 | 1.96 |
| Base (EVA + Label Smoothing) | mean | 768.00 | 0.00 | 5.98 | 1.96 |
| Sample4Geo† [ICCV 2023] | 42 | 768.00 | 0.00 | 6.04 | — |
| Sample4Geo† [ICCV 2023] | 43 | 768.00 | 0.00 | 6.40 | — |
| Sample4Geo† [ICCV 2023] | mean | 768.00 | 0.00 | 6.22 | — |
| DAC† [TCSVT 2024] | 42 | 1024.00 | 0.79 | 6.45 | — |
| DAC† [TCSVT 2024] | 43 | 1024.00 | 0.79 | 6.27 | — |
| DAC† [TCSVT 2024] | mean | 1024.00 | 0.79 | 6.36 | — |
| ConGeo† [ECCV 2024] | 42 | 768.00 | 0.00 | 5.93 | — |
| ConGeo† [ECCV 2024] | 43 | 768.00 | 0.00 | 6.04 | — |
| ConGeo† [ECCV 2024] | mean | 768.00 | 0.00 | 5.99 | — |
| MEAN† [TGRS 2025] | 42 | 768.00 | 0.00 | 6.06 | — |
| MEAN† [TGRS 2025] | 43 | 768.00 | 0.00 | 6.04 | — |
| MEAN† [TGRS 2025] | mean | 768.00 | 0.00 | 6.05 | — |
| QDFL† [TGRS 2025] | 42 | 2048.00 | 20.85 | 10.54 | — |
| QDFL† [TGRS 2025] | 43 | 2048.00 | 20.85 | 14.38 | — |
| QDFL† [TGRS 2025] | mean | 2048.00 | 20.85 | 12.46 | — |
| SinGeo† [CVPR 2026] | 42 | 768.00 | 0.00 | 6.09 | — |
| SinGeo† [CVPR 2026] | 43 | 768.00 | 0.00 | 6.03 | — |
| SinGeo† [CVPR 2026] | mean | 768.00 | 0.00 | 6.06 | — |
| MRGeo‡ [AAAI 2026] | 42 | 3072.00 | 5.90 | 6.67 | — |
| MRGeo‡ [AAAI 2026] | 43 | 3072.00 | 5.90 | 6.63 | — |
| MRGeo‡ [AAAI 2026] | mean | 3072.00 | 5.90 | 6.65 | — |
| Base + QGIN (Ours) | 42 | 768.00 | 0.00 | 7.39 | 1.73 |
| Base + QGIN (Ours) | 43 | 768.00 | 0.00 | 5.93 | 1.73 |
| Base + QGIN (Ours) | mean | 768.00 | 0.00 | 6.66 | 1.73 |
| S4G-QDual (Ours) | 42 | 768.00 | 0.00 | 6.03 | — |
| S4G-QDual (Ours) | 43 | 768.00 | 0.00 | 6.02 | — |
| S4G-QDual (Ours) | mean | 768.00 | 0.00 | 6.03 | — |
| ConGeo-QView (Ours) | 42 | 768.00 | 0.00 | 6.04 | — |
| ConGeo-QView (Ours) | 43 | 768.00 | 0.00 | 6.12 | — |
| ConGeo-QView (Ours) | mean | 768.00 | 0.00 | 6.08 | — |
| SinGeo-QView (Ours) | 42 | 768.00 | 0.00 | 6.97 | — |
| SinGeo-QView (Ours) | 43 | 768.00 | 0.00 | 6.03 | — |
| SinGeo-QView (Ours) | mean | 768.00 | 0.00 | 6.50 | — |
| S4G-StdDual | 42 | 768.00 | 0.00 | 6.36 | — |
| S4G-StdDual | 43 | 768.00 | 0.00 | 6.00 | — |
| S4G-StdDual | mean | 768.00 | 0.00 | 6.18 | — |
