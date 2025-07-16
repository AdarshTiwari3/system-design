"""Bridge Design Pattern:- 

The Bridge Design Pattern is a structural pattern that lets you decouple an abstraction from its implementation, allowing the two to vary independently.
The Bridge Pattern splits a class into two separate hierarchies:

    - One for the abstraction (e.g., shape, UI control)

    - One for the implementation (e.g., rendering engine, platform)

These two hierarchies are "bridged" via composition — not inheritance — allowing you to mix and match independently.
In the Bridge Pattern, "abstraction has-a implementation" — the abstraction delegates work to an implementor object.

or 

The Bridge design pattern is a structural design pattern that decouples an abstraction from its implementation, allowing them to vary independently. It involves creating two separate hierarchies: one for the abstraction (the high-level interface) and one for the implementation (the low-level details), connected via a bridge (typically an interface or abstract class).

in short - 
Abstraction and Implementation are connected via a bridge, so they can vary independently.

Relationship between Abstraction and Implementor:-
The Bridge pattern uses composition (not aggregation) because the Abstraction requires a strong ownership of the Implementor — it cannot function properly without it.
"""

