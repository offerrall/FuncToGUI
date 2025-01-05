from kivy.app import App as KivyApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.absolute()
KV_FILE = CURRENT_DIR / "styles.kv"

print(KV_FILE)

Builder.load_file(str(KV_FILE))

class MainLayout(BoxLayout):
    pass

class App(KivyApp):
    def build(self):
        return MainLayout()