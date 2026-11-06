import hashlib,random
import numpy as np
import torch
def seed_hash(text,seed=42):return int(hashlib.sha256(f'{seed}:{text}'.encode()).hexdigest()[:8],16)
def system_seed(seed):
    random.seed(seed);np.random.seed(seed);torch.manual_seed(seed);torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark=False;torch.backends.cudnn.deterministic=True
    torch.backends.cuda.matmul.allow_tf32=False
