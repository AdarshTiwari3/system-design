"""

Strategy design pattern is one of the behavioral design pattern. Strategy pattern is used when we have multiple algorithm for a specific task and client decides the actual implementation to be used at runtime
The Strategy Design Pattern is a behavioral design pattern that lets you define a family of algorithms, put each one into a separate class, and makes their objects interchangeable — allowing the algorithm to vary independently from the clients that use it.
It’s particularly useful in situations where:

You have multiple ways to perform a task or calculation.

The behavior of a class needs to change dynamically at runtime.

You want to avoid cluttering your code with conditional logic (like if-else or switch statements) for every variation.

The Strategy Pattern solves by encapsulating each behavior in its own class and delegating the responsibility to the right strategy at runtime — keeping your core logic clean, extensible, and testable.
In short-
    👉  When multiple subclasses share the same behavior or method, avoid duplicating it — instead, extract it into a separate class using the Strategy Pattern, making the behavior reusable, interchangeable, and compliant with LSP.

 
"""