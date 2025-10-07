from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.ticket_update_state import TicketUpdateState
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketUpdate")


@_attrs_define
class TicketUpdate:
    """Fields updatable via PATCH.

    Attributes:
        user_id (Union[None, Unset, str]): Identifier of the user to assign the ticket to. Omit to keep the existing
            assignment, and send null to unassign the ticket.
        inbox_id (Union[Unset, str]): Identifier of the inbox to move the ticket into. Omit when the ticket should
            remain in its current inbox.
        state (Union[Unset, TicketUpdateState]): Ticket state to apply. Omit when the current state should not be
            changed.
        label_ids (Union[Unset, list[str]]): Set labels to this list; empty array removes all labels. Omit when the
            ticket's labels should stay as-is.
        spam (Union[Unset, bool]): spam and trash cannot both be true. Omit when the spam flag should remain unchanged.
        trash (Union[Unset, bool]): spam and trash cannot both be true. Omit when the trash flag should remain
            unchanged.
        subject (Union[Unset, str]): Subject line for the ticket. Omit when the existing subject should be preserved.
    """

    user_id: Union[None, Unset, str] = UNSET
    inbox_id: Union[Unset, str] = UNSET
    state: Union[Unset, TicketUpdateState] = UNSET
    label_ids: Union[Unset, list[str]] = UNSET
    spam: Union[Unset, bool] = UNSET
    trash: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        inbox_id = self.inbox_id

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        label_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        spam = self.spam

        trash = self.trash

        subject = self.subject

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if inbox_id is not UNSET:
            field_dict["inbox_id"] = inbox_id
        if state is not UNSET:
            field_dict["state"] = state
        if label_ids is not UNSET:
            field_dict["label_ids"] = label_ids
        if spam is not UNSET:
            field_dict["spam"] = spam
        if trash is not UNSET:
            field_dict["trash"] = trash
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        inbox_id = d.pop("inbox_id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, TicketUpdateState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TicketUpdateState(_state)

        label_ids = cast(list[str], d.pop("label_ids", UNSET))

        spam = d.pop("spam", UNSET)

        trash = d.pop("trash", UNSET)

        subject = d.pop("subject", UNSET)

        ticket_update = cls(
            user_id=user_id,
            inbox_id=inbox_id,
            state=state,
            label_ids=label_ids,
            spam=spam,
            trash=trash,
            subject=subject,
        )

        return ticket_update
