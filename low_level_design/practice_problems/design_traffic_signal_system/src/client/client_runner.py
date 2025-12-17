"""Client Runner"""

import threading
from core.intersection_controller import IntersectionController
from core.traffic_light import TrafficLight
from enums.direction import Direction

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
        # daemon=True
    )
    controller_thread.start()

    print("🚦 Traffic system started\n")

    print("▶ Running normal traffic flow\n")

    controller.wait(20)

    print("\n🚦 Traffic surge detected → extending green time\n")
    controller.update_durations(green_time=15, yellow_time=5)

    controller.wait(20)

    print("🚨 Emergency vehicle approaching from NORTH\n")
    controller.trigger_emergency(Direction.NORTH)

    controller.wait(20)

    print("🚦 Emergency cleared, resuming normal operation\n")
    controller.clear_emergency()

    controller.wait(30)

    controller.update_durations(green_time=18, yellow_time=5)
    controller.wait(30)

    print("🛑 Shutting down traffic system\n")
    controller.stop()
    controller_thread.join()

    print("✅ Traffic system stopped cleanly\n")

