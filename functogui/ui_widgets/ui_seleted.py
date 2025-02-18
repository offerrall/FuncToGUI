from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout

from .ui_base import CustomProperty

class ItemSelected(BoxLayout):
    text = StringProperty("")
    selected = ObjectProperty(False)
    selected_callback = ObjectProperty(None)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.selected = not self.selected
            self.selected_callback()

class ModalSelected(BoxLayout):
    value = ListProperty([])
    values = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for value in self.values:
            is_selected = not value in self.value
            self.ids.selected_layout.add_widget(ItemSelected(text=value,
                                                             selected=is_selected,
                                                             selected_callback=self.update_info))
        
        self.update_info()
    
    def update_info(self):
        num_selected = 0
        for item in self.ids.selected_layout.children:
            if not item.selected:
                num_selected += 1
        self.ids.selected_label.text = f"Selected: {num_selected}"

    def on_touch_down(self, touch):
        if self.ids.selected_button.collide_point(*touch.pos):
            self.parent.dismiss()
            return True
        return super().on_touch_down(touch)

class CustomSeletedProperty(CustomProperty):
    value = ListProperty([])
    values = ListProperty([])
    min_selected = ObjectProperty(0)
    max_selected = ObjectProperty(1_000_000)
    value_changed_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.atm_modaL = None
        self.ids.selected_button.text = f"Selected: {len(self.value)}"
        self.check_limits()

        for value in self.value:
            if value not in self.values:
                raise ValueError(f"Value '{value}' not in values list, values: {self.values}")
    
    def on_touch_down(self, touch):
        if self.ids.selected_button.collide_point(*touch.pos):
            modal = ModalView(background_color=[0, 0, 0, 0.9], on_pre_dismiss=self.update_value)
            modal_selected = ModalSelected(values=self.values, value=self.value)
            modal.add_widget(modal_selected)
            self.atm_modaL = modal_selected
            modal.open()
            return True
        return super().on_touch_down(touch)

    def check_limits(self):
        if len(self.value) < self.min_selected:
            self.error = f"Min selected: {self.min_selected}"
            return False
        if len(self.value) > self.max_selected:
            self.error = f"Max selected: {self.max_selected}"
            return False

    def update_value(self, *args):
        self.value = []
        self.error = ""
        for item in self.atm_modaL.ids.selected_layout.children:
            if not item.selected:
                self.value.append(item.text)
        
        self.ids.selected_button.text = f"Selected: {len(self.value)}"
        self.check_limits()

        if self.value_changed_callback:
            self.value_changed_callback()