"""Cargo plane concrete class of aircraft, component implementation"""

from components.aircraft import Aircraft

class CargoPlane(Aircraft):
    def request_landing(self):
        if self.atc.request_landing(self):
            self.land()

    def land(self):
        print(f"\n[Cargo Plane]- attempting landing of Aircraft: {self.name}...")
        self.atc.notify_landing_complete(self)

