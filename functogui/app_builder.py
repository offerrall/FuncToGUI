from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from pathlib import Path

from .ui_types import inspect_params, get_return_type_name
from .ui_widgets import *

Builder.load_file(str(Path(__file__).parent / "styles.kv"))
simple_types = ["strReturn", "intReturn", "boolReturn"]
all_types = simple_types + ["imageFileReturn"]

class MainLayout(BoxLayout):
    title = StringProperty("Function GUI")
    
    def __init__(self,
                 function,
                 width: int = 350,
                 **kwargs):
        super().__init__(**kwargs)
        self.function = function
        self.user_max_width = width
        self.title = "  " + function.__name__.replace("_", " ").title()
        self.return_type = get_return_type_name(function)
        if self.return_type not in all_types:
            raise TypeError(f"Return type must be one of {all_types}")
        
        self._create_properties(inspect_params(function))
        Clock.schedule_once(self.calculate_function, 0.1)

    def calculate_function(self, *_):
        props = {prop.name.lower().replace(" ", "_"): prop.value 
                for prop in self.ids.properties_layout.children}
        result = self.function(**props)

        for type in simple_types:
            if self.return_type == type:
                self.ids.result_layout.children[0].text = str(result)
        
        if self.return_type == "imageFileReturn":
            self.ids.result_layout.children[0].image_path = result
            self.ids.result_layout.children[0].ids.image.reload()

    def _create_properties(self, properties):
        PROPERTY_TYPES = {
            "strUi": CustomStrProperty,
            "intUi": CustomIntProperty,
            "boolUi": CustomBoolProperty,
            "listUi": CustomListProperty,
            "fileUi": CustomFileProperty
        }
        
        for prop_name, prop_info in properties.items():
            values = {
                "name": prop_name.replace("_", " ").title(),
                **{k: v["default"] for k, v in prop_info["default_params"].items()},
                **prop_info["constructor_values"]
            }
            
            prop = PROPERTY_TYPES[prop_info["default_class"]](**values)
            prop.value_changed_callback = lambda *_: self._schedule_calculation()
            self.ids.properties_layout.add_widget(prop)
        
        for type in simple_types:
            if self.return_type == type:
                self.ids.result_layout.add_widget(StrReturn())
        
        if self.return_type == "imageFileReturn":
            self.ids.result_layout.add_widget(ImageFileReturn())

        Clock.schedule_once(self._ajust_size)
    
    def _schedule_calculation(self):
        Clock.unschedule(self.calculate_function)
        Clock.schedule_once(self.calculate_function, 0.03)
    
    def _ajust_size(self, *_):
        total = 0
        total += self.padding[1] + self.padding[3]
        total += (self.ids.properties_label.height * 2)
        total += self.ids.title_label.height
        total += self.ids.result_layout.height
        total += self.ids.properties_layout.height
        max_width = dp(self.user_max_width)

        Window.size = (max_width, total)

class App(KivyApp):
    def __init__(self,
                 function: callable,
                 width: int = 350,
                 **kwargs):
        super().__init__(**kwargs)
        self.function = function
        self.user_max_width = width
        self.run()

    def build(self):
        main_layout = MainLayout(self.function, width=self.user_max_width)
        return main_layout