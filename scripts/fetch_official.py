"""Fetch pinned third-party sources outside the distributable tree."""
import argparse,json,subprocess
from pathlib import Path

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',default='external');a=p.parse_args()
    root=Path(a.root);root.mkdir(parents=True,exist_ok=True)
    for f in sorted(Path('configs_and_contracts').glob('*.json')):
        c=json.loads(f.read_text())
        if 'url' not in c or 'commit' not in c:continue
        dest=root/f.stem
        if not dest.exists():subprocess.run(['git','clone','--no-checkout',c['url'],str(dest)],check=True)
        subprocess.run(['git','-C',str(dest),'checkout','--detach',c['commit']],check=True)
        actual=subprocess.check_output(['git','-C',str(dest),'rev-parse','HEAD'],text=True).strip()
        assert actual==c['commit']
        print(f.stem,actual)
