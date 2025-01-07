from functogui import App, intUi, boolReturn

def is_even(number: int = intUi(4)) -> boolReturn:
    return number % 2 == 0

App(is_even)