from models.pizza import Pizza

class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.ingredients = ["Green Veggies", "Tomato Sauce", "Oregano", "chilly Flakes"]

    def prepare(self):
        print("Preparing the Cheese Pizza")
        self.show_ingredients()
