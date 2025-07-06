# concreate creator of PizzaStore abstract class

from models.pizza import Pizza
from stores.pizza_store import PizzaStore
from models.corn_pizza import CornPizza

class CornPizzaCreator(PizzaStore):
    def create_pizza(self) -> Pizza:
        return CornPizza()