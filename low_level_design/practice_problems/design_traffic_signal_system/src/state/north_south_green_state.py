"""NorthSouth Green traffic flow implementation using state design pattern"""
from typing import TYPE_CHECKING
from state.intersection_state_interface import IntersectionState
from enums.direction import Direction
from enums.signal_color import SignalColor



if TYPE_CHECKING: #lazy import
    from core.intersection_controller import IntersectionController

class NorthSouthGreenState(IntersectionState):
    def handle(self, context: "IntersectionController"):
        print("North-South Intersection running")
        #turn the green light on for north south traffic light
        context.get_light(Direction.NORTH).start_green()
        context.get_light(Direction.SOUTH).start_green()

        #turn the red light on for other side

        context.get_light(Direction.EAST).set_color(SignalColor.RED)
        context.get_light(Direction.WEST).set_color(SignalColor.RED)

        #simulate green light signal for its duration

        print("Light getting turned on Green")
        # context.wait(context.get_green_time())
        print(f"Turned on for {context.get_green_time()} second")
        


        #transition to yellow light from green
        print("Light getting Turned on Yellow")
        context.get_light(Direction.NORTH).transition()
        context.get_light(Direction.SOUTH).transition()

        #yellow time duration

        # context.wait(context.get_yellow_time())
        print(f"Turned on for {context.get_yellow_time()} second")
        



        #move to next transition from yellow to red
        print("Moving to red light")
        context.get_light(Direction.NORTH).transition()
        context.get_light(Direction.SOUTH).transition()

        #move to next intersection state 
        from state.east_west_green_state import EastWestGreenState #Lazy import 
        context.set_current_state(EastWestGreenState())

        