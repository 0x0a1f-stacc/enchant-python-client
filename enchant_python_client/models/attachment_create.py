from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AttachmentCreate")


@_attrs_define
class AttachmentCreate:
    """
    Attributes:
        name (str): File name.
        type_ (str): MIME type.
        data (str): Base64-encoded file bytes.
    """

    name: str
    type_: str
    data: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        data = d.pop("data")

        attachment_create = cls(
            name=name,
            type_=type_,
            data=data,
        )

        return attachment_create
