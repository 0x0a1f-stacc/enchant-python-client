from enum import Enum


class MessageType(str, Enum):
    NOTE = "note"
    REPLY = "reply"

    def __str__(self) -> str:
        return str(self.value)
