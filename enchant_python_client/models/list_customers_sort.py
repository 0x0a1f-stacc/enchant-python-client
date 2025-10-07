from enum import Enum


class ListCustomersSort(str, Enum):
    CREATED_AT = "created_at"

    def __str__(self) -> str:
        return str(self.value)
