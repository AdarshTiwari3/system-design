"""implementation of cheese decorator"""

from decorator.pizza_decorator import PizzaDecorator

class Cheese(PizzaDecorator):
    def get_price(self) -> float:
        return super().get_price()+58
    
    def get_description(self) -> str:
        return super().get_description()+ "\n Added extra cheese"