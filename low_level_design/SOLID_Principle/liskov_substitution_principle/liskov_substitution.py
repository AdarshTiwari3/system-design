from abc import ABC, abstractmethod

'''
Credit- Internet

Liskov-Substitution Principle: Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.
Goal- Ensure subtypes behave correctly when used as base types
Focus- Behavioral correctness in inheritance or substitution
What it protects- Client code from runtime errors or incorrect behavior

LSP is about correct behavior in inheritance — "if a subclass is used, everything should still work."
LSP is foundational to achieve OCP. 
LSP is about making sure new extensions don’t break the behavior promised by the base class.
OCP code also follows LSP — because it must. If LSP breaks, OCP is meaningless.

'''
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass

class Walkable(ABC):
    @abstractmethod
    def walk(self) -> str:
        pass

class Sparrow(Bird, Flyable):
    def eat(self): return "Sparrow eats seeds"
    def fly(self): return "Sparrow can fly"

class Ostrich(Bird, Walkable):
    def eat(self): return "Ostrich eats plants"
    def walk(self): return "Ostrich can walk"

# Liskov-compliant function
def describe_bird(bird: Bird):
    print(bird.eat())

def describe_flyer(flyer: Flyable):
    print(flyer.fly())

def describe_walker(walker: Walkable):
    print(walker.walk())

def run_liskov_substitution_func():
    
    sparrow = Sparrow()
    ostrich = Ostrich()

    # Both can be substituted as Bird
    describe_bird(sparrow)
    describe_bird(ostrich)

    # Substitution for Flyable
    describe_flyer(sparrow)

    # Substitution for Walkable
    describe_walker(ostrich)

