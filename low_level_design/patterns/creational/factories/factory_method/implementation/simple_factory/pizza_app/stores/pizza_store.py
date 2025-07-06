from factories.simple_pizza_factory import SimpleFactoryPizza
from models.pizza import Pizza
class PizzaStore:
    def __init__(self, factory: SimpleFactoryPizza):
        self.factory=factory # has a relationship with SimpleFactoryPizza as it is creating object of that class
    def order_pizza(self,type_of_pizza) -> Pizza: # returns Pizza
        pizza=self.factory.create_pizza(type_of_pizza) 

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
    

