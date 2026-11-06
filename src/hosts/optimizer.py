"""Name-and-shape restoration of the shared 108-update Adam state."""
import torch
from .model import Encoder


def make_optimizer(model, warmup_optimizer):
    if model.method == 'QDFL':
        return torch.optim.SGD([
            dict(params=[p for p in model.encoder.parameters() if p.requires_grad], lr=.009, ratio=.3),
            dict(params=[p for p in model.head.parameters() if p.requires_grad], lr=.03, ratio=1.)],
            momentum=.9, weight_decay=.0005, nesterov=True)
    shared = [(n, p) for n, p in model.encoder.named_parameters() if n != 'logit_scale' and p.requires_grad]
    shared_ids = {id(p) for _, p in shared}
    new = [p for p in model.parameters() if p.requires_grad and id(p) not in shared_ids]
    groups = [dict(params=[p for _, p in shared])]
    if new:
        groups.append(dict(params=new))
    opt = torch.optim.AdamW(groups, lr=1e-4, weight_decay=.01)
    old = torch.load(warmup_optimizer, map_location='cpu', weights_only=False)
    proto = Encoder()
    names = [(n, list(p.shape)) for n, p in proto.named_parameters() if n != 'logit_scale']
    ids = old['param_groups'][0]['params']
    assert len(ids) == len(names) == len(shared) == 185
    states = {name: (shape, old['state'][pid]) for (name, shape), pid in zip(names, ids)}
    for name, p in shared:
        shape, state = states[name]
        assert shape == list(p.shape) and float(state['step']) == 108
        assert state['exp_avg'].shape == state['exp_avg_sq'].shape == p.shape
        opt.state[p] = {k: v.clone().to(p.device) if torch.is_tensor(v) and k != 'step' else v.clone() if torch.is_tensor(v) else v for k, v in state.items()}
    return opt
