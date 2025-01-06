from dataclasses import dataclass
import inspect
from typing import Any, get_type_hints

@dataclass
class strUi:
    value: str = ""
    min_length: int = 0
    max_length: int = 100

@dataclass
class listUi:
    value: str = ""
    values: list = ""

@dataclass
class intUi:
    value: int = 0
    min_value: int = -1000
    max_value: int = 1000

@dataclass
class boolUi:
    value: bool = True

@dataclass
class fileUi:
    value: str = ""

class strReturn:
    pass

class intReturn:
    pass

class boolReturn:
    pass

class imageFileReturn:
    pass

def get_return_type_name(func: callable) -> str:
    """Get the name of the return type of a function."""
    type_hints = get_type_hints(func)
    return type_hints.get('return', Any).__name__

def inspect_params(func: callable) -> dict:
    """Inspect the parameters of a function and return a dictionary with the information."""
    params_info = {}
    
    for name, param in inspect.signature(func).parameters.items():
        default = param.default
        type_hint = param.annotation

        try:
            current_values = {
                field: getattr(default, field)
                for field in default.__dataclass_fields__
            }
        except AttributeError:
            raise TypeError(f"Parameter {name} must be a type hint")
        
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