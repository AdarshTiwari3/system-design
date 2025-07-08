"""implementation of cooncreate class of button abstract class"""

from products.buttons.buttons import Button

class MacOsButton(Button):
    def __init__(self) -> None:
        self._callback=None # for internal use only
        
    def render(self) -> str:
        return ("rendering MacOS button...")
    
    def on_click(self, callback):
        self._callback=callback

    def simulate_click(self):
        print("[MacButton] Button clicked.")
        if self._callback:
            self._callback()