from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CustomProperty(BoxLayout):
    name = StringProperty("Property")
    value_changed_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CustomIntProperty(CustomProperty):
    value = NumericProperty(0)
    min_value = NumericProperty(0)
    max_value = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.ids.int_textinput.text = str(self.value)
        self.ids.int_slider.value = self.value

    def set_property_value(self, value):
        try:
            if value == "":
                return
            
            value = int(value)
            value = max(self.min_value, min(value, self.max_value))
            
            self.ids.int_textinput.text = str(value)
            self.ids.int_slider.value = value
            self.value = value

            if self.value_changed_callback:
                self.value_changed_callback()
        except ValueError:
            pass