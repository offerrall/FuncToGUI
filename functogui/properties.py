from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CustomProperty(BoxLayout):
    name = StringProperty("Property")
    value_changed_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CustomIntProperty(CustomProperty):
    int_value = NumericProperty(0)
    min_value = NumericProperty(-1000000000000)
    max_value = NumericProperty(1000000000000)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.ids.int_textinput.text = str(self.int_value)
        self.ids.int_slider.value = self.int_value

    def set_property_value(self, value):
        try:
            if value == "":
                return
            
            value = int(value)
            value = max(self.min_value, min(value, self.max_value))
            
            self.ids.int_textinput.text = str(value)
            self.ids.int_slider.value = value
        except ValueError:
            pass