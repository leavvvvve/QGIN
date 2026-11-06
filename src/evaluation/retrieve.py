"""Full-gallery evaluation in any source-to-target direction.

Manifest: {queries: [{path,query_id,label,location_id,height,gps?}], gallery: [...]}
gps entries use {longitude,latitude}. The target manifest selects the evaluation
domain; a checkpoint is loaded once and is never updated by this program.
"""
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from src.hosts.model import Model
from .weather import CONDITIONS, read_image
from .metrics import one_query, official_ap_from_rank


class Images(Dataset):
    def __init__(self, items, condition): self.items,self.condition=items,condition
    def __len__(self): return len(self.items)
    def __getitem__(self,i):
        r=self.items[i]; return read_image(r['path'],self.condition,r['query_id'])


@torch.inference_mode()
def extract(model,items,condition,batch=16,workers=4):
    model.eval(); arrays=[]
    for x in DataLoader(Images(items,condition),batch_size=batch,num_workers=workers):
        x=x.cuda()
        with torch.autocast('cuda',dtype=torch.float16):
            h=model(img1=x).float()+model(img1=x.flip([3])).float()
        arrays.append(F.normalize(h,dim=-1).cpu().numpy())
    result=np.concatenate(arrays); assert np.isfinite(result).all()
    return result


def score(query,gallery,clean,queries,galleries,target,condition):
    gl=np.array([r['label'] for r in galleries]); records=[]
    gps=np.array([[r['gps']['longitude'],r['gps']['latitude']] for r in galleries]) if target=='dense' else None
    bank=torch.tensor(gallery,device='cuda')
    for start in range(0,len(query),128):
        scores=(torch.tensor(query[start:start+128],device='cuda')@bank.T).cpu().numpy()
        clean_scores=(torch.tensor(clean[start:start+128],device='cuda')@bank.T).cpu().numpy()
        for j,(s,cs) in enumerate(zip(scores,clean_scores)):
            item=queries[start+j]; same=gl==item['label']; good=np.flatnonzero(same)
            assert len(good)==(6 if target=='dense' else 1)
            order=np.argsort(s)[::-1];oldneg=int(np.where(same,-np.inf,cs).argmax())
            newneg=int(np.where(same,-np.inf,s).argmax());positive=float(s[same].max())
            oldloc=gl==gl[oldneg];oldmargin=positive-float(s[oldloc].max())
            if target=='dense':
                r=one_query(s,item['label'],gl,[item['gps']['longitude'],item['gps']['latitude']],gps)
                r.pop('top1_gallery_index');r['error_gt200m']=int(r['dis1_m']>200)
            else:
                rank=int(np.flatnonzero(same[order])[0])+1
                r=dict(r1=int(rank==1),r5=int(rank<=5),ap=1/rank,
                       ap_official_trapezoidal=official_ap_from_rank(order,good))
            r.update(condition=condition,query_id=item['query_id'],location_id=item['location_id'],height=item.get('height',item.get('height_tag')),
                m_all=positive-float(s[newneg]),m_old_loc=oldmargin,m_old_img=positive-float(s[oldneg]),
                clean_correct=int(gl[cs.argmax()]==item['label']),negative_location_switched=int(gl[newneg]!=gl[oldneg]),
                top1_location=gl[order[0]])
            records.append(r)
    return records


def main(args):
    manifest=json.loads(Path(args.manifest).read_text()); model=Model(args.train_domain,42,args.host)
    state=torch.load(args.checkpoint,map_location='cpu',weights_only=False)
    (model.encoder if args.host=='Base' else model).load_state_dict(state,strict=True)
    model.cuda().eval()
    g=extract(model,manifest['gallery'],'Clean',args.batch,args.workers)
    clean=extract(model,manifest['queries'],'Clean',args.batch,args.workers); rows=[]
    for c in CONDITIONS:
        q=clean if c=='Clean' else extract(model,manifest['queries'],c,args.batch,args.workers)
        rows+=score(q,g,clean,manifest['queries'],manifest['gallery'],args.target,c)
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    pd.DataFrame(rows).to_csv(args.output,index=False)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    for key in ['manifest','checkpoint','host','train-domain','target','output']:p.add_argument('--'+key,required=True)
    p.add_argument('--batch',type=int,default=16);p.add_argument('--workers',type=int,default=4)
    main(p.parse_args())
