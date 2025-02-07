from functogui import App, fileUi
from typing import Annotated


def read_file_content(file_path: Annotated[str, fileUi] = "") -> str:
    if not file_path:
        return "No file selected"
        
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except Exception as e:
        return f"Error reading file: {str(e)}"


App(read_file_content)