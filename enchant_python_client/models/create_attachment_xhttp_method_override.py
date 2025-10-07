from enum import Enum


class CreateAttachmentXHTTPMethodOverride(str, Enum):
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
