from dataclasses import dataclass
import inspect

@dataclass
class strUi:
    """UI hints for string parameters"""
    value: str
    min_length: int = 0
    max_length: int = 100

@dataclass
class listUi:
    """UI hints for list parameters"""
    value: list

@dataclass
class intUi:
    """UI hints for int parameters"""
    value: int
    min_value: int = 0
    max_value: int = 100


def inspect_params(func):
    
    params_info = {}
    
    for name, param in inspect.signature(func).parameters.items():
        default = param.default
        type_hint = param.annotation

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