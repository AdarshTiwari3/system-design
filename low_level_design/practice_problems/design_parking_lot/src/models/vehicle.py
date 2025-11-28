"""Vehicle class for parking where vehicle details will be stored"""
from abc import ABC
from vehicle_size import VehicleSize
class Vehicle(ABC):
    def __init__(self, vehicle_num: str, vehicle_size: VehicleSize):
        self.vehicle_number= vehicle_num
        self.vehicle_size= vehicle_size

    def get_vehicle_number(self) -> str:
        return self.vehicle_number
    
    def get_vehicle_size(self) -> VehicleSize:
        return self.vehicle_size