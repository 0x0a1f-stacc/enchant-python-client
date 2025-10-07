from enum import Enum


class CreateTicketXHTTPMethodOverride(str, Enum):
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
