"""implementation of large robot concrete class of Robots"""
from flyweights.robo_interface import RobotInterface
class LargeRobot(RobotInterface):
    def __init__(self, _type: str, model: str, color: str):
        """Instrinsic variable for shared state"""
        self.__type=_type
        self.__model=model
        self.__color=color

    @property
    def type(self): return self.__type


    def display(self, context: dict) -> None:
        x=context['x']
        y=context['y']
        print(f"[LargeRobot] Position: ({x}, {y}) | Shared: Type={self.__type}, Model={self.__model}, Color={self.__color}")