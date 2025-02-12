from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class ImageFileReturn(BoxLayout):
    image_path = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)