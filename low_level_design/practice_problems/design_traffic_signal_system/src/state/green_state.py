"""Green- state of signal"""
from state.signal_state import SignalState
from enums.signal_color import SignalColor
from state.yellow_state import YellowState
#Lazy import to avoid circular import issue as state uses TrafficLight and TrafficLight uses SignalState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.traffic_light import TrafficLight

class GreenState(SignalState):
    def handle(self, context: "TrafficLight"):
        context.set_color(SignalColor.GREEN)
        context.set_next_state(YellowState()) 