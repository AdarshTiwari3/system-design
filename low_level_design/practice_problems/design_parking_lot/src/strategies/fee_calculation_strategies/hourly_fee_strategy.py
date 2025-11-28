"""Hourly Fee Strategy Calculation"""

from fee_strategy import FeeStrategy
from src.core.parking_ticket import ParkingTicket
from datetime import datetime, timedelta
import math
class HourlyFeeStrategy(FeeStrategy):

    HOURLY_CHARGES=30.0

    def calculate_price(self, parking_ticket: ParkingTicket) -> float:
        parking_duration=parking_ticket.get_exit_time()-parking_ticket.get_entry_time()
        total_hours=math.ceil(parking_duration.total_seconds()/(60*60)) # seconds to hrs conversation and get round of ceil values
        price_to_pay=total_hours*self.HOURLY_CHARGES
        
        return price_to_pay
        