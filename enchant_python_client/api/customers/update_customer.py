from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.customer import Customer
from ...models.customer_input import CustomerInput
from ...models.error import Error
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: str,
    *,
    body: CustomerInput,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["envelope"] = envelope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/customers/{customer_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Customer, Error, ValidationError]:
    if response.status_code == 200:
        response_200 = Customer.from_dict(response.json())

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
) -> Response[Union[Any, Customer, Error, ValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerInput,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Customer, Error, ValidationError]]:
    """Update a customer

    Args:
        customer_id (str):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.
        body (CustomerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Customer, Error, ValidationError]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
        fields=fields,
        envelope=envelope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerInput,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Customer, Error, ValidationError]]:
    """Update a customer

    Args:
        customer_id (str):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.
        body (CustomerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Customer, Error, ValidationError]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        body=body,
        fields=fields,
        envelope=envelope,
    ).parsed


async def asyncio_detailed(
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerInput,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Response[Union[Any, Customer, Error, ValidationError]]:
    """Update a customer

    Args:
        customer_id (str):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.
        body (CustomerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Customer, Error, ValidationError]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
        fields=fields,
        envelope=envelope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerInput,
    fields: Union[Unset, list[str]] = UNSET,
    envelope: Union[Unset, bool] = False,
) -> Optional[Union[Any, Customer, Error, ValidationError]]:
    """Update a customer

    Args:
        customer_id (str):
        fields (Union[Unset, list[str]]):
        envelope (Union[Unset, bool]):  Default: False.
        body (CustomerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Customer, Error, ValidationError]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            body=body,
            fields=fields,
            envelope=envelope,
        )
    ).parsed
