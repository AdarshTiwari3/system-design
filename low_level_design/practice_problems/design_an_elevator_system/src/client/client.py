"""Elevator Runner or Client Runner Implementation"""

from entities.elevator import Elevator
from observer.display_screen import ElevatorDisplayScreen
from core.elevator_controller import ElevatorController
from strategies.nearest_elevator_strategy import NearestElevatorStrategy
from entities.request import Request
from enums.request_type import RequestType
import time


def main():
    print("\nRunning an Elevator System")

    # ------ Elevator Setup --------

    e1 = Elevator("E1")
    e2 = Elevator("E2")
    e3 = Elevator("E3")
    e4 = Elevator("E4")

    e1.set_floor(1)
    e2.set_floor(4)
    e3.set_floor(7)
    e4.set_floor(10)

    elevators = [e1, e2, e3, e4]

    # ----- Attach Observer to Display Screen -------

    display = ElevatorDisplayScreen()

    for elevator in elevators:
        elevator.add_observer(display)

    # ----- Add Elevator Controller ---------

    strategy = NearestElevatorStrategy()
    controller = ElevatorController(elevators, strategy=strategy, total_floors=10)

    # ----- User Request for an Elevator ------

    request1 = Request(
        source_floor=1, target_floor=6, request_type=RequestType.HALL_CALL
    )  # up request
    request2 = Request(
        source_floor=3, target_floor=8, request_type=RequestType.HALL_CALL
    )  # up request

    request3 = Request(
        source_floor=7, target_floor=2, request_type=RequestType.CABIN_CALL
    )  # down request
    request4 = Request(
        source_floor=10, target_floor=4, request_type=RequestType.HALL_CALL
    )  # down request

    total_requests = []
    total_requests.append(request1)
    total_requests.append(request2)
    total_requests.append(request3)
    total_requests.append(request4)

    # Assign Request to Controller

    for request in total_requests:
        controller.assign_request(request)

    print("\n⏳ Elevator Started\n")

    try:
        while True:
            controller.move_elevators()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down elevator system...")
