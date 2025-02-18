from functogui import App, selectedUi
from typing import Annotated

def rename_selected(selected: Annotated[list, selectedUi(values=["days", "hours", "minutes", "seconds"],
                                                        min_selected=2,
                                                        max_selected=3
                                                        )] = ["days", "hours"]
                              ) -> str:
    
    rename_names = {
        "days": "d",
        "hours": "h",
        "minutes": "m",
        "seconds": "s"
    }
    
    return " ".join([rename_names.get(name, name) for name in selected])


App(rename_selected)