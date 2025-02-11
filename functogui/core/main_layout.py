from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock

from .inspect_fuction import *
from ..ui_widgets import *

from ..ui_widgets import PROPERTY_TYPES
from ..return_widgets import StrReturn, ImageFileReturn

class MainLayout(BoxLayout):
    title = StringProperty("Function GUI")
    error_message = StringProperty("")
    auto_update = BooleanProperty(True)
    
    def __init__(self, function: callable, width: int = 350, **kwargs):
        """
        Create the main layout of the app with the properties and result widgets.
        """
        super().__init__(**kwargs)
        self.function = function
        self.user_max_width = width
        self.return_type = get_return_type_name(function)
        
        self._create_properties(inspect_params(function))
        
        if self.auto_update:
            self.remove_widget(self.ids.apply_function_button_layout)
            Clock.schedule_once(self.calculate_function, 0.1)
            print("Auto update is on")
            return
        
        self.ids.result_layout_container.opacity = 0.5

    def has_any_errors(self):
        """
        Check if any property widget has an error.
        """
        for prop in self.ids.properties_layout.children:
            if prop.error:
                return True
        return False

    def apply_function_button(self):
        """
        Apply the function with the current properties and update the result.
        """
        self.calculate_function()

    def calculate_function(self, *_):
        """
        Calculate the function with the current properties and update the result.
        Only executes if no properties have errors.
        """
        if self.has_any_errors():
            self.error_message = "Cannot execute while there are validation errors"
            for type in basic_return_types:
                if self.return_type == type:
                    self.ids.result_layout.children[0].text = f"Error: {self.error_message}"
            return

        props = {prop.name.lower().replace(" ", "_"): prop.value 
                for prop in self.ids.properties_layout.children}
        
        try:
            self.error_message = ""
            result = self.function(**props)
            self.ids.result_layout_container.opacity = 1
        except Exception as e:
            self.error_message = str(e)

        for type in basic_return_types:
            if self.return_type == type:
                if not self.error_message:
                    self.ids.result_layout.children[0].text = str(result)
                else:
                    self.ids.result_layout.children[0].text = f"Error: {self.error_message}"
        
        if self.return_type == "imageFileReturn":
            self.ids.result_layout.children[0].image_path = result
            self.ids.result_layout.children[0].ids.image.reload()

    def _create_properties(self, properties: dict):
        """
        Create the properties widgets based on the function parameters.
        """
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
        """
        if not self.auto_update:
            return
        Clock.unschedule(self.calculate_function)
        Clock.schedule_once(self.calculate_function, 0.03)
    
    def _ajust_size(self, *_):
        """
        Adjust the size of the window based on the properties and result widgets.
        """
        total = 0
        total += self.padding[1] + self.padding[3]
        total += (self.ids.properties_label.height * 2)
        total += self.ids.title_label.height
        total += self.ids.result_layout.height
        total += self.ids.properties_layout.height

        if not self.auto_update:
            total += dp(50)

        max_width = dp(self.user_max_width)

        Window.size = (max_width, total)