from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.envelope import Envelope
from ...models.error import Error
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, list[str]] = UNSET,
    count: Union[Unset, bool] = False,
    envelope: Union[Unset, bool] = False,
    page: Union[Unset, int] = 1,
    per_page: Union[Unset, int] = 10,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Error, Union["Envelope", list["User"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["Envelope", list["User"]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:
                    response_200_type_0_item = User.from_dict(response_200_type_0_item_data)

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
) -> Response[Union[Any, Error, Union["Envelope", list["User"]]]]:
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
) -> Response[Union[Any, Error, Union["Envelope", list["User"]]]]:
    """List users

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Envelope', list['User']]]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        count=count,
        envelope=envelope,
        page=page,
        per_page=per_page,
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
) -> Optional[Union[Any, Error, Union["Envelope", list["User"]]]]:
    """List users

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Envelope', list['User']]]
    """

    return sync_detailed(
        client=client,
        fields=fields,
        count=count,
        envelope=envelope,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    count: Union[Unset, bool] = False,
    envelope: Union[Unset, bool] = False,
    page: Union[Unset, int] = 1,
    per_page: Union[Unset, int] = 10,
) -> Response[Union[Any, Error, Union["Envelope", list["User"]]]]:
    """List users

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, Union['Envelope', list['User']]]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        count=count,
        envelope=envelope,
        page=page,
        per_page=per_page,
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
) -> Optional[Union[Any, Error, Union["Envelope", list["User"]]]]:
    """List users

    Args:
        fields (Union[Unset, list[str]]):
        count (Union[Unset, bool]):  Default: False.
        envelope (Union[Unset, bool]):  Default: False.
        page (Union[Unset, int]):  Default: 1.
        per_page (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, Union['Envelope', list['User']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            count=count,
            envelope=envelope,
            page=page,
            per_page=per_page,
        )
    ).parsed
