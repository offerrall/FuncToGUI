# FuncToGUI

From function to GUI:

<div style="display: flex; gap: 20px;">
<div>

```python
from functogui import App
from functogui.ui_types import strUi, intUi

def hello_world(name: str = strUi(value="World"),
                times: int = intUi(value=3, min_value=1, max_value=10),
                ) -> str:
    return f"Hello {name}! " * times

App(hello_world)
```
To...

</div>
<img src="screen.png" alt="GUI Result" width="393" height="277">
</div>

Your function becomes a GUI application - perfect for internal tools, quick testing, or prototypes. Cross-platform, real-time updates, no UI code needed. Written in less than 1000 lines.


##  How simple is it?
The entire type system is so simple, here's the complete code - this is all you need to know:

```python
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
```
