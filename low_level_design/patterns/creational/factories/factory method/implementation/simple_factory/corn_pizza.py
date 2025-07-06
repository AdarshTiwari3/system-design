#import the base class of pizza and use here in subclass

from pizza import Pizza

class CornPizza(Pizza):
    def prepare(self):
        print("preparing Corn Pizza")

    def bake(self):
        print("baking the corn pizza")