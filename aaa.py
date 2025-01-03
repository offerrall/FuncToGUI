from _types import *
import json







def test(test_str: str = strUi("hola", 0, 300),
         test_list: list = listUi([1, 2, 3]),
         test_int: int = intUi(5, 0, 100)
         ) -> str:

    return test_str


params = inspect_params(test)

with open('params.json', 'w') as f:
    json.dump(params, f, indent=4)

def test2() -> str:
    test_str = strUi("hola", 0, 300)
    return test_str

params2 = inspect_params(test2)

with open('params2.json', 'w') as f:
    json.dump(params2, f, indent=4)

def test3(hola) -> str:
    return hola

params3 = inspect_params(test3)

with open('params3.json', 'w') as f:
    json.dump(params3, f, indent=4)