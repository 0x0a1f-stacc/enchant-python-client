from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.message_create_inbound_reply_direction import MessageCreateInboundReplyDirection
from ..models.message_create_inbound_reply_type import MessageCreateInboundReplyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageCreateInboundReply")


@_attrs_define
class MessageCreateInboundReply:
    """
    Attributes:
        type_ (MessageCreateInboundReplyType):
        direction (MessageCreateInboundReplyDirection):
        from_name (str):
        body (str):
        htmlized (bool):
        from_ (str):
        to (Union[Unset, str]): Recipient address as provided by the inbound channel. Omit when the incoming message did
            not specify an explicit recipient.
        attachment_ids (Union[Unset, list[str]]): Identifiers of attachments that were part of the inbound reply. Omit
            when the inbound message had no attachments.
    """

    type_: MessageCreateInboundReplyType
    direction: MessageCreateInboundReplyDirection
    from_name: str
    body: str
    htmlized: bool
    from_: str
    to: Union[Unset, str] = UNSET
    attachment_ids: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        direction = self.direction.value

        from_name = self.from_name

        body = self.body

        htmlized = self.htmlized

        from_ = self.from_

        to = self.to

        attachment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = self.attachment_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "direction": direction,
                "from_name": from_name,
                "body": body,
                "htmlized": htmlized,
                "from": from_,
            }
        )
        if to is not UNSET:
            field_dict["to"] = to
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = MessageCreateInboundReplyType(d.pop("type"))

        direction = MessageCreateInboundReplyDirection(d.pop("direction"))

        from_name = d.pop("from_name")

        body = d.pop("body")

        htmlized = d.pop("htmlized")

        from_ = d.pop("from")

        to = d.pop("to", UNSET)

        attachment_ids = cast(list[str], d.pop("attachment_ids", UNSET))

        message_create_inbound_reply = cls(
            type_=type_,
            direction=direction,
            from_name=from_name,
            body=body,
            htmlized=htmlized,
            from_=from_,
            to=to,
            attachment_ids=attachment_ids,
        )

        return message_create_inbound_reply
