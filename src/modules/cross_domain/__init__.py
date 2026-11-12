"""Four task-specific augmentation adapters with an isolated random stream."""
import hashlib
import torch

from .slaug import apply as slaug
from .pasta import apply as pasta
from .afa import apply as afa
from .raffesdg import apply as raffesdg

OPERATORS = {'SLAug': slaug, 'PASTA': pasta, 'AFA': afa, 'RaffeSDG': raffesdg}


def seed_for(base_seed, method, step, sample_index):
    """Derive the same stable per-sample seed as the completed experiment."""
    text = f'{base_seed}|exp003k_op|{method}|{step}|{sample_index}'
    return int.from_bytes(hashlib.sha256(text.encode()).digest()[:8], 'big') % (2**63-1)


@torch.no_grad()
def apply_normalized_batch(view, method, base_seed, step, indices, device):
    """Augment the normalized secondary query view; return a CPU batch."""
    assert method in OPERATORS and view.dtype == torch.float32 and view.ndim == 4
    assert len(view) == len(indices) and view.shape[1] == 3
    rgb = ((view.to(device, non_blocking=True) + 1.0) / 2.0).clamp(0, 1)
    outputs = []
    for x, index in zip(rgb, indices):
        gen = torch.Generator(device=device).manual_seed(seed_for(base_seed, method, step, int(index)))
        y = OPERATORS[method](x, gen)
        assert y.shape == x.shape and y.dtype == torch.float32 and y.device == x.device
        outputs.append(y.nan_to_num(nan=0, posinf=1, neginf=0).clamp(0, 1))
    out = (torch.stack(outputs) * 2 - 1).cpu()
    assert torch.isfinite(out).all() and out.min() >= -1 and out.max() <= 1
    return out
