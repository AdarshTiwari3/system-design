"""implementation of concreate class mac checkbox of abstract class checkbox"""

from products.checkboxes.checkbox import CheckBox

class MacCheckBox(CheckBox):
    def __init__(self) -> None:
        self._callback=None

    def render(self) -> str:
        return "rendering  mac check box..."
    
    def on_check(self, callback):
        self._callback=callback

    def simulate_check(self):
        print("[MacCheckBox] checked!")
        if self._callback:
            self._callback()
