from functogui.ui_types import intUi
from functogui import App

num_leds = intUi(value=30, min_value=1, max_value=1000)
brightness = intUi(value=100, min_value=0, max_value=100)

def calculate_power(num_leds: int = num_leds,
                    brightness: int = brightness
                    ) -> float:

    MAX_LED_POWER = 0.06
    consumption = (MAX_LED_POWER * num_leds * (brightness/100))
    return round(consumption, 2)

app = App(calculate_power)
app.run()