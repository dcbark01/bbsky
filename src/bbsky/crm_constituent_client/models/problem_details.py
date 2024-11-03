from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemDetails")


@_attrs_define
class ProblemDetails:
    """A machine-readable format for specifying errors in HTTP API responses based on https://tools.ietf.org/html/rfc7807.

    Attributes:
        type (Union[Unset, str]): A URI reference [RFC3986] that identifies the problem type. This specification
            encourages that, when dereferenced, it provide human-readable documentation for the problem type (e.g., using
            HTML [W3C.REC-html5-20141028]). When this member is not present, its value is assumed to be "about:blank".
        title (Union[Unset, str]): A short, human-readable summary of the problem type. It SHOULD NOT change from
            occurrence to occurrence of the problem, except for purposes of localization (e.g., using proactive content
            negotiation; see [RFC7231], Section 3.4).
        status (Union[Unset, int]): The HTTP status code ([RFC7231], Section 6) generated by the origin server for this
            occurrence of the problem.
        detail (Union[Unset, str]): A human-readable explanation specific to this occurrence of the problem.
        instance (Union[Unset, str]): A URI reference that identifies the specific occurrence of the problem. It may or
            may not yield further information if dereferenced.
        trace_id (Union[Unset, str]): A request ID that can be provided to Blackbaud Support that may help with further
            troubleshooting.
        span_id (Union[Unset, str]): A request ID that can be provided to Blackbaud Support that may help with further
            troubleshooting.
    """

    type: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    detail: Union[Unset, str] = UNSET
    instance: Union[Unset, str] = UNSET
    trace_id: Union[Unset, str] = UNSET
    span_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        title = self.title

        status = self.status

        detail = self.detail

        instance = self.instance

        trace_id = self.trace_id

        span_id = self.span_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if span_id is not UNSET:
            field_dict["span_id"] = span_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        status = d.pop("status", UNSET)

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        span_id = d.pop("span_id", UNSET)

        problem_details = cls(
            type=type,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            trace_id=trace_id,
            span_id=span_id,
        )

        return problem_details