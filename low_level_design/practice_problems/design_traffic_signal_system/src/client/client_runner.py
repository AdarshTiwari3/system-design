"""Client Runner"""

import threading
from intersection_controller import IntersectionController
from traffic_light import TrafficLight
from enums.direction import Direction
import time
def main():

    traffic_lights = {
        Direction.NORTH: TrafficLight(),
        Direction.SOUTH: TrafficLight(),
        Direction.EAST: TrafficLight(),
        Direction.WEST: TrafficLight(),
    }


    controller=IntersectionController("intersection-01",green_time=10,yellow_time=5,traffic_lights=traffic_lights)

    # 3️⃣ Start controller in a background thread
    controller_thread = threading.Thread(
        target=controller.run,
        daemon=True
    )
    controller_thread.start()

    print("🚦 Traffic system started\n")

    print("▶ Running normal traffic flow\n")

    time.sleep(20)

    print("🚦 Traffic surge detected → extending green time\n")
    controller.update_durations(green_time=15, yellow_time=5)

    time.sleep(25)

    print("🚨 Emergency vehicle approaching from NORTH\n")
    controller.trigger_emergency(Direction.NORTH)

    time.sleep(15)

    print("🚦 Emergency cleared, resuming normal operation\n")
    controller.clear_emergency()

    time.sleep(15)

    print("🛑 Shutting down traffic system\n")
    controller.stop()
    controller_thread.join()

    print("✅ Traffic system stopped cleanly\n")

