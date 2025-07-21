"""Implementation of Peppy Panerr Pizza concrete subclass of pizza interface"""

from components.pizza_interface import Pizza

class PeppyPaneer(Pizza):
    def get_price(self) -> float:
        return 431.87
    
    def get_description(self) -> str:
        return "Peppy Panner Pizza"