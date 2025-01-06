from functogui import App
from functogui.ui_types import intUi, intReturn

def time_to_seconds(hours: int = intUi(value=1, min_value=0, max_value=24),
                    minutes: int = intUi(value=30, min_value=0, max_value=59)
                    ) -> intReturn:
    
    return (hours * 3600) + (minutes * 60)

App(time_to_seconds)