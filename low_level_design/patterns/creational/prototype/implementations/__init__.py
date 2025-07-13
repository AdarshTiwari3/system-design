"""Implementation of prototype design pattern- An object that supports cloning is called a prototype."""

"""
1. Prototype- The Prototype interface declares the cloning methods. In most cases, it’s a single clone method.
2. Concreate Prototypes- The Concrete Prototype class implements the cloning method. In addition to copying the original object’s data to the clone, this method may also handle some edge cases of the cloning process related to cloning linked objects, untangling recursive dependencies, etc.
3. Client- The Client can produce a copy of any object that follows the prototype interface.
4. Prototype Registry(Optional)- The Prototype Registry provides an easy way to access frequently-used prototypes. It stores a set of pre-built objects that are ready to be copied. The simplest prototype registry is a name → prototype hash map. However, if you need better search criteria than a simple name, you can build a much more robust version of the registry
"""
