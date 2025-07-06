
#implementation factory method for pizza store and below are the disadvantage of simple factory which we created 
#credit- internet for below comparison

'''
| Problem                                         | Description                                                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ❌ **Tightly Coupled to Factory**                | `PizzaStore` depends on a **specific** `SimpleFactoryPizza` implementation.                                               |
| ❌ **Violates Open/Closed Principle**            | You must **modify the factory** to add new types (e.g., update the `if/elif` block).                                      |
| ❌ **Inflexible for Subclassing**                | What if different stores want to make pizzas differently (IndianPizzaStore vs USPizzaStore)?                              |
| ❌ **Not Easily Testable or Extendable**         | You can’t easily plug in a different creation strategy without modifying the factory.                                     |
| ❌ **Difficult to scale with multiple creators** | If multiple types of objects (e.g., `Drinks`, `Sides`) need factories, `SimplePizzaFactory` becomes a bloated God Object. |

'''