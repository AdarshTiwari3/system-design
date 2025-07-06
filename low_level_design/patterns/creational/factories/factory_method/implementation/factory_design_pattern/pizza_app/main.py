#implementation of pizza example using factory design pattern
from stores.veggie_pizza_creator import VeggiePizzaCreator
from stores.cheese_pizza_creator import CheesePizzaCreator
from stores.corn_pizza_creator import CornPizzaCreator

def order_pizza_from_menu():
    
    print("\nOrder number-1: Corn Pizza")
    corn_pizza=CornPizzaCreator()
    corn_pizza.order_pizza()

    print("\nOrder number-2: Cheese Pizza")
    cheese_pizza=CheesePizzaCreator()
    cheese_pizza.order_pizza()

    print("\nOrder number-3: Veggie Pizza")
    veggie_pizza=VeggiePizzaCreator()
    veggie_pizza.order_pizza()


if __name__ == "__main__":

    print("\nFactory Design Pattern Implementation")

    order_pizza_from_menu()