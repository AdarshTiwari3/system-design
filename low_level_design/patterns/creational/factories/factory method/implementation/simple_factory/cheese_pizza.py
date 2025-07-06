#sub class of pizza class so implement the features here
from pizza import Pizza
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def bake(self):
        print("baking cheese pizza")