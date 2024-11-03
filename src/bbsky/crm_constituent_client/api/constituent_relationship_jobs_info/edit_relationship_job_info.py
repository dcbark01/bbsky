from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_relationship_job_info import EditRelationshipJobInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    relationship_job_information_id: str,
    *,
    body: EditRelationshipJobInfo,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/relationshipjobsinfo/{relationship_job_information_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    relationship_job_information_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EditRelationshipJobInfo,
) -> Response[Union[Any, ProblemDetails]]:
    """Edit a Relationship Job Info.

     This operation is used to edit relationship job inoperationation.

    Args:
        relationship_job_information_id (str):
        body (EditRelationshipJobInfo): EditRelationshipJobInfo Example: {'job_title':
            'Dietician', 'career_level': 'executive', 'job_category': '', 'start_date':
            '2022-12-15T12:00:00.0000000+00:00', 'end_date': '2026-12-25T12:00:00.0000000+00:00',
            'job_department': '', 'job_division': '', 'job_schedule': {}, 'job_responsibility': '',
            'private_record': 'false', 'sync_end_date_to_relationship': 'true', 'last_job': 'true'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        relationship_job_information_id=relationship_job_information_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    relationship_job_information_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EditRelationshipJobInfo,
) -> Optional[Union[Any, ProblemDetails]]:
    """Edit a Relationship Job Info.

     This operation is used to edit relationship job inoperationation.

    Args:
        relationship_job_information_id (str):
        body (EditRelationshipJobInfo): EditRelationshipJobInfo Example: {'job_title':
            'Dietician', 'career_level': 'executive', 'job_category': '', 'start_date':
            '2022-12-15T12:00:00.0000000+00:00', 'end_date': '2026-12-25T12:00:00.0000000+00:00',
            'job_department': '', 'job_division': '', 'job_schedule': {}, 'job_responsibility': '',
            'private_record': 'false', 'sync_end_date_to_relationship': 'true', 'last_job': 'true'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        relationship_job_information_id=relationship_job_information_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    relationship_job_information_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EditRelationshipJobInfo,
) -> Response[Union[Any, ProblemDetails]]:
    """Edit a Relationship Job Info.

     This operation is used to edit relationship job inoperationation.

    Args:
        relationship_job_information_id (str):
        body (EditRelationshipJobInfo): EditRelationshipJobInfo Example: {'job_title':
            'Dietician', 'career_level': 'executive', 'job_category': '', 'start_date':
            '2022-12-15T12:00:00.0000000+00:00', 'end_date': '2026-12-25T12:00:00.0000000+00:00',
            'job_department': '', 'job_division': '', 'job_schedule': {}, 'job_responsibility': '',
            'private_record': 'false', 'sync_end_date_to_relationship': 'true', 'last_job': 'true'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        relationship_job_information_id=relationship_job_information_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    relationship_job_information_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EditRelationshipJobInfo,
) -> Optional[Union[Any, ProblemDetails]]:
    """Edit a Relationship Job Info.

     This operation is used to edit relationship job inoperationation.

    Args:
        relationship_job_information_id (str):
        body (EditRelationshipJobInfo): EditRelationshipJobInfo Example: {'job_title':
            'Dietician', 'career_level': 'executive', 'job_category': '', 'start_date':
            '2022-12-15T12:00:00.0000000+00:00', 'end_date': '2026-12-25T12:00:00.0000000+00:00',
            'job_department': '', 'job_division': '', 'job_schedule': {}, 'job_responsibility': '',
            'private_record': 'false', 'sync_end_date_to_relationship': 'true', 'last_job': 'true'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            relationship_job_information_id=relationship_job_information_id,
            client=client,
            body=body,
        )
    ).parsed
