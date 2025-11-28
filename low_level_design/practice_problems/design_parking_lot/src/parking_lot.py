"""Singleton class - Parking Manager"""
import threading
from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from hourly_fee_strategy import HourlyFeeStrategy
from nearest_first_strategy import NearestFirstParkingStrategy
from typing import List, Dict, Self, Optional
from parking_strategy import ParkingStrategy
from fee_strategy import FeeStrategy
from vehicle import Vehicle

class ParkingLot:
    """class variables"""
    _instance=None
    _lock=threading.Lock()

    def __init__(self):
        if ParkingLot._instance:
            raise Exception("This is a singleton class")

        self.parking_floors: List[ParkingFloor]=[]
        self.current_active_tickets: Dict[str, ParkingTicket]={}
        self.fee_strategy=HourlyFeeStrategy()
        self.parking_strategy=NearestFirstParkingStrategy()
        self._main_lock=threading.Lock()

    @classmethod
    def get_instance(cls) -> Self:
        if cls._instance is None:
            with cls._lock:
                #double check lock
                if cls._instance is None:
                    cls._instance=ParkingLot()
        return cls._instance
    
    def add_parking_floor(self, parking_floor: ParkingFloor) -> None:
        with self._main_lock:
            self.parking_floors.append(parking_floor)

    def remove_parking_floor(self, parking_floor: ParkingFloor) -> None:
        with self._main_lock:
            # remove if present 
            try:
                self.parking_floors.remove(parking_floor)
            except ValueError:
                print("Floor not found")
    def set_parking_strategy(self, parking_strategy: ParkingStrategy) -> None:
        with self._main_lock:
            self.parking_strategy = parking_strategy

    def set_fee_strategy(self, fee_strategy: FeeStrategy) -> None:
        with self._main_lock:
            self.fee_strategy = fee_strategy

    def park_the_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        with self._main_lock:
            parking_spot=self.parking_strategy.find_parking_spot(self.parking_floors,vehicle)

            if parking_spot:
                parked=parking_spot.park_the_vehicle(vehicle)
                if not parked:
                    print(f"Failed to park vehicle {vehicle.get_vehicle_number()}: spot taken")
                    return None
                
                parking_ticket=ParkingTicket(vehicle,parking_spot)
                self.current_active_tickets[vehicle.get_vehicle_number()]=parking_ticket
                print(f"-----Vehicle {vehicle.get_vehicle_number()} parked at parking spot {parking_spot.get_parking_spot_id()}-----")
                return parking_ticket
            else:
                print(f"Parking not available")
                return None
            
    def unpark_the_vehicle(self, vehicle_number: str) -> Optional[float]:
        with self._main_lock:
            parking_ticket=self.current_active_tickets.pop(vehicle_number, None)

            if parking_ticket:
                # calculate the fee
                parking_ticket.set_exit_time()
                parking_ticket.get_parking_spot().unpark_the_vehicle()
                parking_fee=self.fee_strategy.calculate_price(parking_ticket)
                print(f"Unparking the vehicle {vehicle_number} from {parking_ticket.get_parking_spot().get_parking_spot_id()}")

                return parking_fee
            return None