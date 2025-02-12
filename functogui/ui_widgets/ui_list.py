from kivy.properties import StringProperty, ListProperty
from .ui_base import CustomProperty


class CustomListProperty(CustomProperty):
    value = StringProperty("")
    values = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_kv_post(self, base_widget):
        self.ids.list_spinner.text = self.value
    
    def set_property_value(self, value):
        self.value = value
        self.ids.list_spinner.text = str(value)

        if self.value_changed_callback:
            self.value_changed_callback()