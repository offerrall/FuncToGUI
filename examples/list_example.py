from functogui import App, listUi
from typing import Annotated
from random import choice

valid_characters = [choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3)] # The list can be generated dynamically

def random_choice(characters: Annotated[str, listUi(values=valid_characters)] = valid_characters[0] # Default value must be one of the valid values
                  ) -> str:
    
    return characters

App(random_choice)