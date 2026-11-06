import unittest
import numpy as np
import torch
from src.modules.qgin import sample, network, augment_batch
from src.hosts.objectives import base_loss
from src.baselines.objectives import nce
from src.evaluation.statistics import bootstrap_weights, summarize, interval
from src.evaluation.metrics import haversine_m, official_ap_from_rank


class CoreTests(unittest.TestCase):
    def test_qgin_rng_and_spatial_permutation(self):
        torch.manual_seed(42)
        x=torch.rand(1,3,24,24)*2-1; before=torch.get_rng_state().clone()
        p,q=sample(8,9); y=augment_batch(x,[p],[q])
        self.assertTrue(torch.equal(before,torch.get_rng_state()))
        perm=torch.arange(24*24-1,-1,-1)
        xp=x.flatten(2)[:,:,perm].reshape_as(x)
        yp=augment_batch(xp,[p],[q]).flatten(2)
        self.assertTrue(torch.allclose(yp,y.flatten(2)[:,:,perm],atol=1e-6))
        self.assertEqual(y.dtype,torch.float32)
        self.assertLessEqual(float(y.abs().max()),1.)

    def test_constant_and_identity_fallback(self):
        p,q=sample(8,9)
        y,_,r=network(torch.zeros(1,3,12,12),p,q,True)
        self.assertTrue(torch.isfinite(y).all()); self.assertEqual(r['channel_fallback'],6)
        p['layers'][-1]=(torch.zeros_like(p['layers'][-1][0]),torch.zeros_like(p['layers'][-1][1]))
        x=torch.randn(1,3,12,12).clamp(-1,1)
        y,_,r=network(x,p,q)
        self.assertTrue(torch.equal(x,y));self.assertEqual(r['identity_fallback'],1)

    def test_base_label_smoothing_equivalence_and_gradients(self):
        torch.manual_seed(12)
        q=torch.randn(7,13,requires_grad=True);r=torch.randn(7,13,requires_grad=True)
        x=base_loss(q,r,torch.arange(7))
        a,b=[torch.nn.functional.normalize(z,dim=-1) for z in (q,r)]
        logits=a@b.T/.07;y=torch.arange(7)
        expected=.5*(torch.nn.functional.cross_entropy(logits,y,label_smoothing=.092)+torch.nn.functional.cross_entropy(logits.T,y,label_smoothing=.092))
        gx=torch.autograd.grad(x,(q,r),retain_graph=True);gy=torch.autograd.grad(expected,(q,r))
        self.assertTrue(torch.allclose(x,expected,atol=1e-6))
        for a,b in zip(gx,gy):self.assertTrue(torch.allclose(a,b,atol=1e-6))

    def test_bootstrap_pair_identity_and_metrics(self):
        a=np.array([[0.,2.],[1.,4.],[1.,6.]])
        w=bootstrap_weights(3);p,s=summarize(a,w)
        np.testing.assert_allclose(p,a.mean(0));np.testing.assert_allclose(s-s,0)
        self.assertEqual(interval((s-s)[:,0]),(0.,0.))
        self.assertAlmostEqual(float(haversine_m([0,0],[0,0])),0.)
        self.assertAlmostEqual(float(haversine_m([0,0],[1,0])),111319.49079327357,places=6)
        self.assertAlmostEqual(official_ap_from_rank(np.arange(4),np.array([0,2])),.7916666666666666)


if __name__=='__main__':unittest.main()
