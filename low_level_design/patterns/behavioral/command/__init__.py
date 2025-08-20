"""Command Design Pattern:
The Command Design Pattern is a behavioral pattern that turns a request into a standalone object, allowing you to parameterize actions, queue them, log them, or support undoable operations — all while decoupling the sender from the receiver.

It’s particularly useful in situations where:

You want to encapsulate operations as objects.

You need to queue, delay, or log requests.

You want to support undo/redo functionality.

You want to decouple the object that invokes an operation from the one that knows how to perform it.

We need to treat each command (e.g., “turn on light”, “set thermostat to 22°C”) as a standalone object — something that encapsulates:

What to do
Which device it affects
How to execute it
(Optionally) How to undo it


"""