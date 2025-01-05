from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from pathlib import Path

from .ui_types import inspect_params
from .properties import *

CURRENT_DIR = Path(__file__).parent.absolute()
KV_FILE = CURRENT_DIR / "styles.kv"

Builder.load_file(str(KV_FILE))

class MainLayout(BoxLayout):
    
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.function = function

        properties = inspect_params(function)

        for prop in properties:
            type_propertie = properties[prop]["type"]
            constructor_values = properties[prop]["constructor_values"]
            default_params = properties[prop]["default_params"]

            if type_propertie == "int":
                values = {"name": prop}
                
                for key, value in default_params.items():
                    values[key] = value["default"]
                
                print(values)

    

class App(KivyApp):

    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.function = function

    def build(self):
        return MainLayout(self.function)