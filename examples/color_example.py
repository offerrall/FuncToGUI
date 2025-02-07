from functogui import App, colorUi
from typing import Annotated


def copy_color(color: tuple[int, int, int, int] = (255, 0, 0, 255)) -> str:

    return str(color)

# You can use the Annotated type or not, the tuple[int, int, int, int] is the same as colorUi
# tuple type is only for colorUi for now
def copy_color(color: Annotated[tuple[int, int, int, int], colorUi] = (0, 255, 0, 255)) -> str:

    return str(color)

App(copy_color)