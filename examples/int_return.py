from functogui import App, intUi, intReturn

def time_to_seconds(hours: int = intUi(1, max_value=24),
                    minutes: int = intUi(30, max_value=59)
                    ) -> intReturn:
    
    return (hours * 3600) + (minutes * 60)

App(time_to_seconds)