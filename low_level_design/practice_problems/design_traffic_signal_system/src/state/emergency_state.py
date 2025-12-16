import time
from typing import TYPE_CHECKING
from enums.direction import Direction
from state.intersection_state_interface import IntersectionState

if TYPE_CHECKING:
    from intersection_controller import IntersectionController


class EmergencyState(IntersectionState):
    def __init__(self, emergency_direction: Direction, previous_state: IntersectionState):
        self._emergency_direction = emergency_direction
        self._previous_state = previous_state

    def handle(self, context: "IntersectionController"):
        print(f"🚨 EMERGENCY on {self._emergency_direction.name} 🚨")

        # 1. Force all lights to RED
        for direction in Direction:
            context.get_light(direction).force_red()

        # 2. Give GREEN to emergency direction
        context.get_light(self._emergency_direction).start_green()

        # 3. Hold green until emergency clears
        while context.is_emergency_active():
            time.sleep(10)

        print("🚦 Emergency cleared, restoring normal flow")

        # 4. Safely complete the cycle
        context.get_light(self._emergency_direction).transition()
        time.sleep(context.get_yellow_time())
        context.get_light(self._emergency_direction).transition()

        # 5. Restore previous intersection state
        context.set_current_state(self._previous_state)
