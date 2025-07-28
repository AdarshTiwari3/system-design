"""Flyweight Robot Factory which will be responsible for object creation of shared state and be consumed by client"""
from typing import Dict
from flyweights.robo_interface import RobotInterface
from flyweights.small_robot import SmallRobot
from flyweights.large_robots import LargeRobots
class RobotFlyweightFactory:
    def __init__(self):
        self._robots: Dict[str, RobotInterface]={}

    def get_robot(self, robot_size: str)-> RobotInterface:

        if robot_size not in self._robots: #checks the map or dictionary if present then no need (as we can use it as a shared state) to create else create it
            if robot_size=="small":
                self._robots[robot_size]=SmallRobot("1X-Zeta", "Model-ZetaTyco", "Green")
            elif robot_size=="large":
                self._robots[robot_size]=LargeRobots("1TRX-100","Zeco-350","Red")
            else:
                raise ValueError("Robots not found")
        
        return self._robots[robot_size]