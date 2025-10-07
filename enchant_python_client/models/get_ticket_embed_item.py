from enum import Enum


class GetTicketEmbedItem(str, Enum):
    CUSTOMER = "customer"
    GROUP = "group"
    INBOX = "inbox"
    LABELS = "labels"
    MESSAGES = "messages"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
