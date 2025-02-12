from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.button import Button
from kivy.metrics import dp

from .ui_base import CustomProperty


class CustomColorProperty(CustomProperty):
    value = ObjectProperty((0, 0, 0, 255))
    color = ListProperty([0, 0, 0, 1])

    def get_kivy_color(self):
        return [c / 255 for c in self.value]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_kv_post(self, base_widget):
        self.color = self.get_kivy_color()
    
    def on_touch_down(self, touch):
        if self.ids.color_widget.collide_point(*touch.pos):
            modal_color = ModalView(background_color=[0, 0, 0, 0.5])
            color_picker = ColorPicker()
            color_picker.bind(color=self.set_color)
            color_picker.color = self.color
            esc_or_click = Button(text="Press ESC or click to close", size_hint_y=None, height=dp(20))
            esc_or_click.bind(on_release=modal_color.dismiss)
            box_layout = BoxLayout(orientation="vertical")
            box_layout.add_widget(esc_or_click)
            box_layout.add_widget(color_picker)
            modal_color.add_widget(box_layout)
            modal_color.open()

            return True
    
    def set_color(self, instance, value):
        self.color = value
        self.value = [int(c * 255) for c in value]
        self.value = tuple(self.value)

        if self.value_changed_callback:
            self.value_changed_callback()