"""Base Element interface which defines the accept method for Visitors."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitors.visitor_base import Visitor


class Element(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor"):
        pass