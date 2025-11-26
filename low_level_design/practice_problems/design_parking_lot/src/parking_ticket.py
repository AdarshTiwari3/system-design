"""Parking ticket implementation"""
from vehicle import Vehicle
from parking_spot import ParkingSpot
from datetime import datetime
import uuid
from typing import Optional

class ParkingTicket:
    def __init__(self,vehicle: Vehicle, parking_spot: ParkingSpot):
        self.ticket_id: str =str(uuid.uuid4())
        self.vehicle=vehicle
        self.parking_spot=parking_spot
        self.entry_time: datetime=datetime.now()
        self.exit_time: Optional[datetime]=None

    def get_vehicle(self) -> Vehicle:
        return self.vehicle
    
    def get_ticket_number(self) -> str:
        return self.ticket_id
    
    def get_parking_spot(self) -> ParkingSpot:
        return self.parking_spot
    
    def get_entry_time(self) -> datetime:
        return self.entry_time
    
    def get_exit_time(self):
        return self.exit_time
    
    def set_exit_time(self) -> None:
        self.exit_time=datetime.now()