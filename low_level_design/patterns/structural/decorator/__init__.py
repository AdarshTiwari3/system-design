"""
The Decorator Design Pattern is a structural pattern that lets you dynamically add new behavior or responsibilities to objects without modifying their underlying code.

It’s particularly useful in situations where:

- You want to extend the functionality of a class without subclassing it.

- You need to compose behaviors at runtime, in various combinations.

- You want to avoid bloated classes filled with if-else logic for optional features.

or 
The Decorator Pattern allows you to add responsibilities to objects dynamically, without altering their structure or modifying their original code.
At its core, the pattern relies on wrapping an object inside another object (a decorator) that implements the same interface and adds new behavior before or after delegating to the wrapped object.
This creates a layered effect, where decorators can be stacked to apply multiple enhancements without creating a complex inheritance tree.
Real-World Analogy:- 
  -Think of a plain coffee. Now add milk. Now add sugar.



"""