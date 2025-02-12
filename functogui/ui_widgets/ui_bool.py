from kivy.properties import BooleanProperty
from .ui_base import CustomProperty


class CustomBoolProperty(CustomProperty):
    value = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_kv_post(self, base_widget):
        self.ids.bool_switch.active = self.value
    
    def set_property_value(self, value):
        self.value = value
        self.ids.bool_switch.active = value

        if self.value_changed_callback:
            self.value_changed_callback()