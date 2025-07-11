"""house builder interface"""
from typing_extensions import Self
from abc import ABC, abstractmethod
from product.house import House
class HouseBuilder(ABC):
    
    @abstractmethod
    def set_walls(self, present: bool) -> Self:
        pass

    @abstractmethod
    def set_doors(self, present: bool) -> Self:
        pass

    @abstractmethod
    def set_windows(self, present: bool) -> Self:
        pass

    @abstractmethod
    def set_roof(self,present: bool) -> Self:
        pass

    @abstractmethod
    def build(self) -> House: pass