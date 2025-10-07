from enum import Enum


class ListTicketsSort(str, Enum):
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    USER_ID_UPDATED_AT = "user_id,-updated_at"
    VALUE_1 = "-updated_at"
    VALUE_3 = "-created_at"

    def __str__(self) -> str:
        return str(self.value)
