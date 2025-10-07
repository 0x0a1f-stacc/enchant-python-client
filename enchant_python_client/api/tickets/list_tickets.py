import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.envelope import Envelope
from ...models.error import Error
from ...models.list_tickets_sort import ListTicketsSort
from ...models.list_tickets_state_item import ListTicketsStateItem
from ...models.ticket import Ticket
from ...models.ticket_type import TicketType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, list[str]] = UNSET,
    count: Union[Unset, bool] = False,
    envelope: Union[Unset, bool] = False,
    page: Union[Unset, int] = 1,
    per_page: Union[Unset, int] = 10,
    sort: Union[Unset, ListTicketsSort] = ListTicketsSort.VALUE_3,
    id: Union[Unset, list[str]] = UNSET,
    inbox_id: Union[Unset, list[str]] = UNSET,
    state: Union[Unset, list[ListTicketsStateItem]] = UNSET,
    user_id: Union[Unset, list[Union[None, str]]] = UNSET,
    label_id: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[TicketType]] = UNSET,
    spam: Union[Unset, bool] = UNSET,
    trash: Union[Unset, bool] = UNSET,
    since_created_at: Union[Unset, datetime.datetime] = UNSET,
    since_updated_at: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["count"] = count

    params["envelope"] = envelope

    params["page"] = page

    params["per_page"] = per_page

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_id: Union[Unset, list[str]] = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    json_inbox_id: Union[Unset, list[str]] = UNSET
    if not isinstance(inbox_id, Unset):
        json_inbox_id = inbox_id

    params["inbox_id"] = json_inbox_id

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    json_user_id: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = []
        for user_id_item_data in user_id:
            user_id_item: Union[None, str]
            user_id_item = user_id_item_data
            json_user_id.append(user_id_item)

    params["user_id"] = json_user_id

    json_label_id: Union[Unset, list[str]] = UNSET
    if not isinstance(label_id, Unset):
        json_label_id = label_id

    params["label_id"] = json_label_id

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params["spam"] = spam

    params["trash"] = trash

    json_since_created_at: Union[Unset, str] = UNSET
    if not isinstance(since_created_at, Unset):
        json_since_created_at = since_created_at.isoformat()
    params["since_created_at"] = json_since_created_at

    json_since_updated_at: Union[Unset, str] = UNSET
    if not isinstance(since_updated_at, Unset):
        json_since_updated_at = since_updated_at.isoformat()
    params["since_updated_at"] = json_since_updated_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tickets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Error, Union["Envelope", list["Ticket"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["Envelope", list["Ticket"]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:
                    response_200_type_0_item = Ticket.from_dict(response_200_type_0_item_data)

                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = Envelope.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error, Union["Envelope", list["Ticket"]]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    count: Union[Unset, bool] = False,
    envelope: Union[Unset, bool] = False,
    page: Union[Unset, int] = 1,
    per_page: Union[Unset, int] = 10,
    sort: Union[Unset, ListTicketsSort] = ListTicketsSort.VALUE_3,
    id: Union[Unset, list[str]] = UNSET,
    inbox_id: Union[Unset, list[str]] = UNSET,
    state: Union[Unset, list[ListTicketsStateItem]] = UNSET,
    user_id: Union[Unset, list[Union[None, str]]] = UNSET,
    label_id: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[TicketType]] = UNSET,
    spam: Union[Unset, bool] = UNSET,
    trash: Union[Unset, bool] = UNSET,
    since_created_at: Union[Unset, datetime.datetime] = UNSET,
    since_updated_at: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, Error, Union["Envelope", list["Ticket"]]]]:
    """List tickets

     Returns tickets. Supports filtering, pagination, sorting, field filtering, counting and enveloping.

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, ListTicketsSort]):  Default: ListTicketsSort.VALUE_3.
        id (Union[Unset, list[str]]):
        inbox_id (Union[Unset, list[str]]):
        state (Union[Unset, list[ListTicketsStateItem]]):
        user_id (Union[Unset, list[Union[None, str]]]):
        label_id (Union[Unset, list[str]]):
        type_ (Union[Unset, list[TicketType]]):
        spam (Union[Unset, bool]):
        trash (Union[Unset, bool]):
        since_created_at (Union[Unset, datetime.datetime]):
        since_updated_at (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Envelope', list['Ticket']]]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        count=count,
        envelope=envelope,
        page=page,
        per_page=per_page,
        sort=sort,
        id=id,
        inbox_id=inbox_id,
        state=state,
        user_id=user_id,
        label_id=label_id,
        type_=type_,
        spam=spam,
        trash=trash,
        since_created_at=since_created_at,
        since_updated_at=since_updated_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    count: Union[Unset, bool] = False,
    envelope: Union[Unset, bool] = False,
    page: Union[Unset, int] = 1,
    per_page: Union[Unset, int] = 10,
    sort: Union[Unset, ListTicketsSort] = ListTicketsSort.VALUE_3,
    id: Union[Unset, list[str]] = UNSET,
    inbox_id: Union[Unset, list[str]] = UNSET,
    state: Union[Unset, list[ListTicketsStateItem]] = UNSET,
    user_id: Union[Unset, list[Union[None, str]]] = UNSET,
    label_id: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[TicketType]] = UNSET,
    spam: Union[Unset, bool] = UNSET,
    trash: Union[Unset, bool] = UNSET,
    since_created_at: Union[Unset, datetime.datetime] = UNSET,
    since_updated_at: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, Error, Union["Envelope", list["Ticket"]]]]:
    """List tickets

     Returns tickets. Supports filtering, pagination, sorting, field filtering, counting and enveloping.

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, ListTicketsSort]):  Default: ListTicketsSort.VALUE_3.
        id (Union[Unset, list[str]]):
        inbox_id (Union[Unset, list[str]]):
        state (Union[Unset, list[ListTicketsStateItem]]):
        user_id (Union[Unset, list[Union[None, str]]]):
        label_id (Union[Unset, list[str]]):
        type_ (Union[Unset, list[TicketType]]):
        spam (Union[Unset, bool]):
        trash (Union[Unset, bool]):
        since_created_at (Union[Unset, datetime.datetime]):
        since_updated_at (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Envelope', list['Ticket']]]
    """

    return sync_detailed(
        client=client,
        fields=fields,
        count=count,
        envelope=envelope,
        page=page,
        per_page=per_page,
        sort=sort,
        id=id,
        inbox_id=inbox_id,
        state=state,
        user_id=user_id,
        label_id=label_id,
        type_=type_,
        spam=spam,
        trash=trash,
        since_created_at=since_created_at,
        since_updated_at=since_updated_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    count: Union[Unset, bool] = False,
    envelope: Union[Unset, bool] = False,
    page: Union[Unset, int] = 1,
    per_page: Union[Unset, int] = 10,
    sort: Union[Unset, ListTicketsSort] = ListTicketsSort.VALUE_3,
    id: Union[Unset, list[str]] = UNSET,
    inbox_id: Union[Unset, list[str]] = UNSET,
    state: Union[Unset, list[ListTicketsStateItem]] = UNSET,
    user_id: Union[Unset, list[Union[None, str]]] = UNSET,
    label_id: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[TicketType]] = UNSET,
    spam: Union[Unset, bool] = UNSET,
    trash: Union[Unset, bool] = UNSET,
    since_created_at: Union[Unset, datetime.datetime] = UNSET,
    since_updated_at: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, Error, Union["Envelope", list["Ticket"]]]]:
    """List tickets

     Returns tickets. Supports filtering, pagination, sorting, field filtering, counting and enveloping.

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, ListTicketsSort]):  Default: ListTicketsSort.VALUE_3.
        id (Union[Unset, list[str]]):
        inbox_id (Union[Unset, list[str]]):
        state (Union[Unset, list[ListTicketsStateItem]]):
        user_id (Union[Unset, list[Union[None, str]]]):
        label_id (Union[Unset, list[str]]):
        type_ (Union[Unset, list[TicketType]]):
        spam (Union[Unset, bool]):
        trash (Union[Unset, bool]):
        since_created_at (Union[Unset, datetime.datetime]):
        since_updated_at (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Envelope', list['Ticket']]]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        count=count,
        envelope=envelope,
        page=page,
        per_page=per_page,
        sort=sort,
        id=id,
        inbox_id=inbox_id,
        state=state,
        user_id=user_id,
        label_id=label_id,
        type_=type_,
        spam=spam,
        trash=trash,
        since_created_at=since_created_at,
        since_updated_at=since_updated_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    count: Union[Unset, bool] = False,
    envelope: Union[Unset, bool] = False,
    page: Union[Unset, int] = 1,
    per_page: Union[Unset, int] = 10,
    sort: Union[Unset, ListTicketsSort] = ListTicketsSort.VALUE_3,
    id: Union[Unset, list[str]] = UNSET,
    inbox_id: Union[Unset, list[str]] = UNSET,
    state: Union[Unset, list[ListTicketsStateItem]] = UNSET,
    user_id: Union[Unset, list[Union[None, str]]] = UNSET,
    label_id: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[TicketType]] = UNSET,
    spam: Union[Unset, bool] = UNSET,
    trash: Union[Unset, bool] = UNSET,
    since_created_at: Union[Unset, datetime.datetime] = UNSET,
    since_updated_at: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, Error, Union["Envelope", list["Ticket"]]]]:
    """List tickets

     Returns tickets. Supports filtering, pagination, sorting, field filtering, counting and enveloping.

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, ListTicketsSort]):  Default: ListTicketsSort.VALUE_3.
        id (Union[Unset, list[str]]):
        inbox_id (Union[Unset, list[str]]):
        state (Union[Unset, list[ListTicketsStateItem]]):
        user_id (Union[Unset, list[Union[None, str]]]):
        label_id (Union[Unset, list[str]]):
        type_ (Union[Unset, list[TicketType]]):
        spam (Union[Unset, bool]):
        trash (Union[Unset, bool]):
        since_created_at (Union[Unset, datetime.datetime]):
        since_updated_at (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Envelope', list['Ticket']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            count=count,
            envelope=envelope,
            page=page,
            per_page=per_page,
            sort=sort,
            id=id,
            inbox_id=inbox_id,
            state=state,
            user_id=user_id,
            label_id=label_id,
            type_=type_,
            spam=spam,
            trash=trash,
            since_created_at=since_created_at,
            since_updated_at=since_updated_at,
        )
    ).parsed
