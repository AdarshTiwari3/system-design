"""Elevator class (Context) for elevator states"""

from state.elevator_state import ElevatorState
from threading import RLock
from state.idle_state import IdleState
from typing import Set
from entities.request import Request


class Elevator:
    def __init__(self, elevator_id: str):
        self._elevator_id = elevator_id
        self._current_floor = 1
        self._current_state = IdleState()
        self._up_requests: Set[int] = set()
        self._down_requests: Set[int] = set()
        self._lock = (
            RLock()
        )  # A reentrant lock allows the same thread to acquire the lock multiple times without deadlocking itself.

    @property
    def direction(self):
        with self._lock:
            return self._current_state.direction

    @property
    def current_floor(self) -> int:
        with self._lock:
            return self._current_floor

    @property
    def elevator_id(self) -> int:
        return self._elevator_id

    def set_state(self, state: ElevatorState):
        with self._lock:
            self._current_state = state

    def move(self):
        with self._lock:
            self._current_state.move(self)

    def add_request(self, request: Request):
        with self._lock:
            self._current_state.add_request(self, request)

    def has_up_requests(self):
        return len(self._up_requests) > 0

    def has_down_requests(self):
        return len(self._down_requests) > 0

    def add_up_request(self, floor: int) -> None:
        self._up_requests.add(floor)

    def add_down_request(self, floor: int) -> None:
        self._down_requests.add(floor)

    def move_one_up_floor(self):
        self._current_floor += 1

    def move_one_down_floor(self):
        self._current_floor -= 1

    def peek_next_up_request(self) -> int:
        """
        Returns the closest upward request without removing it.
        """
        return min(self._up_requests)

    def peek_next_down_request(self) -> int:
        """
        Returns the closest downward request without removing it.
        """
        return max(self._down_requests)

    def pop_next_up_request(self) -> int:
        """
        Removes and returns the closest upward request.
        """
        floor = min(self._up_requests)

        self._up_requests.remove(floor)
        return floor

    def pop_next_down_request(self) -> int:
        """
        Removes and returns the closest downward request.
        """
        floor = max(self._down_requests)
        self._down_requests.remove(floor)
        return floor
