"""Fighter jet concrete class of aircraft, component implementation"""
from components.aircraft import Aircraft

class FighterJet(Aircraft):
    def request_landing(self):
        if self.atc.request_landing(self): # here self inside request_landing refers Fighter Jet class
            self.land()

    def land(self):
        print(f"\n[Fighter Jet]- performs high-speed landing. Attempting landing of Aircraft: {self.name}...")
        self.atc.notify_landing_complete(self)

