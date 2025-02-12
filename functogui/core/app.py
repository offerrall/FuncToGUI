from kivy.app import App as KivyApp
from .main_layout import MainLayout

class App(KivyApp):
    """
    Create a Kivy app with a GUI for a given type-annotated function.
    Args:
        function (callable): The function to be used in the app.
        width (int): The width of the app. Default is 350.
    """
    def __init__(self,
                 function: callable,
                 width: int = 350,
                 **kwargs):
        super().__init__(**kwargs)
        self.main_layout = MainLayout(function,
                                      width=width,
                                      title="  " + function.__name__.replace("_", " ").title())
        self.run()

    def build(self):
        return self.main_layout