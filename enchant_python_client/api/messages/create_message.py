from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_message_xhttp_method_override import CreateMessageXHTTPMethodOverride
from ...models.envelope import Envelope
from ...models.error import Error
from ...models.message import Message
from ...models.message_create_inbound_reply import MessageCreateInboundReply
from ...models.message_create_note import MessageCreateNote
from ...models.message_create_outbound_reply import MessageCreateOutboundReply
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticket_id: str,
    *,
    body: Union["MessageCreateInboundReply", "MessageCreateNote", "MessageCreateOutboundReply"],
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateMessageXHTTPMethodOverride] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_http_method_override, Unset):
        headers["X-HTTP-Method-Override"] = str(x_http_method_override)

    params: dict[str, Any] = {}

    params["envelope"] = envelope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/tickets/{ticket_id}/messages",
        "params": params,
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, MessageCreateNote):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MessageCreateInboundReply):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Envelope, Error, Message, ValidationError]:
    if response.status_code == 200:
        response_200 = Envelope.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Message.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 415:
        response_415 = Error.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Envelope, Error, Message, ValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["MessageCreateInboundReply", "MessageCreateNote", "MessageCreateOutboundReply"],
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateMessageXHTTPMethodOverride] = UNSET,
) -> Response[Union[Any, Envelope, Error, Message, ValidationError]]:
    """Create a message on a ticket

     Creates a note, an inbound reply, or an outbound reply on the given ticket. Attachments must be
    uploaded first and referenced by `attachment_ids`.

    Args:
        ticket_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateMessageXHTTPMethodOverride]):
        body (Union['MessageCreateInboundReply', 'MessageCreateNote',
            'MessageCreateOutboundReply']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Envelope, Error, Message, ValidationError]]
    """

    kwargs = _get_kwargs(
        ticket_id=ticket_id,
        body=body,
        envelope=envelope,
        x_http_method_override=x_http_method_override,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["MessageCreateInboundReply", "MessageCreateNote", "MessageCreateOutboundReply"],
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateMessageXHTTPMethodOverride] = UNSET,
) -> Optional[Union[Any, Envelope, Error, Message, ValidationError]]:
    """Create a message on a ticket

     Creates a note, an inbound reply, or an outbound reply on the given ticket. Attachments must be
    uploaded first and referenced by `attachment_ids`.

    Args:
        ticket_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateMessageXHTTPMethodOverride]):
        body (Union['MessageCreateInboundReply', 'MessageCreateNote',
            'MessageCreateOutboundReply']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Envelope, Error, Message, ValidationError]
    """

    return sync_detailed(
        ticket_id=ticket_id,
        client=client,
        body=body,
        envelope=envelope,
        x_http_method_override=x_http_method_override,
    ).parsed


async def asyncio_detailed(
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["MessageCreateInboundReply", "MessageCreateNote", "MessageCreateOutboundReply"],
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateMessageXHTTPMethodOverride] = UNSET,
) -> Response[Union[Any, Envelope, Error, Message, ValidationError]]:
    """Create a message on a ticket

     Creates a note, an inbound reply, or an outbound reply on the given ticket. Attachments must be
    uploaded first and referenced by `attachment_ids`.

    Args:
        ticket_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateMessageXHTTPMethodOverride]):
        body (Union['MessageCreateInboundReply', 'MessageCreateNote',
            'MessageCreateOutboundReply']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Envelope, Error, Message, ValidationError]]
    """

    kwargs = _get_kwargs(
        ticket_id=ticket_id,
        body=body,
        envelope=envelope,
        x_http_method_override=x_http_method_override,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["MessageCreateInboundReply", "MessageCreateNote", "MessageCreateOutboundReply"],
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateMessageXHTTPMethodOverride] = UNSET,
) -> Optional[Union[Any, Envelope, Error, Message, ValidationError]]:
    """Create a message on a ticket

     Creates a note, an inbound reply, or an outbound reply on the given ticket. Attachments must be
    uploaded first and referenced by `attachment_ids`.

    Args:
        ticket_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateMessageXHTTPMethodOverride]):
        body (Union['MessageCreateInboundReply', 'MessageCreateNote',
            'MessageCreateOutboundReply']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Envelope, Error, Message, ValidationError]
    """

    return (
        await asyncio_detailed(
            ticket_id=ticket_id,
            client=client,
            body=body,
            envelope=envelope,
            x_http_method_override=x_http_method_override,
        )
    ).parsed
