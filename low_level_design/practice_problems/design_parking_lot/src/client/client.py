"""Client Runner"""
from core.parking_lot import ParkingLot
from core.parking_floor import ParkingFloor
from core.parking_spot import ParkingSpot
from models.vehicle_size import VehicleSize
from strategies.fee_calculation_strategies.hourly_fee_strategy import HourlyFeeStrategy
from strategies.fee_calculation_strategies.vehicle_based_strategy import VehicleBasedFeeStrategy
from strategies.parking_strategies.nearest_first_strategy import NearestFirstParkingStrategy
from strategies.parking_strategies.farthest_parking_strategy import FarthestFirstParkingStrategy
from strategies.parking_strategies.best_fit_parking_strategy import BestFitParkingStrategy
from models.bike import Bike
from models.car import Car
from models.truck import Truck

def main():

    #singleton object
    parking_lot=ParkingLot.get_instance()
    #add parking floors and spots

    parking_floor_1=ParkingFloor(1)
    parking_floor_2=ParkingFloor(2)
    parking_floor_3=ParkingFloor(3)
    
    parking_floor_1.add_parking_spot(ParkingSpot('p1',VehicleSize.MEDIUM))
    parking_floor_1.add_parking_spot(ParkingSpot('p2',VehicleSize.SMALL))
    parking_floor_1.add_parking_spot(ParkingSpot('p3',VehicleSize.SMALL))
    parking_floor_1.add_parking_spot(ParkingSpot('p4',VehicleSize.LARGE))
    parking_floor_1.add_parking_spot(ParkingSpot('p5',VehicleSize.MEDIUM))
    parking_floor_1.add_parking_spot(ParkingSpot('p6',VehicleSize.LARGE))


    parking_floor_2.add_parking_spot(ParkingSpot('p7',VehicleSize.LARGE))
    parking_floor_2.add_parking_spot(ParkingSpot('p8',VehicleSize.LARGE))
    parking_floor_2.add_parking_spot(ParkingSpot('p9',VehicleSize.LARGE))
    parking_floor_2.add_parking_spot(ParkingSpot('p10',VehicleSize.MEDIUM))
    parking_floor_2.add_parking_spot(ParkingSpot('p11',VehicleSize.MEDIUM))

    parking_floor_3.add_parking_spot(ParkingSpot('p12',VehicleSize.SMALL))
    parking_floor_3.add_parking_spot(ParkingSpot('p13',VehicleSize.LARGE))
    parking_floor_3.add_parking_spot(ParkingSpot('p14',VehicleSize.MEDIUM))

    #add the floors to parking
    parking_lot.add_parking_floor(parking_floor_1)
    parking_lot.add_parking_floor(parking_floor_2)
    parking_lot.add_parking_floor(parking_floor_3)

    #add fee strategy

    parking_lot.set_fee_strategy(HourlyFeeStrategy())

    #add parking strategy
    parking_lot.set_parking_strategy(NearestFirstParkingStrategy())

    #total available parking
    parking_floor_1.get_total_available_parking_spots()
    parking_floor_2.get_total_available_parking_spots()
    parking_floor_3.get_total_available_parking_spots()

    # park the vehicle
    car1=Car("DL-CAR1234")
    bike1=Bike("UK-BIKE0123")
    truck1=Truck("HR-TRUCK0123")

    car_ticket1=parking_lot.park_the_vehicle(car1)
    bike_ticket1=parking_lot.park_the_vehicle(bike1)
    truck_ticket1=parking_lot.park_the_vehicle(truck1)

    #print ticket
    print("\nTicket Number of CAR=",car_ticket1.get_ticket_number())
    print("\nTicket Number of Bike=",bike_ticket1.get_ticket_number())
    print("\nTicket Number of Truck=",truck_ticket1.get_ticket_number())

    #total available parking after parking 3 vehicle
    print(f"\n------Available parking after parking some vehicles-----")
    parking_floor_1.get_total_available_parking_spots()
    parking_floor_2.get_total_available_parking_spots()
    parking_floor_3.get_total_available_parking_spots()

    #do some more parking and change the strategy for fee as VehicleBased and Farthest Parking
    print("\n Using Vehicle Based Fee and Farthest Parking Strategy")
    parking_lot.set_fee_strategy(VehicleBasedFeeStrategy())

    #add parking strategy
    parking_lot.set_parking_strategy(FarthestFirstParkingStrategy())

    car2=Car("UP-CAR1234")
    bike2=Bike("US-BIKE0123")
    truck2=Truck("RR-TRUCK0123")

    car_ticket2=parking_lot.park_the_vehicle(car2)
    bike_ticket2=parking_lot.park_the_vehicle(bike2)
    truck_ticket2=parking_lot.park_the_vehicle(truck2)

    print(f"\n------Available parking after parking some vehicles-----")
    parking_floor_1.get_total_available_parking_spots()
    parking_floor_2.get_total_available_parking_spots()
    parking_floor_3.get_total_available_parking_spots()

    #Show Active Tickets in the parking
    print("\nActive Parking=",parking_lot.current_active_tickets)

    print("\n Using Vehicle Based Fee and Best Fit Parking Strategy")
    parking_lot.set_parking_strategy(BestFitParkingStrategy())

    car3=Car("RJ-CAR1235")
    bike3=Bike("KL-BIKE0123")
    truck3=Truck("TN-TRUCK0123")

    car_ticket3=parking_lot.park_the_vehicle(car3)
    bike_ticket3=parking_lot.park_the_vehicle(bike3)
    truck_ticket3=parking_lot.park_the_vehicle(truck3)

    print(f"\n------Available parking after parking some vehicles-----")
    parking_floor_1.get_total_available_parking_spots()
    parking_floor_2.get_total_available_parking_spots()
    parking_floor_3.get_total_available_parking_spots()

    #unpark some vehicle and perform exit
    print(f"\nExit the Vehicle")
    if truck_ticket1:
        parking_fee=parking_lot.unpark_the_vehicle(truck1.get_vehicle_number())
        if parking_fee:
            print(f"\nPay the parking price {parking_fee} for vehicle {truck1.get_vehicle_number()}")

    print("\n Total Parking Available after Exit")

    parking_floor_1.get_total_available_parking_spots()
    parking_floor_2.get_total_available_parking_spots()
    parking_floor_3.get_total_available_parking_spots()




