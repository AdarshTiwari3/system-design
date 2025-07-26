"""
The Flyweight Design Pattern is a structural design pattern that focuses on efficiently sharing common parts of object state across many objects to reduce memory usage and boost performance.

It’s particularly useful in situations where:

You need to create a large number of similar objects, but most of their data is shared or repeated.

Storing all object data individually would result in high memory consumption.

You want to separate intrinsic state (shared, reusable data) from extrinsic(unique) state (context-specific, passed in at runtime).
"""