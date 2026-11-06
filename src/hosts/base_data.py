"""Base paired resize, shared flip and independent affine photometry."""
import numpy as np
import torch
import cv2
from torch.utils.data import Dataset
from .utils import seed_hash
def image_read(path):
    im=cv2.imread(str(path))
    if im is None:raise RuntimeError('Cannot decode '+str(path))
    return cv2.resize(cv2.cvtColor(im,cv2.COLOR_BGR2RGB),(384,384),interpolation=cv2.INTER_LINEAR_EXACT)
def tensor_image(im):return torch.from_numpy(((im.astype(np.float32)/255.-.5)/.5).transpose(2,0,1).copy())
class Pairs(Dataset):
    def __init__(self,rows,epoch,seed):self.rows=rows;self.epoch=epoch;self.seed=seed
    def __len__(self):return len(self.rows)
    def __getitem__(self,i):
        item=self.rows[i];q=image_read(item['query_path']);r=image_read(item['reference_path'])
        rng=np.random.default_rng(seed_hash(f"{item['query_id']}:aug:{self.epoch}",self.seed))
        if rng.random()<.5:q=q[:,::-1].copy();r=r[:,::-1].copy()
        for im in [q,r]:
            if rng.random()<.5:
                contrast=rng.uniform(.85,1.15);brightness=rng.uniform(-.15,.15)*255
                im[:]=np.clip(im.astype(float)*contrast+brightness,0,255).astype(np.uint8)
        return tensor_image(q),tensor_image(r),i
