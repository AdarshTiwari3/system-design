# subclass of builder interface
from builder.builder_interface import HouseBuilder
from product.house import House


class CreateHouseBuilder(HouseBuilder):
    def __init__(self):
        self._walls = False
        self._doors = False
        self._windows = False
        self._roof = False

    def set_walls(self, present: bool):
        self._walls = present
        return self

    def set_doors(self, present: bool):
        self._doors = present
        return self

    def set_windows(self, present: bool):
        self._windows = present
        return self

    def set_roof(self, present: bool):
        self._roof = present
        return self

    def build(self) -> House:
        if not self._walls:
            raise ValueError("House must have at least walls.")
        house = House()
        house._set_walls(self._walls)
        house._set_doors(self._doors)
        house._set_windows(self._windows)
        house._set_roof(self._roof)
        return house