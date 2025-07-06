#implement veggie pizza here extend the feature of pizza

from models.pizza import Pizza

class VeggiePizza(Pizza):
    def prepare(self):
        print("preparing veggie pizza")