import torch
import torch.nn.functional as F
from .official import official
def nce(a,b,scale):
 a=F.normalize(a.float(),dim=-1);b=F.normalize(b.float(),dim=-1);logits=scale*a@b.T;y=torch.arange(len(a),device=a.device)
 return .5*(F.cross_entropy(logits,y,label_smoothing=.1)+F.cross_entropy(logits.T,y,label_smoothing=.1))
def objective(h,m,labels=None):
 if m.method=='QDFL':
  from src.baselines.qdfl import loss
  return loss([m.head_forward(t) for t in h],labels)
 if m.method=='MRGeo':
  a,b=[m.head_forward(t) for t in h];logits=a@b.T/.07;y=torch.arange(len(a),device=a.device);l=.5*(F.cross_entropy(logits,y)+F.cross_entropy(logits.T,y));return l,dict(cross=l)
 scale=m.logit_scale.exp()
 if m.method=='Sample4Geo':scale=scale.clamp(max=100)
 if m.method in ['DAC','MEAN']:
  a,b=[m.head_forward(t) for t in h]
  local=official(m.method,'sample4geo/loss/'+('DSA_loss.py' if m.method=='DAC' else 'CDA_loss.py'))
  cls=getattr(local,'DSA_loss' if m.method=='DAC' else 'CDA_loss')(torch.nn.CrossEntropyLoss(),device='cuda')
  ce=sum(F.cross_entropy(x.float(),labels) for x in a[1])/len(a[1])+sum(F.cross_entropy(x.float(),labels) for x in b[1])/len(b[1])
  parts={'cross':nce(a[-2],b[-2],scale),'classification':.1*ce,'alignment':(.6 if m.method=='DAC' else .75)*cls(a[0].float(),b[0].float(),scale)}
  return sum(parts.values()),parts
 q,r=h[:2];parts={'cross':nce(q,r,scale)}
 if m.method=='ConGeo':
  qa,ra=h[2:];parts.update(query=.5*nce(qa,q,scale),satellite=.5*nce(ra,r,scale),aug_cross=.25*nce(qa,r,scale))
 if m.method=='SinGeo':
  qa,ra=h[2:];parts.update(query=.5*nce(qa,q,scale),satellite=.5*nce(ra,r,scale),cross_q=.25*nce(qa,r,scale),cross_r=.25*nce(q,ra,scale),cross_both=.25*nce(qa,ra,scale))
 return sum(parts.values()),parts
