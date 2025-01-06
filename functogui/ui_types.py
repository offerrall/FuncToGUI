from dataclasses import dataclass
import inspect

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


def inspect_params(func: callable) -> dict:
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