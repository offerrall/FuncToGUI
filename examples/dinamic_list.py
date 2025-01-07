from functogui import App, listUi, strReturn
from random import choice

valid_characters = [choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3)]

def random_choice(characters: str = listUi(valid_characters[0], values=valid_characters)
                  ) -> strReturn:
    
    return characters

App(random_choice)
