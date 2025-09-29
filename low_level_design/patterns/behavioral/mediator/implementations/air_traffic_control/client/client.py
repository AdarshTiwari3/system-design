"""client runner"""
from mediator.control_tower import ControlTower
from components.cargo_plane import CargoPlane
from components.fighter_jet import FighterJet
from components.passenger_plane import PassengerPlane

def run_atc_mediator():
    print(f'\nRunning ATC of mediator design pattern')
    atc=ControlTower()

    aircraft_names={
        'passenger_plane':'vistara-boeing-777-max',
        'figher_plane':'Su-30 MKI 7155-IND',
        'cargo_plane':'fedex-airbus-990'
    }

    plane1=PassengerPlane(aircraft_names['passenger_plane'],atc)
    plane2=CargoPlane(aircraft_names['cargo_plane'],atc)
    plane3=FighterJet(aircraft_names['figher_plane'],atc)

    atc.register_aircraft(plane1)
    atc.register_aircraft(plane2)
    atc.register_aircraft(plane3)

    plane1.request_landing()
    plane2.request_landing()
    plane3.request_landing()
