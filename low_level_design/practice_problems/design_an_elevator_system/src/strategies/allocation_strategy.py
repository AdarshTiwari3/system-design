"""Allocation Strategy Interface- Pick the elevator with minimum distance to request floor."""

from abc import ABC, abstractmethod
from entities.request import Request
from typing import List
from entities.elevator import Elevator


class AllocationStrategy(ABC):
    """
    Strategy interface for selecting an elevator for a request.
    """

    @abstractmethod
    def select_elevator(self, request: Request, elevators: List[Elevator]) -> Elevator:
        pass
