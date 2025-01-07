from functogui import App

def is_even(number: int = 4) -> bool:
    return number % 2 == 0

App(is_even)