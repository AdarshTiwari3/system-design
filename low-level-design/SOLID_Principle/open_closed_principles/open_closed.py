"""
Open/Closed Principle (OCP) Practice

Definition:
Existing classes should be open for extension, but closed for modification.
This allows adding new functionality without changing existing tested code.
"""

from typing import List
from open_closed_principles.shapes import Shape, Circle, Rectangle
from open_closed_principles.discounts import StudentDiscount, SeniorDiscount

def run_open_closed_():
    print("🔸 Shape Area Calculations")
    shapes: List[Shape] = [
        Circle(5),
        Rectangle(4, 6)
    ]

    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.calculate_area():.2f}")

    print("\n🔸 Discount Price Calculations")
    student = StudentDiscount()
    senior = SeniorDiscount()
    price=1000
    print(f"Student Discount on ₹{price}: ₹{student.apply(price):.2f}")
    print(f"Senior Discount on ₹{price}: ₹{senior.apply(price):.2f}")
