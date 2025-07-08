'''
Abstract Factory Design Pattern:

- It is a "factory of factories".
- The Abstract Factory is a creational design pattern that provides an interface to create **families of related or dependent objects** without specifying their concrete classes. like 
  The client interacts only with abstract interfaces like GUIFactory, Button, and Checkbox,
  without knowing or depending on the concrete classes like MacButton or WindowsCheckbox.

- In simple terms:
  Group related product creation methods together (like `create_button()`, `create_checkbox()`, etc.) in a single factory interface (e.g., `GUIFactory`).
  Concrete factories (e.g., `WindowsFactory`, `MacFactory`) implement this interface to produce platform-specific objects.

Example:
- A `WindowsFactory` can create:
    → `WindowsButton`
    → `WindowsCheckbox`
    → `WindowsMenu`

Differences from Factory Method Pattern:

1. **Number of products:**
   - Factory Method typically focuses on creating **one type of object** (e.g., only Button).
   - Abstract Factory creates **multiple related objects** (e.g., Button, Checkbox, Menu) through different methods.

2. **Grouping:**
   - Factory Method provides **one method** to create one object.
   - Abstract Factory provides **a set of related creation methods** (one per product type), grouped in a single interface.

3. **Consistency:**
   - Abstract Factory ensures that all created objects belong to the **same family** (e.g., all Mac or all Windows).
   - Factory Method has no such coordination between products.

4. **Client usage:**
   - With Abstract Factory, the client uses a **single factory instance** to get all related objects.
   - With Factory Method, the client may need multiple creators or subclasses to get different product types.

'''
