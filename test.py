from functogui.ui_types import intUi, strUi
from functogui import App

def concatenate_n_texts(text: str = strUi(value="Hello", min_length=2, max_length=5),
                        n: int = intUi(value=3, min_value=1, max_value=10),
                        ) -> str:
    return text * n


App(concatenate_n_texts)