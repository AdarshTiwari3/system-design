"""Vehicle based price calculation"""

from models.vehicle_size import VehicleSize
from .fee_strategy import FeeStrategy
from core.parking_ticket import ParkingTicket
import math

class VehicleBasedFeeStrategy(FeeStrategy):
    HOURLY_CHARGES={
        VehicleSize.LARGE: 100.0,
        VehicleSize.MEDIUM: 50.0,
        VehicleSize.SMALL: 20.0
    }

    def calculate_price(self, parking_ticket: ParkingTicket):

        parking_duration=parking_ticket.get_entry_time()-parking_ticket.get_exit_time()
        total_hours=math.ceil(parking_duration.total_seconds()/(60*60)) # seconds to hrs conversation and get round of ceil values
        if total_hours==0:
            total_hours+=1
        vehicle=parking_ticket.get_vehicle().get_vehicle_size()
        price_to_pay=total_hours*self.HOURLY_CHARGES[vehicle]
        
        return price_to_pay
        