from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_status_response_200 import GetStatusResponse200
from ...types import Response


def _get_kwargs_getStatus() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/profile/status",
    }

    return _kwargs


def _parse_response_getStatus(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetStatusResponse200]:
    if response.status_code == 200:
        response_200 = GetStatusResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getStatus(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response_getStatus(client=client, response=response),
    )


async def asyncio_detailed_getStatus(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetStatusResponse200]:
    """получение информации о своем статусе

     Параметры запроса отсутствуют

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatusResponse200]
    """

    kwargs = _get_kwargs_getStatus()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response_getStatus(client=client, response=response)


async def getStatus(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetStatusResponse200]:
    """получение информации о своем статусе

     Параметры запроса отсутствуют

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatusResponse200
    """

    return (
        await asyncio_detailed_getStatus(
            client=client,
        )
    ).parsed
