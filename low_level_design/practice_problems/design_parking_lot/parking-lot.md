# Design a Parking Lot System 

### Requirements 

1. The parking lot should have multiple levels, each level with a certain number of parking spots.
2. The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
3. Each parking spot should be able to accommodate a specific type of vehicle.
4. The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
5. The system should track the availability of parking spots and provide real-time information to customers.
6. The system should handle multiple entry and exit points and support concurrent access.

### Identify Core Objects

1. **Vehicle**: This object represents a vehicle that needs a spot. It encapsulates details like the license plate and size (small for motorcycles, medium for cars, large for trucks), serving as the foundation for spot assignment and fee calculation.

2. **ParkingTicket**: This object represents a parking ticket issued when a Vehicle enters the parking lot. It stores critical details, including the ticket ID, the associated Vehicle, the assigned ParkingSpot, and entry time, which are later used to calculate fees and free up spots upon exit.

3. **ParkingSpot**: This object models an individual parking spot in the parking lot. It’s the physical space where a Vehicle parks, ensuring only appropriately sized vehicles can park based on its capacity.

4. **VehicleSize** enum defines the different types of vehicles supported by the parking lot.

5. **FeeStrategy**: defines the parking fee calculation including **HourlyFeeStrategy** and **VehicleBasedFeeStrategy**

6. **ParkingStrategy**: defines the type of parking strategy i.e **BestFit, Nearest and Farthest** parking strategy

7. **ParkingLot** acts as a parking manager who is responsible for parking, unparking vehicle and other operations
