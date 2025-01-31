from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from pathlib import Path

from .inspect_fuction import inspect_params, get_return_type_name
from .ui_widgets import *

Builder.load_file(str(Path(__file__).parent / "styles.kv"))
basic_return_types = ["strReturn", "intReturn", "boolReturn", "floatReturn"]

class MainLayout(BoxLayout):
    title = StringProperty("Function GUI")
    
    def __init__(self, function, width: int = 350, **kwargs):
        """
        Create the main layout of the app with the properties and result widgets.
        """
        super().__init__(**kwargs)
        self.function = function
        self.user_max_width = width
        self.return_type = get_return_type_name(function)
        
        self._create_properties(inspect_params(function))
        Clock.schedule_once(self.calculate_function, 0.1)

    def calculate_function(self, *_):
        """
        Calculate the function with the current properties and update the result.
        """
        props = {prop.name.lower().replace(" ", "_"): prop.value 
                for prop in self.ids.properties_layout.children}
        result = self.function(**props)

        for type in basic_return_types:
            if self.return_type == type:
                self.ids.result_layout.children[0].text = str(result)
        
        if self.return_type == "imageFileReturn":
            self.ids.result_layout.children[0].image_path = result
            self.ids.result_layout.children[0].ids.image.reload()

    def _create_properties(self, properties):
        """
        Create the properties widgets based on the function parameters.
        """
        PROPERTY_TYPES = {
            "strUi": CustomStrProperty,
            "intUi": CustomIntProperty,
            "boolUi": CustomBoolProperty,
            "listUi": CustomListProperty,
            "fileUi": CustomFileProperty,
            "floatUi": CustomFloatProperty,
            "colorUi": CustomColorProperty,
            "folderUi": CustomFolderProperty
        }
        
        for prop_name, prop_info in properties.items():
            values = {
                "name": prop_name.replace("_", " ").title(),
                "value": prop_info["default"],
                **prop_info["options"]
            }
            
            prop = PROPERTY_TYPES[prop_info["ui_type"]](**values)
            prop.value_changed_callback = self._schedule_calculation
            self.ids.properties_layout.add_widget(prop)
        
        for type in basic_return_types:
            if self.return_type == type:
                self.ids.result_layout.add_widget(StrReturn())
        
        if self.return_type == "imageFileReturn":
            self.ids.result_layout.add_widget(ImageFileReturn())

        Clock.schedule_once(self._ajust_size)
    
    def _schedule_calculation(self):
        """
        Schedule the calculation of the function with the current properties.
        This is used to avoid calling the function too many times when the user is changing the properties.
        """
        Clock.unschedule(self.calculate_function)
        Clock.schedule_once(self.calculate_function, 0.03)
    
    def _ajust_size(self, *_):
        """
        Ajust the size of the window based on the properties and result widgets.
        """
        total = 0
        total += self.padding[1] + self.padding[3]
        total += (self.ids.properties_label.height * 2)
        total += self.ids.title_label.height
        total += self.ids.result_layout.height
        total += self.ids.properties_layout.height
        max_width = dp(self.user_max_width)

        Window.size = (max_width, total)

class App(KivyApp):
    """
    Create a Kivy app with a GUI for a given type-annotated function.
    """
    def __init__(self,
                 function: callable,
                 width: int = 350,
                 **kwargs):
        super().__init__(**kwargs)
        self.function = function
        self.user_max_width = width
        self.title = "  " + function.__name__.replace("_", " ").title()
        self.run()

    def build(self):
        """
        Create the main layout of the app.
        """
        main_layout = MainLayout(self.function, width=self.user_max_width, title=self.title)
        return main_layout