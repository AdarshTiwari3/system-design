"""Nearest Elevator Allocation Strategy"""

from strategies.allocation_strategy import AllocationStrategy
from entities.elevator import Elevator
from entities.request import Request
from typing import List
from exceptions.domain_exceptions import NoElevatorAvailableError
import math


class NearestElevatorStrategy(AllocationStrategy):
    def select_elevator(self, request: Request, elevators: List[Elevator]):
        if not elevators:
            raise NoElevatorAvailableError("No Elevators Available")

        source_floor = request.source_floor

        return min(
            elevators,
            key=lambda elevator: abs(
                elevator.current_floor - source_floor
            ),  # checks the min distance from each current floor of each elevator and choose the best
        )

    """Does the same as lambda function but using only simple method to do it"""

    def _find_nearest_elevator(self, request: Request, elevators: List[Elevator]):
        if not elevators:
            raise NoElevatorAvailableError("Elevators not available")

        source_floor = request.source_floor  # origin floor of request or pickup floor

        best_elevator = None

        min_distance = math.inf

        for elevator in elevators:
            distance = abs(elevator.current_floor - source_floor)

            if distance < min_distance:
                min_distance = distance
                best_elevator = elevator

        return best_elevator
