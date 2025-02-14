from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, StringProperty
from kivy.animation import Animation

class CustomButton(Button):
    is_hovered = BooleanProperty(False)
    text_on_release = StringProperty("")
    _animating = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        
    def on_mouse_pos(self, *args):
        pos = self.to_widget(*args[1])
        self.is_hovered = self.collide_point(*pos)
    
    def on_release(self):
        if self._animating:
            return super().on_release()
            
        self._animating = True
        anim = Animation(opacity=0.5, duration=0.1) + Animation(opacity=1, duration=0.1)
        
        if self.text_on_release:
            original_text = self.text
            self.text = self.text_on_release
            
        def on_complete(*args):
            if self.text_on_release:
                self.text = original_text
            self._animating = False
            
        anim.bind(on_complete=on_complete)
        anim.start(self)
        return super().on_release()