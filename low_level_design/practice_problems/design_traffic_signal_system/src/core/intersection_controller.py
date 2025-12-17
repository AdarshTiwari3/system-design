from typing import Dict
from state.intersection_state_interface import IntersectionState
from state.east_west_green_state import EastWestGreenState
from core.traffic_light import TrafficLight
from enums.direction import Direction
import threading


class IntersectionController:
    def __init__(self, intersection_id:str, green_time: int, yellow_time: int, traffic_lights: Dict[Direction, TrafficLight]):
        self._id=intersection_id
        self._traffic_lights=traffic_lights
        self._green_time=green_time
        self._yellow_time=yellow_time
        self._current_state: IntersectionState =EastWestGreenState()
        self._is_running=True
        self._emergency_active = False
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)


    def get_id(self) -> str:
        return self._id
    
    def get_current_state(self) -> IntersectionState:
        with self._lock:
            return self._current_state

    def set_current_state(self, state: IntersectionState):
        with self._lock:
            self._current_state = state
            self._condition.notify_all() #Something important changed — wake up NOW from time.sleep()

    def get_green_time(self) -> int:
        return self._green_time
    
    def get_yellow_time(self) -> int:
        return self._yellow_time
    
    def get_light(self, direction: Direction) -> TrafficLight:
        return self._traffic_lights[direction]
    
    def run(self):
        print(f"Starting Intersection Controller [{self._id}]")

        while True:
            with self._lock:
                if not self._is_running:
                    break
                state = self._current_state

            # execute ONE state step
            state.handle(self)

            # controller-controlled wait
            duration = self._green_time
            elapsed = 0

            while elapsed < duration:
                with self._condition:
                    self._condition.wait(timeout=1)

                
                if self._emergency_active:
                    break

                elapsed += 1

    def stop(self):
        with self._lock:
            self._is_running = False
            self._condition.notify_all()

    def trigger_emergency(self, direction: Direction):
        with self._lock:
            if self._emergency_active:
                return  # already in emergency

            self._emergency_active = True
            previous_state = self._current_state

            from state.emergency_state import EmergencyState #Lazy Import to Avoid Circular import error

            self._current_state = EmergencyState(direction, previous_state)
            self._condition.notify_all()

    def clear_emergency(self):
        with self._lock:
            self._emergency_active = False
            self._condition.notify_all()

    def is_emergency_active(self) -> bool:
        with self._lock:
            return self._emergency_active
        
    def update_green_time(self, green_time: int):
        with self._lock:
            if green_time <= 0:
                raise ValueError("Green time must be positive")
            self._green_time = green_time
            self._condition.notify_all()

    def update_yellow_time(self, yellow_time: int):
        with self._lock:
            if yellow_time <= 0:
                raise ValueError("Yellow time must be positive")
            self._yellow_time = yellow_time

    def update_durations(self, green_time: int, yellow_time: int):
        with self._lock:
            if green_time <= 0 or yellow_time <= 0:
                raise ValueError("Durations must be positive")
            self._green_time = green_time
            self._yellow_time = yellow_time

    def wait(self, timeout):
        with self._condition:
            self._condition.wait(timeout=timeout)
