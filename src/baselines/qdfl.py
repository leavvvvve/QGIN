"""Pinned official QDFL head and adapters; EVA token/rope interface adaptation."""
import torch,math
import torch.nn.functional as F
from .official import SOURCE,official
import ast,torch.nn as nn
def definitions(path,ns,selected=None):
 nodes=ast.parse(path.read_text()).body
 exec(compile(ast.Module(body=[n for n in nodes if isinstance(n,(ast.ClassDef,ast.FunctionDef)) and (selected is None or n.name in selected)],type_ignores=[]),str(path),'exec'),ns);return ns
class Serial(nn.Module):
 def __init__(self,original,adapter):super().__init__();self.original=original;self.adapter=adapter
 def forward(self,*a,**kw):return self.adapter(self.original(*a,**kw))
class Parallel(nn.Module):
 def __init__(self,original,adapter):super().__init__();self.original=original;self.adapter=adapter
 def forward(self,x):return self.original(x)+.2*self.adapter(x)
def enable_input_gradient(module,args,result):
 return result.requires_grad_(True) if torch.is_grad_enabled() and module.training else result
def build(encoder,classes):
 from einops import einops
 from torchvision.ops.deform_conv import deform_conv2d
 from torch.nn.modules.utils import _pair
 root=SOURCE/'QDFL'
 ns=definitions(root/'model/backbones/dinov2_backbone/block_adapter.py',dict(torch=torch,nn=nn),['Adapter']);Adapter=ns['Adapter']
 encoder.requires_grad_(False)
 for block in encoder.model.blocks:
  block.attn=Serial(block.attn,Adapter(768,mlp_ratio=.5))
  block.mlp=Parallel(block.mlp,Adapter(768,mlp_ratio=.5,skip_connect=False))
  # Parent DINO constructor calls init_weights_vit_timm on ALL Linear modules.
  for adapter in [block.attn.adapter,block.mlp.adapter]:
   for layer in adapter.modules():
    if isinstance(layer,nn.Linear):nn.init.trunc_normal_(layer.weight,std=.02);nn.init.zeros_(layer.bias)
 encoder.model.norm_pre.register_forward_hook(enable_input_gradient)
 ns=definitions(root/'model/components/QDFL.py',dict(torch=torch,nn=nn,F=F,math=math,einops=einops,Tensor=torch.Tensor,init=nn.init,_pair=_pair,deform_conv2d_tv=deform_conv2d))
 return ns['QDFL'](768,classes,True,dict(num_queries=8),2,return_f=True)
def loss(outputs,labels):
 from pytorch_metric_learning import losses,miners
 from pytorch_metric_learning.distances import DotProductSimilarity,CosineSimilarity
 cal=official('QDFL','utils/cal_loss.py');a,b=outputs
 ms=losses.MultiSimilarityLoss(alpha=5.,beta=100,base=.1,distance=DotProductSimilarity());miner=miners.MultiSimilarityMiner(epsilon=.4,distance=CosineSimilarity())
 ce=cal.cal_loss(a[0],labels,nn.CrossEntropyLoss())+cal.cal_loss(b[0],labels,nn.CrossEntropyLoss())
 contrast=cal.cal_MS_loss(a[1],b[1],labels,ms,miner)+cal.cal_MS_loss(b[1],a[1],labels,ms,miner)
 kl=.5*cal.cal_js_loss(a[0],b[0],nn.KLDivLoss(reduction='batchmean'))+.5*cal.cal_js_loss(b[0],a[0],nn.KLDivLoss(reduction='batchmean'))
 parts=dict(classification=ce,multi_similarity=contrast,kl=kl);return sum(parts.values()),parts
