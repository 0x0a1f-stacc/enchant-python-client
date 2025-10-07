from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.envelope_headers import EnvelopeHeaders
    from ..models.envelope_response import EnvelopeResponse


T = TypeVar("T", bound="Envelope")


@_attrs_define
class Envelope:
    """Envelope wrapper returned when `envelope=true` is used. The actual response is in the `response` property.

    Attributes:
        status (int):
        headers (EnvelopeHeaders):
        response (EnvelopeResponse): Original response payload.
    """

    status: int
    headers: "EnvelopeHeaders"
    response: "EnvelopeResponse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        headers = self.headers.to_dict()

        response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "headers": headers,
                "response": response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.envelope_headers import EnvelopeHeaders
        from ..models.envelope_response import EnvelopeResponse

        d = dict(src_dict)
        status = d.pop("status")

        headers = EnvelopeHeaders.from_dict(d.pop("headers"))

        response = EnvelopeResponse.from_dict(d.pop("response"))

        envelope = cls(
            status=status,
            headers=headers,
            response=response,
        )

        envelope.additional_properties = d
        return envelope

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
