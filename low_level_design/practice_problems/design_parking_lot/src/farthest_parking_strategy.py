"""Farthest Parking Strategy"""

from parking_strategy import ParkingStrategy
from parking_floor import ParkingFloor
from vehicle import Vehicle
from parking_spot import ParkingSpot
from typing import List, Optional

class FarthestFirstParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        for parking_floor in reversed(parking_floors):
            parking_spot=parking_floor.find_available_parking_spots(vehicle)
            if parking_spot:
                return parking_spot[-1]

        return None 