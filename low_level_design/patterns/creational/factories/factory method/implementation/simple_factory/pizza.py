#implement the pizza class this will be abstract class
from abc import ABC, abstractmethod
class Pizza(ABC):

    #define the methods of pizza 
    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("baking the pizza")

    def cut(self):
        print("cutting the pizza")

    def box(self):
        print("pack the pizza in a box")