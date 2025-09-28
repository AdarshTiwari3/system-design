"""Implementation of visitor interface"""

from abc import ABC , abstractmethod
from elements.paragraph import Paragraph
from elements.image_element import ImageElement
from elements.table_element import TableElement

class Visitor(ABC):

    @abstractmethod
    def visit_paragraph(self, paragraph:Paragraph) -> None:
        pass

    @abstractmethod
    def visit_image(self, image:ImageElement) -> None:
        pass


    @abstractmethod
    def visit_table(self, table:TableElement) -> None:
        pass