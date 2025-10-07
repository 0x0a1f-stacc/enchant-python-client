from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.contact import Contact
from ...models.contact_input import ContactInput
from ...models.create_contact_xhttp_method_override import CreateContactXHTTPMethodOverride
from ...models.envelope import Envelope
from ...models.error import Error
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: str,
    *,
    body: ContactInput,
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateContactXHTTPMethodOverride] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_http_method_override, Unset):
        headers["X-HTTP-Method-Override"] = str(x_http_method_override)

    params: dict[str, Any] = {}

    params["envelope"] = envelope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/customers/{customer_id}/contacts",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Contact, Envelope, Error, ValidationError]:
    if response.status_code == 200:
        response_200 = Envelope.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Contact.from_dict(response.json())

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
) -> Response[Union[Any, Contact, Envelope, Error, ValidationError]]:
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
    body: ContactInput,
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateContactXHTTPMethodOverride] = UNSET,
) -> Response[Union[Any, Contact, Envelope, Error, ValidationError]]:
    """Create a contact for a customer

    Args:
        customer_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateContactXHTTPMethodOverride]):
        body (ContactInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Contact, Envelope, Error, ValidationError]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
        envelope=envelope,
        x_http_method_override=x_http_method_override,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ContactInput,
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateContactXHTTPMethodOverride] = UNSET,
) -> Optional[Union[Any, Contact, Envelope, Error, ValidationError]]:
    """Create a contact for a customer

    Args:
        customer_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateContactXHTTPMethodOverride]):
        body (ContactInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Contact, Envelope, Error, ValidationError]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        body=body,
        envelope=envelope,
        x_http_method_override=x_http_method_override,
    ).parsed


async def asyncio_detailed(
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ContactInput,
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateContactXHTTPMethodOverride] = UNSET,
) -> Response[Union[Any, Contact, Envelope, Error, ValidationError]]:
    """Create a contact for a customer

    Args:
        customer_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateContactXHTTPMethodOverride]):
        body (ContactInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Contact, Envelope, Error, ValidationError]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
        envelope=envelope,
        x_http_method_override=x_http_method_override,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ContactInput,
    envelope: Union[Unset, bool] = False,
    x_http_method_override: Union[Unset, CreateContactXHTTPMethodOverride] = UNSET,
) -> Optional[Union[Any, Contact, Envelope, Error, ValidationError]]:
    """Create a contact for a customer

    Args:
        customer_id (str):
        envelope (Union[Unset, bool]):  Default: False.
        x_http_method_override (Union[Unset, CreateContactXHTTPMethodOverride]):
        body (ContactInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Contact, Envelope, Error, ValidationError]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            body=body,
            envelope=envelope,
            x_http_method_override=x_http_method_override,
        )
    ).parsed
