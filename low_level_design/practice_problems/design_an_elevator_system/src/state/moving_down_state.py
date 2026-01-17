"""If Elevator Moving down- MovingDownState"""

from state.elevator_state import ElevatorState
from enums.direction import Direction
from enums.request_type import RequestType


class MovingDownState(ElevatorState):

    def move(self, elevator):

        # Lazy imports
        from state.moving_up_state import MovingUpState
        from state.idle_state import IdleState

        if not elevator.has_down_requests():
            if elevator.has_up_requests():
                elevator.set_state(MovingUpState())

            else:
                # idle state
                elevator.set_state(IdleState())

            return

        # has down request so lets execute it

        current_floor = elevator.current_floor
        next_floor = elevator.peek_next_down_request()

        if current_floor == next_floor:
            # pop it first
            elevator.pop_next_down_request()
            print(f"Elevator {elevator.elevator_id} stopped at floor {current_floor}")
            # edge case what if we have other requests

            if not elevator.has_down_requests():
                if elevator.has_up_requests():
                    elevator.set_state(MovingUpState())
                else:
                    elevator.set_state(IdleState())

            return

        # move one step down or go to next floor

        elevator.move_one_down_floor()

    def add_request(self, elevator, request):
        current_floor = elevator.current_floor
        target_floor = request.target_floor

        # fullfil the cabin request first

        if request.request_type == RequestType.CABIN_CALL:
            if target_floor < current_floor:  # accept down requests
                elevator.add_down_request(target_floor)
            else:
                # accept up request
                elevator.add_up_request(target_floor)
            return
        # accept hall requests

        if request.request_type == RequestType.HALL_CALL:
            if request.direction == Direction.DOWN and target_floor <= current_floor:
                # accept down requests
                elevator.add_down_request(target_floor)
            elif request.direction == Direction.UP:
                # accept up requests
                elevator.add_up_request(target_floor)

    @property
    def direction(self) -> Direction:
        return Direction.DOWN
