from functogui import App, passwordUi
from typing import Annotated

def test_password(password: Annotated[str, passwordUi(max_length=10,
                                                      regex_pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                                                      min_length=3)] = "Secret123",
                ) -> str:
    
    no_password_allowed = ["A*2312xc"]
    if password in no_password_allowed:
        raise ValueError("Password not allowed")
    
    return f"Psswd: {password}"

App(test_password, auto_update=False, width=500)