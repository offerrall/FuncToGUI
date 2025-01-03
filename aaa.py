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