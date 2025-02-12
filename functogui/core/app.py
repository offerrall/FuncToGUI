from kivy.app import App as KivyApp
from .main_layout import MainLayout

class App(KivyApp):
    """
    Create a Kivy app with a GUI for a given type-annotated function.
    Args:
        function (callable): The function to be used in the app.
        auto_update (bool): If True, the function will be called automatically when the properties change. Default is True.
        width (int): The width of the app. Default is 350.
    """
    def __init__(self,
                 function: callable,
                 auto_update: bool = True,
                 width: int = 350,
                 **kwargs):
        super().__init__(**kwargs)
        title = function.__name__.replace("_", " ").title()
        self.main_layout = MainLayout(function,
                                      width=width,
                                      title=title,
                                      auto_update=auto_update)
        self.run()

    def build(self):
        return self.main_layout