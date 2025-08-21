"""State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.
The State Design Pattern is a behavioral design pattern that lets an object change its behavior when its internal state changes, as if it were switching to a different class at runtime

It’s particularly useful in situations where:

    - An object can be in one of many distinct states, each with different behavior.
    - The object’s behavior depends on current context, and that context changes over time.
    - You want to avoid large, monolithic if-else or switch statements that check for every possible state.

or 

The State pattern allows an object (the Context) to alter its behavior when its internal state changes. The object appears to change its class because its behavior is now delegated to a different state object.

"""