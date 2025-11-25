"""Parking spot class where all the spot related details will be described"""
import threading
from vehicle_size import VehicleSize
from vehicle import Vehicle
class ParkingSpot:
    def __init__(self,parking_spot_id:str, parking_spot_size):
        self.parking_spot_id=parking_spot_id
        self.parking_spot_size=parking_spot_size
        self.is_empty=True
        self.parked_vehicle=None
        self._lock=threading.Lock()


    def get_parking_spot_id(self) -> str:
        return self.parking_spot_id
    
    def get_parking_spot_size(self) -> VehicleSize:
        return self.parking_spot_size
    
    
    def is_parking_available(self) -> bool:
        return self.is_empty
        
    def park_the_vehicle(self, vehicle: Vehicle) -> bool:
        with self._lock:
            if not self.is_empty:
                return False
            
            if not self.can_fit_the_vehicle(vehicle):
                return False

            self.parked_vehicle = vehicle
            self.is_empty = False
            return True

    def unpark_the_vehicle(self) -> Vehicle:
        with self._lock:
            vehicle=self.parked_vehicle
            self.parked_vehicle=None
            self.is_empty=True
            return vehicle

    def can_fit_the_vehicle(self,vehicle: Vehicle) -> bool:
        return vehicle.get_vehicle_size()==self.parking_spot_size
            
