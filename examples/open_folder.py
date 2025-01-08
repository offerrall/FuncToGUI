from functogui import App, folderUi
import os
from typing import Annotated

def list_dir(folder: Annotated[str, folderUi] = ""
             ) -> str:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        return "Folder not found"
    return "\n".join(files)

App(list_dir)