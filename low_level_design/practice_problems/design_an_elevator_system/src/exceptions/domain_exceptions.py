"""Domain Exceptions for an Elevator"""


class ElevatorException(Exception):
    pass


class NoElevatorAvailableError(ElevatorException):
    pass


class InvalidRequestError(ElevatorException):
    pass


class CapacityExceededError(ElevatorException):
    pass
