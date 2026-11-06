"""Paper reimplementation, not official code. See the MRGeo contract for the fixed implementation choices."""
import torch
import torch.nn.functional as F
import torch.nn as nn
class MRGeo(nn.Module):
 def __init__(self):
  super().__init__();self.global_qkv=nn.Linear(768,2304,bias=False);self.local_qkv=nn.Linear(768,2304,bias=False);self.gate=nn.Linear(1536,768);self.projection=nn.Linear(768,768);self.channel_conv=nn.Conv1d(1,1,3,padding=1);self.channel_linear=nn.Linear(768,768);self.alpha=nn.Parameter(torch.tensor(.001))
  xy=torch.stack(torch.meshgrid(torch.arange(24),torch.arange(24),indexing='ij'),-1).reshape(-1,2);mask=(xy[:,None]-xy[None,:]).abs().amax(-1)<=1;self.register_buffer('local_mask',mask)
 def forward(self,x):
  q,k,v=self.global_qkv(x).chunk(3,-1);global_=F.scaled_dot_product_attention(q[:,None],k[:,None],v[:,None]).squeeze(1)
  q,k,v=self.local_qkv(x).chunk(3,-1);local=F.scaled_dot_product_attention(q[:,None],k[:,None],v[:,None],attn_mask=self.local_mask).squeeze(1)
  merged=global_+torch.sigmoid(self.gate(torch.cat([global_,local],-1)))*local
  f=merged.mean(1);fh=self.channel_conv(f[:,None]).squeeze(1);fl=self.channel_linear(f)
  correction=fh*fl.sum(-1,keepdim=True)+fl*fh.sum(-1,keepdim=True)
  out=self.projection(merged)+self.alpha*correction[:,None,:]
  regions=F.adaptive_avg_pool2d(out.transpose(1,2).reshape(-1,768,24,24),(2,2)).flatten(2).transpose(1,2).flatten(1)
  return F.normalize(regions,dim=-1)
