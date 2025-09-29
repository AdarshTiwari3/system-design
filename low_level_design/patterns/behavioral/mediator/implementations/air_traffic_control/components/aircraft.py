"""Aircraft Interface component implementation"""

from abc import ABC, abstractmethod
from mediator.air_traffic_control import AirTrafficControl

class Aircraft(ABC):
    def __init__(self, name:str, atc: AirTrafficControl) -> None:
        self.name=name
        self._atc: AirTrafficControl = atc

    @property
    def atc(self) -> AirTrafficControl:
        return self._atc
    
    @abstractmethod
    def request_landing(self):
        """Send landing request to ATC."""
        pass

    @abstractmethod
    def land(self):
        """Perform Landing Operation"""

        pass