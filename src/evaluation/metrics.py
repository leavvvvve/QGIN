"""Official DenseUAV AP/SDM compatibility plus genuine geographic Top1 error."""
import numpy as np
def haversine_m(query_lonlat,gallery_lonlat):
    q=np.asarray(query_lonlat,dtype=np.float64);g=np.asarray(gallery_lonlat,dtype=np.float64)
    qlon,qlat=np.deg2rad(q[...,0]),np.deg2rad(q[...,1]);glon,glat=np.deg2rad(g[...,0]),np.deg2rad(g[...,1])
    a=np.sin((glat-qlat)/2)**2+np.cos(qlat)*np.cos(glat)*np.sin((glon-qlon)/2)**2
    return 2*6378137.*np.arcsin(np.sqrt(np.clip(a,0,1)))
def official_ap_from_rank(index,good_indices):
    rows=np.flatnonzero(np.isin(index,good_indices));n=len(good_indices)
    if n==0:return float('nan')
    i=np.arange(n,dtype=float);precision=(i+1)/(rows+1);old=np.ones(n);nz=rows!=0;old[nz]=i[nz]/rows[nz]
    return float(np.sum((old+precision)/(2*n)))
def sdm_official(query_lonlat,gallery_lonlat,k):
    # Match official float32 coordinates and squared-degree norm, while using
    # exp(-x) to avoid the original exp(x) overflow for distant candidates.
    q=np.asarray(query_lonlat,np.float32);g=np.asarray(gallery_lonlat[:k],np.float32);d=np.sqrt(np.sum((g-q)**2,axis=1,dtype=np.float32));w=1-np.arange(k)/k
    return float(np.sum(np.exp(-d*5e3)*w)/w.sum())
def one_query(scores,label,gallery_labels,query_lonlat,gallery_lonlat):
    index=np.argsort(scores)[::-1];good=np.flatnonzero(gallery_labels==label);assert len(good)==6
    top=index[:10];coords=gallery_lonlat[top]
    neg=np.flatnonzero(gallery_labels!=label);posmax=float(scores[good].max());negmax=float(scores[neg].max());hardneg=int(neg[np.argmax(scores[neg])])
    result=dict(r1=int(gallery_labels[top[0]]==label),r5=int(np.any(gallery_labels[top[:5]]==label)),ap=official_ap_from_rank(index,good),
        dis1_m=float(haversine_m(query_lonlat,coords[0])),coordinates_valid=1,positive_n=len(good),top1_gallery_index=int(top[0]))
    result.update(max_positive_similarity=posmax,max_negative_similarity=negmax,pos_neg_margin=posmax-negmax,hard_negative_distance_m=float(haversine_m(query_lonlat,gallery_lonlat[hardneg])))
    for k in [1,3,5,10]:result[f'sdm{k}']=sdm_official(query_lonlat,coords,k)
    return result
