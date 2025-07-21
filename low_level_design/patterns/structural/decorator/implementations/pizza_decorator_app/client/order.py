from components.farm_house import FarmHouse
from components.margherita import Margherita
from components.peppy_panner import PeppyPaneer
from decorator.cheese import Cheese
from decorator.corn import Corn
from decorator.mushroom import Mushrooms
def run_decorate_pizza():

    print("\nBuild margherita")
    margherita=Margherita()
    print("\nAdding Cheese")
    margherita=Cheese(margherita)
    print("\nAdding Corn")
    margherita=Corn(margherita)

    print("\nMaking Peppy Paneer pizza with extra Cheese and Mushrooms")
    peppy_paneer=Mushrooms(Cheese(PeppyPaneer())) # here decorator works as a wrapper class

    print("\nDescription:",margherita.get_description())
    print("\nPrice: ₹",margherita.get_price())

    print("\nDescription:",peppy_paneer.get_description())
    print("\nPrice: ₹",peppy_paneer.get_price())

    
    
