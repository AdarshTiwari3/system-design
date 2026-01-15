from enum import Enum


class Direction(Enum):
    """Represents the movement direction of the elevator."""

    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"
