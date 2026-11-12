"""Export the four selected EXP-003K adapters from the archived experiment.

The archival source directory is supplied by the user and is never modified.
This exporter preserves all digits from the recorded CSVs.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'paper_assets' / 'exp003k'
METHODS = ('SLAug', 'PASTA', 'AFA', 'RaffeSDG')
ARMS = {'ConGeo', 'ConGeo-QView', *METHODS}
CONDITIONS = ('Clean', 'Fog', 'Snow', 'Blur', 'Gamma', 'ExposureClip', 'Posterize4')


def read_json(path):
    return json.loads(path.read_text(encoding='utf8'))


def write_json(path, data):
    with path.open('w', encoding='utf8', newline='\n') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def filtered_csv(source, target, predicate):
    with source.open(encoding='utf8', newline='') as src:
        reader = csv.DictReader(src)
        rows = [row for row in reader if predicate(row)]
        fields = reader.fieldnames
    assert fields and rows, source
    with target.open('w', encoding='utf8', newline='') as dst:
        writer = csv.DictWriter(dst, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    return rows


def export(source):
    OUT.mkdir(parents=True, exist_ok=True)
    source = source.resolve()
    assert source != OUT.resolve()
    selected = lambda row: row['method'] in ARMS
    bench = filtered_csv(source / 'benchmark_metrics.csv', OUT / 'benchmark_metrics.csv', selected)
    paired = filtered_csv(source / 'paired_bootstrap_ci.csv', OUT / 'paired_bootstrap_ci.csv',
                          lambda row: row['reference'] in {'ConGeo', *METHODS})
    cte = filtered_csv(source / 'cte_trajectory_summary.csv', OUT / 'competitive_events.csv', selected)
    ops = {'QGIN', *METHODS}
    diag = filtered_csv(source / 'operator_mechanism_diagnostics.csv', OUT / 'operator_diagnostics.csv',
                        lambda row: row['method'] in ops)
    pairs = filtered_csv(source / 'operator_mechanism_per_pair.csv', OUT / 'operator_diagnostics_per_pair.csv',
                         lambda row: row['method'] in ops)
    filtered_csv(source / 'operator_diagnostics_paired_ci.csv', OUT / 'operator_diagnostics_paired_ci.csv',
                 lambda row: row['method'] == 'QGIN' and row['reference'] in METHODS)
    assert len(bench) == 4 * 6 * 3 * 9
    assert len(diag) == 5 and len(pairs) == 5 * 128
    assert set(row['reference'] for row in paired) == {'ConGeo', *METHODS}
    assert set(row['method'] for row in cte) == ARMS

    training = read_json(source / 'training_verification.json')
    evaluation = read_json(source / 'evaluation_verification.json')
    receipt = read_json(source / 'local_delivery_receipt.json')
    assert training['complete'] and evaluation['complete'] and receipt['complete']
    models = []
    training_rows = []
    training_fields = None
    for item in training['models']:
        if item['method'] not in METHODS:
            continue
        method, domain, seed = item['method'], item['domain'], int(item['seed'])
        assert item['updates'] == 648
        name = f'{method}_{domain}_s{seed}'
        saved = receipt['models'][name]
        assert saved['model_sha256'] == item['model_sha256']
        assert saved['optimizer_sha256'] == item['optimizer_sha256']
        models.append({key: item[key] for key in
                       ('method', 'domain', 'seed', 'updates', 'model_sha256', 'optimizer_sha256', 'all_attempt_rows')})
        with (source / 'checkpoints' / name / 'train_metrics.csv').open(encoding='utf8', newline='') as f:
            reader = csv.DictReader(f)
            fields = [k for k in reader.fieldnames if k != 'run_id']
            if training_fields is None:
                training_fields = ['method', 'domain', 'seed'] + fields
            assert training_fields == ['method', 'domain', 'seed'] + fields
            rows = list(reader)
        assert [int(row['step']) for row in rows] == list(range(1, 649))
        assert all(int(row['nan_inf_count']) == 0 for row in rows)
        for row in rows:
            training_rows.append({'method': method, 'domain': domain, 'seed': seed,
                                  **{k: row[k] for k in fields}})
    assert len(models) == 16 and len(training_rows) == 16 * 648
    with (OUT / 'training_curves.csv').open('w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=training_fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(training_rows)
    write_json(OUT / 'checkpoint_checksums.json', {'models': models})

    records = [{key: item[key] for key in
                ('method', 'domain', 'target', 'seed', 'checkpoint_sha256', 'gallery_sha256', 'retrieval_sha256')}
               for item in evaluation['records'] if item['method'] in METHODS]
    assert len(records) == 32
    write_json(OUT / 'evaluation_checksums.json', {'selected_model_target_evaluations': len(records),
               'conditions_per_evaluation': 7, 'records': records})

    smoke = read_json(source / 'smoke_verification.json')
    smokes = [record for record in smoke['smoke_records'] if record['method'] in METHODS]
    assert smoke['passed'] and len(smokes) == 8 and all(record['passed'] for record in smokes)
    write_json(OUT / 'smoke_verification.json', {'selected_smokes': len(smokes), 'records': smokes})

    source_audit = read_json(source / 'upstream_source_audit.json')
    pins = [record for record in source_audit['sources'] if record['method'].split('/')[0] in METHODS]
    assert len(pins) == 4
    write_json(OUT / 'source_provenance.json', {'audit_date': source_audit['audit_date'], 'sources': pins})

    lock = read_json(source / 'protocol_lock.json')
    operator_sha = {name: lock['code_sha256'][f'operators/{name.lower()}.py'] for name in METHODS}
    for name, expected in operator_sha.items():
        assert digest(ROOT / 'src/modules/cross_domain' / f'{name.lower()}.py') == expected
    protocol = {key: lock[key] for key in ('experiment', 'created_utc', 'taskbook_sha256', 'datasets',
               'seeds', 'actual_host_loss', 'rng', 'replay_chunk', 'effective_batch',
               'checkpoint_rule', 'eval_conditions', 'bootstrap')}
    protocol.update(selected_adaptations=list(METHODS), selected_formal_models=16,
                    selected_training_updates=16 * 648, selected_model_target_evaluations=32,
                    selected_condition_combinations=32 * 7, operator_code_sha256=operator_sha)
    assert protocol['eval_conditions'] == list(CONDITIONS)
    write_json(OUT / 'selected_protocol.json', protocol)
    print(f'Exported {len(models)} models, {len(records)} evaluation groups, '
          f'{len(training_rows)} training records and {len(pairs)} diagnostic pairs.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='archived experiment output directory')
    export(parser.parse_args().source)


if __name__ == '__main__':
    main()
