from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.envelope import Envelope
from ...models.error import Error
from ...models.get_ticket_embed_item import GetTicketEmbedItem
from ...models.ticket_with_embeds import TicketWithEmbeds
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticket_id: str,
    *,
    embed: Union[Unset, list[GetTicketEmbedItem]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_embed: Union[Unset, list[str]] = UNSET
    if not isinstance(embed, Unset):
        json_embed = []
        for embed_item_data in embed:
            embed_item = embed_item_data.value
            json_embed.append(embed_item)

    params["embed"] = json_embed

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["envelope"] = envelope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tickets/{ticket_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Error, Union["Envelope", "TicketWithEmbeds"]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["Envelope", "TicketWithEmbeds"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = TicketWithEmbeds.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = Envelope.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error, Union["Envelope", "TicketWithEmbeds"]]]:
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
    embed: Union[Unset, list[GetTicketEmbedItem]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Error, Union["Envelope", "TicketWithEmbeds"]]]:
    """Get a ticket

    Args:
        ticket_id (str):
        embed (Union[Unset, list[GetTicketEmbedItem]]):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Envelope', 'TicketWithEmbeds']]]
    """

    kwargs = _get_kwargs(
        ticket_id=ticket_id,
        embed=embed,
        fields=fields,
        envelope=envelope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    embed: Union[Unset, list[GetTicketEmbedItem]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Error, Union["Envelope", "TicketWithEmbeds"]]]:
    """Get a ticket

    Args:
        ticket_id (str):
        embed (Union[Unset, list[GetTicketEmbedItem]]):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Envelope', 'TicketWithEmbeds']]
    """

    return sync_detailed(
        ticket_id=ticket_id,
        client=client,
        embed=embed,
        fields=fields,
        envelope=envelope,
    ).parsed


async def asyncio_detailed(
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    embed: Union[Unset, list[GetTicketEmbedItem]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Error, Union["Envelope", "TicketWithEmbeds"]]]:
    """Get a ticket

    Args:
        ticket_id (str):
        embed (Union[Unset, list[GetTicketEmbedItem]]):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Envelope', 'TicketWithEmbeds']]]
    """

    kwargs = _get_kwargs(
        ticket_id=ticket_id,
        embed=embed,
        fields=fields,
        envelope=envelope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    embed: Union[Unset, list[GetTicketEmbedItem]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Error, Union["Envelope", "TicketWithEmbeds"]]]:
    """Get a ticket

    Args:
        ticket_id (str):
        embed (Union[Unset, list[GetTicketEmbedItem]]):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Envelope', 'TicketWithEmbeds']]
    """

    return (
        await asyncio_detailed(
            ticket_id=ticket_id,
            client=client,
            embed=embed,
            fields=fields,
            envelope=envelope,
        )
    ).parsed
