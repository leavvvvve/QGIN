"""Render publication tables and figures from the shipped aggregate CSVs."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'paper_assets';S=P/'summary_csv';FIG=P/'figures';FIG.mkdir(exist_ok=True)
CONDS=['Clean','Fog','Snow','Blur','Gamma','ExposureClip','Posterize4','CorrMean6','NonSnowMean5']
DIRS=['dense_to_dense','sues_to_sues','dense_to_sues','sues_to_dense']
DIRLABEL=dict(zip(DIRS,['Dense → Dense','SUES → SUES','Dense → SUES','SUES → Dense']))
HOSTS=['Sample4Geo','DAC','ConGeo','MEAN','QDFL','SinGeo','MRGeo']
MAIN=['Base']+HOSTS+['Base + QGIN','S4G-QDual','ConGeo-QView','SinGeo-QView']
FIX='w/o Quantile Anchoring (Fixed Zero-Hinge)'
LABEL={'Base':'Base (EVA + Label Smoothing)','Sample4Geo':'Sample4Geo† [ICCV 2023]','DAC':'DAC† [TCSVT 2024]','ConGeo':'ConGeo† [ECCV 2024]','MEAN':'MEAN† [TGRS 2025]','QDFL':'QDFL† [TGRS 2025]','SinGeo':'SinGeo† [CVPR 2026]','MRGeo':'MRGeo‡ [AAAI 2026]','ConGeo-QView':'ConGeo-QView (Ours)','Base + QGIN':'Base + QGIN (Ours)','S4G-QDual':'S4G-QDual (Ours)','SinGeo-QView':'SinGeo-QView (Ours)'}
MET=['r1','r5','ap','sdm3','dis1_m','error_gt200m','worst_height_r1']
MLABEL=dict(zip(MET,['R@1 ↑','R@5 ↑','AP ↑','SDM@3 ↑','Dis@1 (m) ↓','>200 m (%) ↓','Worst-height R@1 ↑']))
score=pd.read_csv(S/'benchmark_all.csv',dtype={'seed':str})
paired=pd.read_csv(S/'paired_host_gains.csv',dtype={'seed':str})
cte=pd.read_csv(S/'cte_paired.csv',dtype={'seed':str})
def f(x):return '—' if pd.isna(x) else f'{x:.2f}'
def ci(r,col='value'):
 if pd.isna(r[col]):return '—'
 return f'{r[col]:.2f} [{r.ci_low:.2f}, {r.ci_high:.2f}]'
def table(headers,rows):return '\n| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(str(v) for v in row)+' |\n' for row in rows)+'\n'
def write(name,s):(P/name).write_text(s.rstrip()+'\n',encoding='utf-8')
def metric_tables(d,methods):
 text=''
 for seed in ['mean','42','43']:
  text+='\n### '+('Two-seed mean' if seed=='mean' else 'Seed '+seed)+'\n'
  for condition in CONDS:
   text+='\n#### '+condition+'\n'
   z=d[(d.seed==seed)&(d.condition==condition)].set_index(['method','metric'])
   text+=table(['Method']+[MLABEL[m] for m in MET],[[LABEL.get(m,m)]+[ci(z.loc[m,k]) if (m,k) in z.index else '—' for k in MET] for m in methods])
 return text

protocol='''All scores are percentages except Dis@1 in meters. Brackets give percentile 95% confidence intervals from 2,000 place-cluster bootstrap draws. DenseUAV has 777 test places, each with three query heights, and an 18,198-image gallery with six positives per query. SUES-200 has 80 test places, four heights and 50 frames per height; its 200-image gallery includes one positive per query. Every frame, height and condition of a sampled place stays together. Two-seed means average the fixed seed-42 and seed-43 endpoints within each common resampling replicate. Worst-height R@1 is the minimum over height-specific means, recomputed in each replicate, then averaged over the two seeds.

CorrMean6 averages all six degraded conditions. NonSnowMean5 averages Fog, Blur, Gamma, ExposureClip and Posterize4. AP follows the evaluated dataset protocols: trapezoidal AP for DenseUAV and standard AP (reciprocal rank for one positive) for SUES-200. SDM@3 uses the official exponentially weighted coordinate-distance score. SUES-200 has no GPS in the evaluation manifest, so its SDM and meter-based endpoints are marked —. Cross-domain checkpoints are evaluated directly without target updates.
'''
text='# Main benchmark tables\n\nThe benchmark uses a common EVA-family ViT-B/16 encoder at 384 × 384 resolution, domain/seed-matched 108-update warmups, and 648 formal updates per method. † denotes the controlled official-source implementation; ‡ denotes the MRGeo paper reimplementation. The exact backbone identifier, host-specific heads, optimization and source pins are in [Method](02_Method_Formulation.md) and [contracts](../configs_and_contracts/).\n\n'+protocol+'\nThe tables retain every condition and both training seeds. The machine-readable source is [benchmark_all.csv](summary_csv/benchmark_all.csv).\n'
for direction in DIRS:text+='\n## '+DIRLABEL[direction]+'\n'+metric_tables(score[score.direction==direction],MAIN)
write('03_Main_Benchmark_Tables.md',text)

text='# Plug-and-play host comparisons\n\nEach row compares a host with its paired QGIN variant using the same source sampling plan and host loss. Differences are candidate minus host; positive values favor QGIN for retrieval scores, and negative values favor QGIN for distance/error endpoints. Each Δ is followed by its paired 95% confidence interval. Absolute scores and their confidence intervals are in the [main tables](03_Main_Benchmark_Tables.md).\n\n'+protocol+'\nThe machine-readable source is [paired_host_gains.csv](summary_csv/paired_host_gains.csv).\n'
for direction in DIRS:
 text+='\n## '+DIRLABEL[direction]+'\n'
 for metric in MET:
  text+='\n### '+MLABEL[metric]+'\n';rows=[]
  for host in ['Base','Sample4Geo','ConGeo','SinGeo']:
   for condition in CONDS:
    d=paired[(paired.direction==direction)&(paired.host==host)&(paired.metric==metric)&(paired.condition==condition)].set_index('seed')
    row=[host,condition]
    for seed in ['42','43','mean']:
     r=d.loc[seed];row += [f(r.host_value),f(r.method_value),ci(r,'delta')]
    rows.append(row)
  text+=table(['Host','Condition','Host 42','QGIN 42','Δ42 [95% CI]','Host 43','QGIN 43','Δ43 [95% CI]','Host mean','QGIN mean','Δmean [95% CI]'],rows)
write('04_PlugAndPlay_Host_Tables.md',text)

text=r'''# Competitive takeovers, spatial errors and ablations

## A. Competitive-takeover trajectories

For a reference encoder, let $Q_0$ be queries retrieved correctly in Clean. Under each degraded condition, $m_{\rm old,loc}$ compares the best positive with the best image of the clean hardest-negative place, and $m_{\rm all}$ compares the best positive with the current hardest negative. A competitive takeover event (CTE) satisfies $m_{\rm old,loc}>10^{-6}$ and $m_{\rm all}<-10^{-6}$ within $Q_0$.

Rescue rate counts CTE queries whose candidate margin exceeds $10^{-6}$, divided by all reference CTE queries. New-failure rate counts candidate R@1 failures among the reference's still-correct degraded queries ($m_{\rm all}>10^{-6}$), divided by that still-correct set. Far-error removal counts reference CTE queries with Dis@1 > 200 m whose candidate error is ≤ 200 m, divided by reference CTE queries beyond 200 m. A zero denominator is shown as —. Exact numerators, denominators and Clean-correct set sizes for each seed are included in [cte_paired.csv](summary_csv/cte_paired.csv).

The primary frame uses each model's original host as reference. The common frame uses Base for all candidates. Both frames use the reference's Clean-correct set and degraded margins consistently. Seed-mean rates are the arithmetic mean of the two seed-specific rates; their confidence intervals use the same place resampling indices. A rate with a missing seed denominator has no two-seed mean.
'''
for direction in DIRS:
 text+='\n### '+DIRLABEL[direction]+'\n'
 for frame in ['host','common']:
  text+='\n#### '+('Primary host reference' if frame=='host' else 'Common Base reference')+'\n';rows=[]
  for method in ['Base + QGIN','S4G-QDual','ConGeo-QView','SinGeo-QView']:
   for condition in CONDS[:7]:
    for seed in ['42','43','mean']:
     d=cte[(cte.direction==direction)&(cte.method==method)&(cte.frame==frame)&(cte.condition==condition)&(cte.seed==seed)].set_index('metric')
     rows.append([method,condition,seed]+[ci(d.loc[m]) if m in d.index else '—' for m in ['rescue','new_failure','far200_removed']])
  text+=table(['Method','Condition','Seed','Rescue % [CI]','New failure % [CI]','Far-error removal % [CI]'],rows)
text+='\n## B. Photometric operator ablations\n\nStdDual uses scalar contrast/brightness; ColorJitter-Dual uses brightness/contrast/saturation 0.40 and hue 0.10; AugMix-Dual uses severity 3, width 3, stochastic depth and alpha 1.00. The Fixed Zero-Hinge control has the same sampled pointwise architecture, normalization and single mix as QGIN. SUES-trained ColorJitter-Dual was not evaluated and is shown as —.\n'
for direction in ['dense_to_dense','sues_to_sues']:
 text+='\n### '+DIRLABEL[direction]+'\n'
 text+=metric_tables(score[score.direction==direction],['Base','Base + StdDual','Base + ColorJitter-Dual','Base + AugMix-Dual',FIX,'Base + QGIN','Sample4Geo','S4G-StdDual','S4G-QDual']).replace('### Two-seed','#### Two-seed').replace('### Seed','#### Seed')
text+='\n## C. Complexity and inference cost\n\nLatency is the measured median of 30 single-image FP16 inference repetitions after 10 warmup repetitions on an RTX 4090, without flip augmentation or input I/O. Extra parameters are relative to the shared Base inference encoder. QGIN adds no learned or inference parameters. Training memory reports the maximum allocated memory on any one device during the recorded training process; the CSV retains each device peak and execution scope. A dash denotes an unrecorded training-memory measurement. Latency and memory means average the two runs; these device measurements have no place-bootstrap CI.\n'
cost=pd.read_csv(S/'inference_cost.csv')
for domain in ['dense','sues']:
 rows=[]
 for method in MAIN+['S4G-StdDual']:
  z=cost[(cost.domain==domain)&(cost.method==method)]
  for seed in ['42','43','mean']:
   d=z if seed=='mean' else z[z.seed==int(seed)]
   rows.append([LABEL.get(method,method),seed,f(d.descriptor_dim.mean()),f(d.extra_params.mean()/1e6),f(d.single_image_ms_median.mean()),f(d.training_peak_memory_gib.mean())])
 text+='\n### '+domain.title()+' training\n'+table(['Method','Seed','Dim','Extra params (M)','Single image (ms)','Training peak (GiB)'],rows)
write('05_CTE_Spatial_and_Ablation.md',text)

diag=pd.read_csv(S/'diagnostic_intervals.csv',dtype={'seed':str})
text=r'''# Photometric robustness and competitor reordering

## Similarity-margin decomposition

For the current best positive score $s_+$, the clean hardest-negative image $n_0$, and the current hardest-negative image $n_*$,

$$m_{\rm all}=s_+-s(n_*)=\underbrace{s_+-s(n_0)}_{m_{\rm old}}-\underbrace{[s(n_*)-s(n_0)]}_{\text{switch penalty}}.$$

The diagnostic uses the frozen encoder after 108 warmup updates and 324 further source updates, two training seeds and 2,331 DenseUAV queries. The native-image Snow transformation shifts both query appearance and the identity of the strongest competitor. MonoHistogramSnow preserves the ordering of HLS lightness while matching the Snow lightness histogram. Image-level and place-level negative switches are listed separately.

Margins and switch penalties are reported ×100 so small changes retain two-decimal readability. Retrieval and switching rates are percentages. Confidence intervals use 2,000 paired resamples of the 777 places.
'''
rows=[]
for seed in ['42','43','mean']:
 for c in ['Clean','Snow','MonoHistogramSnow','Gamma']:
  z=diag[(diag.family=='competition')&(diag.seed==seed)&(diag.condition==c)].set_index('metric')
  rows.append([seed,c]+[ci(z.loc[m]) for m in ['r1','m_all','m_old','switch_penalty','negative_image_switched','negative_location_switched']])
text+=table(['Seed','Condition','R@1 %','m_all ×100','m_old ×100','Penalty ×100','Image switch %','Place switch %'],rows)
text+='\n## First- and second-order photometric controls\n\nP matches Clean per-channel means and standard deviations to its paired Snow image; R restores Snow to the paired Clean image statistics. The photo fraction is (m_Clean − m_P)/(m_Clean − m_Snow), and the feature-oracle recovery fraction is (m_O_Snow − m_Snow)/(m_Clean − m_Snow). O_Snow restores paired Clean shallow-feature means and standard deviations; R restores pixel-level statistics. These controls quantify the portion of the observed margin loss recovered by affine moment matching. The small photo fraction and residual retrieval degradation motivate richer non-affine intensity transformations.\n'
rows=[]
for seed in ['42','43','mean']:
 for c in ['Clean','Snow','P','R','O_Snow']:
  z=diag[(diag.family=='affine')&(diag.seed==seed)&(diag.condition==c)].set_index('metric')
  rows.append([seed,c]+[ci(z.loc[m]) for m in ['r1','margin','same_relation_margin']])
text+=table(['Seed','Condition','R@1 %','Margin ×100','Fixed-negative margin ×100'],rows)
rows=[]
for seed in ['42','43','mean']:
 z=diag[(diag.family=='affine')&(diag.seed==seed)].set_index(['condition','metric'])
 rows.append([seed,ci(z.loc['ratio','photo_margin_fraction']),ci(z.loc['ratio','feature_oracle_margin_fraction']),ci(z.loc['R_minus_Snow','r1'])])
text+=table(['Seed','Photo fraction %','Feature-oracle margin recovery %','Pixel-oracle R@1 gain (pp)'],rows)
source=pd.read_csv(S/'source_operator_intervals.csv')
text+='\n## Quantile anchoring and activation coverage\n\nThe source diagnostic fixes 32 source images and four random parameter draws per image, giving 128 image–parameter pairs. Source confidence intervals resample the 32 images as clusters and retain the four parameter draws and channel measurements. This diagnostic uses a fixed seed-42 source plan. It measures augmentation behavior before downstream training.\n\nFor positive activation fraction f₊, hinge_miss is f₊ < 0.01 or f₊ > 0.99, and active_hinge is 0.20 ≤ f₊ ≤ 0.80. DC_share is HW times the squared norm of the spatial channel mean divided by output energy plus 10⁻⁶; AC_share is its complement. Energy shares refer to the raw nonlinear output before norm alignment and mixing.\n'
rows=[]
for method in [FIX,'QGIN']:
 for layer in [1,2,3]:
  z=source[(source['transform']==method)&(source.layer==layer)].set_index('metric')
  rows.append([method,layer]+[f'{z.loc[m,"value"]*100:.2f} [{z.loc[m,"ci_low"]*100:.2f}, {z.loc[m,"ci_high"]*100:.2f}]' for m in ['hinge_miss','active_hinge']])
text+=table(['Operator','Layer','Hinge miss % [CI]','Active hinge % [CI]'],rows)
rows=[]
for method in [FIX,'QGIN']:
 vals=[]
 for m in ['DC_share','AC_share','E1_delta','E2_delta']:
  z=source[(source['transform']==method)&(source.metric==m)]
  if m.startswith('E'):z=z[z.subset=='all']
  r=z.iloc[0];vals.append(f'{r.value*100:.2f} [{r.ci_low*100:.2f}, {r.ci_high*100:.2f}]')
 rows.append([method]+vals)
text+='\nThe residual E1_delta fits a per-channel affine map; E2_delta fits a full RGB affine map. Fits use 2,048 pixels and are evaluated on 2,048 held-out pixels. Their squared residual is normalized by the centered augmentation-shift energy. The following table reports medians ×100.\n'+table(['Operator','DC % [CI]','AC % [CI]','E1_delta ×100 [CI]','E2_delta ×100 [CI]'],rows)
text+='\nThe un-clipped subset excludes saturated pixels and retains 127 valid pairs per operator. Its held-out residual medians are listed separately.\n'
rows=[]
for method in [FIX,'QGIN']:
 z=source[(source['transform']==method)&(source.subset=='unclipped')].set_index('metric')
 rows.append([method]+[f'{z.loc[m,"value"]*100:.2f} [{z.loc[m,"ci_low"]*100:.2f}, {z.loc[m,"ci_high"]*100:.2f}]' for m in ['E1_delta','E2_delta']])
text+=table(['Operator','Unclipped E1_delta ×100 [CI]','Unclipped E2_delta ×100 [CI]'],rows)
ratio=[]
for metric in ['E1_delta','E2_delta']:
 z=source[(source.metric==metric)&(source.subset=='unclipped')].set_index('transform')
 ratio.append(f'{metric}: {z.loc["QGIN","value"]/z.loc[FIX,"value"]:.2f}×')
text+='\nUnclipped median residual ratios (QGIN / Fixed Zero-Hinge): '+', '.join(ratio)+'.\n\n![Quantile hinge coverage](figures/hinge_coverage.png)\n\nThese measurements connect spatial quantile anchoring to greater activation coverage, increased alternating spatial energy and stronger nonlinear photometric variation. The downstream operator ablations are in [CTE, spatial and ablation tables](05_CTE_Spatial_and_Ablation.md).\n'
write('01_Motivation_and_Diagnosis.md',text)

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':200})
fig,axes=plt.subplots(1,2,figsize=(8,3.3),layout='constrained')
for ax,metric,title in zip(axes,['hinge_miss','active_hinge'],['Hinge miss','Active hinge']):
 for method,label in [(FIX,'Fixed zero hinge'),('QGIN','QGIN')]:
  z=source[(source['transform']==method)&(source.metric==metric)].sort_values('layer')
  ax.plot(z.layer,z.value*100,'o-',label=label)
 ax.set(xticks=[1,2,3],xlabel='Hidden layer',ylabel='Channels (%)',title=title,ylim=(-3,103));ax.legend()
for suffix in ['png','pdf']:fig.savefig(FIG/f'hinge_coverage.{suffix}')
plt.close(fig)
fig,ax=plt.subplots(figsize=(8,4),layout='constrained');ys=np.arange(4)
for i,(method,label) in enumerate([('Base + QGIN','Base'),('S4G-QDual','Sample4Geo'),('ConGeo-QView','ConGeo'),('SinGeo-QView','SinGeo')]):
 z=paired[(paired.method==method)&(paired.seed=='mean')&(paired.metric=='r1')&(paired.condition=='CorrMean6')].set_index('direction').loc[DIRS]
 ax.errorbar(z.delta,ys+(i-1.5)*.16,xerr=np.vstack([z.delta-z.ci_low,z.ci_high-z.delta]),fmt='o',label=label,capsize=2)
ax.axvline(0,c='grey',lw=.8);ax.set(yticks=ys,yticklabels=[DIRLABEL[d] for d in DIRS],xlabel='CorrMean6 R@1 gain (percentage points)',title='Paired QGIN gains with 95% place-cluster CI');ax.legend(ncol=2)
for suffix in ['png','pdf']:fig.savefig(FIG/f'paired_gains.{suffix}')
plt.close(fig)

rows=[]
for direction in DIRS:
 d=paired[(paired.direction==direction)&(paired.method=='ConGeo-QView')&(paired.seed=='mean')&(paired.metric=='r1')&(paired.condition=='CorrMean6')].iloc[0]
 rows.append([DIRLABEL[direction],f(d.host_value),f(d.method_value),ci(d,'delta')])
readme='''# QGIN: Quantile-Guided Intensity Network

QGIN is a training-time pointwise photometric augmentation for cross-view geo-localization. It anchors random nonlinear activation hinges to spatial quantiles while keeping pixel locations fixed. **ConGeo-QView** applies QGIN to the secondary query of a four-view ConGeo objective. The retrieval encoder and its 768-dimensional inference descriptor remain unchanged.

The release contains portable operator/host code, pinned baseline contracts, seven-condition evaluation, place-cluster statistics, and complete paper tables. All runs use the shared EVA-family ViT-B/16 identifier `vit_base_patch16_rope_reg1_gap_256.sbb_in1k`, 384 × 384 input, 108 common warmup updates, 648 formal updates and seeds 42/43.

## ConGeo-QView results

CorrMean6 R@1, two-seed means. Gains use paired 2,000-draw place-cluster 95% confidence intervals.
'''+table(['Train → test','ConGeo†','ConGeo-QView','Gain (pp) [95% CI]'],rows)+'''
![Paired gains across hosts](paper_assets/figures/paired_gains.png)

## Paper assets

- [Motivation and diagnosis](paper_assets/01_Motivation_and_Diagnosis.md)
- [Method equations and implementation](paper_assets/02_Method_Formulation.md)
- [Complete main benchmark tables](paper_assets/03_Main_Benchmark_Tables.md)
- [Paired host comparisons](paper_assets/04_PlugAndPlay_Host_Tables.md)
- [CTE trajectories, spatial errors, ablations and cost](paper_assets/05_CTE_Spatial_and_Ablation.md)
- [Evidence paths and SHA256 manifest](paper_assets/FILE_MANIFEST.md)

## Code and execution

```text
src/modules/       QGIN, fixed-zero-hinge and standard photometric operators
src/hosts/         shared encoder, source views, objectives, optimizer and replay training
src/baselines/     pinned official-source adapters and MRGeo implementation
src/evaluation/    seven conditions, full-gallery retrieval, cluster bootstrap and CTE
configs_and_contracts/  exact training/evaluation settings and source pins
paper_assets/      paper documents, aggregate CSVs and scientific figures
```

Install the CUDA 12.1 wheels and dependencies in a Python 3.10 environment:

```bash
pip install torch==2.1.2 torchvision==0.16.2 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
python scripts/fetch_official.py --root external
python -m unittest discover -s tests -v
```

The fetch script checks out the exact upstream commits used by the contracts. It can also use a previously fetched pinned tree at `QGIN_OFFICIAL_ROOT`. See [third-party sources](THIRD_PARTY.md).

Training accepts local source-only plans and checkpoint inputs:

```bash
python -m src.hosts.train --config configs_and_contracts/run.example.json
```

Edit the example's paths to your dataset, 108-update warmup model/optimizer, and six block plans. Each plan is JSON with `rows` and `batches`; a row contains `query_path`, `reference_path`, `query_id`, `location_id`, and integer `label`. Each block contains 108 index batches. Augmentation files provide frozen per-row `packed` convolution parameters, `p` quantiles, and optional `std` or `seeds` for the controls. The exact historical artifacts and their checksums are indexed by the manifest. The release does not bundle datasets or weights.

Full-gallery evaluation uses a trained model and a target dataset manifest:

```bash
python -m src.evaluation.retrieve --host ConGeo --train-domain dense --target sues --checkpoint checkpoints/congeo_qview.pth --manifest data/sues_test.json --output outputs/retrieval.csv
python -m src.evaluation.summarize inputs.json outputs/benchmark.csv
python scripts/render_assets.py
```

The evaluation manifest schema is documented in `src/evaluation/retrieve.py`. The summary input is a JSON list of `{direction, method, seed, path}` entries pointing to evaluation CSVs. Source and target choices are independent, enabling both zero-shot directions. Evaluation performs no optimization. The renderer rebuilds the paper tables and figures from the committed aggregate CSVs.

## Measurement conventions

The tables retain seed-specific values, two-seed means, uncertainty, and all positive and negative paired changes. DenseUAV uses official trapezoidal AP; SUES-200 uses standard one-positive AP. SUES-200 spatial endpoints are not applicable because its manifest has no GPS. The SUES-trained ColorJitter control was not evaluated. Available training-memory measurements are reported; unrecorded cells are marked —. Checkpoint SHA256 lists identify the evaluated model files without distributing model binaries.
'''
(ROOT/'README.md').write_text(readme,encoding='utf-8')
print('rendered five-document asset set and README')
