"""implementation of concreate class windows checkbox of abstract class checkbox"""

from products.checkboxes.checkbox import CheckBox

class WindowsCheckBox(CheckBox):
    def __init__(self) -> None:
        self._callback=None #for internal use only

    def render(self) -> str:
        return "rendering windows check box..."
    
    def on_check(self, callback):
        self._callback=callback

    def simulate_check(self):
        print("[WindowsCheckBox] checked!")
        if self._callback:
            self._callback() #this holds function that is coming from callback from on check params