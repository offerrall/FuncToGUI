from kivy.properties import StringProperty, BooleanProperty, ListProperty
from .ui_base import CustomProperty
from plyer import filechooser
import os

class CustomFileProperty(CustomProperty):
    value = StringProperty("")
    multiple = BooleanProperty(False)
    filters = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):        
        self.set_button_text()

    def set_button_text(self):
        if self.value == "":
            self.ids.file_button.text = "Select a file"
            return
        max_l = 15
        file = self.value if len(self.value) < max_l else "..." + self.value[-max_l:]
        self.ids.file_button.text = file
    
    def open_file_dialog(self):
        original_dir = os.getcwd()
        
        try:
            file_path = filechooser.open_file(multiple=self.multiple, filters=self.filters)

            if file_path:
                self.value = ",".join(file_path) if self.multiple else file_path[0]
                self.set_button_text()

                if self.value_changed_callback:
                    self.value_changed_callback()
        finally:
            os.chdir(original_dir)


class CustomFolderProperty(CustomProperty):
    value = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_kv_post(self, base_widget):        
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
        original_dir = os.getcwd()
        
        try:
            folder_path = filechooser.choose_dir()

            if folder_path:
                self.value = folder_path[0]
                self.set_button_text()

                if self.value_changed_callback:
                    self.value_changed_callback()
        finally:
            os.chdir(original_dir)