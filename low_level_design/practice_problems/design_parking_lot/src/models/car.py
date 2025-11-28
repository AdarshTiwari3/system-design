"""Car vehicle type"""
from vehicle import Vehicle
from vehicle_size import VehicleSize

class Car(Vehicle):
    def __init__(self, vehicle_num:str):
        super().__init__(vehicle_num, VehicleSize.MEDIUM)