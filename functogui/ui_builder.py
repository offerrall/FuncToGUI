from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from pathlib import Path

from .ui_types import inspect_params
from .properties import *

CURRENT_DIR = Path(__file__).parent.absolute()
KV_FILE = CURRENT_DIR / "styles.kv"
WINDOW_WIDTH = dp(400)
Builder.load_file(str(KV_FILE))

class MainLayout(BoxLayout):
    title = StringProperty("Function GUI")
    
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.function = function

        properties = inspect_params(function)
        name_function = function.__name__
        self.title = name_function.replace("_", " ").title()

        for prop in properties:
            type_propertie = properties[prop]["type"]
            constructor_values = properties[prop]["constructor_values"]
            default_params = properties[prop]["default_params"]

            if type_propertie == "int":
                values = {"name": prop.replace("_", " ").title()}
                
                for key, value in default_params.items():
                    values[key] = value["default"]

                for key, value in constructor_values.items():
                    values[key] = value

                self.ids.properties_layout.add_widget(CustomIntProperty(**values))

        empty_widget = Widget()
        self.ids.properties_layout.add_widget(empty_widget)

class App(KivyApp):
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.function = function

        Window.size = (WINDOW_WIDTH, Window.size[1])
        Window.minimum_width = WINDOW_WIDTH
        Window.maximum_width = WINDOW_WIDTH

    def build(self):
        return MainLayout(self.function)