"""Truck vehicle class"""

from vehicle import Vehicle
from vehicle_size import VehicleSize

class Truck(Vehicle):
    def __init__(self, vehicle_num: str):
        super().__init__(vehicle_num, VehicleSize.LARGE)