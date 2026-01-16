"""Request Implementation"""

from dataclasses import dataclass, field
from enums.request_type import RequestType
from enums.direction import Direction


@dataclass(
    frozen=True
)  # object immutable after creation. why? Multiple threads can safely read the same Request object. or After the object is created, no attribute can be modified.
class Request:
    """
    Represents a pickup or destination request in the elevator system.
    """

    source_floor: int
    target_floor: int
    request_type: RequestType
    direction: Direction = field(
        init=False
    )  # does not allow Request to pass this value in constructor, A request should never change once created. A passenger doesn’t suddenly change destination inside the system.
    """A user requested to go from Floor A → Floor B.

    Once created:

    That fact should never change."""

    """__post_init__() is a special hook provided by Python’s @dataclass, dataclass automatically creates __init__()"""

    def __post_init__(self):
        if self.source_floor == self.target_floor:
            raise ValueError("Source floor and target floor cannot be the same.")

        object.__setattr__(
            self, "direction", self._derive_direction()
        )  # Calculate the direction once and permanently store it inside the Request object. or self.direction = self._derive_direction()

    def _derive_direction(self) -> Direction:
        """
        Derives direction based on source and target floors, it computes the direction once.
        """
        if self.target_floor > self.source_floor:
            return Direction.UP

        return Direction.DOWN
