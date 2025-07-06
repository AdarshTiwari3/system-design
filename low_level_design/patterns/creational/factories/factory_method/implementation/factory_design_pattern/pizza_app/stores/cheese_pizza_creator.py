from stores.pizza_store import PizzaStore
from models.pizza import Pizza
from models.cheese_pizza import CheesePizza
#concreate creator of PizzaStore class

class CheesePizzaCreator(PizzaStore):
    def create_pizza(self) -> Pizza:
        return CheesePizza()
    
    