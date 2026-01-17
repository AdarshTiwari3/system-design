"""If Elevator moving in up direction - MovingUpState"""

from state.elevator_state import ElevatorState
from enums.direction import Direction

from enums.request_type import RequestType


class MovingUpState(ElevatorState):
    """
    Elevator is moving upward serving upward requests.
    """

    def move(self, elevator):
        """
        Move elevator one floor upward and serve requests if needed.

        """
        # lazy imports
        from state.moving_down_state import MovingDownState
        from state.idle_state import IdleState

        if not elevator.has_up_requests():
            if elevator.has_down_requests():

                elevator.set_state(MovingDownState())

            else:

                elevator.set_state(IdleState())
            return

        current_floor = elevator.current_floor
        next_floor = elevator.peek_next_up_request()

        if current_floor == next_floor:
            elevator.pop_next_up_request()
            print(f"Elevator {elevator.elevator_id} stopped at floor {current_floor}")

            if not elevator.has_up_requests():
                if elevator.has_down_requests():
                    elevator.set_state(MovingDownState())
                else:
                    elevator.set_state(IdleState())
            return
        elevator.move_one_up_floor()

    def add_request(self, elevator, request):
        """
        Handle incoming request while moving up.
        """

        current_floor = elevator.current_floor
        target_floor = request.target_floor

        # Internal requests always accepted
        if request.request_type == RequestType.CABIN_CALL:
            if target_floor > current_floor:
                # move up
                elevator.add_up_request(target_floor)

            else:
                # move down
                elevator.add_down_request(target_floor)
                return

        # External requests (HALL CALL)
        if request.request_type == RequestType.HALL_CALL:
            if request.direction == Direction.UP and target_floor >= current_floor:
                elevator.add_up_request(target_floor)

            elif request.direction == Direction.DOWN:
                elevator.add_down_request(target_floor)

    @property
    def direction(self) -> Direction:
        return Direction.UP
