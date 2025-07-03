
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

#this is a demo file of all type of singleton design pattern


from singleton_lazy_initialization import run_lazy_initialization_singleton
from singleton_eager_initialization import run_eager_singleton
from thread_safe_singleton import run_thread_safe_singleton as run_thread_safe_and_double_checked_lock

if __name__=="__main__":

    print("\nLazy Initialization Singleton\n")
    run_lazy_initialization_singleton()
    print("\n")

    print("\nEager Initialization Singleton\n")
    run_eager_singleton()
    print("\n")

    print("\nThread Safe and Double checked lock pattern Singleton\n")
    run_thread_safe_and_double_checked_lock()
    print("\n")