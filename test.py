from functogui import App
from functogui.ui_types import intUi

def multiply(a: int = intUi(0),
             b: int = intUi(0)) -> int:
    return a * b


app = App(multiply)
app.run()