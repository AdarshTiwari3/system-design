"""simulate the game"""
from flyweights.robot_factory import RobotFlyweightFactory
from flyweights.small_robot import SmallRobot
from flyweights.large_robots import LargeRobots
import random
def run_game():
    robo_factory=RobotFlyweightFactory()

    """Create small but shared robots"""

    for _ in range(10):
        robot=robo_factory.get_robot("small")
        context={'x':random.randint(0,100), 'y':random.randint(0,100)}
        robot.display(context)


    """create large size robots"""

    for _ in range(10):
        robot=robo_factory.get_robot("large")
        context={'x':random.randint(0,100), 'y':random.randint(0,100)}
        robot.display(context)
