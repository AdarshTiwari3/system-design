#Entry point of the design
#client code

from factories.simple_pizza_factory import SimpleFactoryPizza
from stores.pizza_store import PizzaStore


#pizza menu 
def choose_pizza_from_menu():
    factory=SimpleFactoryPizza()
    pizza_store_=PizzaStore(factory)
 
    print("\nOrder Number-1: Corn Pizza")
    pizza_store_.order_pizza("corn")

    print("\nOrder Number-2: Cheese Pizza")
    pizza_store_.order_pizza("cheese")

    print("\nOrder Number-3: Veggie Pizza")
    pizza_store_.order_pizza("veggie")



if __name__ == "__main__":

    print("\nSimple Factory Example\n")
    choose_pizza_from_menu()