from functogui import App
from functogui.core.ui_types import timeUi
from typing import Annotated
from datetime import datetime

def time_diff(time1: Annotated[str, timeUi()] = "9:00 AM",
              time2: Annotated[str, timeUi()] = "5:00 PM"
              ) -> str:
    t1 = datetime.strptime(time1, "%I:%M %p")
    t2 = datetime.strptime(time2, "%I:%M %p")
   
    diff = t2 - t1
    total_hours = diff.total_seconds() / 3600
   
    if total_hours < 0:
        total_hours = 24 + total_hours
       
    hours = int(total_hours)
    mins = int((total_hours - hours) * 60)
   
    if hours == 0:
        return f"{mins} minutos"
    if mins == 0:
        return f"{hours} horas"
    return f"{hours} horas y {mins} minutos"

if __name__ == "__main__":
    App(time_diff)