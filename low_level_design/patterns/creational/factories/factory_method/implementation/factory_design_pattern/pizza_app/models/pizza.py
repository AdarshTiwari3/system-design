from abc import ABC, abstractmethod
from typing import List
class Pizza(ABC):
    def __init__(self):
        self.ingredients:List[str]=[]
        
    @abstractmethod
    def prepare(self):
        """Each pizza type must define its own preparation steps."""
        pass

    def bake(self):
        print("Baking the pizza")

    def cut(self):
        print("cutting the pizza into slices")

    def box(self):
        print("pack the pizza in a box")

    def show_ingredients(self):
        print(f"Ingredients:{','.join(self.ingredients)}")