#simple factory implementation
'''This isn't the actual factory method pattern, but rather an improvement over straightforward object creation. It helps illustrate why the factory method is beneficial.
Consider a scenario where we have a Pizza class and multiple types of pizzas as subclasses. If we create each pizza type directly using conditional statements (like if-else), the code becomes tightly coupled and violates the Open-Closed Principle from SOLID — which states that classes should be open for extension but closed for modification.
To address this, instead of instantiating pizza types directly inside conditionals, we can introduce a SimplePizzaFactory. This factory class will contain a createPizza() method, responsible for creating and returning the correct pizza object based on the input condition. This design promotes loose coupling and better scalability.

'''

#or 

'''
A Simple Factory is not an official design pattern but a commonly used approach to improve code organization. Suppose we have a base Pizza class and several specific types of pizza. If we directly instantiate different pizza types using if-else statements throughout the code, it results in tight coupling and violates the Open-Closed Principle — meaning the system is not easily extensible without modifying existing code.
To address this, we introduce a SimplePizzaFactory class. It contains a method like createPizza() that takes a type or identifier as input and returns the appropriate Pizza object. This way, the creation logic is centralized, making the codebase cleaner, more modular, and easier to extend without modifying client code.
'''
#Basically, the client (here PizzaStore) will interact with the simple factory, which will be responsible for object creation on the basis of some condition. This will provide the feature of encapsulation (i.e., it will hide the actual implementation from the client).