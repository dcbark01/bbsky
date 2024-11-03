import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConstituentFundraiser")


@_attrs_define
class ConstituentFundraiser:
    """GetConstituentFundraiser.

    Attributes:
        date_from (Union[Unset, datetime.datetime]): The date from. Uses the format YYYY-MM-DDThh:mm:ss. An example
            date: <i>1955-11-05T22:04:00</i>.
        date_to (Union[Unset, datetime.datetime]): The date to. Uses the format YYYY-MM-DDThh:mm:ss. An example date:
            <i>1955-11-05T22:04:00</i>.
    """

    date_from: Union[Unset, datetime.datetime] = UNSET
    date_to: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date_from: Union[Unset, str] = UNSET
        if not isinstance(self.date_from, Unset):
            date_from = self.date_from.isoformat()

        date_to: Union[Unset, str] = UNSET
        if not isinstance(self.date_to, Unset):
            date_to = self.date_to.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date_from = d.pop("date_from", UNSET)
        date_from: Union[Unset, datetime.datetime]
        if isinstance(_date_from, Unset):
            date_from = UNSET
        else:
            date_from = isoparse(_date_from)

        _date_to = d.pop("date_to", UNSET)
        date_to: Union[Unset, datetime.datetime]
        if isinstance(_date_to, Unset):
            date_to = UNSET
        else:
            date_to = isoparse(_date_to)

        constituent_fundraiser = cls(
            date_from=date_from,
            date_to=date_to,
        )

        return constituent_fundraiser
