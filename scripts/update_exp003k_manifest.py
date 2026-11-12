"""Refresh the selected-experiment checksums and repository file index."""
import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN = '<!-- EXP003K HASHES BEGIN -->'
END = '<!-- EXP003K HASHES END -->'


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main():
    manifest = ROOT / 'paper_assets/FILE_MANIFEST.md'
    paths = sorted(path for path in (ROOT / 'paper_assets/exp003k').iterdir() if path.is_file())
    section = [BEGIN, '## EXP-003K selected comparison output hashes', '',
               'The selected results are derived from the archived experiment; source-cell and '
               'operator equivalence checks are included in the selection directory.', '',
               '| File | SHA256 |', '|---|---|']
    section += [f'| `{p.relative_to(ROOT).as_posix()}` | `{sha256(p)}` |' for p in paths]
    section += [END]
    text = manifest.read_text(encoding='utf8')
    if BEGIN in text:
        assert text.count(BEGIN) == text.count(END) == 1
        left, rest = text.split(BEGIN, 1)
        _, right = rest.split(END, 1)
        text = left + '\n'.join(section) + right
    else:
        text = text.rstrip() + '\n\n' + '\n'.join(section) + '\n'
    with manifest.open('w', encoding='utf8', newline='\n') as f:
        f.write(text)

    names = subprocess.check_output(['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'],
                                    cwd=ROOT).decode('utf8').split('\0')
    names = sorted(name for name in names if name and (ROOT / name).is_file())
    assert len(names) == len(set(names))
    with (ROOT / 'paper_assets/FILE_TREE.txt').open('w', encoding='utf8', newline='\n') as f:
        f.write('\n'.join(names) + '\n')
    print(f'Updated {len(paths)} selected asset hashes and the {len(names)}-file index.')


if __name__ == '__main__':
    main()
