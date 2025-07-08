""" implement windows factory which will implement windows button and windows check box"""

from factories.gui_factory import GUIFactory
from products.buttons.buttons import Button
from products.checkboxes.checkbox import CheckBox
from products.buttons.windows_button import WindowsButton
from products.checkboxes.windows_checkbox import WindowsCheckBox
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()