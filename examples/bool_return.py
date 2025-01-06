from functogui import App
from functogui.ui_types import intUi, boolUi, boolReturn

def check_even_number(
    number: int = intUi(value=4, min_value=0, max_value=100),
    ) -> boolReturn:
    
    return number % 2 == 0

App(check_even_number)