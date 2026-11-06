"""Check source syntax, publication scope and aggregate-output hashes."""
from pathlib import Path
import ast,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
BLOCKED={'.pth','.pt','.ckpt','.bin','.safetensors','.zip','.tar','.npy','.npz','.h5','.log'}

def main():
    count=0
    for p in ROOT.rglob('*'):
        if not p.is_file() or set(p.parts)&{'.git','external','__pycache__','.venv'}:continue
        if set(p.relative_to(ROOT).parts)&{'data','checkpoints','outputs'}:continue
        assert p.suffix not in BLOCKED,p
        assert p.stat().st_size<50*1024**2,p
        if p.suffix=='.py':ast.parse(p.read_text(encoding='utf-8'))
        count+=1
    manifest=(ROOT/'paper_assets/FILE_MANIFEST.md').read_text(encoding='utf-8')
    hashes=re.findall(r'\| `(paper_assets/summary_csv/[^`]+)` \| `([0-9a-f]{64})` \|',manifest)
    for path,digest in hashes:
        h=hashlib.sha256()
        with (ROOT/path).open('rb') as f:
            for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
        actual=h.hexdigest()
        assert actual==digest,path
    print(f'PASS: {count} publication files; {len(hashes)} aggregate hashes')

if __name__=='__main__':main()
