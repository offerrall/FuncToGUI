from functogui import App, dateUi
from typing import Annotated
from datetime import datetime

def calculate_time_difference(start_date: Annotated[str, dateUi] = "01/01/2025",
                              end_date: Annotated[str, dateUi] = "02/01/2025"
                              ) -> str:
    date1 = datetime.strptime(start_date, "%d/%m/%Y")
    date2 = datetime.strptime(end_date, "%d/%m/%Y")
    
    diff = date2 - date1

    total_seconds = int(diff.total_seconds())
    days = diff.days
    hours = total_seconds // 3600 % 24
    minutes = total_seconds // 60 % 60
    seconds = total_seconds % 60
    
    return (
        f"Time difference:\n"
        f"Days: {days}\n"
        f"Hours: {hours}\n"
        f"Minutes: {minutes}\n"
        f"Seconds: {seconds}\n"
        f"Total seconds: {total_seconds}"
    )


App(calculate_time_difference)