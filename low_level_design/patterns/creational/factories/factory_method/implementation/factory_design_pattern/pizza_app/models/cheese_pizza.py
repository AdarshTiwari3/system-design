from models.pizza import Pizza

class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.ingredients = ["Cheese", "Tomato Sauce", "Oregano"]

    def prepare(self):
        print("Preparing the Cheese Pizza")
        self.show_ingredients()
