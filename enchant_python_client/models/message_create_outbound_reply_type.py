from enum import Enum


class MessageCreateOutboundReplyType(str, Enum):
    REPLY = "reply"

    def __str__(self) -> str:
        return str(self.value)
