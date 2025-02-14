from kivy.properties import BooleanProperty, StringProperty
from .ui_base import CustomProperty

class CustomTimeProperty(CustomProperty):
    value = BooleanProperty(False)
    hour = StringProperty("12")
    minutes = StringProperty("00")
    pm_am = StringProperty("AM")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        self.ids.time_spinner_minute.values = [str(i).zfill(2) for i in range(0, 60)]
        self.ids.time_spinner_hour.values = [str(i) for i in range(1, 13)]
        
        if self.value:
            try:
                data = self.value.split(":")
                self.hour = data[0]
                data = data[1].split(" ")
                self.minutes = data[0]
                self.pm_am = data[1]

            except:
                raise ValueError("Invalid time format, please use hh:mm AM/PM")
        
        self.ids.time_spinner_hour.text = self.hour
        self.ids.time_spinner_minute.text = self.minutes
        self.ids.time_spinner_pm_am.text = self.pm_am
    
    def set_property_value(self):
        self.value = f"{self.ids.time_spinner_hour.text}:{self.ids.time_spinner_minute.text} {self.ids.time_spinner_pm_am.text}"

        if self.value_changed_callback:
            self.value_changed_callback()