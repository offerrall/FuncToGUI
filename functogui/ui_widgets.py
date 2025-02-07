from kivy.properties import NumericProperty, StringProperty, ObjectProperty, BooleanProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.button import Button
from kivy.metrics import dp

from os.path import exists

class CustomProperty(BoxLayout):
    name = StringProperty("Property")
    value_changed_callback = ObjectProperty(None)
    error = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CustomStrProperty(CustomProperty):
    value = StringProperty("")
    min_length = NumericProperty(0)
    max_length = NumericProperty(100)
    password_mode = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.ids.str_textinput.text = self.value

    def set_property_value(self, value):

        if len(value) > self.max_length:
            self.error = f"Max: {self.max_length}"
            return
        
        if len(value) < self.min_length:
            self.error = f"Min: {self.min_length}"
            return
        
        self.ids.str_textinput.text = value
        self.value = value
        self.error = ""

        if self.value_changed_callback:
            self.value_changed_callback()

class CustomPasswordProperty(CustomStrProperty):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password_mode = True

class CustomIntProperty(CustomProperty):
    value = NumericProperty(0)
    min_value = NumericProperty(0)
    max_value = NumericProperty(0)
    int_mode = BooleanProperty(True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.ids.int_textinput.text = str(self.value)
        if self.int_mode:
            self.ids.int_slider.value = self.value

    def set_property_value(self, value):
        if value == "":
            self.error = "Empty value"
            return
        
        if value == "-":
            self.error = "Invalid value"
            return

        value = int(value) if self.int_mode else float(value)
        
        self.ids.int_textinput.text = str(value)
        if self.int_mode:
            self.ids.int_slider.value = value
        self.value = value

        if self.min_value > value:
            self.error = f"Min: {self.min_value}"
            return
        if self.max_value < value:
            self.error = f"Max: {self.max_value}"
            return
        self.error = ""
        if self.value_changed_callback:
            self.value_changed_callback()

class CustomFloatProperty(CustomIntProperty):

    def on_kv_post(self, base_widget):
        self.int_mode = False
        self.ids.numeric_layout.remove_widget(self.ids.int_slider)
        super().on_kv_post(base_widget)


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

class CustomFileProperty(CustomProperty):
    value = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        if self.value == "":
            self.set_button_text()
            return
        
        if not exists(self.value):
            self.value = ""
            self.set_button_text()
            return
        
        self.set_button_text()

    def set_button_text(self):
        text = self.value
        if text == "" or text is None or text == " ":
            self.ids.file_button.text = "Select a file"
            return
        max_l = 15
        file = text if len(text) < max_l else "..." + text[-max_l:]
        self.ids.file_button.text = file
    
    def open_file_dialog(self):
        from plyer import filechooser
        
        file_path = filechooser.open_file()

        if file_path:
            self.value = file_path[0]
            self.set_button_text()

            if self.value_changed_callback:
                self.value_changed_callback()

class CustomFolderProperty(CustomProperty):
    value = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_kv_post(self, base_widget):
        if self.value == "":
            self.set_button_text()
            return
        
        if not exists(self.value):
            self.value = ""
            self.set_button_text()
            return
        
        self.set_button_text()
    
    def set_button_text(self):
        text = self.value
        if text == "" or text is None or text == " ":
            self.ids.folder_button.text = "Select a folder"
            return
        max_l = 15
        folder = text if len(text) < max_l else "..." + text[-max_l:]
        self.ids.folder_button.text = folder
    
    def open_folder_dialog(self):
        from plyer import filechooser
        
        folder_path = filechooser.choose_dir()

        if folder_path:
            self.value = folder_path[0]
            self.set_button_text()

            if self.value_changed_callback:
                self.value_changed_callback()

class StrReturn(BoxLayout):
    text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def copy_text(self):
        from kivy.core.clipboard import Clipboard
        Clipboard.copy(self.text)

class ImageFileReturn(BoxLayout):
    image_path = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)