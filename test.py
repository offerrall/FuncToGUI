from functogui.ui_types import intUi, strUi, boolUi, listUi, fileUi, inspect_params
from functogui import App



def concatenate_n_texts(text: str = strUi(value="Hello", min_length=2, max_length=5),
                        n: int = intUi(value=3, min_value=1, max_value=10),
                        add_exclamation_mark: bool = boolUi(),
                        file_path: str = fileUi("C:/Users/offer/Downloads/ESTE-AUMENTO-NO-TE-D---.txt"),
                        no_use_chars: str = listUi(value="a", values = ["a", "b"])) -> str:

    text = "".join([char for char in text if char not in no_use_chars])
    return (text + "!" if add_exclamation_mark else text) * n


App(concatenate_n_texts)