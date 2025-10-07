from enum import Enum


class MessageCreateInboundReplyDirection(str, Enum):
    IN = "in"

    def __str__(self) -> str:
        return str(self.value)
