"""Intersection States- Like traffic flow in EastWest Green light and NorthSouth Green Light"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING: #lazy import
    from core.intersection_controller import IntersectionController
    
class IntersectionState(ABC):
    @abstractmethod
    def handle(self, context: "IntersectionController"):
        pass