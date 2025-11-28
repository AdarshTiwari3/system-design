"""Nearest Parking Strategy"""

from parking_strategy import ParkingStrategy
from src.core.parking_floor import ParkingFloor
from src.models.vehicle import Vehicle
from src.core.parking_spot import ParkingSpot
from typing import List, Optional

class NearestFirstParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        for parking_floor in parking_floors:
            parking_spot=parking_floor.find_available_parking_spots(vehicle)
            if parking_spot:
                return parking_spot[0]

        return None 