# pathlib

from pathlib import Path

wd = Path('.')

# iteracje

for file in wd.iterdir:
    pass

for file in wd.glob("*"):
    pass

for file in wd.rglob("*"):
    pass

# sprawdzenia

wd.is_dir() == True

wd.exists() == True

wd.mkdir(parents=True, exist_ok=True)

# części ścieżki

p = Path("/usr/bin/python3")

p.parts == ('/', 'usr', 'bin', 'python3')

p.parent == Path("/usr/bin")

p.parents ==  # TODO
p.parents[1] == Path("/usr")

p.root == "/"


import shutil

shutil.copyfile(src, dst)

