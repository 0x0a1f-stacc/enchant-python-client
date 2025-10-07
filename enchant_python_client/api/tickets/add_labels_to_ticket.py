from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.envelope import Envelope
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticket_id: str,
    label_ids: list[str],
    *,
    envelope: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["envelope"] = envelope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/tickets/{ticket_id}/labels/{label_ids}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Envelope, Error]:
    if response.status_code == 200:
        response_200 = Envelope.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Union[Any, Envelope, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticket_id: str,
    label_ids: list[str],
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Envelope, Error]]:
    """Add one or more labels to a ticket

    Args:
        ticket_id (str):
        label_ids (list[str]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Envelope, Error]]
    """

    kwargs = _get_kwargs(
        ticket_id=ticket_id,
        label_ids=label_ids,
        envelope=envelope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticket_id: str,
    label_ids: list[str],
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Envelope, Error]]:
    """Add one or more labels to a ticket

    Args:
        ticket_id (str):
        label_ids (list[str]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Envelope, Error]
    """

    return sync_detailed(
        ticket_id=ticket_id,
        label_ids=label_ids,
        client=client,
        envelope=envelope,
    ).parsed


async def asyncio_detailed(
    ticket_id: str,
    label_ids: list[str],
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Envelope, Error]]:
    """Add one or more labels to a ticket

    Args:
        ticket_id (str):
        label_ids (list[str]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Envelope, Error]]
    """

    kwargs = _get_kwargs(
        ticket_id=ticket_id,
        label_ids=label_ids,
        envelope=envelope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticket_id: str,
    label_ids: list[str],
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Envelope, Error]]:
    """Add one or more labels to a ticket

    Args:
        ticket_id (str):
        label_ids (list[str]):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Envelope, Error]
    """

    return (
        await asyncio_detailed(
            ticket_id=ticket_id,
            label_ids=label_ids,
            client=client,
            envelope=envelope,
        )
    ).parsed
