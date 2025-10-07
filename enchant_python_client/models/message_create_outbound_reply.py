from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.message_create_outbound_reply_direction import MessageCreateOutboundReplyDirection
from ..models.message_create_outbound_reply_type import MessageCreateOutboundReplyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageCreateOutboundReply")


@_attrs_define
class MessageCreateOutboundReply:
    """
    Attributes:
        type_ (MessageCreateOutboundReplyType):
        direction (MessageCreateOutboundReplyDirection):
        body (str):
        htmlized (bool):
        user_id (str):
        to (str):
        attachment_ids (Union[Unset, list[str]]): Identifiers of previously uploaded attachments to include with the
            outbound reply. Omit when sending a reply without attachments.
    """

    type_: MessageCreateOutboundReplyType
    direction: MessageCreateOutboundReplyDirection
    body: str
    htmlized: bool
    user_id: str
    to: str
    attachment_ids: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        direction = self.direction.value

        body = self.body

        htmlized = self.htmlized

        user_id = self.user_id

        to = self.to

        attachment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = self.attachment_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "direction": direction,
                "body": body,
                "htmlized": htmlized,
                "user_id": user_id,
                "to": to,
            }
        )
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = MessageCreateOutboundReplyType(d.pop("type"))

        direction = MessageCreateOutboundReplyDirection(d.pop("direction"))

        body = d.pop("body")

        htmlized = d.pop("htmlized")

        user_id = d.pop("user_id")

        to = d.pop("to")

        attachment_ids = cast(list[str], d.pop("attachment_ids", UNSET))

        message_create_outbound_reply = cls(
            type_=type_,
            direction=direction,
            body=body,
            htmlized=htmlized,
            user_id=user_id,
            to=to,
            attachment_ids=attachment_ids,
        )

        return message_create_outbound_reply
