"""Pizza Decorator abstract class implementation. this will have is-a and has-a relationship"""
from components.pizza_interface import Pizza
class PizzaDecorator(Pizza):
    def __init__(self,pizza:Pizza) -> None:
        self._pizza=pizza

    def get_price(self) -> float:
        return self._pizza.get_price()