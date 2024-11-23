from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tribute")


@_attrs_define
class Tribute:
    """GetTribute.

    Attributes:
        tribute_id (str): The tribute. Read-only in the SOAP API.
        amount (float): The amount.
        designation_id (Union[Unset, str]): The default designation. Read-only in the SOAP API.
        base_currency_id (Union[Unset, str]): The base currency. Read-only in the SOAP API.
        tribute_anonymous (Union[Unset, bool]): Indicates whether do not display on website.
        friends_asking_friends (Union[Unset, bool]): Indicates whether friends asking friends. Read-only in the SOAP
            API.
    """

    tribute_id: str
    amount: float
    designation_id: Union[Unset, str] = UNSET
    base_currency_id: Union[Unset, str] = UNSET
    tribute_anonymous: Union[Unset, bool] = UNSET
    friends_asking_friends: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tribute_id = self.tribute_id

        amount = self.amount

        designation_id = self.designation_id

        base_currency_id = self.base_currency_id

        tribute_anonymous = self.tribute_anonymous

        friends_asking_friends = self.friends_asking_friends

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "tribute_id": tribute_id,
                "amount": amount,
            }
        )
        if designation_id is not UNSET:
            field_dict["designation_id"] = designation_id
        if base_currency_id is not UNSET:
            field_dict["base_currency_id"] = base_currency_id
        if tribute_anonymous is not UNSET:
            field_dict["tribute_anonymous"] = tribute_anonymous
        if friends_asking_friends is not UNSET:
            field_dict["friends_asking_friends"] = friends_asking_friends

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tribute_id = d.pop("tribute_id")

        amount = d.pop("amount")

        designation_id = d.pop("designation_id", UNSET)

        base_currency_id = d.pop("base_currency_id", UNSET)

        tribute_anonymous = d.pop("tribute_anonymous", UNSET)

        friends_asking_friends = d.pop("friends_asking_friends", UNSET)

        tribute = cls(
            tribute_id=tribute_id,
            amount=amount,
            designation_id=designation_id,
            base_currency_id=base_currency_id,
            tribute_anonymous=tribute_anonymous,
            friends_asking_friends=friends_asking_friends,
        )

        return tribute
