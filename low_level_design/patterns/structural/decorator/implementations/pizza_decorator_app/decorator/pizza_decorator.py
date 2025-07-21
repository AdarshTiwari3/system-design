"""Pizza Decorator abstract class implementation. this will have is-a and has-a relationship"""
from components.pizza_interface import Pizza
from abc import ABC
class PizzaDecorator(Pizza, ABC):
    def __init__(self,pizza:Pizza) -> None:
        self._pizza=pizza # has-a relationship

    def get_price(self) -> float:
        return self._pizza.get_price()
    
    def get_description(self) -> str:
        return self._pizza.get_description()