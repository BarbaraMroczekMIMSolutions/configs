# pathlib

from pathlib import Path
wd = Path('.')

## iteracje

for file in wd.iterdir:
    pass
for file in wd.glob("*"):
    pass
for file in wd.rglob("*"):
    pass

## sprawdzenia

wd.is_dir() == True
wd.exists() == True
wd.mkdir(parents=True, exist_ok=True)

## części ścieżki

p = Path("/usr/bin/python3")
p.parts == ('/', 'usr', 'bin', 'python3')
p.parent == Path("/usr/bin")
p.parents ==  # TODO
p.parents[1] == Path("/usr")
p.root == "/"

import shutil
shutil.copyfile(src, dst)

# pickle

import pickle

a = {'hello': 'world'}

with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)

# notebooks

import os
while "notebooks" in os.getcwd():
    os.chdir("..")


# formatowanie wypisywania liczb:

f"{i:03d}"  # wypisz na 3 cyfrach inta d
f"{i:.3f}"  # wypisz 3 cyfry po przecinku


# hydra

# załadowanie configu poza skryptem
from hydra import compose, initialize
from omegaconf import OmegaConf

with initialize(version_base=None, config_path="conf", job_name="test_app"):
    cfg = compose(config_name="config", overrides=["db=mysql", "db.user=me"])

print(OmegaConf.to_yaml(cfg))

# zmień config podczas odpalenia skryptu:
python my_script.py --config-name "new_name" --config-path "new_path"

# popraw ścieżki importów (toporne, ale działa):
PYTHONPATH=. python3 my_script.py

# ładnie wypisz config:
from omegaconf import OmegaConf
print(OmegaConf.to_yaml(cfg, resolve=True))


# obliczenia dni roboczych
## kiedy minie okres
import pandas as pd
holidays = ['2024-12-25', '2025-01-01']  # use GPT
start_date = pd.Timestamp('2024-12-19')
end_date = start_date + pd.offsets.CustomBusinessDay(n=10, holidays=holidays)
print("Time limit ends on:", end_date.date())
## ile dni w okresie
custom_business_day = pd.offsets.CustomBusinessDay(holidays=holidays)
business_days = pd.date_range(start=start_date, end=end_date, freq=custom_business_day)
count = len(business_days)
print("Number of business days:", count)
