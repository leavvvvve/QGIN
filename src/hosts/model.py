import math
import torch
from torch import nn
import torch.nn.functional as F
import timm
MODEL='vit_base_patch16_rope_reg1_gap_256.sbb_in1k'

class Encoder(nn.Module):
    def __init__(self,checkpoint=None):
        super().__init__()
        self.model=timm.create_model(MODEL,pretrained=False,img_size=384,num_classes=0)
        self.logit_scale=nn.Parameter(torch.tensor(math.log(1/.07)))
        assert self.model.patch_embed.num_patches==576 and self.model.num_prefix_tokens==1
        if checkpoint:
            state=torch.load(checkpoint,map_location='cpu',weights_only=False)
            self.load_state_dict(state.get('model',state),strict=True)
    def forward(self,img1):return self.model(img1)
    def set_grad_checkpointing(self,enabled=True):self.model.set_grad_checkpointing(enabled)

class Model(nn.Module):
 def __init__(self,domain,seed,method,warmup=None):
  super().__init__();self.method=method;self.encoder=Encoder(warmup);self.encoder.logit_scale.requires_grad_(True)
  self.encoder.logit_scale.data.fill_(math.log(1/.07));self.encoder.set_grad_checkpointing(True)
  self.head=None;self.adapt=None
  if method in ['DAC','MEAN']:
   from src.baselines.heads import handcrafted
   self.head=handcrafted(method,2256 if domain=='dense' else 120)
   if method=='DAC':self.adapt=nn.Conv2d(768,1024,1)
  elif method=='QDFL':
   from src.baselines.qdfl import build
   self.head=build(self.encoder,2256 if domain=='dense' else 120)
  elif method=='MRGeo':
   from src.baselines.mrgeo import MRGeo
   self.head=MRGeo();self.encoder.logit_scale.requires_grad_(False)
  elif method not in ['Base','Sample4Geo','ConGeo','SinGeo']:raise NotImplementedError(method)
  if method=='Base':self.encoder.logit_scale.requires_grad_(False)
 @property
 def logit_scale(self):return self.encoder.logit_scale
 def head_forward(self,tokens):
  if self.method=='MRGeo':return self.head(self.encoder.model.fc_norm(tokens[:,1:]))
  gap=self.encoder.model.forward_head(tokens);spatial=tokens[:,1:].transpose(1,2).reshape(-1,768,24,24)
  if self.adapt is not None:
   spatial=self.adapt(spatial);gap=F.linear(gap,self.adapt.weight[:,:,0,0],self.adapt.bias)
  if self.method=='QDFL':
   with torch.autocast('cuda',enabled=False):return self.head((gap.float(),spatial.float()))
  return self.head((gap,spatial))
 def forward(self,img1):
  if self.head is None:return self.encoder(img1=img1)
  result=self.head_forward(self.encoder.model.forward_features(img1))
  if self.training or self.method=='MRGeo':return result
  if self.method=='QDFL':return result.flatten(1)
  return result[-2]
 def cache_forward(self,x):return self.encoder.model.forward_features(x) if self.head is not None else self.forward(x)
