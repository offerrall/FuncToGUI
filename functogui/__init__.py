from platform import system
from kivy.lang import Builder
from pathlib import Path
from kivy.config import Config
from .ui_widgets import *
from .core.ui_types import *
from .core.app_builder import App

if system() in ['Windows', 'Linux', 'Darwin']:
    Config.set('graphics', 'resizable', False)

for kv in ['main', 'ui_widgets', 'return']:
    Builder.load_file(str(Path(__file__).parent / f"{kv}.kv"))