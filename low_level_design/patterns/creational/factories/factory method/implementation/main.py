#implementation of factory design pattern
'''
Factory Design Pattern:- 
- It is a creational design pattern which is used in creating object of similar types.
- It is a creational design pattern that is used to create objects of related types.
- It hides the object creation logic from the client and lets a separate factory class decide which object to create based on input or conditions.

The Factory Method Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
It’s particularly useful in situations where:
    The exact type of object to be created isn't known until runtime.
    Object creation logic is complex, repetitive, or needs encapsulation.
    You want to follow the Open/Closed Principle — open for extension, closed for modification
Factory method lets you create different objects without tightly coupling your code to specific classes.

In simple words-
Here’s the idea:
    - You create a separate class—a “factory”—whose only job is to centralize and encapsulate object creation.
    
Instead of putting the burden of decision-making in a single place, we distribute object creation responsibilities across the system in a clean, organized way.

'''

def run_factory_design_pattern():
    print("\nFactory Design pattern")


if __name__=="__main__":
    run_factory_design_pattern()