from functogui import App, intUi, boolUi, boolReturn

def check_even_number(number: int = intUi(4, max_value=100)) -> boolReturn:
    return number % 2 == 0

App(check_even_number)