"""Elevator Controller Implementation"""

from typing import List
from entities.elevator import Elevator
from strategies.allocation_strategy import AllocationStrategy
from entities.request import Request
from exceptions.domain_exceptions import NoElevatorAvailableError, InvalidRequestError


class ElevatorController:
    def __init__(
        self, elevators: List[Elevator], strategy: AllocationStrategy, total_floors: int
    ):
        self._elevators = elevators
        self._strategy = strategy
        self._total_floors = total_floors

    def assign_request(self, request: Request) -> None:
        """Assigns a request to the most suitable elevator using the strategy."""
        # Validate floors

        if not (1 <= request.source_floor <= self._total_floors):
            raise InvalidRequestError(f"Invalid source floor: {request.source_floor}")

        if not (1 <= request.target_floor <= self._total_floors):
            raise InvalidRequestError(f"Invalid target floor: {request.target_floor}")

        # Select Elevator

        elevator = self._strategy.select_elevator(request, self._elevators)

        if not elevator:
            raise NoElevatorAvailableError("No suitable elevator found")

        # add the request

        elevator.add_request(request)

    def move_elevators(self) -> None:
        """Moves all elevators one step based on their current state."""
        for elevator in self._elevators:
            elevator.move()
