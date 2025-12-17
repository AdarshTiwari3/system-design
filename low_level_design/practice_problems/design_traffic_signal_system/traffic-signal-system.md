# Design Traffic Signal System

## Requirements

1. Manage traffic flow at an intersection with multiple roads.
2. Support three signal types: RED, YELLOW, and GREEN.
3. Signal durations should be configurable.
4. Ensure smooth and safe transitions between signal states.
5. Handle emergency situations such as ambulances or fire trucks.
6. The design should be simple, scalable, and extensible.

---

## Core Objects

### 1. Signal
Enum representing the traffic signal state.

- RED  
- YELLOW  
- GREEN  

---

### 2. Direction
Enum representing road directions.

- NORTH  
- SOUTH  
- EAST  
- WEST  

---

### 3. TrafficLight
Represents a traffic light for a single direction.

**Responsibilities**
- Maintain current signal state
- Change signal safely

---

### 4. IntersectionController
Controls all traffic lights at an intersection.

**Responsibilities**
- Manage signal timing
- Switch between traffic states
- Handle emergency situations

---

### 5. IntersectionState
Abstract representation of a traffic state.

**Responsibilities**
- Define which directions are allowed to move
- Control transition to the next state

---

### 6. Concrete States
Examples:
- NorthSouthGreenState
- EastWestGreenState
- EmergencyState

**Responsibilities**
- Apply signal changes for the state
- Decide the next state

---

## Design Pattern Used

- State Pattern – to manage traffic signal transitions cleanly

