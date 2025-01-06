from functogui.ui_types import intUi, strUi, boolUi
from functogui import App

def concatenate_n_texts(text: str = strUi(value="Hello", min_length=2, max_length=5),
                        n: int = intUi(value=3, min_value=1, max_value=10),
                        add_exclamation_mark: bool = boolUi()
                        ) -> str:
    return (text + "!" if add_exclamation_mark else text) * n


App(concatenate_n_texts)