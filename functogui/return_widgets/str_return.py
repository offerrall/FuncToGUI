from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard


class StrReturn(BoxLayout):
    text = StringProperty("Waiting...")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def copy_text(self):
        Clipboard.copy(self.text)