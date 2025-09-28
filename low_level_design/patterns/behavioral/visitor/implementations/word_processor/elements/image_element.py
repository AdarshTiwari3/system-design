"""Image concrete class implementation of Element class"""

from elements.base_element import Element
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitors.visitor_base import Visitor

class ImageElement(Element):
    def __init__(self, image) -> None:
        self.image=image

    def accept(self, visitor: "Visitor"):
        print(f"\nImage Element")

        return visitor.visit_image(self)