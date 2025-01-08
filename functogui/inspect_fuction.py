from functogui.ui_types import intUi, strUi, fileUi, listUi, boolUi, floatUi
from typing import Any, get_type_hints

import inspect

primite_types_allowed = ["int", "str", "bool", "float"]

ui_types = ["intUi", "strUi", "fileUi", "listUi", "boolUi", "floatUi"]

map_primitive_ui = {"int": intUi,
                    "str": strUi,
                    "bool": boolUi,
                    "float": floatUi,
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
    print(name)
    return name

def inspect_params(func):
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