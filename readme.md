# FuncToGUI

From function

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
<img src="./examples/hello.png" alt="GUI Result" width="393" height="277">
</div>

Your function becomes a GUI application - perfect for internal tools, quick testing, or prototypes. Cross-platform, real-time updates, no UI code needed. Written in less than 1000 lines.

FuncToGui use Kivy for the GUI and pyler for file management.

##  Installation

```bash
git clone https://github.com/offerrall/FuncToGUI
cd FuncToGUI

pip install -e .
```

