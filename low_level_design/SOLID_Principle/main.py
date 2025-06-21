"""
---------------SOLID Principle--------------
----------------------------------------------------------------------------------------
S- Single Responsibility Principle---->A class should have one, and only one, reason to change. This means that a class must have only one responsibility.
O- Open-Closed------> Existing Classes should be open for extension, but closed for modification or Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
L- Liskov Substitution Principle----> Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program
I- Interface Segregation Principle-----> By segregating the interfaces, each class only needs to implement the methods it actually requires. This not only makes the code more maintainable but also prevents clients from being forced to depend on methods they don't use.
D- Dependency Inversion Principle--------> High-level modules should not depend on low-level modules; both should depend on abstractions. This means that a particular class should not depend directly on another class, but on an abstraction (interface) of this class.
----------------------------------------------------------------------------------------
"""
#imports

from single_responsibility.single_responsibility import single_responsibility_fun as run_single_responsibilty
from open_closed_principles.open_closed import run_open_closed_
#code practice

if __name__ == "__main__":
    print("\n🔹 SINGLE RESPONSIBILITY PRINCIPLE\n")
    run_single_responsibilty()
    print()

    print("\n🔹 Open-Closed PRINCIPLE\n")
    run_open_closed_()
    print()
