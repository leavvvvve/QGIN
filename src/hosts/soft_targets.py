"""Allowed-candidate bidirectional soft-target CE; no outer row weighting."""
import torch
import torch.nn.functional as F

def soft_parts(logits,invalid,alpha):
    invalid=torch.as_tensor(invalid,device=logits.device,dtype=torch.bool)
    alpha=torch.as_tensor(alpha,device=logits.device,dtype=logits.dtype).detach()
    allowed=~invalid;krow=allowed.sum(1);kcol=allowed.sum(0)
    assert torch.all(krow>0) and torch.all(kcol>0) and not torch.diag(invalid).any()
    a=logits.masked_fill(invalid,float('-inf'))
    lpr=F.log_softmax(a,dim=1);lpc=F.log_softmax(a,dim=0)
    uniform_row=-lpr.masked_fill(invalid,0).sum(1)/krow
    uniform_col=-lpc.masked_fill(invalid,0).sum(0)/kcol
    row=alpha*(-lpr.diag())+(1-alpha)*uniform_row
    col=alpha*(-lpc.diag())+(1-alpha)*uniform_col
    return .5*(row+col),dict(krow=krow,kcol=kcol,diag_target_row=alpha+(1-alpha)/krow,diag_target_col=alpha+(1-alpha)/kcol)

def targets(invalid,alpha):
    allowed=(~invalid).to(alpha.dtype);n=len(alpha);eye=torch.eye(n,device=alpha.device,dtype=alpha.dtype)
    row=alpha[:,None]*eye+(1-alpha[:,None])*allowed/allowed.sum(1)[:,None]
    col=alpha[None,:]*eye+(1-alpha[None,:])*allowed/allowed.sum(0)[None,:]
    return row,col
