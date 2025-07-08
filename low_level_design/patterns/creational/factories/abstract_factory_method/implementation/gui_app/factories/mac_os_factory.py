"""implement macos factory of gui factory interface"""

from factories.gui_factory import GUIFactory
from products.buttons.buttons import Button
from products.checkboxes.checkbox import CheckBox
from products.buttons.mac_button import MacOsButton
from products.checkboxes.mac_checkbox import MacCheckBox

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOsButton()
    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()