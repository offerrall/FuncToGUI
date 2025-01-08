from dataclasses import dataclass

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
    min_value: int = 0
    max_value: int = 1000

@dataclass
class floatUi:
    value: float = 0.0
    min_value: float = 0.0
    max_value: float = 1000.0

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

class floatReturn:
    pass

class imageFileReturn:
    pass