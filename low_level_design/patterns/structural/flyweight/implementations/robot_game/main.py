"""client runner"""
from game.game import run_game
def run_flyweight_robots_game():
    print("\nrunning the robo games using flying weight design patterns")
    run_game()


if __name__ == "__main__":
    print("\nFlyweight Design Pattern")
    run_flyweight_robots_game()