"""Elevator class (Context) for elevator states"""

from state.elevator_state import ElevatorState
from threading import RLock
from state.idle_state import IdleState
from typing import Set
from entities.request import Request
from typing import List
from observer.elevator_observer import ElevatorObserver
from exceptions.domain_exceptions import NoPendingRequestError


class Elevator:
    def __init__(self, elevator_id: str):
        self._elevator_id = elevator_id
        self._current_floor = 1
        self._current_state: ElevatorState = IdleState()
        self._up_requests: Set[int] = set()
        self._down_requests: Set[int] = set()
        self._observers: List[ElevatorObserver] = []
        self._lock = (
            RLock()
        )  # A reentrant lock allows the same thread to acquire the lock multiple times without deadlocking itself.

    # -------  Observer Management -------

    def add_observer(self, observer: ElevatorObserver) -> None:
        with self._lock:
            if observer not in self._observers:
                self._observers.append(observer)
                observer.update(self)  # initial update

    def remove_observer(self, observer: ElevatorObserver) -> None:
        with self._lock:
            if observer in self._observers:
                self._observers.remove(observer)

    def _notify_observers(self) -> None:
        with self._lock:
            for observer in self._observers:
                observer.update(self)

    # ------ Properties ------

    @property
    def direction(self):
        with self._lock:
            return self._current_state.direction

    @property
    def current_floor(self) -> int:
        with self._lock:
            return self._current_floor

    @property
    def elevator_id(self) -> str:
        return self._elevator_id

    # -------- State Handling -------

    def set_state(self, state: ElevatorState):
        with self._lock:
            self._current_state = state
            self._notify_observers()

    def move(self):
        with self._lock:
            self._current_state.move(self)

    def add_request(self, request: Request):
        with self._lock:
            self._current_state.add_request(self, request)

    # ------- Request Queues --------

    def has_up_requests(self):
        with self._lock:
            return len(self._up_requests) > 0

    def has_down_requests(self):
        with self._lock:
            return len(self._down_requests) > 0

    def add_up_request(self, floor: int) -> None:
        with self._lock:
            self._up_requests.add(floor)

    def add_down_request(self, floor: int) -> None:
        with self._lock:
            self._down_requests.add(floor)

    # ------ Movement ------

    def move_one_up_floor(self):
        with self._lock:
            self._current_floor += 1
            self._notify_observers()

    def move_one_down_floor(self):
        with self._lock:
            self._current_floor -= 1
            self._notify_observers()

    # ------ Request Selection ------

    def peek_next_up_request(self) -> int:
        """
        Returns the closest upward request without removing it.

        """
        with self._lock:
            if not self._up_requests:
                raise NoPendingRequestError("No upward requests available")

            return min(self._up_requests)

    def peek_next_down_request(self) -> int:
        """
        Returns the closest downward request without removing it.
        """
        with self._lock:
            if not self._down_requests:
                raise NoPendingRequestError("No downward requests available")

            return max(self._down_requests)

    def pop_next_up_request(self) -> int:
        """
        Removes and returns the closest upward request.
        """
        with self._lock:
            if not self._up_requests:
                raise NoPendingRequestError("No upward requests available")

            floor = min(self._up_requests)

            self._up_requests.remove(floor)
            return floor

    def pop_next_down_request(self) -> int:
        """
        Removes and returns the closest downward request.
        """
        with self._lock:
            if not self._down_requests:
                raise NoPendingRequestError("No downward requests available")

            floor = max(self._down_requests)
            self._down_requests.remove(floor)
            return floor
