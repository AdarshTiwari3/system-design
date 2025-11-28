"""Parking Strategy - to get parking spot"""

from abc import ABC, abstractmethod
from core.parking_floor import ParkingFloor
from typing import List, Optional
from models.vehicle import Vehicle
from core.parking_spot import ParkingSpot

class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, parking_floors: List[ParkingFloor] ,vehicle: Vehicle) -> Optional[ParkingSpot]:
        pass
    