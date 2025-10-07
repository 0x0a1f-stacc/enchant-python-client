from enum import Enum


class TicketUpdateState(str, Enum):
    CLOSED = "closed"
    HOLD = "hold"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
