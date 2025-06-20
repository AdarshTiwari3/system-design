from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass

class StudentDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.9

class SeniorDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.85
