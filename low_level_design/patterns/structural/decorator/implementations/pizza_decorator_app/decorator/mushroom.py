"""implementation of Mushroom decorator"""

from decorator.pizza_decorator import PizzaDecorator

class Mushrooms(PizzaDecorator):
    def get_price(self) -> float:
        return super().get_price()+30.00
    
    def get_description(self) -> str:
        return super().get_description()+ "\n Added mushrooms"