"""Flyweight Robot Factory which will be responsible for object creation of shared state and be consumed by client"""
from typing import Dict
from flyweights.robo_interface import RobotInterface
from flyweights.small_robot import SmallRobot
from flyweights.large_robot import LargeRobot
from game.robot_types import RobotSize
class RobotFlyweightFactory:
    """Flyweight factory that will be responsible for shared state"""
    __robots: Dict[RobotSize, RobotInterface]={}

    @classmethod
    def get_robot(cls, robot_size: RobotSize)-> RobotInterface:

        if robot_size not in cls.__robots: #checks the map or dictionary if present then no need (as we can use it as a shared state) to create else create it
            if robot_size==RobotSize.SMALL:
                cls.__robots[robot_size]=SmallRobot("1X-Zeta", "Model-ZetaTyco", "Green")
            elif robot_size==RobotSize.LARGE:
                cls.__robots[robot_size]=LargeRobot("1TRX-100","Zeco-350","Red")
            else:
                raise ValueError("Robots not found")
        
        return cls.__robots[robot_size]
    
    @classmethod
    def total_robots_created(cls) -> int:
        return len(cls.__robots)