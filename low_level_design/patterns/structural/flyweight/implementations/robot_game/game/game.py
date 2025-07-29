"""simulate the game"""
from flyweights.robot_factory import RobotFlyweightFactory
from flyweights.small_robot import SmallRobot
from flyweights.large_robot import LargeRobot
from game.robot_types import RobotSize
import random
def run_game():
    robo_factory=RobotFlyweightFactory()
    

    """Create small but shared robots"""
    # robot=None
    for _ in range(10):
        robot=robo_factory.get_robot(RobotSize.SMALL)
        context={'x':random.randint(0,100), 'y':random.randint(0,100)}
        robot.display(context)


    """create large size robots"""

    for _ in range(10):
        robot=robo_factory.get_robot(RobotSize.LARGE)
        context={'x':random.randint(0,100), 'y':random.randint(0,100)}
        robot.display(context)
        

    """Lets check how many robots created: ideally in this case it should be 2 only but if you see we tried to create 20 robots but as we are using shared state of robots so only two got created and hence memory is optimized"""
    print(f"\nTotal robots created (shared): {robo_factory.total_robots_created()}")
