"""
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

or 

The Observer Design Pattern is a behavioral pattern that defines a one-to-many dependency between objects — so that when one object (the subject) changes its state, all its dependents (observers) are automatically notified and updated
It’s particularly useful in situations where:

   - You have multiple parts of the system that need to react to a change in one central component.

   - You want to decouple the publisher of data from the subscribers who react to it.

   - You need a dynamic, event-driven communication model without hardcoding who is listening to whom.

The Observer Design Pattern provides a clean and flexible solution to the problem of broadcasting changes from one central object (the Subject) to many dependent objects (the Observers) — all while keeping them loosely coupled.
whenever an important event happens to the publisher, it goes over its subscribers and calls the specific notification method on their objects.

Use the pattern when some objects in your app must observe others, but only for a limited time or in specific cases.



initial uml diagram credit- refactoring guru

"""


