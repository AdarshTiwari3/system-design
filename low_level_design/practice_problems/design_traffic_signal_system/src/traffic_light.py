"""Traffic Light- context for states whether it is red , green or yellow the state will be changed accordingly"""
from state.red_state import RedState
from state.signal_state import SignalState
from typing import Optional
from enums.signal_color import SignalColor
from state.green_state import GreenState

class TrafficLight:
    def __init__(self):
        self._current_state: SignalState = RedState()
        self._next_state: Optional[SignalState]=None
        self._current_color: Optional[SignalColor]=None

    def set_color(self, color: SignalColor):
        self._current_color=color


    def set_next_state(self, state: SignalState):
        self._current_state=state

    def get_current_color(self) -> SignalColor:
        return self._current_color
    
    def get_current_state(self) -> SignalState:
        return self._current_state
    
    #will be used by intersection controller
    def start_green(self):
        # starts the green yellow red lights
        self._current_state=GreenState()
        self._current_state.handle(self) #passes self=Traffic Signal as context

    def transition(self):
        #just move the current state to next state i.e Green to Yellow and Yellow to Red

        self._current_state=self._next_state
        self._current_state.handle(self)