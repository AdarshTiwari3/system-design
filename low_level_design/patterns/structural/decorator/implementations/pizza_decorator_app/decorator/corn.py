"""implementation of corn decorator"""

from decorator.pizza_decorator import PizzaDecorator

class Corn(PizzaDecorator):
    def get_price(self) -> float:
        return super().get_price()+ 70.21
    
    def get_description(self) -> str:
        return super().get_description()+ "\n Added extra corn"