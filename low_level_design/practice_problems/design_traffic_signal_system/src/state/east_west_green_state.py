"""EastWestGreenState- because traffic flows like this only"""

from typing import TYPE_CHECKING
from state.intersection_state_interface import IntersectionState
from enums.direction import Direction
from enums.signal_color import SignalColor


if TYPE_CHECKING: #lazy import
    from core.intersection_controller import IntersectionController

class EastWestGreenState(IntersectionState):
    def handle(self, context: "IntersectionController"):
        print("\nEast-West Intersection running")
        # turns green for east and west direction for traffic light
        context.get_light(Direction.EAST).start_green()
        context.get_light(Direction.WEST).start_green()
        # and turns the north and south as red lights
        context.get_light(Direction.NORTH).set_color(SignalColor.RED)
        context.get_light(Direction.SOUTH).set_color(SignalColor.RED)

        
        print("Light getting turned on Green")
        # context.wait(context.get_green_time())
        print(f"Turned on for {context.get_green_time()} second")
        

        print("Light getting Turned on Yellow")
        context.get_light(Direction.EAST).transition() # moves to yellow from green for East Traffic Light at intersection
        context.get_light(Direction.WEST).transition()

        
        # context.wait(context.get_yellow_time())
        print(f"Turned on for {context.get_yellow_time()} second")
        

        print("Moving to next state")
        print("Moving to Red")
        context.get_light(Direction.EAST).transition() # moves to red from yellow for East Traffic Light at intersection
        context.get_light(Direction.WEST).transition()
        
        #set the other state as true i.e NorthSouth state for traffic light

        # 🔁 Lazy import HERE
        from state.north_south_green_state import NorthSouthGreenState
       
        context.set_current_state(NorthSouthGreenState())

        

        