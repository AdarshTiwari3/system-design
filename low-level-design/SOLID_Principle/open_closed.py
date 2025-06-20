#code practice of open_closed

'''

Definition- Existing Classes should be open for extension, but closed for modification.
This means the design of a software entity should be such that you can introduce new functionality or behavior without modifying the existing code since changing the existing code might introduce bugs.

'''


#example-1

from abc import ABC, abstractmethod #abstract class

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        #pi*r*r
        return 3.14*self.radius**2

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width
        
#use any
def open_closed_func():
    circle = Circle(5)
    print(circle.calculate_area())

    rectangle = Rectangle(4, 6)
    print(rectangle.calculate_area())

def run_open_closed_():
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]

    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.calculate_area():.2f}")
