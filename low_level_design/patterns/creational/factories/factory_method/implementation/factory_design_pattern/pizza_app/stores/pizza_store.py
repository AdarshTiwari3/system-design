#Creator lets make this abstract so that its concreate creator can implement the object creation logic

from abc import ABC, abstractmethod
from models.pizza import Pizza
class PizzaStore(ABC):

    def order_pizza(self):
        # print("Order pizza")
        pizza=self.create_pizza()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
    
        
        
    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass