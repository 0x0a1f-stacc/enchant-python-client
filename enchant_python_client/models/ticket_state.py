from enum import Enum


class TicketState(str, Enum):
    ARCHIVED = "archived"
    CLOSED = "closed"
    HOLD = "hold"
    OPEN = "open"
    SNOOZED = "snoozed"

    def __str__(self) -> str:
        return str(self.value)
