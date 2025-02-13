from platform import system
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')

if system() in ['Windows', 'Linux', 'Darwin']:
    Config.set('graphics', 'resizable', False)

from kivy.lang import Builder
from pathlib import Path

from .ui_widgets import *
from .core.ui_types import *
from .core.app import App

from .styles import *

for kv in ['styles', 'main', 'ui_widgets', 'return']:
    Builder.load_file(str(Path(__file__).parent / f"{kv}.kv"))