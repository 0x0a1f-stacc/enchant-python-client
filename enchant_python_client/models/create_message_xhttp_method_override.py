from enum import Enum


class CreateMessageXHTTPMethodOverride(str, Enum):
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
