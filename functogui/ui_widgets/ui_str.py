from kivy.properties import StringProperty, ObjectProperty, NumericProperty, BooleanProperty
from kivy.core.clipboard import Clipboard
from .ui_base import CustomProperty


class CustomStrProperty(CustomProperty):
    value = StringProperty("")
    min_length = NumericProperty(0)
    max_length = NumericProperty(100)
    password_mode = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.ids.str_textinput.text = self.value
    
    def on_touch_down(self, touch):
        if touch.button == "right":
            if self.collide_point(*touch.pos):
                clipboard_text = Clipboard.paste()
                if clipboard_text:
                    self.set_property_value(clipboard_text)
                return True
        return super().on_touch_down(touch)

    def set_property_value(self, value):
        if len(value) > self.max_length:
            self.error = f"Max: {self.max_length}"
        elif len(value) < self.min_length:
            self.error = f"Min: {self.min_length}"
        else:
            self.error = ""
        
        self.ids.str_textinput.text = value
        self.value = value

        if self.value_changed_callback:
            self.value_changed_callback()


class CustomPasswordProperty(CustomStrProperty):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password_mode = True