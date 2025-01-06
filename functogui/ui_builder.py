from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from pathlib import Path

from .ui_types import inspect_params
from .properties import *

Builder.load_file(str(Path(__file__).parent / "styles.kv"))
WINDOW_WIDTH = dp(400)

class MainLayout(BoxLayout):
    title = StringProperty("Function GUI")
    
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.function = function
        self.title = "  " + function.__name__.replace("_", " ").title()
        
        self._create_properties(inspect_params(function))
        Clock.schedule_once(self.calculate_function, 0.1)
    
    def _create_properties(self, properties):
        PROPERTY_TYPES = {
            "int": CustomIntProperty,
            "str": CustomStrProperty,
            "bool": CustomBoolProperty
        }
        
        for prop_name, prop_info in properties.items():
            values = {
                "name": prop_name.replace("_", " ").title(),
                **{k: v["default"] for k, v in prop_info["default_params"].items()},
                **prop_info["constructor_values"]
            }
            
            prop = PROPERTY_TYPES[prop_info["type"]](**values)
            prop.value_changed_callback = lambda *_: self._schedule_calculation()
            self.ids.properties_layout.add_widget(prop)
    
    def _schedule_calculation(self):
        Clock.unschedule(self.calculate_function)
        Clock.schedule_once(self.calculate_function, 0.1)

    def calculate_function(self, *_):
        props = {prop.name.lower().replace(" ", "_"): prop.value 
                for prop in self.ids.properties_layout.children}
        result = self.function(**props)
        self.ids.result_layout.clear_widgets()
        self.ids.result_layout.add_widget(Label(text=str(result)))

class App(KivyApp):
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.function = function
        for dim in ['minimum_width', 'maximum_width', 'size']:
            setattr(Window, dim, (WINDOW_WIDTH, Window.size[1]) if dim == 'size' else WINDOW_WIDTH)
        self.run()

    def build(self):
        return MainLayout(self.function)