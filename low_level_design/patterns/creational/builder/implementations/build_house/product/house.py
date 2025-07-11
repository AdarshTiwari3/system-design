""" Product of builder design pattern"""

class House():
    def __init__(self):
        self.__walls=False
        self.__doors=False
        self.__windows=False
        self.__roof=False
        
    def _set_walls(self, present: bool): 
        self.__walls = present

    def _set_doors(self, present: bool):
        self.__doors = present

    def _set_windows(self, present: bool):
        self.__windows = present

    def _set_roof(self, present: bool):
        self.__roof = present

    def __str__(self) -> str:
        parts = []
        if self.__walls: parts.append("Walls")
        if self.__doors: parts.append("Doors")
        if self.__windows: parts.append("Windows")
        if self.__roof: parts.append("Roof")
        return f"House with: {', '.join(parts)}" if parts else "Empty House"

        