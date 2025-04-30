# run ipython profile create to create the default file
# it's located at ~/.ipython/profile_default/ipython_config.py

# used options only

## lines of code to run at IPython startup.
#  Default: []
import datetime

log_file = f"notebooks/{datetime.datetime.now().strftime('%Y-%m-%d')}-log.py"
c.InteractiveShellApp.exec_lines = [
    "%load_ext autoreload",
    "%autoreload 2",
    f"%logstart {log_file} append",
]

## Automatically add/delete closing bracket or quote when opening bracket or
#  quote is entered/deleted. Brackets: (), [], {} Quotes: '', ""
#  Default: False
c.TerminalInteractiveShell.auto_match = True

## Autoformatter to reformat Terminal code. Can be `'black'`, `'yapf'` or `None`
#  Default: None
c.TerminalInteractiveShell.autoformatter

## Set the color scheme (NoColor, Neutral, Linux, or LightBG).
#  See also: InteractiveShell.colors
c.TerminalInteractiveShell.colors = "Linux"
