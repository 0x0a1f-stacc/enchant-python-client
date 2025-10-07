from enum import Enum


class MessageCreateOutboundReplyDirection(str, Enum):
    OUT = "out"

    def __str__(self) -> str:
        return str(self.value)
