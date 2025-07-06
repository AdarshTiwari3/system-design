#concreate creator of PizzaStore
from models.veggie_pizza import VeggiePizza
from models.pizza import Pizza
from stores.pizza_store import PizzaStore

class VeggiePizzaCreator(PizzaStore):
    def create_pizza(self) -> Pizza:
        return VeggiePizza()