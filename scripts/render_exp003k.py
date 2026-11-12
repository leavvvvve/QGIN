"""Render the selected EXP-003K manuscript tables from the committed CSVs."""
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'paper_assets/exp003k'
METHODS = ('ConGeo', 'SLAug', 'PASTA', 'AFA', 'RaffeSDG', 'ConGeo-QView')
REFS = ('ConGeo', 'SLAug', 'PASTA', 'AFA', 'RaffeSDG')
DIRECTIONS = (('dense', 'dense'), ('sues', 'sues'), ('dense', 'sues'), ('sues', 'dense'))


def rows(name):
    with (DATA / name).open(encoding='utf8', newline='') as f:
        return list(csv.DictReader(f))


def number(value):
    if value in ('', None):
        return float('nan')
    return float(value)


def fmt(value, scale=1., decimals=2):
    value = number(value)
    return f'{value * scale:.{decimals}f}' if math.isfinite(value) else '—'


def main():
    benchmark = rows('benchmark_metrics.csv')
    metrics = {(r['train_domain'], r['target'], r['method'], r['condition']): r
               for r in benchmark if r['seed'] == 'mean42_43'}
    cis = {(r['train_domain'], r['target'], r['reference'], r['condition']): r
           for r in rows('paired_bootstrap_ci.csv')
           if r['seed'] == 'mean42_43' and r['metric'] == 'r1'}
    diagnostic = {r['method']: r for r in rows('operator_diagnostics.csv')}
    assert len(metrics) == 4 * len(METHODS) * 9

    # Validate the restricted-set point claims rather than hard-coding them.
    for domain, target in DIRECTIONS:
        for condition, field in (('Snow', 'r1'), ('CorrMean6', 'r1'), ('CorrMean6', 'ap')):
            ours = number(metrics[domain, target, 'ConGeo-QView', condition][field])
            assert ours > max(number(metrics[domain, target, ref, condition][field]) for ref in REFS)
        if target == 'dense':
            for field in ('dis1_m', 'error_gt200m'):
                ours = number(metrics[domain, target, 'ConGeo-QView', 'CorrMean6'][field])
                assert ours < min(number(metrics[domain, target, ref, 'CorrMean6'][field]) for ref in REFS)

    out = [
        '# EXP-003K: selected cross-domain augmentation comparison',
        '',
        'This paper-ready selection compares four specified task-specific augmentation adapters '
        'with the historical ConGeo host and ConGeo-QView. Rankings below apply to this selected set.',
        '',
        '## Protocol and measurement boundaries',
        '',
        'Each adapter is applied to the secondary drone query view during training under the same '
        'ConGeo objective, 108-update warmup model and optimizer, six 108-update blocks, and seeds '
        '42 and 43. The selected subset comprises 16 new models and 224 model–target–condition '
        'evaluations. ConGeo and ConGeo-QView are previously archived references; they were not retrained.',
        '',
        'The four adapters follow the task-specific configurations described in '
        '[the operator contract](../../configs_and_contracts/exp003k/PROTOCOL.md). '
        'They are not full reproductions of the cited methods. All models use the same '
        'EVA-family backbone identifier and single-encoder retrieval interface. Synthetic Snow and '
        'Fog do not establish performance under real weather.',
        '',
        'CorrMean6 equally averages Fog, Snow, Blur, Gamma, ExposureClip and Posterize4. '
        'R@1 and AP are percentages, Dis@1 is in metres and >200m is a percentage. '
        'SUES-200 has no GPS measurements, so both distance columns are unavailable for that target. '
        'Dense AP uses the historical trapezoidal multi-positive convention; SUES AP uses a '
        'single-positive convention. Two-seed averages do not measure training-seed uncertainty.',
        '',
        '## Four-direction results (two-seed mean)',
        '',
        '| Train → target | Method | Clean R@1 | Snow R@1 | Snow AP | CorrMean6 R@1 | CorrMean6 AP | CorrMean6 Dis@1 (m) | CorrMean6 >200m |',
        '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |',
    ]
    for domain, target in DIRECTIONS:
        for arm in METHODS:
            clean, snow, corr = [metrics[domain, target, arm, condition]
                                 for condition in ('Clean', 'Snow', 'CorrMean6')]
            label = arm if arm in ('ConGeo', 'ConGeo-QView') else arm + '*'
            values = [fmt(clean['r1'], 100), fmt(snow['r1'], 100), fmt(snow['ap'], 100),
                      fmt(corr['r1'], 100), fmt(corr['ap'], 100), fmt(corr['dis1_m'], decimals=1),
                      fmt(corr['error_gt200m'], 100)]
            out.append('| ' + ' | '.join([f'{domain} → {target}', label, *values]) + ' |')

    out.extend(['', '## R@1 by condition (two-seed mean)', '',
                '| Train → target | Method | Clean | Fog | Snow | Blur | Gamma | ExposureClip | Posterize4 | CorrMean6 | NonSnowMean5 |',
                '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |'])
    for domain, target in DIRECTIONS:
        for arm in METHODS:
            conditions = ('Clean', 'Fog', 'Snow', 'Blur', 'Gamma', 'ExposureClip',
                          'Posterize4', 'CorrMean6', 'NonSnowMean5')
            values = [fmt(metrics[domain, target, arm, condition]['r1'], 100) for condition in conditions]
            out.append('| ' + ' | '.join([f'{domain} → {target}', arm, *values]) + ' |')

    out.extend(['', '## Four-direction macro-average (descriptive)', '',
                'Each direction contributes equally; macro AP combines two different dataset-specific AP conventions.',
                '', '| Method | Clean R@1 | Snow R@1 | CorrMean6 R@1 | CorrMean6 AP |',
                '| --- | ---: | ---: | ---: | ---: |'])
    for arm in METHODS:
        cells = []
        for condition, field in (('Clean', 'r1'), ('Snow', 'r1'), ('CorrMean6', 'r1'), ('CorrMean6', 'ap')):
            v = sum(number(metrics[d, t, arm, condition][field]) for d, t in DIRECTIONS) / len(DIRECTIONS)
            cells.append(fmt(v, 100))
        out.append('| ' + ' | '.join([arm if arm in ('ConGeo', 'ConGeo-QView') else arm + '*', *cells]) + ' |')

    out.extend(['', '## Paired differences for R@1', '',
                'QView minus each selected reference, in percentage points, with 2,000-draw '
                'paired 95% place-cluster bootstrap intervals. Both seeds use the same resampled '
                'test places; intervals condition on these trained models and do not cover retraining variability.',
                '', '| Train → target | Reference | Snow Δ [95% CI] | CorrMean6 Δ [95% CI] |',
                '| --- | --- | ---: | ---: |'])
    for domain, target in DIRECTIONS:
        for ref in REFS:
            values = []
            for condition in ('Snow', 'CorrMean6'):
                c = cis[domain, target, ref, condition]
                values.append(f"{100*float(c['delta']):+.2f} [{100*float(c['ci_low']):+.2f}, {100*float(c['ci_high']):+.2f}]")
            out.append('| ' + ' | '.join([f'{domain} → {target}', ref, *values]) + ' |')

    out.extend(['', 'A positive point estimate whose interval includes zero is not presented as a '
                'resolved advantage. These are exploratory comparisons without a multiple-testing correction.',
                '', '## Source128 operator diagnostics', '',
                'Thirty-two source images were sampled four times per operator. E1 and E2 are '
                'held-out RMS residuals after per-channel affine and full-channel affine fits, respectively. '
                'DC is squared spatial-mean perturbation energy; AC is all remaining spatial perturbation '
                'energy, not a high-frequency band. The edge statistic is the pixelwise RGB Sobel gradient '
                'cosine; pixels for which it is undefined are set to zero. These descriptive measurements '
                'do not establish a causal mechanism.', '',
                '| Method | E1 | E2 | DC | AC | Edge cosine | Valid edge cosine | Valid fraction |',
                '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |'])
    for method in ('SLAug', 'PASTA', 'AFA', 'RaffeSDG', 'QGIN'):
        row = diagnostic[method]
        vals = [fmt(row[k], decimals=4 if k in ('E1_delta', 'E2_delta') else 3)
                for k in ('E1_delta', 'E2_delta', 'DC_share', 'AC_share',
                          'EdgeGrad_CosSim', 'EdgeGrad_CosSim_valid', 'edge_valid_fraction')]
        out.append('| ' + ' | '.join([method, *vals]) + ' |')

    out.extend(['', '## Competitive takeover events: two reference anchors', '',
                'A competitive takeover event (CTE) is a retrieval event, not an observed flight '
                'trajectory. For each reference anchor, Q0 comprises the reference model’s '
                'Clean-correct queries. Rescue and new-failure rates have different denominators; '
                'net gain is (rescued CTEs − new failures) / |Q0|. The table reports percentages, '
                'averaging per-seed rates; CorrMean6 also averages six condition-specific rates. '
                'Counts and denominators for each seed and condition are retained in the CTE CSV.',
                '', '| Train → target | Anchor | Method | Condition | Rescue rate | New-failure rate | Net gain / Q0 |',
                '| --- | --- | --- | --- | ---: | ---: | ---: |'])
    events = rows('competitive_events.csv')
    for domain, target in DIRECTIONS:
        for anchor in ('ConGeo_clean', 'Base_clean'):
            for arm in METHODS:
                for condition in ('Snow', 'CorrMean6'):
                    subset = [r for r in events if r['train_domain'] == domain and r['target'] == target
                              and r['anchor'] == anchor and r['method'] == arm and r['condition'] == condition]
                    assert len(subset) == 2 and {r['seed'] for r in subset} == {'42', '43'}
                    values = []
                    for field in ('rescue_rate', 'new_failure_rate', 'net_trajectory_gain'):
                        both = [number(r[field]) for r in subset]
                        values.append(fmt(sum(both) / 2, 100) if all(map(math.isfinite, both)) else '—')
                    out.append('| ' + ' | '.join([f'{domain} → {target}', anchor, arm, condition, *values]) + ' |')

    out.extend(['', '## Suggested manuscript text', '',
                '**English.** We compared four selected, task-specific cross-domain augmentation '
                'adapters under the same ConGeo host, warmup and update budget. In this selected '
                'comparison, ConGeo-QView achieved the highest two-seed point estimates for Snow '
                'R@1 and CorrMean6 R@1/AP in all four train–test directions. It also had the lowest '
                'CorrMean6 distance and >200 m error among these references in the two directions '
                'with DenseUAV as the target. Several paired CorrMean6 R@1 intervals include zero; '
                'we therefore report the intervals and avoid treating every point-estimate ranking '
                'as a resolved difference. The adapters are controlled implementations, not complete '
                'reproductions of the original methods.',
                '',
                '**中文。** 我们在相同 ConGeo 宿主、warmup 和更新预算下，对四种选定的跨领域增强适配体进行受控比较。'
                '在这一选定对照集合中，ConGeo-QView 在四个训练—测试方向的 Snow R@1 和 CorrMean6 R@1/AP 双种子点估计最高；'
                '以 DenseUAV 为测试域的两个方向也具有最低的 CorrMean6 距离和大于 200 米错误率。部分 CorrMean6 R@1 '
                '配对区间跨零，因此同时报告区间，不能把每个点估计排序都解释为确定优势。各对照是受控适配体，'
                '并非原方法的完整复现。',
                '',
                '## Evidence and interpretation',
                '',
                '- Full per-condition and per-seed aggregates: [benchmark metrics](benchmark_metrics.csv).',
                '- Paired intervals: [bootstrap CSV](paired_bootstrap_ci.csv).',
                '- Competitive takeover event counts and rates: [CTE CSV](competitive_events.csv). '
                'CTE describes a retrieval competition event, not an observed flight trajectory; '
                'net gain must be interpreted with its reference anchor and denominator.',
                '- Operator-level source observations: [summary](operator_diagnostics.csv), '
                '[per-pair values](operator_diagnostics_per_pair.csv), '
                '[exploratory paired intervals](operator_diagnostics_paired_ci.csv).',
                '- [Training records](training_curves.csv), [checkpoint hashes](checkpoint_checksums.json), '
                '[evaluation hashes](evaluation_checksums.json), [smoke checks](smoke_verification.json), '
                '[operator equivalence checks](operator_code_equivalence.json), '
                '[data source verification](data_source_verification.json), and '
                '[selected protocol](selected_protocol.json).',
                '',
                'Data, image features, original per-query outputs and model/optimizer binaries are not '
                'included; recorded hashes identify the archived files. The released training entry point '
                'is a portable refactoring and has not been used to retrain these archived results.',
                ''])
    path = DATA / 'paper_section_and_tables.md'
    with path.open('w', encoding='utf8', newline='\n') as f:
        f.write('\n'.join(out))
    print(f'Rendered {path.relative_to(ROOT)} from selected aggregate CSVs.')


if __name__ == '__main__':
    main()
