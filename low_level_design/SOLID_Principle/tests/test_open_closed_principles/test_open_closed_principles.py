import pytest
from low_level_design.SOLID_Principle.open_closed_principles.shapes import Circle, Rectangle, Shape
from low_level_design.SOLID_Principle.open_closed_principles.discounts import StudentDiscount, SeniorDiscount, Discount

class TestShapes:
    def test_circle_area(self):
        circle = Circle(5)
        expected = 3.14 * 25
        assert abs(circle.calculate_area() - expected) < 1e-6

    def test_rectangle_area(self):
        rect = Rectangle(4, 6)
        expected = 24
        assert abs(rect.calculate_area() - expected) < 1e-6

    def test_shape_cannot_instantiate(self):
        with pytest.raises(TypeError):
            Shape() # this can't be possible because abstract class can't have object

class TestDiscounts:
    def test_student_discount(self):
        discount = StudentDiscount()
        assert abs(discount.apply(1000) - 900) < 1e-6

    def test_senior_discount(self):
        discount = SeniorDiscount()
        assert abs(discount.apply(1000) - 850) < 1e-6

    def test_discount_cannot_instantiate(self):
        with pytest.raises(TypeError):
            Discount()
