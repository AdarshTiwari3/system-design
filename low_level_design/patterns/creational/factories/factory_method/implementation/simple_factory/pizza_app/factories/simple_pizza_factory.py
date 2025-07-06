# this is simple factory for pizza order, this will be responsible for object creation and it will manage directly with client
from models.pizza import Pizza
from models.cheese_pizza import CheesePizza
from models.veggie_pizza import VeggiePizza
from models.corn_pizza import CornPizza
class SimpleFactoryPizza:
    def create_pizza(self,type:str) -> Pizza:
        pizza_type=type.lower()

        if pizza_type == "corn":
            return CornPizza()
        elif pizza_type == "veggie":
            return VeggiePizza()
        elif pizza_type == "cheese":
            return CheesePizza()
        else:
            raise ValueError(f"it is unknow type of {pizza_type}")