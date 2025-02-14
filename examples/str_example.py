from functogui import App, strUi
from typing import Annotated



def validate_email(email: Annotated[str, strUi(min_length=5,
                                               max_length=50,
                                               regex_pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                                               )] = "") -> str:

    return f"Valid email: {email}"


# Example usage:
if __name__ == "__main__":
    # Choose which validation to run
    App(validate_email)
