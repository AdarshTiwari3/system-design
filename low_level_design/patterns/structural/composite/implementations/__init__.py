"""
- Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.
- Using the Composite pattern makes sense only when the core model of your app can be represented as a tree.
- Use the pattern when you want the client code to treat both simple and complex elements uniformly.


  1. For example, imagine that you have two types of objects: Products and Boxes. A Box can contain several Products as well as a number of smaller Boxes. These little Boxes can also hold some Products or even smaller Boxes, and so on.
    - The Composite pattern suggests that you work with Products and Boxes through a common interface which declares a method for calculating the total price.
  2. Graphic editors (where a shape can be a line or a group of shapes)

     File systems (where a directory can contain files or other directories)

     Organization hierarchies (employee vs manager who has other employees)


            Component
              ↑
        ┌─────┴─────┐
       Leaf     Composite
                    │
             ┌──────┴───────┐
            Component  Component ...


"""