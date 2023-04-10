from pathlib import Path

cwd = Path.cwd()

DATA = cwd / 'Monofasica' / 'data'


def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

rm_tree(DATA)