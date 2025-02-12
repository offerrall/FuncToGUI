from os.path import exists
from kivy.properties import StringProperty
from .ui_base import CustomProperty


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