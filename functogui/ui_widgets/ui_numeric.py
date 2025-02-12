from kivy.properties import NumericProperty, BooleanProperty
from .ui_base import CustomProperty


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

    def _parse_value(self, value):
        """Convert input to appropriate numeric type"""
        if isinstance(value, (int, float)):
            return int(value) if self.int_mode else float(value)
        
        clean_value = value.strip().replace("-", "")
        if not clean_value:
            raise ValueError("Empty value")
            
        parsed = float(clean_value)
        return int(parsed) if self.int_mode else parsed

    def _validate_bounds(self, value):
        """Check if value is within bounds"""
        if self.min_value > value:
            return f"Min: {self.min_value:_.0f}"
        if self.max_value < value:
            return f"Max: {self.max_value:_.0f}"
        return ""

    def set_property_value(self, value):
        try:
            new_value = self._parse_value(value)
            self.error = self._validate_bounds(new_value)
            self.value = new_value
            
            if self.int_mode:
                if not (self.value < self.min_value or self.value > self.max_value):
                    self.ids.int_slider.value = self.value
                
                self.ids.int_textinput.text = str(self.value)
                
        except ValueError as e:
            self.error = str(e) if str(e) != "could not convert string to float: ''" else "Empty value"

        if self.value_changed_callback:
            self.value_changed_callback()


class CustomFloatProperty(CustomIntProperty):

    def on_kv_post(self, base_widget):
        self.int_mode = False
        self.ids.numeric_layout.remove_widget(self.ids.int_slider)
        super().on_kv_post(base_widget)
