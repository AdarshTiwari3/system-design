from enum import Enum


class RequestType(Enum):
    """Represents the origin of a request: hall call or cabin call."""

    HALL_CALL = "HALL_CALL"
    CABIN_CALL = "CABIN_CALL"
