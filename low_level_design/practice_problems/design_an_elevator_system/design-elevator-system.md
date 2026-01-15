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
