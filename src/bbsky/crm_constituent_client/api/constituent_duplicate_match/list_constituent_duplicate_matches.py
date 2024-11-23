from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constituent_duplicate_match_list_collection import ConstituentDuplicateMatchListCollection
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    max_results: Union[Unset, int] = UNSET,
    email_address: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    key_name: Union[Unset, str] = UNSET,
    address_block: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    post_code: Union[Unset, str] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    session_key: Union[Unset, str] = UNSET,
    infinity_session: Union[Unset, str] = UNSET,
    more_rows_range_key: Union[Unset, str] = UNSET,
    start_row_index: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["max_results"] = max_results

    params["email_address"] = email_address

    params["first_name"] = first_name

    params["key_name"] = key_name

    params["address_block"] = address_block

    params["country"] = country

    params["post_code"] = post_code

    params["phone_number"] = phone_number

    params["title"] = title

    params["limit"] = limit

    params["session_key"] = session_key

    params["infinity_session"] = infinity_session

    params["more_rows_range_key"] = more_rows_range_key

    params["start_row_index"] = start_row_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/constituents/constituentduplicatematch",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = ConstituentDuplicateMatchListCollection.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    max_results: Union[Unset, int] = UNSET,
    email_address: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    key_name: Union[Unset, str] = UNSET,
    address_block: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    post_code: Union[Unset, str] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    session_key: Union[Unset, str] = UNSET,
    infinity_session: Union[Unset, str] = UNSET,
    more_rows_range_key: Union[Unset, str] = UNSET,
    start_row_index: Union[Unset, int] = UNSET,
) -> Response[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]:
    """List constituent duplicate matches.

     List of constituents matching web operations automatch threshold.

    Args:
        max_results (Union[Unset, int]):
        email_address (Union[Unset, str]):
        first_name (Union[Unset, str]):
        key_name (Union[Unset, str]):
        address_block (Union[Unset, str]):
        country (Union[Unset, str]):
        post_code (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        title (Union[Unset, str]):
        limit (Union[Unset, int]):
        session_key (Union[Unset, str]):
        infinity_session (Union[Unset, str]):
        more_rows_range_key (Union[Unset, str]):
        start_row_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        max_results=max_results,
        email_address=email_address,
        first_name=first_name,
        key_name=key_name,
        address_block=address_block,
        country=country,
        post_code=post_code,
        phone_number=phone_number,
        title=title,
        limit=limit,
        session_key=session_key,
        infinity_session=infinity_session,
        more_rows_range_key=more_rows_range_key,
        start_row_index=start_row_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    max_results: Union[Unset, int] = UNSET,
    email_address: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    key_name: Union[Unset, str] = UNSET,
    address_block: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    post_code: Union[Unset, str] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    session_key: Union[Unset, str] = UNSET,
    infinity_session: Union[Unset, str] = UNSET,
    more_rows_range_key: Union[Unset, str] = UNSET,
    start_row_index: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]:
    """List constituent duplicate matches.

     List of constituents matching web operations automatch threshold.

    Args:
        max_results (Union[Unset, int]):
        email_address (Union[Unset, str]):
        first_name (Union[Unset, str]):
        key_name (Union[Unset, str]):
        address_block (Union[Unset, str]):
        country (Union[Unset, str]):
        post_code (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        title (Union[Unset, str]):
        limit (Union[Unset, int]):
        session_key (Union[Unset, str]):
        infinity_session (Union[Unset, str]):
        more_rows_range_key (Union[Unset, str]):
        start_row_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        max_results=max_results,
        email_address=email_address,
        first_name=first_name,
        key_name=key_name,
        address_block=address_block,
        country=country,
        post_code=post_code,
        phone_number=phone_number,
        title=title,
        limit=limit,
        session_key=session_key,
        infinity_session=infinity_session,
        more_rows_range_key=more_rows_range_key,
        start_row_index=start_row_index,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    max_results: Union[Unset, int] = UNSET,
    email_address: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    key_name: Union[Unset, str] = UNSET,
    address_block: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    post_code: Union[Unset, str] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    session_key: Union[Unset, str] = UNSET,
    infinity_session: Union[Unset, str] = UNSET,
    more_rows_range_key: Union[Unset, str] = UNSET,
    start_row_index: Union[Unset, int] = UNSET,
) -> Response[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]:
    """List constituent duplicate matches.

     List of constituents matching web operations automatch threshold.

    Args:
        max_results (Union[Unset, int]):
        email_address (Union[Unset, str]):
        first_name (Union[Unset, str]):
        key_name (Union[Unset, str]):
        address_block (Union[Unset, str]):
        country (Union[Unset, str]):
        post_code (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        title (Union[Unset, str]):
        limit (Union[Unset, int]):
        session_key (Union[Unset, str]):
        infinity_session (Union[Unset, str]):
        more_rows_range_key (Union[Unset, str]):
        start_row_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        max_results=max_results,
        email_address=email_address,
        first_name=first_name,
        key_name=key_name,
        address_block=address_block,
        country=country,
        post_code=post_code,
        phone_number=phone_number,
        title=title,
        limit=limit,
        session_key=session_key,
        infinity_session=infinity_session,
        more_rows_range_key=more_rows_range_key,
        start_row_index=start_row_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    max_results: Union[Unset, int] = UNSET,
    email_address: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    key_name: Union[Unset, str] = UNSET,
    address_block: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    post_code: Union[Unset, str] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    session_key: Union[Unset, str] = UNSET,
    infinity_session: Union[Unset, str] = UNSET,
    more_rows_range_key: Union[Unset, str] = UNSET,
    start_row_index: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]]:
    """List constituent duplicate matches.

     List of constituents matching web operations automatch threshold.

    Args:
        max_results (Union[Unset, int]):
        email_address (Union[Unset, str]):
        first_name (Union[Unset, str]):
        key_name (Union[Unset, str]):
        address_block (Union[Unset, str]):
        country (Union[Unset, str]):
        post_code (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        title (Union[Unset, str]):
        limit (Union[Unset, int]):
        session_key (Union[Unset, str]):
        infinity_session (Union[Unset, str]):
        more_rows_range_key (Union[Unset, str]):
        start_row_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstituentDuplicateMatchListCollection, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            max_results=max_results,
            email_address=email_address,
            first_name=first_name,
            key_name=key_name,
            address_block=address_block,
            country=country,
            post_code=post_code,
            phone_number=phone_number,
            title=title,
            limit=limit,
            session_key=session_key,
            infinity_session=infinity_session,
            more_rows_range_key=more_rows_range_key,
            start_row_index=start_row_index,
        )
    ).parsed
