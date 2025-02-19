from functogui import App, selectedUi
from typing import Annotated

def rename_selected(selected: Annotated[list, selectedUi(values=["days", "hours", "minutes", "seconds"], # values to select
                                                        min_selected=2, # min selected values
                                                        max_selected=3 # max selected values
                                                        )] = ["days", "hours"] # default selected values
                              ) -> str:
    
    rename_names = {
        "days": "d",
        "hours": "h",
        "minutes": "m",
        "seconds": "s"
    }
    
    return " ".join([rename_names.get(name, name) for name in selected])


App(rename_selected)