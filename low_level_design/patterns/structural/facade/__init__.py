"""Facade Design Pattern:-
It is used when we have to hide the system complexity from the client.
or 
The Facade pattern is used to hide the complexity of a subsystem by providing a simplified interface to the client.

Example: A car — as a driver, you only use the accelerator, brake, and steering. Internally, these controls are connected to complex systems (engine control, braking system, steering mechanism), but the driver does not need to understand or interact with those complexities.

The Facade is there to offer simplicity, but clients are still free to access the underlying system directly.
It’s particularly useful in situations where:
    -Your system contains many interdependent classes or low-level APIs.
    -The client doesn’t need to know how those parts work internally.
    -You want to reduce the learning curve or coupling between clients and complex systems.
"""