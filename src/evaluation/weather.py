"""Native-resolution deterministic weather, followed by 384-square resize."""
import random
import numpy as np
import cv2
import torch
import albumentations as A
from src.hosts.utils import seed_hash
CONDITIONS = ['Clean','Fog','Snow','Blur','Gamma','ExposureClip','Posterize4']


def transform(rgb, condition, query_id):
    if condition not in CONDITIONS:
        raise ValueError(condition)
    if condition == 'Clean': return rgb.copy()
    if condition == 'Gamma': return (rgb.astype(np.float32)/255)**np.float32(.5)
    if condition == 'ExposureClip': return np.clip(rgb.astype(np.float32)/255*1.8, 0, 1)
    if condition == 'Posterize4': return rgb & np.uint8(240)
    state = random.getstate(), np.random.get_state()
    try:
        seed = seed_hash(query_id+':'+condition)
        random.seed(seed); np.random.seed(seed)
        if condition == 'Fog':
            return A.RandomFog(fog_coef_lower=.3, fog_coef_upper=.3, alpha_coef=.08, p=1)(image=rgb)['image']
        if condition == 'Snow':
            return A.RandomSnow(snow_point_lower=.2, snow_point_upper=.2, brightness_coeff=2.5, p=1)(image=rgb)['image']
        kernel = np.zeros((9,9),np.float32); kernel[4,:] = 1/9
        return cv2.filter2D(rgb,-1,kernel,borderType=cv2.BORDER_REFLECT_101)
    finally:
        random.setstate(state[0]); np.random.set_state(state[1])


def read_image(path, condition, query_id):
    im = cv2.imread(str(path))
    if im is None: raise RuntimeError(f'Cannot decode {path}')
    im = transform(cv2.cvtColor(im,cv2.COLOR_BGR2RGB),condition,query_id)
    im = cv2.resize(im,(384,384),interpolation=cv2.INTER_LINEAR_EXACT)
    if im.dtype == np.uint8: im = im.astype(np.float32)/255
    return torch.from_numpy(((im-.5)/.5).transpose(2,0,1).copy())
