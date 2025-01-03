from _types import *
import json

from dataclasses import dataclass

def save_params(func):
    try:
        params = inspect_params(func)
        with open(f'{func.__name__}_params.json', 'w') as f:
            json.dump(params, f, indent=4)
    except Exception as e:
        print(f"Error saving params of {func.__name__}: {e}")
        

def test(test_str: str = strUi("hola", 0, 300),
         test_list: list = listUi([1, 2, 3]),
         test_int: int = intUi(5, 0, 100)
         ) -> str:

    return test_str

def test2() -> str:
    test_str = strUi("hola", 0, 300)
    return test_str

def test3(hola) -> str:
    return hola

def test4(test_str: str = "hola") -> str:
    return test_str

save_params(test)
save_params(test2)
save_params(test3)
save_params(test4)