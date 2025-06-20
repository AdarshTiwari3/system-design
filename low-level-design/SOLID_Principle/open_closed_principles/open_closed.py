"""
Open/Closed Principle (OCP) Practice

Definition:
Existing classes should be open for extension, but closed for modification.
This allows adding new functionality without changing existing tested code.
"""

from abc import ABC, abstractmethod
from typing import List


# ---------------- Example 1: Shapes ---------------- #

class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width


# ---------------- Example 2: Discounts ---------------- #

class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass

class StudentDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.9

class SeniorDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.85


# ---------------- Runner Functions ---------------- #

def open_closed_func():
    print("\n🔹 Shape Calculations (Function 1)")
    circle = Circle(5)
    print(f"Circle Area: {circle.calculate_area():.2f}")

    rectangle = Rectangle(4, 6)
    print(f"Rectangle Area: {rectangle.calculate_area():.2f}")

def run_open_closed_():
    print("\n🔹 Shape Area Calculation (Function 2)")
    shapes: List[Shape] = [
        Circle(5),
        Rectangle(4, 6)
    ]

    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.calculate_area():.2f}")

    print("\n🔹 Discount Price Calculation")
    student = StudentDiscount()
    senior = SeniorDiscount()

    print(f"Student Price (on ₹100): INR {student.apply(100):.2f}")
    print(f"Senior Price  (on ₹100): INR {senior.apply(100):.2f}")


    print(f"Student Price (on ₹100): INR {student.apply(100):.2f}")
