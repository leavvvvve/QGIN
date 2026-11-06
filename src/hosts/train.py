"""Train from source-only fixed batch plans and cached augmentation parameters.

Run: python -m src.hosts.train --config configs_and_contracts/run.example.json
Paths in a run configuration refer to local data and user-owned checkpoints.
"""
import argparse, json, math, time
from pathlib import Path
import torch
from torch.utils.data import DataLoader
from .model import Model
from .optimizer import make_optimizer
from .objectives import objective
from . import replay, utils
from .data import Pairs
from .base_data import Pairs as BasePairs
from src.modules.augmentations import secondary


class Cache(torch.nn.Module):
    def __init__(self, model):
        super().__init__(); self.model = model
    def forward(self, img1):
        return self.model.cache_forward(img1)


def train_step(model, opt, views, labels, method):
    opt.zero_grad(set_to_none=True)
    cache_model = Cache(model)
    cached = [replay.cached(cache_model, x) for x in views]
    h = [v[0] for v in cached]
    loss, parts = objective(h, model, method, labels.cuda())
    assert torch.isfinite(loss)
    loss.backward()
    bn_counts = {n: b.num_batches_tracked.clone() for n, b in model.named_modules() if isinstance(b, torch.nn.modules.batchnorm._BatchNorm)}
    for view, (proxy, states) in zip(views, cached):
        replay.replay(cache_model, view, states, proxy.grad)
    for n, b in model.named_modules():
        if n in bn_counts:
            assert torch.equal(b.num_batches_tracked, bn_counts[n])
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters() if p.requires_grad)
    if model.method == 'Base':
        norm = torch.nn.utils.clip_grad_norm_(model.parameters(), 100.)
    else:
        norm = torch.nn.utils.clip_grad_norm_(model.parameters(), float('inf'))
        if model.method != 'QDFL':
            torch.nn.utils.clip_grad_value_(model.parameters(), 100.)
    opt.step()
    return dict(loss=float(loss.detach()), grad_norm=float(norm), **{k: float(v.detach()) for k, v in parts.items()})


def run(config):
    seed, method, host = config['seed'], config['method'], config['host']
    utils.system_seed(seed)
    model = Model(config['domain'], seed, host, config['warmup_model']).cuda().train()
    opt = make_optimizer(model, config['warmup_optimizer'])
    replay.CHUNK = config.get('chunk', 8)
    output = Path(config['output']); output.mkdir(parents=True, exist_ok=False)
    assert len(config['blocks']) == 6
    start = time.time(); count = 0
    for block, spec in enumerate(config['blocks'], 1):
        # A saved boundary RNG state reproduces a supplied source sampling plan.
        if spec.get('rng_state'):
            import random, numpy as np
            state = torch.load(spec['rng_state'], map_location='cpu', weights_only=False)
            random.setstate(state['python']); np.random.set_state(state['numpy'])
            torch.set_rng_state(state['cpu']); torch.cuda.set_rng_state_all(state['cuda'][:torch.cuda.device_count()])
        else:
            utils.system_seed(seed + block)
        plan = json.loads(Path(spec['plan']).read_text())
        rows, batches = plan['rows'], plan['batches']
        assert len(batches) == 108
        ds = BasePairs(rows, block, seed) if host == 'Base' else Pairs(rows, batches, config['domain'], seed, block, host)
        params = torch.load(spec['augmentation'], map_location='cpu', weights_only=True) if spec.get('augmentation') else None
        augmented = method in ['Base + QGIN','S4G-QDual','S4G-StdDual','ConGeo-QView','SinGeo-QView','FixedZeroHinge'] or any(x in method for x in ['StdDual','AugMix','ColorJitter'])
        assert (params is not None) == augmented, 'Method and augmentation file must agree'
        loader = DataLoader(ds, batch_sampler=batches, num_workers=config.get('workers', 8), pin_memory=True)
        for raw in loader:
            count += 1
            if host == 'Base':
                q, r, indices = raw; views = [q, r]
                labels = torch.tensor([rows[int(i)]['label'] for i in indices])
            else:
                views, labels, indices = raw; views = list(views)
            assert len(labels.unique()) == len(labels)
            if params is not None:
                view = 2 if host in ['ConGeo', 'SinGeo'] else 0
                aug = secondary(views[view], method, indices, params)
                if view == 0: views.append(aug)
                else: views[view] = aug
            lr = (1e-6 + .5*(1e-4-1e-6)*(1+math.cos(math.pi*(count-1)/647)) if host == 'Base'
                  else 1e-4*.5*(1+math.cos(math.pi*(count-1)/648)))
            if host == 'QDFL': lr = .03*min(1., count/175)*.5*(1+math.cos(math.pi*(count-1)/648))
            for group in opt.param_groups: group['lr'] = lr*group.get('ratio', 1.)
            rec = train_step(model, opt, views, labels, method)
            with (output/'training.jsonl').open('a') as f:
                f.write(json.dumps(dict(step=count, n=len(labels), lr=lr, **rec))+'\n')
    assert count == 648
    # Base exports keep the encoder checkpoint schema.
    state = model.encoder.state_dict() if host == 'Base' else model.state_dict()
    torch.save({k:v.detach().cpu() for k,v in state.items()}, output/'model.pth')
    torch.save(opt.state_dict(), output/'optimizer.pth')
    (output/'complete.json').write_text(json.dumps(dict(updates=count, seconds=time.time()-start,
        peak_allocated_bytes=torch.cuda.max_memory_allocated()), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--config', required=True)
    run(json.loads(Path(parser.parse_args().config).read_text()))
