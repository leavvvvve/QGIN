"""Official host transformations, shared paired RNG and secondary-view sampling."""
import torch,numpy as np
from src.baselines.official import SOURCE,official
from src.hosts import utils as base
import random,cv2,ast,albumentations as alb
from albumentations.pytorch import ToTensorV2
from torch.utils.data import Dataset
class Pairs(Dataset):
 def __init__(self,rows,batches,domain,seed,block,method):
  self.rows=rows;self.seed=seed;self.block=block;self.method=method
  ids=sorted({str(r['location_id']) for r in rows});self.labels={k:i for i,k in enumerate(ids)}
  assert len(ids)==(2256 if domain=='dense' else 120)
  self.groups={k:sorted({r['query_path'] for r in rows if str(r['location_id'])==k}) for k in ids}
  self.steps={i:(block-1)*108+bi+1 for bi,b in enumerate(batches) for i in b}
  # Official University transformations, with the common EVA normalization.
  if method in ['DAC','MEAN','QDFL']:
   path=SOURCE/('DAC' if method=='QDFL' else method)/'sample4geo/dataset/university.py';nodes=ast.parse(path.read_text()).body
   ns=dict(A=alb,cv2=cv2,ToTensorV2=ToTensorV2)
   exec(compile(ast.Module(body=[z for z in nodes if isinstance(z,ast.FunctionDef) and z.name=='get_transforms'],type_ignores=[]),str(path),'exec'),ns)
   _,self.sat,self.drone=ns['get_transforms']((384,384),mean=[.5]*3,std=[.5]*3)
  elif method=='SinGeo':
   mod=official('SinGeo','singeo/dataset/university.py')
   _,self.sat,_,self.drone,self.drone2=mod.get_transforms_singeo_university((384,384),mean=[.5]*3,std=[.5]*3)
  else:
   mod=official('ConGeo','ConGeo/congeo/dataset/university.py') if method=='ConGeo' else official('Sample4Geo','sample4geo/dataset/university.py')
   _,self.sat,self.drone=mod.get_transforms((384,384),mean=[.5]*3,std=[.5]*3)
 def __len__(self):return len(self.rows)
 def __getitem__(self,i):
  row=self.rows[i];key=str(row['location_id']);seed=base.seed_hash(f'{self.method}:{self.block}:{i}',self.seed)
  random.seed(seed);np.random.seed(seed)
  def image(p):
   z=cv2.imread(str(p));assert z is not None,p;return cv2.cvtColor(z,cv2.COLOR_BGR2RGB)
  q=image(row['query_path']);r=image(row['reference_path']);flip=(np.random.random()<.5) if self.method!='QDFL' else False
  if flip:q=cv2.flip(q,1);r=cv2.flip(r,1)
  views=[self.drone(image=q)['image'],self.sat(image=r)['image']]
  if self.method in ['ConGeo','SinGeo']:
   candidates=[p for p in self.groups[key] if p!=row['query_path']];assert candidates
   q2=image(random.choice(candidates));q2=cv2.flip(q2,1) if flip else q2
   r2=r.copy()
   if self.method=='SinGeo':
    # Official base satellite view has no rotation; task overrides secondary
    # keep-probability/angles with explicit rotation probability and 3 angles.
    sat2=alb.Compose([z for z in self.sat.transforms if not isinstance(z,alb.RandomRotate90)])
    if random.random()<.75*self.steps[i]/648:r2=np.ascontiguousarray(np.rot90(r2,random.choice([1,2,3])))
    views.extend([self.drone2(image=q2)['image'],sat2(image=r2)['image']])
   else:views.extend([self.drone(image=q2)['image'],self.sat(image=r2)['image']])
  return tuple(views),self.labels[key],i
