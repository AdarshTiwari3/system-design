"""Yellow- state of signal"""
from state.signal_state import SignalState
from enums.signal_color import SignalColor
from state.red_state import RedState
#Lazy import to avoid circular import issue as state uses TrafficLight and TrafficLight uses SignalState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.traffic_light import TrafficLight

class YellowState(SignalState):
    def handle(self, context: "TrafficLight"):
        context.set_color(SignalColor.YELLOW)
        context.set_next_state(RedState()) #reset the state as red 