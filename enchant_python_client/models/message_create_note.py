from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.message_create_note_type import MessageCreateNoteType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageCreateNote")


@_attrs_define
class MessageCreateNote:
    """
    Attributes:
        type_ (MessageCreateNoteType):
        user_id (str):
        body (str):
        htmlized (bool):
        attachment_ids (Union[Unset, list[str]]): Identifiers of attachments to include with the note. Omit when the
            note does not reference any attachments.
    """

    type_: MessageCreateNoteType
    user_id: str
    body: str
    htmlized: bool
    attachment_ids: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        user_id = self.user_id

        body = self.body

        htmlized = self.htmlized

        attachment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = self.attachment_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "user_id": user_id,
                "body": body,
                "htmlized": htmlized,
            }
        )
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = MessageCreateNoteType(d.pop("type"))

        user_id = d.pop("user_id")

        body = d.pop("body")

        htmlized = d.pop("htmlized")

        attachment_ids = cast(list[str], d.pop("attachment_ids", UNSET))

        message_create_note = cls(
            type_=type_,
            user_id=user_id,
            body=body,
            htmlized=htmlized,
            attachment_ids=attachment_ids,
        )

        return message_create_note
