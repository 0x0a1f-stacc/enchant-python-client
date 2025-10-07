from enum import Enum


class ListTicketsStateItem(str, Enum):
    CLOSED = "closed"
    HOLD = "hold"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
