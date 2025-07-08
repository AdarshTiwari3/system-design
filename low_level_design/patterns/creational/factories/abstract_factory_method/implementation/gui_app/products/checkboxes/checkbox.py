'''implement CheckBox Abstract class - Product B'''

from abc import ABC, abstractmethod

class CheckBox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def on_check(self, callback): # here call back is param of checkbox like check box clicked
        pass

    @abstractmethod
    def simulate_check(self):
        pass
    