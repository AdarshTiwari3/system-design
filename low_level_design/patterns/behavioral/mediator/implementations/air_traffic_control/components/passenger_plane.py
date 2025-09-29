"""Passenger plane concrete class of aircraft, component implementation"""
from components.aircraft import Aircraft

class PassengerPlane(Aircraft):
    def request_landing(self):
        if self.atc.request_landing(self):
            self.land()

    def land(self):
        print(f'\n[Passenger Plane]- attempting landing of Aircraft: {self.name}...')
        self.atc.notify_landing_complete(self)

