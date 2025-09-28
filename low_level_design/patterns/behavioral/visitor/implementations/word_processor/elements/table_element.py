"""Implementation of table element concrete class of Element"""

from elements.base_element import Element
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitors.visitor_base import Visitor

class TableElement(Element):
    def __init__(self, data: list[list[str]]) -> None:
        self.data=data

    def accept(self, visitor: "Visitor"):
        print(f"\nTable Element")
        return visitor.visit_table(self)