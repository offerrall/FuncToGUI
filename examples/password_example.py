from functogui import App, passwordUi
from typing import Annotated

def test_password(password: Annotated[str, passwordUi(max_length=10, min_length=3)] = "Secret123"
                  ) -> str:
    
    return f"Psswd: {password}"

App(test_password)