"""Class Implementation of Parking Floors"""
from typing import Dict, List, Optional
from parking_spot import ParkingSpot
from src.models.vehicle import Vehicle
from collections import defaultdict
from src.models.vehicle_size import VehicleSize
import threading

class ParkingFloor:
    def __init__(self, floor_number:int):
        self.parking_floor_number=floor_number
        self.parking_spots: Dict[str,ParkingSpot]={}
        self._lock=threading.Lock()

    def add_parking_spot(self, parking_spot:ParkingSpot) -> None:
        with self._lock:
            self.parking_spots[parking_spot.get_parking_spot_id()]=parking_spot

    def remove_parking_spot(self, parking_spot:ParkingSpot) -> Optional[ParkingSpot]:
        with self._lock:
            return self.parking_spots.pop(parking_spot.get_parking_spot_id(), None)

    def find_available_parking_spots(self,vehicle:Vehicle) -> List[ParkingSpot]:
        with self._lock:
            available_parking_spots: List[ParkingSpot]=[]
            for parking_spot in self.parking_spots.values():
                if parking_spot.is_parking_available() and parking_spot.can_fit_the_vehicle(vehicle):
                    available_parking_spots.append(parking_spot)

            return available_parking_spots
        
    def get_total_available_parking_spots(self) -> Dict[VehicleSize, int]:
        """
        Print counts of available spots by size. Snapshot taken under lock.
        """
        with self._lock:
            available_parking_spots=defaultdict(int)

            for parking_spot in self.parking_spots.values():
                if parking_spot.is_parking_available():
                    available_parking_spots[parking_spot.get_parking_spot_size()]+=1 # gives type of parking size is available
        print(f"-----Floor-----{self.parking_floor_number}----Available-------")
        for size in VehicleSize:
            print(f"{size.value} parking spots:{available_parking_spots[size]}")

        return dict(available_parking_spots)
