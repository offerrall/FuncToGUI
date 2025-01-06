from kivy.properties import NumericProperty, StringProperty, ObjectProperty, BooleanProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout


class CustomProperty(BoxLayout):
    name = StringProperty("Property")
    value_changed_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CustomStrProperty(CustomProperty):
    value = StringProperty("")
    min_length = NumericProperty(0)
    max_length = NumericProperty(100)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.ids.str_textinput.text = self.value

    def set_property_value(self, value):

        if len(value) < self.min_length or len(value) > self.max_length:
            self.ids.str_textinput.text = self.value
            return

        self.ids.str_textinput.text = value
        self.value = value

        if self.value_changed_callback:
            self.value_changed_callback()

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