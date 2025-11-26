"""Parking Strategy - to get parking spot"""

from abc import ABC, abstractmethod
from parking_floor import ParkingFloor
from typing import List, Optional
from vehicle import Vehicle
from parking_spot import ParkingSpot

class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, parking_floors: List[ParkingFloor] ,vehicle: Vehicle) -> Optional[ParkingSpot]:
        pass
    