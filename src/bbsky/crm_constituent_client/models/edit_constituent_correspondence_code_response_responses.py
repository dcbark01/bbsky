import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditConstituentCorrespondenceCodeResponseResponses")


@_attrs_define
class EditConstituentCorrespondenceCodeResponseResponses:
    """EditConstituentCorrespondenceCodeResponseResponses.

    Attributes:
        response_category (str): The category. This simple list can be queried at https://api.sky.blackbaud.com/crm-
            adnmg/simplelists/fa5c3e42-aea6-450c-a66f-e79919df98d8.
        response (str): The response. This simple list can be queried at https://api.sky.blackbaud.com/crm-
            adnmg/simplelists/e48745a4-b8cd-4e31-885a-3173d7374ea6?parameters=responsecategoryid,{response_category}.
        date (Union[Unset, datetime.date]): date
        code (Union[Unset, str]): code
    """

    response_category: str
    response: str
    date: Union[Unset, datetime.date] = UNSET
    code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        response_category = self.response_category

        response = self.response

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response_category": response_category,
                "response": response,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        response_category = d.pop("response_category")

        response = d.pop("response")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        code = d.pop("code", UNSET)

        edit_constituent_correspondence_code_response_responses = cls(
            response_category=response_category,
            response=response,
            date=date,
            code=code,
        )

        edit_constituent_correspondence_code_response_responses.additional_properties = d
        return edit_constituent_correspondence_code_response_responses

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
