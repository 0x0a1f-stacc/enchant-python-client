from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.attachment import Attachment
from ...models.envelope import Envelope
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    attachment_id: str,
    *,
    envelope: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["envelope"] = envelope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/attachments/{attachment_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Error, Union["Attachment", "Envelope"]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["Attachment", "Envelope"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = Attachment.from_dict(data)

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
) -> Response[Union[Any, Error, Union["Attachment", "Envelope"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Error, Union["Attachment", "Envelope"]]]:
    """Get an attachment

    Args:
        attachment_id (str):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Attachment', 'Envelope']]]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
        envelope=envelope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Error, Union["Attachment", "Envelope"]]]:
    """Get an attachment

    Args:
        attachment_id (str):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Attachment', 'Envelope']]
    """

    return sync_detailed(
        attachment_id=attachment_id,
        client=client,
        envelope=envelope,
    ).parsed


async def asyncio_detailed(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Error, Union["Attachment", "Envelope"]]]:
    """Get an attachment

    Args:
        attachment_id (str):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Attachment', 'Envelope']]]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
        envelope=envelope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Error, Union["Attachment", "Envelope"]]]:
    """Get an attachment

    Args:
        attachment_id (str):
        envelope (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Attachment', 'Envelope']]
    """

    return (
        await asyncio_detailed(
            attachment_id=attachment_id,
            client=client,
            envelope=envelope,
        )
    ).parsed
