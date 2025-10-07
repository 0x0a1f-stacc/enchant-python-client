import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ticket_state import TicketState
from ..models.ticket_type import TicketType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer import Customer
    from ..models.message import Message
    from ..models.ticket_with_embeds_inbox import TicketWithEmbedsInbox
    from ..models.ticket_with_embeds_labels_item import TicketWithEmbedsLabelsItem
    from ..models.user import User


T = TypeVar("T", bound="TicketWithEmbeds")


@_attrs_define
class TicketWithEmbeds:
    """
    Attributes:
        id (str):
        number (int): Friendly ticket number, unique across the help desk.
        customer_id (str):
        inbox_id (str): Associated inbox id.
        label_ids (list[str]):
        state (TicketState):
        subject (str):
        type_ (TicketType):
        spam (bool):
        trash (bool):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        user_id (Union[None, Unset, str]): Assigned user id. Can be null. This will be null when the ticket has not been
            assigned to an agent.
        snoozed_until (Union[None, Unset, datetime.datetime]): Timestamp for when a snoozed ticket reopens. This is null
            when the ticket is not currently snoozed.
        reply_to (Union[None, Unset, str]): DEPRECATED. Default To: field of a new reply. This is null when no legacy
            default reply address has been configured for the ticket.
        reply_cc (Union[None, Unset, str]): DEPRECATED. Default Cc: field of a new reply. This is null when no legacy
            default Cc recipients are configured for the ticket.
        summary (Union[None, Unset, str]): Concise overview of the latest conversation on the ticket. This is null until
            the ticket has any messages to summarize or summarization is disabled.
        customer (Union[Unset, Customer]):
        labels (Union[Unset, list['TicketWithEmbedsLabelsItem']]): Embedded label metadata. This array is omitted unless
            label embedding is requested in the response.
        messages (Union[Unset, list['Message']]): Embedded messages for the ticket. This array is omitted unless
            `embed=messages` is requested.
        user (Union[Unset, User]):
        inbox (Union[Unset, TicketWithEmbedsInbox]): Embedded inbox details. This object is omitted unless inbox
            embedding is requested for the ticket response.
    """

    id: str
    number: int
    customer_id: str
    inbox_id: str
    label_ids: list[str]
    state: TicketState
    subject: str
    type_: TicketType
    spam: bool
    trash: bool
    updated_at: datetime.datetime
    created_at: datetime.datetime
    user_id: Union[None, Unset, str] = UNSET
    snoozed_until: Union[None, Unset, datetime.datetime] = UNSET
    reply_to: Union[None, Unset, str] = UNSET
    reply_cc: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    customer: Union[Unset, "Customer"] = UNSET
    labels: Union[Unset, list["TicketWithEmbedsLabelsItem"]] = UNSET
    messages: Union[Unset, list["Message"]] = UNSET
    user: Union[Unset, "User"] = UNSET
    inbox: Union[Unset, "TicketWithEmbedsInbox"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        customer_id = self.customer_id

        inbox_id = self.inbox_id

        label_ids = self.label_ids

        state = self.state.value

        subject = self.subject

        type_ = self.type_.value

        spam = self.spam

        trash = self.trash

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        snoozed_until: Union[None, Unset, str]
        if isinstance(self.snoozed_until, Unset):
            snoozed_until = UNSET
        elif isinstance(self.snoozed_until, datetime.datetime):
            snoozed_until = self.snoozed_until.isoformat()
        else:
            snoozed_until = self.snoozed_until

        reply_to: Union[None, Unset, str]
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

        reply_cc: Union[None, Unset, str]
        if isinstance(self.reply_cc, Unset):
            reply_cc = UNSET
        else:
            reply_cc = self.reply_cc

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        customer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        labels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        inbox: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inbox, Unset):
            inbox = self.inbox.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "customer_id": customer_id,
                "inbox_id": inbox_id,
                "label_ids": label_ids,
                "state": state,
                "subject": subject,
                "type": type_,
                "spam": spam,
                "trash": trash,
                "updated_at": updated_at,
                "created_at": created_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if snoozed_until is not UNSET:
            field_dict["snoozed_until"] = snoozed_until
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if reply_cc is not UNSET:
            field_dict["reply_cc"] = reply_cc
        if summary is not UNSET:
            field_dict["summary"] = summary
        if customer is not UNSET:
            field_dict["customer"] = customer
        if labels is not UNSET:
            field_dict["labels"] = labels
        if messages is not UNSET:
            field_dict["messages"] = messages
        if user is not UNSET:
            field_dict["user"] = user
        if inbox is not UNSET:
            field_dict["inbox"] = inbox

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer import Customer
        from ..models.message import Message
        from ..models.ticket_with_embeds_inbox import TicketWithEmbedsInbox
        from ..models.ticket_with_embeds_labels_item import TicketWithEmbedsLabelsItem
        from ..models.user import User

        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        customer_id = d.pop("customer_id")

        inbox_id = d.pop("inbox_id")

        label_ids = cast(list[str], d.pop("label_ids"))

        state = TicketState(d.pop("state"))

        subject = d.pop("subject")

        type_ = TicketType(d.pop("type"))

        spam = d.pop("spam")

        trash = d.pop("trash")

        updated_at = isoparse(d.pop("updated_at"))

        created_at = isoparse(d.pop("created_at"))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_snoozed_until(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                snoozed_until_type_0 = isoparse(data)

                return snoozed_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        snoozed_until = _parse_snoozed_until(d.pop("snoozed_until", UNSET))

        def _parse_reply_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        def _parse_reply_cc(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reply_cc = _parse_reply_cc(d.pop("reply_cc", UNSET))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, Customer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = Customer.from_dict(_customer)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = TicketWithEmbedsLabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _inbox = d.pop("inbox", UNSET)
        inbox: Union[Unset, TicketWithEmbedsInbox]
        if isinstance(_inbox, Unset):
            inbox = UNSET
        else:
            inbox = TicketWithEmbedsInbox.from_dict(_inbox)

        ticket_with_embeds = cls(
            id=id,
            number=number,
            customer_id=customer_id,
            inbox_id=inbox_id,
            label_ids=label_ids,
            state=state,
            subject=subject,
            type_=type_,
            spam=spam,
            trash=trash,
            updated_at=updated_at,
            created_at=created_at,
            user_id=user_id,
            snoozed_until=snoozed_until,
            reply_to=reply_to,
            reply_cc=reply_cc,
            summary=summary,
            customer=customer,
            labels=labels,
            messages=messages,
            user=user,
            inbox=inbox,
        )

        ticket_with_embeds.additional_properties = d
        return ticket_with_embeds

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
