""""Air Traffic Control Interface implementation"""
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from components.aircraft import Aircraft

class AirTrafficControl(ABC):

    @abstractmethod
    def register_aircraft(self, aircraft: "Aircraft"):
        pass

    @abstractmethod
    def request_landing(self, aircraft: "Aircraft") -> bool:
        pass

    @abstractmethod
    def notify_landing_complete(self, aircraft: "Aircraft"):
        pass
