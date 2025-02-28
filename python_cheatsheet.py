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

# zamiast uruchomienia skryptu pokaż config
python my_script.py --cfg [job|hydra|all] --resolve

# popraw ścieżki importów (toporne, ale działa):
PYTHONPATH=. python3 my_script.py

# ładnie wypisz config:
from omegaconf import OmegaConf
print(OmegaConf.to_yaml(cfg, resolve=True))

# dodanie własnego resolvera
from omegaconf import OmegaConf
# to może żyć gdziekolwiek, ale musi być zaimportowane przed użyciem @hydra.main
OmegaConf.register_new_resolver("code_const", lambda x: globals()[x])  # to wrzuca stałe
# przykład importu w skrypcie
import lib.crawler  # noqa: F401  # for the resolver
# tak wygląda użycie w configu
positive_key_words: ${code_const:EXTENDED_POSITIVE_KWS}

# wewnątrz configu

# @package bond.james   # where to put the whole config
defaults:  # everything that's not explicitly defined but still gets combined
    - other/config/file  # to import another config
    - random_config@new_config.new_key  # to place it somewhere else
    - override other/db: mysql  # change selection of variants
    - _self_  # sets priority of this file (last = most important)
debug: True  # contents of _self_
db:  # adds or overwrites just these fields (configs will be merged)
    host: backup

# wiele uruchomień (sweeper)
# więcej o dostępnych funkcjach: https://hydra.cc/docs/advanced/override_grammar/extended/#sweeps
# dodaj w głównym configu
hydra:
  mode: MULTIRUN
  sweeper:
    params:
      model.params.n_clusters: range(3, 8)
      data: glob(*,exclude=support)


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


# autoreload w notatniku:
%load_ext autoreload
%autoreload 2


# pandas wyświetlenie całej tabali:
with (pd.option_context(
    'display.max_rows', None,
    'display.max_columns', None,
    'display.max_colwidth', None,
    'display.max_seq_items', None,
)):
    display(df)

# pandas podejrzenie ustawień wyświetlania:
pd.describe_option('display')

# schowanie pandasowego SettingWithCopyWarning
with pd.option_context('mode.chained_assignment','warn'):

# schowanie warningów w notebooku:
with warnings.catch_warnings(record=True) as caught_warnings:


# Time profiler for python:
from pyinstrument import Profiler
from pyinstrument.renderers import HTMLRenderer
profiler = Profiler()
profiler.start()
# slow code goes here
profiler.stop()
profiler_session = profiler.last_session
HTMLRenderer().open_in_browser(profiler_session, output_filename="./profiler_output.html")


# debug
w notebooku:
    %debug  # trzeba użyć q  wychodząc, bo inaczej stracę focus jądra
puść skrypt i wejdź w tryb debug przy błędzie:
    python -m pdb my_script.py
    # domyślnie zatrzymuje się przy rozpoczęciu wykonywania wejścia
    # żeby zatrzymał się dopiero przy błędzie:
    python -m pdb -c continue my_script.py
ustaw breakpoint:
    import pdb; pdb.set_trace()
post mortem w interaktywnej konsoli pythona:
    import pdb; pdb.pm()
komendy:
    c(ont(inue)) – Continue execution
    n(ext) – Step to the next line
    s(tep) – Step into a function call
    p var – Print the value of a variable
    q(uit) – Exit and abort program
    d(own) – move down in the stack trace
    u(p) – move up in the stack trace
    h(elp) – list available commands

