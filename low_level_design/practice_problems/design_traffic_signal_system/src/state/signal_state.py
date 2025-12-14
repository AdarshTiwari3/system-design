"""Signal State Interface: which keeps track of different state of signal i.e red, green and yellow"""
from abc import ABC, abstractmethod
#Lazy import to avoid circular import issue as state uses TrafficLight and TrafficLight uses SignalState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from traffic_light import TrafficLight
    
class SignalState(ABC):
    @abstractmethod
    def handle(self, context: "TrafficLight"):
        pass