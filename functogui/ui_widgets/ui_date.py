from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from ..styles import CustomButton
from datetime import datetime
import calendar

from .ui_base import CustomProperty

class DatePicker(BoxLayout):
    callback = ObjectProperty(None)

    def __init__(self, callback=None, initial_date=None):
        super().__init__(orientation='vertical', spacing=10, padding=10)
        self.callback = callback
        self.current_date = initial_date if initial_date else datetime.now()
        
        self.setup_header()
        self.setup_weekdays()
        self.setup_calendar()
        
    def setup_header(self):
        header = BoxLayout(size_hint_y=0.2)
        self.month_label = Label()
        
        for widget in [
            CustomButton(text='<', size_hint_x=0.2, on_press=self.prev_month),
            self.month_label,
            CustomButton(text='>', size_hint_x=0.2, on_press=self.next_month)
        ]:
            header.add_widget(widget)
            
        self.add_widget(header)
        self.update_month_label()
        
    def setup_weekdays(self):
        weekdays = BoxLayout(size_hint_y=0.1)
        for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
            weekdays.add_widget(Label(text=day))
        self.add_widget(weekdays)
        
    def setup_calendar(self):
        self.calendar = GridLayout(cols=7, spacing=10)
        self.update_calendar()
        self.add_widget(self.calendar)
        
    def update_month_label(self):
        self.month_label.text = self.current_date.strftime('%B %Y')
        
    def update_calendar(self):
        self.calendar.clear_widgets()
        
        first_day = self.current_date.replace(day=1)
        _, days_in_month = calendar.monthrange(self.current_date.year, self.current_date.month)
        
        [self.calendar.add_widget(Label()) for _ in range(first_day.weekday())]
        
        for day in range(1, days_in_month + 1):
            btn = CustomButton(text=str(day))
            btn.bind(on_press=lambda x, d=day: self.on_select(d))
            self.calendar.add_widget(btn)
            
        remaining = 42 - (first_day.weekday() + days_in_month)
        [self.calendar.add_widget(Label()) for _ in range(remaining)]
        
    def prev_month(self, *args):
        year = self.current_date.year - (self.current_date.month == 1)
        month = 12 if self.current_date.month == 1 else self.current_date.month - 1
        
        _, last_day = calendar.monthrange(year, month)
        new_day = min(self.current_date.day, last_day)
        
        self.current_date = self.current_date.replace(
            year=year,
            month=month,
            day=new_day
        )
        self.update_month_label()
        self.update_calendar()

    def next_month(self, *args):
        year = self.current_date.year + (self.current_date.month == 12)
        month = 1 if self.current_date.month == 12 else self.current_date.month + 1
        
        _, last_day = calendar.monthrange(year, month)
        new_day = min(self.current_date.day, last_day)
        
        self.current_date = self.current_date.replace(
            year=year,
            month=month,
            day=new_day
        )
        self.update_month_label()
        self.update_calendar()
        
    def on_select(self, day):
        selected = self.current_date.replace(day=day)
        if self.callback:
            self.callback(selected.strftime('%d/%m/%Y'))
        if hasattr(self, 'modal') and self.modal:
            self.modal.dismiss()

class CustomDateProperty(CustomProperty):
    value = StringProperty("")
    value_changed_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.value:
            self.value = datetime.now().strftime('%d/%m/%Y')
        self.validate_date(self.value)

    def validate_date(self, date_str):
        try:
            day, month, year = map(int, date_str.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
                raise ValueError
            datetime(year, month, day)
        except (ValueError, TypeError):
            raise ValueError("Invalid date format. Use DD/MM/YYYY")

    def on_touch_down(self, touch):
        if self.ids.date_picker_button.collide_point(*touch.pos):
            modal = ModalView(background_color=[0, 0, 0, 0.9])
            date_picker = DatePicker(callback=self.on_date_selected,
                                     initial_date=datetime.strptime(self.value, '%d/%m/%Y')
                                     )
            date_picker.modal = modal
            modal.add_widget(date_picker)
            modal.open()
            return True
        return super().on_touch_down(touch)

    def on_date_selected(self, date_str):
        self.value = date_str
        if self.value_changed_callback:
            self.value_changed_callback()