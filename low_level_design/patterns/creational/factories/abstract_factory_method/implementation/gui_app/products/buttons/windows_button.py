""" windows buttons concreate class implementation"""
from products.buttons.buttons import Button
class WindowsButton(Button):
    def __init__(self):
        self._callback=None

    def render(self) -> str:
        return "rendering windows buttons..."
    
    def on_click(self, callback):
        self._callback=callback

    def simulate_click(self):
        print("[Windows] Button clicked.")
        if self._callback:
            self._callback()

    