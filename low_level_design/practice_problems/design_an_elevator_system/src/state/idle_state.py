"""Idle state of an Elevator"""

from enums.direction import Direction
from entities.request import Request
from state.elevator_state import ElevatorState


class IdleState(ElevatorState):
    def move(self, elevator):
        if elevator.has_up_requests():
            from state.moving_up_state import (
                MovingUpState,
            )  # lazy imports to avoid circular dependencies

            elevator.set_state(MovingUpState())

        elif elevator.has_down_requests():
            from state.moving_down_state import MovingDownState

            elevator.set_state(MovingDownState())

    def add_request(self, elevator, request: Request):
        current_floor = elevator.current_floor
        target_floor = request.target_floor

        if target_floor > current_floor:
            elevator.add_up_request(target_floor)

        elif target_floor < current_floor:
            elevator.add_down_request(target_floor)
        else:
            # same floor
            raise ValueError(
                f"Invalid request: target floor {target_floor} "
                f"is same as current floor {current_floor}"
            )

    @property
    def direction(self) -> Direction:
        return Direction.IDLE
