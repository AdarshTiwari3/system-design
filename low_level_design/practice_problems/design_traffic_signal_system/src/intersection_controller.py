from typing import Dict
from state.intersection_state_interface import IntersectionState
from state.east_west_green_state import EastWestGreenState
from traffic_light import TrafficLight
from enums.direction import Direction



class IntersectionController:
    def __init__(self, intersection_id:str, green_time: int, yellow_time: int, traffic_lights: Dict[Direction, TrafficLight]):
        self._id=intersection_id
        self._traffic_lights=traffic_lights
        self._green_time=green_time
        self._yellow_time=yellow_time
        self._current_state: IntersectionState =EastWestGreenState()

    def get_id(self) -> str:
        return self._id
    
    def get_current_state(self) -> IntersectionState:
        return self._current_state
    
    def set_current_state(self, state: IntersectionState):
        self._current_state=state

    def get_green_time(self) -> int:
        return self._green_time
    
    def get_yellow_time(self) -> int:
        return self._yellow_time
    
    def get_light(self, direction: Direction) -> TrafficLight:
        return self._traffic_lights[direction]
