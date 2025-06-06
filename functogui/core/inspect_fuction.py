from .ui_types import intUi, strUi, boolUi, floatUi, colorUi
from typing import Any, get_type_hints

import inspect

primite_types_allowed = ["int", "str", "bool", "float", "tuple", "list"]

ui_types = ["intUi", "strUi", "fileUi", "listUi", "boolUi", "floatUi", "colorUi", "folderUi", "passwordUi", "timeUi", "dateUi", "selectedUi"]

basic_return_types = ["strReturn", "intReturn", "boolReturn", "floatReturn"]

map_primitive_ui = {"int": intUi,
                    "str": strUi,
                    "bool": boolUi,
                    "float": floatUi,
                    "tuple": colorUi,
                    }

map_return_ui = {"int": "intReturn",
                 "str": "strReturn",
                 "bool": "boolReturn",
                 "float": "floatReturn",
                 }

def get_return_type_name(func: callable) -> str:
    """Get the name of the return type of a function."""
    type_hints = get_type_hints(func, include_extras=True).get('return', Any)

    if not "_AnnotatedAlias" in type(type_hints).__name__:
        name = type_hints.__name__
        if not name in primite_types_allowed:
            raise ValueError(f"Return type '{name}' is not allowed, must be one of {primite_types_allowed}")
        name = map_return_ui[name]
        return name

    metadata = type_hints.__metadata__[0]
    if type(metadata) == type:
        metadata = metadata()
    name = metadata.__class__.__name__

    return name

def inspect_params(func: callable) -> dict:
    """
    Inspects function parameters and returns UI configuration info.
    
    Args:
        func: Function to inspect
    
    Returns:
        dict: Parameter info with structure:
            {param_name: {
                'type': primitive type name,
                'ui_type': UI widget class name,
                'default': default value,
                'options': UI widget configuration
            }}
    
    Raises:
        ValueError: For missing defaults, type hints or invalid types
    """

    parameters = inspect.signature(func).parameters.items()
    parameters_info = {}

    for name, param in parameters:
        name = param.name
        annotation = param.annotation
        default = param.default

        if "inspect._empty" in str(default):
            raise ValueError(f"Parameter {name} has no default value")
        
        if "inspect._empty" in str(annotation):
            raise ValueError(f"Parameter {name} has no type hint")

        if not "_AnnotatedAlias" in type(annotation).__name__:
            type_primitive = annotation.__name__

            if not type_primitive in primite_types_allowed:
                raise ValueError(f"Parameter {name} has an invalid type hint '{type_primitive}'")

            if type_primitive == "tuple":
                is_color4_tuple = True

                try: # Tuple can fail if is empty
                    if not len(annotation.__args__) == 4:
                        is_color4_tuple = False
                    for arg in annotation.__args__:
                        if not arg.__name__ == "int":
                            is_color4_tuple = False
                            break
                except:
                    is_color4_tuple = False
                
                if not is_color4_tuple:
                    raise ValueError(f"Tuple only supports 4 int values for colorUI, not for any other type, like this: tuple[int, int, int, int]")

            ui_type = map_primitive_ui[type_primitive]

            default_ui = ui_type()
            options = {k:v for k,v in default_ui.__dict__.items() if k != 'value'}

            info_param = {"type": type_primitive,
                          "ui_type": ui_type.__name__,
                          "default": default,
                          "options": options}
        else:
            metadata = annotation.__metadata__[0]
            if type(metadata) == type:
                metadata = metadata()
            type_primitive = annotation.__args__[0].__name__
            ui_type = metadata.__class__.__name__

            if not ui_type in ui_types:
                raise ValueError(f"Parameter {name} has an invalid Ui type '{ui_type}', must be one of {ui_types}")
            
            metadata_attrs = {k:v for k,v in metadata.__dict__.items() if k != 'value'}

            info_param = {"type": type_primitive,
                          "ui_type": metadata.__class__.__name__,
                          "default": default,
                          "options": metadata_attrs}

        if not type_primitive in primite_types_allowed:
            raise ValueError(f"Parameter {name} has an invalid type hint '{type_primitive}'")

        parameters_info[name] = info_param
    
    return parameters_info