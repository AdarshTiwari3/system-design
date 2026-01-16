"""
Observer interface for receiving elevator state updates.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.elevator import (
        Elevator,
    )  # Lazy import to avoid circular dependency with Elevator


class ElevatorObserver(ABC):
    @abstractmethod
    def update(self, elevator: "Elevator") -> None:
        """Called whenever the elevator state changes."""
        pass
