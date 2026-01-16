"""Elevator State Interface"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from entities.request import Request
from enums.direction import Direction

if TYPE_CHECKING:
    from entities.elevator import Elevator


class ElevatorState(ABC):
    @abstractmethod
    def move(self, elevator: "Elevator"):
        pass

    @abstractmethod
    def add_request(self, elevator: "Elevator", request: Request):
        pass

    @property
    @abstractmethod
    def direction(self) -> Direction:
        pass
