#implmentation

'''
Singleton Pattern is a creational design pattern that guarantees a class has only one instance and provides a global point of access to it.
It involves only one class which is responsible for instantiating itself, making sure it creates not more than one instance.
example: thread pools, caches, loggers etc.
To implement the singleton pattern, we must prevent external objects from creating instances of the singleton class.
Additionally, we need to provide a method for external objects to access the singleton object.

This can be achieved by making the constructor private and providing a static method for external objects to access it.
'''

'''
Singleton ensures that only one instance of a class exists throughout the application and provides a global access point to that instance.

'''