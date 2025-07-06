from models.pizza import Pizza

class CornPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.ingredients = ["Corn", "Tomato Sauce", "Mozzarella Cheese"]

    def prepare(self):
        print("Preparing the Corn Pizza")
        self.show_ingredients()

    def bake(self):
        print("baking the Corn Pizza")

    def cut(self):
        print("Cutting the corn pizza into different slices")