"""Runtime adapter for pinned DAC and MEAN source definitions."""
import torch,numpy as np
import torch.nn.functional as F
from .official import SOURCE,official
import ast,torch.nn as nn
class Features(nn.Module):
 def forward(self,pair):return pair
def handcrafted(method,classes):
 path=SOURCE/method/'sample4geo/hand_convnext/ConvNext/make_model.py'
 nodes=ast.parse(path.read_text()).body
 module=ast.Module(body=[z for z in nodes if isinstance(z,(ast.ClassDef,ast.FunctionDef))],type_ignores=[])
 ns=dict(torch=torch,nn=nn,F=F,np=np,Variable=torch.autograd.Variable,Parameter=nn.Parameter,init=official(method,'sample4geo/Utils/init.py'),create_model=lambda *a,**kw:Features())
 exec(compile(module,str(path),'exec'),ns)
 head=ns['build_convnext'](classes,block=2,return_f=True,resnet=False)
 if method=='DAC':
  # This module is allocated by official code but never called in forward.
  head.proj_obj.requires_grad_(False)
 return head
