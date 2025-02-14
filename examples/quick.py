from functogui import App

def check_even_number(number: int = 4) -> bool:
    return number % 2 == 0

App(check_even_number)