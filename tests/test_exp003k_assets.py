import csv
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'paper_assets' / 'exp003k'
ARMS = {'ConGeo', 'ConGeo-QView', 'SLAug', 'PASTA', 'AFA', 'RaffeSDG'}
ADAPTERS = {'SLAug', 'PASTA', 'AFA', 'RaffeSDG'}


def read_csv(name):
    with (DATA / name).open(encoding='utf8', newline='') as f:
        return list(csv.DictReader(f))


class PublishedExperimentTests(unittest.TestCase):
    def test_metric_grid_and_missing_geolocation(self):
        rows = read_csv('benchmark_metrics.csv')
        self.assertEqual(len(rows), 4 * 6 * 3 * 9)
        keys = {(r['train_domain'], r['target'], r['method'], r['seed'], r['condition']) for r in rows}
        self.assertEqual(len(keys), len(rows))
        self.assertEqual({r['method'] for r in rows}, ARMS)
        self.assertEqual({r['seed'] for r in rows}, {'42', '43', 'mean42_43'})
        for row in rows:
            self.assertTrue(0 <= float(row['r1']) <= 1)
            if row['target'] == 'sues':
                self.assertEqual(row['dis1_m'], '')
                self.assertEqual(row['error_gt200m'], '')
        for domain in ('dense', 'sues'):
            for target in ('dense', 'sues'):
                for method in ARMS:
                    for condition in ('Snow', 'CorrMean6'):
                        selected = [r for r in rows if r['train_domain'] == domain and r['target'] == target
                                    and r['method'] == method and r['condition'] == condition]
                        mean = next(float(r['r1']) for r in selected if r['seed'] == 'mean42_43')
                        seeds = [float(r['r1']) for r in selected if r['seed'] in ('42', '43')]
                        self.assertEqual(len(seeds), 2)
                        self.assertTrue(math.isclose(mean, sum(seeds) / 2, abs_tol=1e-12))

    def test_checksum_ledger_and_training_records(self):
        model = json.loads((DATA / 'checkpoint_checksums.json').read_text(encoding='utf8'))['models']
        evaluation = json.loads((DATA / 'evaluation_checksums.json').read_text(encoding='utf8'))['records']
        self.assertEqual(len(model), 16)
        self.assertEqual(len(evaluation), 32)
        indexed = {(r['method'], r['domain'], int(r['seed'])): r for r in model}
        self.assertEqual(len(indexed), 16)
        self.assertEqual({r['method'] for r in model}, ADAPTERS)
        for r in evaluation:
            expected = indexed[r['method'], r['domain'], int(r['seed'])]
            self.assertEqual(r['checkpoint_sha256'], expected['model_sha256'])
            self.assertEqual(len(r['retrieval_sha256']), 64)
            self.assertEqual(len(r['gallery_sha256']), 64)
        curves = read_csv('training_curves.csv')
        self.assertEqual(len(curves), 16 * 648)
        grouped = {}
        for r in curves:
            grouped.setdefault((r['method'], r['domain'], int(r['seed'])), []).append(int(r['step']))
            self.assertEqual(int(r['nan_inf_count']), 0)
            self.assertTrue(math.isfinite(float(r['loss'])))
        self.assertEqual(set(grouped), set(indexed))
        for steps in grouped.values():
            self.assertEqual(steps, list(range(1, 649)))

    def test_diagnostics_and_intervals(self):
        pairs = read_csv('operator_diagnostics_per_pair.csv')
        self.assertEqual(len(pairs), 5 * 128)
        for method in ADAPTERS | {'QGIN'}:
            r = [x for x in pairs if x['method'] == method]
            self.assertEqual(len(r), 128)
            self.assertEqual(len({x['image_index'] for x in r}), 32)
            self.assertEqual({x['group'] for x in r}, {'0', '1', '2', '3'})
        intervals = read_csv('paired_bootstrap_ci.csv')
        self.assertEqual({r['reference'] for r in intervals}, ADAPTERS | {'ConGeo'})
        for row in intervals:
            self.assertLessEqual(float(row['ci_low']), float(row['ci_high']))
            self.assertEqual(int(row['resamples']), 2000)


if __name__ == '__main__':
    unittest.main()
