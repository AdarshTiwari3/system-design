"""Implementation of visitors concrete class- Spellchecker Visitor class"""
from __future__ import annotations

from visitors.visitor_base import Visitor
from elements.paragraph import Paragraph
from elements.image_element import ImageElement
from elements.table_element import TableElement

class SpellCheckerVisitor(Visitor):
    def visit_image(self, image:ImageElement):
        print(f"\n[SpellCheck] skipping spell checks in Image- {image.image}")
    
    def visit_paragraph(self, paragraph:Paragraph):
        print(f"\n[SpellCheck] checking spellings in Paragraph - {paragraph.text}")
    
    def visit_table(self, table: TableElement):
        print(f"\n[SpellCheck] checking table cells- {table.data}")

        for row in table.data:
            for cell in row:
                  print(f" - Checking: {cell}")