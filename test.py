from functogui.ui_types import intUi
from functogui import App


def calculate_power(num_leds: int = intUi(value=30, min_value=1, max_value=1000),
                    brightness: int = intUi(value=100, min_value=0, max_value=100),
                    ) -> float:
    consumption = (0.06 * num_leds * (brightness/100))
    return round(consumption, 2)

app = App(calculate_power)
app.run()