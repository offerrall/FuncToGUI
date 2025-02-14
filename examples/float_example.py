from functogui import App, floatUi
from typing import Annotated

def divide(a: float = 3.0,
           b: Annotated[float, floatUi(max_value=10.0)] = 2.0
           ) -> float:
    return a / b # 0 division is handled by the UI


App(divide, auto_update=False)