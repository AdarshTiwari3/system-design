"""Implementation of visitor interface"""

from abc import ABC , abstractmethod

class Visitor(ABC):

    @abstractmethod
    def visit_paragraph(self, paragraph) -> None:
        pass

    @abstractmethod
    def visit_image(self, image) -> None:
        pass


    @abstractmethod
    def visit_table(self, table) -> None:
        pass