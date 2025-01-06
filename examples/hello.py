from functogui import App
from functogui.ui_types import strUi, intUi

def hello_world(name: str = strUi(value="World"),
                times: int = intUi(value=3, min_value=1, max_value=10)
                ) -> str:
    return f"Hello {name}! " * times

App(hello_world)