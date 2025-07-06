#import the base class of pizza and use here in subclass

from models.pizza import Pizza

class CornPizza(Pizza):
    def prepare(self):
        print("preparing Corn Pizza")

    def bake(self):
        print("baking the corn pizza")