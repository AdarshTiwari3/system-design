""" abstract factory interface, GUI factory and its methods"""
from abc import ABC, abstractmethod
from products.buttons.buttons import Button
from products.checkboxes.checkbox import CheckBox
class GUIFactory(ABC):
    """abstract factory methods"""
    @abstractmethod
    def create_button(self) -> Button: 
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass