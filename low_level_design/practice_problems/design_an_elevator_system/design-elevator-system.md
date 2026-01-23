# Design Elevator System

## Requirements

1. The system should support multiple elevators operating across multiple floors in a building.
2. Each elevator should enforce a maximum passenger capacity and must not exceed this limit at any time.
3. Users should be able to request an elevator from any floor and select a destination floor.
4. The system should efficiently assign elevators to incoming requests to minimize waiting time and overall travel time.
5. Elevator scheduling should prioritize requests based on the current direction of travel and the proximity of elevators to the requested floor.
6. Each elevator should be capable of handling multiple requests concurrently and processing them in an optimal order.
7. The system should ensure thread safety and prevent race conditions when multiple threads interact with elevators and shared system resources.

---

## Core Objects

- **Elevator**  
  Represents a single elevator car. Maintains current floor, direction, state, pending requests, capacity, and notifies observers on state changes.

- **Request**  
  Represents a user request containing source floor, target floor, request type (hall/cabin), and derived travel direction.

- **ElevatorState (IdleState, MovingUpState, MovingDownState)**  
  Encapsulates elevator behavior based on its current operational state using the State pattern.

- **ElevatorController**  
  Coordinates request validation, elevator allocation, and movement orchestration.

- **AllocationStrategy (NearestElevatorStrategy)**  
  Selects the most suitable elevator for a request based on proximity and availability.

- **ElevatorObserver (ElevatorDisplayScreen)**  
  Observes elevator state changes and displays real-time status updates.

- **DomainExceptions**  
  Defines business-level errors such as invalid requests, no elevator available, capacity exceeded, and no pending requests.

---

## Design Patterns Used

- **State Pattern**  
  Controls elevator behavior based on its current movement state.

- **Strategy Pattern**  
  Allows pluggable elevator allocation algorithms without modifying core logic.

- **Observer Pattern**  
  Enables automatic updates to display systems when elevator state changes.

- **Facade / Controller Pattern**  
  Provides a simplified interface for interacting with the elevator system.

---

## Non-Functional Considerations

- **Thread Safety**  
  Shared elevator state and request queues are protected using locks.

- **Scalability**  
  New elevators, strategies, or observers can be added with minimal changes.

- **Extensibility**  
  The design supports adding new scheduling strategies or elevator states easily.

- **Maintainability**  
  Clear separation of concerns and modular folder structure improves readability and testability.

---
