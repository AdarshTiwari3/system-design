"""
Robot Game using Flyweight Design Pattern

In this game, we need to create many robot objects. But if we create a new object every time, 
it can waste a lot of memory—especially when most robots look or behave the same.

To solve this, we use the Flyweight Design Pattern.

Flyweight helps us reuse existing objects instead of creating new ones every time.

It separates robot properties into two types:

1. **Intrinsic State (Shared)**:
   - These are common properties shared by all robots of the same type.
   - Example: robot type (e.g., 'Small', 'Large'), shape, model, or color.

2. **Extrinsic State (Unique)**:
   - These are the changing or external properties specific to each robot.
   - Example: its position on the battlefield (like x and y coordinates), health, or status.

We use a **RobotFactory**(FlyweightFactory) to manage and reuse shared (intrinsic) robot objects.
The client (game logic) only needs to pass the unique data (extrinsic), like position,
and the factory gives back a shared robot object to use.

This approach saves memory and improves performance.
"""
