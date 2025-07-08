'''implement product class A of button- abstract class'''
from abc import ABC, abstractmethod
from typing import Callable

class Button(ABC):

    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def on_click(self, callback:Callable[[], None]): # here call back is param of button
        pass

    @abstractmethod
    def simulate_click(self):
        pass
    