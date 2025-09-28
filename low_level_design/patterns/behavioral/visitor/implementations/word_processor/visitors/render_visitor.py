"""Implementation of concrete visitor- Render Visitor"""
from __future__ import annotations

from elements.paragraph import Paragraph
from elements.image_element import ImageElement
from elements.table_element import TableElement
from visitors.visitor_base import Visitor


class RenderVisitor(Visitor):
    def visit_image(self, image: ImageElement) -> None:
        print(f"\n[Render] image - {image.image}")
    
    def visit_paragraph(self, paragraph: Paragraph) -> None:
        print(f"\n[Render] paragraph - {paragraph.text}")
    
    def visit_table(self, table: TableElement) -> None:
        print(f"\n[Render] table - {table.data}")
        
        """Print the table on the screen it is in a kind of matrix form"""
        for row in table.data:
                    print(" | ".join(row))