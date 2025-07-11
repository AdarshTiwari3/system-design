from builder.create_house_builder import HouseBuilder
from product.house import House

class ConstructionDirector:
    def __init__(self, builder: HouseBuilder):
        self._builder = builder

    def construct_simple_house(self) -> House:
        return (
            self._builder
            .set_walls(True)
            .set_roof(True)
            .build()
        )

    def construct_luxury_house(self) -> House:
        """
        Builds a luxury house using method chaining.
        Method chaining allows calling multiple builder methods in one continuous line.
        """
        #Method chaining means calling multiple methods in one continuous line,
        return (
            self._builder #this holds object of HouseBuilder
            .set_walls(True)
            .set_doors(True)
            .set_windows(True)
            .set_roof(True)
            .build()
        )
