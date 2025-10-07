import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_direction import MessageDirection
from ..models.message_type import MessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """Message (reply or note) on a ticket.

    Attributes:
        id (str):
        body (str):
        htmlized (bool):
        attachments (list['Attachment']):
        type_ (MessageType):
        created_at (datetime.datetime):
        from_name (Union[None, Unset, str]): Display name associated with the message. This is null when the sender did
            not include a display name.
        user_id (Union[None, Unset, str]): Id of the user who created the message. null if customer. This remains null
            for customer-authored or automated system messages.
        direction (Union[Unset, MessageDirection]): Message direction relative to the help desk. This is null for notes
            or channels where a direction is not applicable.
        from_ (Union[None, Unset, str]): Contact information of sender. This is null when the sender's address is not
            available for the channel.
        to (Union[None, Unset, str]): Contact information of recipient. This is null when the message is not directed at
            a specific recipient (for example, internal notes).
        more_body (Union[None, Unset, str]): Contains signature if removed from body. This is null when no signature was
            trimmed from the original content.
    """

    id: str
    body: str
    htmlized: bool
    attachments: list["Attachment"]
    type_: MessageType
    created_at: datetime.datetime
    from_name: Union[None, Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    direction: Union[Unset, MessageDirection] = UNSET
    from_: Union[None, Unset, str] = UNSET
    to: Union[None, Unset, str] = UNSET
    more_body: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        body = self.body

        htmlized = self.htmlized

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        type_ = self.type_.value

        created_at = self.created_at.isoformat()

        from_name: Union[None, Unset, str]
        if isinstance(self.from_name, Unset):
            from_name = UNSET
        else:
            from_name = self.from_name

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        more_body: Union[None, Unset, str]
        if isinstance(self.more_body, Unset):
            more_body = UNSET
        else:
            more_body = self.more_body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "body": body,
                "htmlized": htmlized,
                "attachments": attachments,
                "type": type_,
                "created_at": created_at,
            }
        )
        if from_name is not UNSET:
            field_dict["from_name"] = from_name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if direction is not UNSET:
            field_dict["direction"] = direction
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if more_body is not UNSET:
            field_dict["more_body"] = more_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment import Attachment

        d = dict(src_dict)
        id = d.pop("id")

        body = d.pop("body")

        htmlized = d.pop("htmlized")

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        type_ = MessageType(d.pop("type"))

        created_at = isoparse(d.pop("created_at"))

        def _parse_from_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_name = _parse_from_name(d.pop("from_name", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, MessageDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = MessageDirection(_direction)

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to = _parse_to(d.pop("to", UNSET))

        def _parse_more_body(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        more_body = _parse_more_body(d.pop("more_body", UNSET))

        message = cls(
            id=id,
            body=body,
            htmlized=htmlized,
            attachments=attachments,
            type_=type_,
            created_at=created_at,
            from_name=from_name,
            user_id=user_id,
            direction=direction,
            from_=from_,
            to=to,
            more_body=more_body,
        )

        message.additional_properties = d
        return message

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
