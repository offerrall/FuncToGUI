from functogui import App, strUi, intUi
from typing import Annotated

def hello_world(name: Annotated[str, strUi(max_length=10, min_length=3)] = "World",
                times: Annotated[int, intUi(min_value=1, max_value=10)] = 3
                ) -> str:
    
    return f"Hello {name}! " * times

App(hello_world)