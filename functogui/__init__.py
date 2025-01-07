from platform import system

sistem = system()

if sistem == 'Windows' or sistem == 'Linux' or sistem == 'Darwin':
    from kivy.config import Config
    Config.set('graphics', 'resizable', False)

from .ui_widgets import *
from .ui_types import *
from .app_builder import App