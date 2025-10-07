from enum import Enum


class ContactType(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    TWITTER = "twitter"

    def __str__(self) -> str:
        return str(self.value)
