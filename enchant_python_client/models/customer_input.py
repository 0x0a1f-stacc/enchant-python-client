from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_input import ContactInput


T = TypeVar("T", bound="CustomerInput")


@_attrs_define
class CustomerInput:
    """
    Attributes:
        first_name (Union[None, Unset, str]): Customer's given name to create or update. Omit or send null when the
            first name is unknown.
        last_name (Union[None, Unset, str]): Customer's family name to create or update. Omit or send null when the last
            name should remain unset.
        summary (Union[None, Unset, str]): Internal notes about the customer. Omit or send null when no summary should
            be stored.
        contacts (Union[Unset, list['ContactInput']]): Contact points such as email or phone. Omit when not adding or
            modifying contact information in this request.
    """

    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    contacts: Union[Unset, list["ContactInput"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        contacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_input import ContactInput

        d = dict(src_dict)

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = ContactInput.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        customer_input = cls(
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            contacts=contacts,
        )

        return customer_input
