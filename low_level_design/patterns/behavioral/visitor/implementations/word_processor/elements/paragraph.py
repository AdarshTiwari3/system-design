"""Paragraph Element implementation"""
from elements.base_element import Element
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitors.visitor_base import Visitor

class Paragraph(Element):

    def __init__(self, text: str) -> None:
        self.text=text

    def accept(self, visitor: "Visitor"):
        print(f"\nParagraph Element")
        return visitor.visit_paragraph(self)