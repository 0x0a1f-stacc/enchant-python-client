from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.contact_type import ContactType

T = TypeVar("T", bound="ContactInput")


@_attrs_define
class ContactInput:
    """
    Attributes:
        type_ (ContactType):
        value (str):
    """

    type_: ContactType
    value: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ContactType(d.pop("type"))

        value = d.pop("value")

        contact_input = cls(
            type_=type_,
            value=value,
        )

        return contact_input
