"""
The Builder Design Pattern is a creational design pattern that lets you construct complex objects step-by-step, 
separating the construction logic from the final representation.

It’s particularly useful in situations where:
- An object requires many optional fields, and not all of them are needed every time.
- You want to avoid telescoping constructors or large constructors with multiple parameters e.g - multiple params in constructors to create an object
- The object construction process involves multiple steps that need to happen in a particular order.
-  You have a complex object to construct, like a request with many optional fields.

You have a complex object to construct, like a request with many optional fields and some required fields

In the Builder Pattern:
- The construction logic is encapsulated in a Builder.
- The final object (the "Product") is created by calling a build() method.
- The object itself typically has a private or package-private constructor, forcing construction through the builder.

To understand the Builder Pattern, let’s break down its vital components:

- Director: Guides complex object creation, ensuring cooperation among builders.
- Builder Interface: Blueprint for complex object construction, enforcing method consistency.
- Concrete Builder: Workers specializing in specific complex object parts.
- Product: End result, varies based on the concrete builder used.

lets take a real life example-
lets suppose we have to make a house, so builder method says create it step by step as-
 - add_wall()
 - add_doors()
 - add_roof()
 - add_window()

 we create these methods and call it using builder class to build this as-
    builder.add_walls()
    builder.add_doors()
    builder.add_windows()
    builder.add_roof()
    house = builder.build()

"""