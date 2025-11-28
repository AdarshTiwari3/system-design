"""Best Fit Parking Strategy"""

from .parking_strategy import ParkingStrategy
from core.parking_floor import ParkingFloor
from models.vehicle import Vehicle
from core.parking_spot import ParkingSpot
from typing import List, Optional
from models.vehicle_size import VehicleSize

SIZE_RANK = {
    VehicleSize.SMALL: 0,
    VehicleSize.MEDIUM: 1,
    VehicleSize.LARGE: 2,
}
class BestFitParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        best_parking_spot=None

        for parking_floor in parking_floors:
            current_floor_parking_spot=parking_floor.find_available_parking_spots(vehicle)

            if not current_floor_parking_spot:
                continue
            current_floor_parking_spot.sort(key=lambda spot: SIZE_RANK[spot.get_parking_spot_size()])
            floor_best=current_floor_parking_spot[0]

            #global best on size
            if not best_parking_spot:
                best_parking_spot=floor_best
            else:
                #moving towards more smaller size , best fit
                if SIZE_RANK[floor_best.get_parking_spot_size()] < SIZE_RANK[best_parking_spot.get_parking_spot_size()]:
                    best_parking_spot = floor_best


        return best_parking_spot

