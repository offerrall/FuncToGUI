from dataclasses import dataclass, field

@dataclass
class strUi:
    value: str = ""
    min_length: int = 0
    max_length: int = 100
    regex_pattern: str = ""

@dataclass
class passwordUi(strUi):
    pass

@dataclass
class listUi:
    value: str = ""
    values: list = ""

@dataclass
class intUi:
    value: int = 0
    min_value: int = 0
    max_value: int = 1000000

@dataclass
class floatUi:
    value: float = 0.0
    min_value: float = 0.0
    max_value: float = 1000000.0

@dataclass
class boolUi:
    value: bool = True

@dataclass
class colorUi:
    value: tuple[int, int, int, int] = (0, 0, 0, 255)

@dataclass
class fileUi:
    value: str = ""
    multiple: bool = False
    filters: list = field(default_factory=list)

@dataclass
class folderUi:
    value: str = ""
    
@dataclass
class timeUi:
    value: str = ""

@dataclass
class dateUi:
    value: str = ""

@dataclass
class selectedUi:
    value: list = field(default_factory=list)
    values: list = field(default_factory=list)
    min_selected: int = 0
    max_selected: int = 1_000_000

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