from functogui import App, folderUi
import os
from typing import Annotated

def list_dir(folder: Annotated[str, folderUi] = ""
             ) -> str:

    files = os.listdir(folder)
    return "\n".join(files)

App(list_dir)