"""Clean-correct competitive takeover events and paired recovery counts."""
import numpy as np
import pandas as pd
from .statistics import bootstrap_weights,ratio_bootstrap,interval


def decompose(reference, candidate, draws=2000):
    q0=set(reference.loc[(reference.condition=='Clean')&(reference.r1==1),'query_id'])
    keys=['query_id','condition']
    x=reference.merge(candidate,on=keys,suffixes=('_ref','_new'),validate='one_to_one')
    assert len(x)==len(reference)==len(candidate)
    ids=sorted(reference.location_id.unique());w=bootstrap_weights(len(ids),draws)
    rows=[]
    for c,z in x[x.query_id.isin(q0)].groupby('condition'):
        takeover=(z.m_old_loc_ref>1e-6)&(z.m_all_ref< -1e-6)
        correct=z.m_all_ref>1e-6
        metrics={'rescue':(takeover&(z.m_all_new>1e-6),takeover),
                 'new_failure':(correct&(z.r1_new==0),correct)}
        if 'dis1_m_ref' in z:
            far=takeover&(z.dis1_m_ref>200)
            metrics['far200_removed']=(far&(z.dis1_m_new<=200),far)
        for name,(num,den) in metrics.items():
            a=pd.DataFrame({'id':z.location_id_ref,'num':num.astype(int),'den':den.astype(int)}).groupby('id')[['num','den']].sum().reindex(ids,fill_value=0)
            value,bs=ratio_bootstrap(a.num.to_numpy(),a.den.to_numpy(),w);lo,hi=interval(bs)
            rows.append(dict(condition=c,metric=name,value=value,ci_low=lo,ci_high=hi,numerator=int(num.sum()),denominator=int(den.sum()),Q0_n=len(q0)))
    return pd.DataFrame(rows)
