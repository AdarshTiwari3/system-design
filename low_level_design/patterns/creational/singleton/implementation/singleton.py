#implementation of singleton design pattern

"""
Singleton Design Pattern in Python.

__new__ vs __init__:

- __init__ is the initializer, not the true constructor. It is called after the object is created.
- __new__ is the actual constructor responsible for creating the object.
- __new__ is a static method that receives 'cls' and returns an instance.
- __init__ receives 'self' and initializes the object.
- __new__ is called before __init__ and is used here to implement the Singleton pattern.

Steps in implementing Singleton:
1. Create a private class variable to hold the instance.
2. Use __new__ to control object creation and ensure only one instance exists.
3. A getInstance() method is optional in Python, since instantiation can be controlled via __new__.
"""

from typing_extensions import Self


class Singleton:
    _instance=None   #using class variable and keeping private although not using double underscore, it will work with double underscore also , but in python we treat single underscore variable is used for internal purpose only like private

    def __new__(cls,*args) -> Self: #Singleton
        if cls._instance==None:
            # if instance is none means no object has been created then only it will create object otherwise not
            cls._instance=super().__new__(cls)

        return cls._instance
    
    def __init__(self, value=None):
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = True  # prevent reinitialization

    @classmethod
    def get_instance(cls):
        return cls._instance

obj1=Singleton("first instance")
obj2=Singleton("second instance")

print(obj1 is obj2)
print(obj1.value)
print(obj2.value) #will still give first instance
