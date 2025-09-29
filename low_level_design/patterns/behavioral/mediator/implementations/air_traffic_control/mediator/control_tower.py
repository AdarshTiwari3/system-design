"""Control tower concrete class implementation"""
from mediator.air_traffic_control import AirTrafficControl
from components.aircraft import Aircraft
from typing import List

class ControlTower(AirTrafficControl):
    def __init__(self) -> None:
        self._aircrafts:List[Aircraft] =[]
        self._is_run_busy: bool=False

    def register_aircraft(self, aircraft: Aircraft):
        self._aircrafts.append(aircraft)
        print(f"[ATC] registered the plane: {aircraft.name}")

    def request_landing(self, aircraft: Aircraft) -> bool:
        if self._is_run_busy:
            print(f"\n[ATC]- {aircraft.name} please hold you position, runway is busy")
            return False
        print(f'\n[ATC]- runway is clear, {aircraft.name} you may proceed for landing')
        return True
    
    def notify_landing_complete(self, aircraft: Aircraft):
        print(f"\n[ATC] {aircraft.name} has landed, now runway is clear")
        self._is_run_busy=False