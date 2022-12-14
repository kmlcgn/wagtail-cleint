from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_node_scripts_response_200 import GetNodeScriptsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    node_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/scripts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["node-id"] = node_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetNodeScriptsResponse200]:
    if response.status_code == 200:
        response_200 = GetNodeScriptsResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetNodeScriptsResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    node_id: Union[Unset, None, str] = UNSET,
) -> Response[GetNodeScriptsResponse200]:
    """Get Node Scripts

     Get Node Scripts

    Args:
        node_id (Union[Unset, None, str]):  Example: 1.

    Returns:
        Response[GetNodeScriptsResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        node_id=node_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    node_id: Union[Unset, None, str] = UNSET,
) -> Optional[GetNodeScriptsResponse200]:
    """Get Node Scripts

     Get Node Scripts

    Args:
        node_id (Union[Unset, None, str]):  Example: 1.

    Returns:
        Response[GetNodeScriptsResponse200]
    """

    return sync_detailed(
        client=client,
        node_id=node_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    node_id: Union[Unset, None, str] = UNSET,
) -> Response[GetNodeScriptsResponse200]:
    """Get Node Scripts

     Get Node Scripts

    Args:
        node_id (Union[Unset, None, str]):  Example: 1.

    Returns:
        Response[GetNodeScriptsResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        node_id=node_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    node_id: Union[Unset, None, str] = UNSET,
) -> Optional[GetNodeScriptsResponse200]:
    """Get Node Scripts

     Get Node Scripts

    Args:
        node_id (Union[Unset, None, str]):  Example: 1.

    Returns:
        Response[GetNodeScriptsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            node_id=node_id,
        )
    ).parsed
