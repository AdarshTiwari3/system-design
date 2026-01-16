"""Elevator (cabin) Display Screen Concrete Implementation"""

from observer.elevator_observer import ElevatorObserver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.elevator import Elevator


class ElevatorDisplayScreen(ElevatorObserver):
    """Represents the elevator display screen that shows current floor and direction"""

    def update(self, elevator: Elevator) -> None:
        self._show(elevator)

    def _show(self, elevator: Elevator) -> None:
        print(
            f"[Display] Elevator { elevator.elevator_id} | "
            f"Floor: {elevator.current_floor} | "
            f"Direction: {elevator.direction.name}"
        )
