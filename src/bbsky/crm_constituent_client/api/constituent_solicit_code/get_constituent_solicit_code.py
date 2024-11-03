from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constituent_solicit_code import ConstituentSolicitCode
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    constituent_solicit_code_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/solicitcodes/{constituent_solicit_code_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ConstituentSolicitCode, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = ConstituentSolicitCode.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ConstituentSolicitCode, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituent_solicit_code_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ConstituentSolicitCode, ProblemDetails]]:
    """Get a constituent solicit code.

     Edit a constituent solicit code

    Args:
        constituent_solicit_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstituentSolicitCode, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        constituent_solicit_code_id=constituent_solicit_code_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_solicit_code_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ConstituentSolicitCode, ProblemDetails]]:
    """Get a constituent solicit code.

     Edit a constituent solicit code

    Args:
        constituent_solicit_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstituentSolicitCode, ProblemDetails]
    """

    return sync_detailed(
        constituent_solicit_code_id=constituent_solicit_code_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    constituent_solicit_code_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ConstituentSolicitCode, ProblemDetails]]:
    """Get a constituent solicit code.

     Edit a constituent solicit code

    Args:
        constituent_solicit_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstituentSolicitCode, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        constituent_solicit_code_id=constituent_solicit_code_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_solicit_code_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ConstituentSolicitCode, ProblemDetails]]:
    """Get a constituent solicit code.

     Edit a constituent solicit code

    Args:
        constituent_solicit_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstituentSolicitCode, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            constituent_solicit_code_id=constituent_solicit_code_id,
            client=client,
        )
    ).parsed