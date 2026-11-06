"""Regenerate benchmark endpoints from user-supplied per-query CSV paths.

Input JSON: [{direction, method, seed, path}], seeds 42 and 43.
python -m src.evaluation.summarize inputs.json output.csv
"""
import json,sys
import numpy as np
import pandas as pd
from .statistics import bootstrap_weights,interval
CONDITIONS=['Clean','Fog','Snow','Blur','Gamma','ExposureClip','Posterize4']
METRICS=['r1','r5','ap','sdm3','dis1_m','error_gt200m','worst_height_r1']


def estimate(df):
    d=df.copy()
    if 'height_tag' in d:d['height']=d.height_tag
    if 'error_gt200m' not in d and 'dis1_m' in d:d['error_gt200m']=(d.dis1_m>200).astype(float)
    d['location_id']=d.location_id.astype(int)
    ids=sorted(d.location_id.unique());heights=sorted(d.height.unique())
    assert not d.duplicated(['condition','query_id']).any()
    assert set(d.condition)==set(CONDITIONS)
    assert d.groupby(['condition','location_id','height']).size().nunique()==1
    cols=[m for m in METRICS[:-1] if m in d]
    g=d.groupby(['location_id','condition','height'])[cols].mean()
    g=g.reindex(pd.MultiIndex.from_product([ids,CONDITIONS,heights],names=['location_id','condition','height']))
    arr=np.full((len(ids),7,len(heights),6),np.nan)
    for j,c in enumerate(cols):arr[:,:,:,METRICS.index(c)]=g.to_numpy().reshape(len(ids),7,len(heights),len(cols))[:,:,:,j]
    arr=np.concatenate([arr,arr[:,1:].mean(1,keepdims=True),arr[:,[1,3,4,5,6]].mean(1,keepdims=True)],axis=1)
    w=bootstrap_weights(len(ids));a=arr.mean(2).reshape(len(ids),-1)
    score=a.mean(0).reshape(9,6);bs=(w@a).reshape(2000,9,6)
    h=arr[:,:,:,0];worst=h.mean(0).min(-1)
    wh=(w@h.reshape(len(ids),-1)).reshape(2000,9,len(heights)).min(-1)
    return ids,np.column_stack([score,worst]),np.concatenate([bs,wh[:,:,None]],axis=-1)


def main(inputs,output):
    cache={};rows=[]
    def append(direction,method,seed,p,b):
        for i,c in enumerate(CONDITIONS+['CorrMean6','NonSnowMean5']):
            for j,m in enumerate(METRICS):
                lo,hi=interval(b[:,i,j]);scale=1 if m=='dis1_m' else 100
                rows.append(dict(direction=direction,method=method,seed=seed,condition=c,metric=m,value=p[i,j]*scale,ci_low=lo*scale,ci_high=hi*scale))
    for item in inputs:
        key=item['direction'],item['method'],int(item['seed'])
        cache[key]=estimate(pd.read_csv(item['path']))
        append(*key,*cache[key][1:])
    for direction,method in sorted({k[:2] for k in cache}):
        a,b=[cache[direction,method,s] for s in [42,43]];assert a[0]==b[0]
        append(direction,method,'mean',(a[1]+b[1])/2,(a[2]+b[2])/2)
    pd.DataFrame(rows).to_csv(output,index=False,float_format='%.12g')


if __name__=='__main__':main(json.load(open(sys.argv[1])),sys.argv[2])
