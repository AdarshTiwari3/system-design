"""
Prototype Design Pattern:- The Prototype Design Pattern is a creational design pattern that lets you create new objects by cloning existing ones, instead of instantiating them from scratch.

It’s particularly useful in situations where:
 - Creating a new object is expensive, time-consuming, or resource-intensive.
 - You want to avoid duplicating complex initialization logic.
 - You need many similar objects with only slight differences.

* The Prototype Pattern allows you to create new instances by cloning a pre-configured prototype object, ensuring consistency while reducing boilerplate and complexity.

* Instead of having external code copy or recreate the object, the object itself knows how to create its clone. It exposes a clone() or copy() method that returns a new instance with the same data.
You want to create a new object by copying an existing object (a prototype), instead of building it from scratch
- An object that supports cloning is called a prototype. 
In short- 
    - When we want to reuse an existing object’s structure and behavior by making a copy of it, and then tweak the copy as needed, we use the Prototype Design Pattern.

Real Life Example- 
You're using a design tool like Figma or Photoshop. You create a button with:

Background color: Blue

Text: "Submit"

Font: Bold

Size: 14px

Now, you want to create 10 more buttons that are almost the same, but maybe:

One says "Cancel"

Another is red

Another has different size

The best example of Prototype Design Pattern would be differenent Template of Documents
"""