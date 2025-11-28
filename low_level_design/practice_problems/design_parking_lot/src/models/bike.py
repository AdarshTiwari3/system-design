"""Bike Vehicle class"""

from vehicle import Vehicle
from vehicle_size import VehicleSize

class Bike(Vehicle):
    def __init__(self, vehicle_num:str):
        super().__init__(vehicle_num, VehicleSize.SMALL)