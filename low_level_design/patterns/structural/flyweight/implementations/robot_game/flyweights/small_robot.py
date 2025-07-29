from flyweights.robo_interface import RobotInterface

class SmallRobot(RobotInterface):
    """small robot concrete class"""
    def __init__(self, _type: str, model: str, color: str) -> None:
        """Instrinsic variable for shared state"""
        self.__type=_type
        self.__model=model
        self.__color=color

    @property
    def robot_type(self): return self.__type

    def display(self, context: dict)-> None:
        """Displays the robot with extrinsic context"""
        x = context["x"]
        y = context["y"]
        print(f"[SmallRobot] Position: ({x}, {y}) | Shared: Type={self.__type}, Model={self.__model}, Color={self.__color}")