# here is the steps to design a factory design pattern-
#credit- internet
'''
# Steps to Design a Factory Method Pattern:

1. Define a Product abstract class (e.g., Pizza) and its concrete implementations (e.g., CheesePizza, CornPizza).

2. Define a Creator abstract class (e.g., PizzaStore) that declares a factory method (`create_pizza`).

3. The Creator also provides a high-level method (`order_pizza`) which defines the **template** for ordering a pizza:
   - It delegates the creation logic to the abstract `create_pizza` method.
   - And then executes steps like `prepare`, `bake`, `cut`, and `box`.

4. Subclasses of the Creator (e.g., CheesePizzaStore, CornPizzaStore) override `create_pizza` to return specific types of Pizza.

5. This design allows for flexibility and adheres to SOLID principles:
   - **Open/Closed Principle**: Easily add new pizza types without changing existing logic.
   - **Single Responsibility Principle**: Object creation logic is separated from processing logic.

6. This is called the **Factory Method** pattern because the logic to instantiate the product is deferred to subclasses.

Note:
- This pattern creates **one product at a time**.
- If you need to create multiple related objects together, then consider the **Abstract Factory Pattern**.

'''