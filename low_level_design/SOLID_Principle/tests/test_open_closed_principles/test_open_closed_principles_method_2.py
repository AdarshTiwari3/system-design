import pytest
from low_level_design.SOLID_Principle.open_closed_principles.shapes import Circle, Rectangle, Shape
from low_level_design.SOLID_Principle.open_closed_principles.discounts import StudentDiscount, SeniorDiscount, Discount

'''
Test files and functions must start with test_
'''

# Shape Tests

def test_circle_area():
    circle = Circle(radius=5)
    expected_area = 3.14 * 5 ** 2
    assert circle.calculate_area() == pytest.approx(expected_area, rel=1e-6) #rel=1e-6 means relative tolerance of 0.000001.

def test_rectangle_area():
    rect = Rectangle(length=4, width=6)
    expected_area = 4 * 6
    assert rect.calculate_area() == pytest.approx(expected_area, rel=1e-6)

def test_shape_abstract_class():
    with pytest.raises(TypeError):
        Shape()  # Cannot instantiate abstract class


# Discount Tests

def test_student_discount():
    discount = StudentDiscount()
    price = 1000
    expected_price = price * 0.9
    assert discount.apply(price) == pytest.approx(expected_price, rel=1e-6)

def test_senior_discount():
    discount = SeniorDiscount()
    price = 1000
    expected_price = price * 0.85
    assert discount.apply(price) == pytest.approx(expected_price, rel=1e-6)

def test_discount_abstract_class():
    with pytest.raises(TypeError):
        Discount()  # Discount is abstract, instantiation should raise TypeError
