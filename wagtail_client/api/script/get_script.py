from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_script_response_200 import GetScriptResponse200
from ...models.get_script_response_500 import GetScriptResponse500
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/scripts/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetScriptResponse200, GetScriptResponse500]]:
    if response.status_code == 200:
        response_200 = GetScriptResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = GetScriptResponse500.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetScriptResponse200, GetScriptResponse500]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[GetScriptResponse200, GetScriptResponse500]]:
    """Get Script

     Get Script

    Args:
        id (str):  Example: 1.

    Returns:
        Response[Union[GetScriptResponse200, GetScriptResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[Union[GetScriptResponse200, GetScriptResponse500]]:
    """Get Script

     Get Script

    Args:
        id (str):  Example: 1.

    Returns:
        Response[Union[GetScriptResponse200, GetScriptResponse500]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[GetScriptResponse200, GetScriptResponse500]]:
    """Get Script

     Get Script

    Args:
        id (str):  Example: 1.

    Returns:
        Response[Union[GetScriptResponse200, GetScriptResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[Union[GetScriptResponse200, GetScriptResponse500]]:
    """Get Script

     Get Script

    Args:
        id (str):  Example: 1.

    Returns:
        Response[Union[GetScriptResponse200, GetScriptResponse500]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
