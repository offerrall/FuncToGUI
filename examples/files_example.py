from functogui import App, fileUi
from typing import Annotated
from kivy.core.clipboard import Clipboard

"""
**filters** *(iterable)*: either a list of wildcard patterns
        or of sequences that contain the name of the filter and any
        number of wildcards that will be grouped under that name
        (e.g. [["Music", "*mp3", "*ogg", "*aac"], "*jpg", "*py"])
"""
filters = [["Text", "*.txt", "*.md", "*.ini"], ["Programming", "*.py", "*.js", "*.java"], ["All Files", "*.*"]]

def copy_files_to_clipboard(file_paths: Annotated[str, fileUi(filters=filters, multiple=True)] = "") -> str:
    if not file_paths:
        return "No files selected"
    
    # file_paths comes as a string, not a list
    print(file_paths) 
    # Convert the string to a list when multiple=True is enabled
    file_paths = file_paths.split(",") 
    print(file_paths)
    
    try:
        combined_content = []
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                combined_content.append(content)
        
        final_content = "\n\n".join(combined_content)
        Clipboard.copy(final_content)
        
        return f"Copied {len(file_paths)} file(s) to clipboard"
    except Exception as e:
        return f"Error: {str(e)}"

App(copy_files_to_clipboard)