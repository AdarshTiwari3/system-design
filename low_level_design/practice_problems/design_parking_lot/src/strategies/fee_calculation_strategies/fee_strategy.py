"""Parking Fee strategy interface"""

from abc import ABC, abstractmethod
from src.core.parking_ticket import ParkingTicket
class FeeStrategy(ABC):

    @abstractmethod
    def calculate_price(self, parking_ticket: ParkingTicket) -> float:
        pass