from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CustomProperty(BoxLayout):
    name = StringProperty("Property")
    value_changed_callback = ObjectProperty(None)
    error = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)