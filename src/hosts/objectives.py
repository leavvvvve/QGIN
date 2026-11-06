"""Paired host objectives used for the QGIN comparisons."""
import torch
import torch.nn.functional as F
from .soft_targets import soft_parts
from src.baselines.objectives import nce, objective as baseline_objective


def base_loss(q, r, labels):
    q, r = F.normalize(q.float(), dim=-1), F.normalize(r.float(), dim=-1)
    invalid = (labels[:, None] == labels[None, :]) & ~torch.eye(len(labels), device=q.device, dtype=torch.bool)
    return soft_parts(q @ r.T / .07, invalid, torch.full((len(q),), .908, device=q.device))[0].mean()


def objective(features, model, method, labels):
    if model.method == 'Base':
        clean = base_loss(features[0], features[1], labels)
        if len(features) == 2:
            return clean, {'clean': clean}
        aug = base_loss(features[2], features[1], labels)
        return .5 * (clean + aug), {'clean': .5 * clean, 'augmented': .5 * aug}
    if method in ['S4G-QDual', 'S4G-StdDual']:
        scale = model.logit_scale.exp().clamp(max=100)
        clean = .5 * nce(features[0], features[1], scale)
        aug = .5 * nce(features[2], features[1], scale)
        return clean + aug, {'clean': clean, 'augmented': aug}
    return baseline_objective(features, model, labels)
