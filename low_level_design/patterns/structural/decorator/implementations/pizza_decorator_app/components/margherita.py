"""implementation of Margherita Pizza concrete class of pizza interface"""

from components.pizza_interface import Pizza

class Margherita(Pizza):
    def get_price(self) -> float:
        return 239.0
    
    def get_description(self) -> str:
        return "Margherita Pizza"