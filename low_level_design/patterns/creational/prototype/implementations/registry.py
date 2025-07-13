#this is optional 
"""It stores a collection of named prototypes"""
from prototype import Prototype
class PrototypeRegistry:
    def __init__(self) -> None:
        self._prototype = {}

    def register(self, key, prototype):
        """Store a prototype under a key."""
        if not isinstance(prototype, Prototype):
            raise TypeError("Prototype must implement the Prototype interface")
        self._prototype[key] = prototype

    def unregister(self, key):
        """Remove a prototype from the registry."""
        if key in self._prototype:
            del self._prototype[key]

    def clone(self, key):
        """Clone the prototype associated with the given key."""
        prototype = self._prototype.get(key) # Holds objects that implement the Prototype interface
        if prototype:
            return prototype.clone()
        raise ValueError(f"No prototype registered under key: {key}")
