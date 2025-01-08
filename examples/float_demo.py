from functogui import App, floatUi
from typing import Annotated

def divide(a: float = 3.0,
           b: Annotated[float, floatUi(min_value=0.1, max_value=10.0)] = 2.0
           ) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0

App(divide)