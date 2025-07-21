"""implementation of farm house pizza, it is concrete class or subclass of pizza interface"""

from components.pizza_interface import Pizza

class FarmHouse(Pizza):
    def get_price(self) -> float:
        return 335.80
    
    def get_description(self) -> str:
        return "Farm House Pizza"