from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from kivy.animation import Animation

class CustomButton(Button):
    is_hovered = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        
    def on_mouse_pos(self, *args):
        pos = self.to_widget(*args[1])
        self.is_hovered = self.collide_point(*pos)
    
    def on_release(self):
        anim = Animation(opacity=0.5, duration=0.1) + Animation(opacity=1, duration=0.1)
        anim.start(self)
        return super().on_release()
