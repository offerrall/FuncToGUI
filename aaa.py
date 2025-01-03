from dataclasses import dataclass

@dataclass
class strUi:
    value: str
    min_length: int = 0
    max_length: int = 100

@dataclass
class listUi:
    value: list

@dataclass
class intUi:
    value: int
    min_value: int = 0
    max_value: int = 100

def test(test_str: str = strUi("hola", 0, 300),
         test_list: list = listUi([1, 2, 3]),
         test_int: int = intUi(5, 0, 100)
         ) -> str:

    return test_str

def inspect_params(func):
    import inspect
    
    params_info = {}
    
    for name, param in inspect.signature(func).parameters.items():
        default = param.default
        type_hint = param.annotation
        
        # Obtenemos los valores actuales del constructor
        current_values = {
            field: getattr(default, field)
            for field in default.__dataclass_fields__
        }
        
        params_info[name] = {
            'type': type_hint.__name__,
            'default_class': default.__class__.__name__,
            'constructor_values': current_values,
            'default_params': {
                param_name: {
                    'type': param.annotation.__name__,
                    'default': param.default if param.default != param.empty else None
                }
                for param_name, param in inspect.signature(default.__class__).parameters.items()
            }
        }
    
    return params_info

# Uso
result = inspect_params(test)
print(result)

# Uso
inspect_params(test)