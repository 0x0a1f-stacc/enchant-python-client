from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvelopeHeaders")


@_attrs_define
class EnvelopeHeaders:
    """
    Attributes:
        rate_limit_limit (Union[Unset, int]): Maximum request credits for the current rate-limit window. This header is
            omitted when rate limiting does not apply to the operation.
        rate_limit_remaining (Union[Unset, int]): Remaining request credits in the current window. This header is
            omitted when the rate-limit information is unavailable for the response.
        rate_limit_used (Union[Unset, int]): Credits consumed by the request. This header is omitted when usage tracking
            is not reported for the response.
        rate_limit_reset (Union[Unset, int]): Seconds until the rate-limit window resets. This header is omitted when
            the reset time is not applicable (for example, unlimited plans).
    """

    rate_limit_limit: Union[Unset, int] = UNSET
    rate_limit_remaining: Union[Unset, int] = UNSET
    rate_limit_used: Union[Unset, int] = UNSET
    rate_limit_reset: Union[Unset, int] = UNSET
    additional_properties: dict[str, Union[int, str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate_limit_limit = self.rate_limit_limit

        rate_limit_remaining = self.rate_limit_remaining

        rate_limit_used = self.rate_limit_used

        rate_limit_reset = self.rate_limit_reset

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        field_dict.update({})
        if rate_limit_limit is not UNSET:
            field_dict["Rate-Limit-Limit"] = rate_limit_limit
        if rate_limit_remaining is not UNSET:
            field_dict["Rate-Limit-Remaining"] = rate_limit_remaining
        if rate_limit_used is not UNSET:
            field_dict["Rate-Limit-Used"] = rate_limit_used
        if rate_limit_reset is not UNSET:
            field_dict["Rate-Limit-Reset"] = rate_limit_reset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate_limit_limit = d.pop("Rate-Limit-Limit", UNSET)

        rate_limit_remaining = d.pop("Rate-Limit-Remaining", UNSET)

        rate_limit_used = d.pop("Rate-Limit-Used", UNSET)

        rate_limit_reset = d.pop("Rate-Limit-Reset", UNSET)

        envelope_headers = cls(
            rate_limit_limit=rate_limit_limit,
            rate_limit_remaining=rate_limit_remaining,
            rate_limit_used=rate_limit_used,
            rate_limit_reset=rate_limit_reset,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union[int, str]:
                return cast(Union[int, str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        envelope_headers.additional_properties = additional_properties
        return envelope_headers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[int, str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[int, str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
