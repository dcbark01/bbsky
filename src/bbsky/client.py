import hashlib
from typing import Literal, Optional

from attrs import define, field

from bbsky.data_cls import URL

API_BASE_URL = URL("https://api.sky.blackbaud.com")


def create_hash(string: str) -> str:
    return hashlib.sha256(string.encode(encoding="utf-8")).hexdigest()


@define(frozen=True, slots=True)
class HTTPRequestData:
    url: URL
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    headers: dict[str, str]
    data: dict[str, str]
    params: dict[str, str]


@define(frozen=True, slots=True, kw_only=True)
class SearchConstituentsParams:
    """
    Search for constituents in the Blackbaud Sky API.

    See docs:
    https://developer.sky.blackbaud.com/api#api=crm-conmg&operation=SearchConstituents
    """

    id_: Optional[str] = field(default=None, alias="id")
    lookup_id: Optional[str] = field(default=None)
    sort_constituent_name: Optional[str] = field(default=None)
    address: Optional[str] = field(default=None)
    city: Optional[str] = field(default=None)
    state: Optional[str] = field(default=None)
    post_code: Optional[str] = field(default=None)
    country_id: Optional[str] = field(default=None)
    gives_anonymously: Optional[bool] = field(default=None)
    classof: Optional[int] = field(default=None)
    organization: Optional[bool] = field(default=None)
    name: Optional[str] = field(default=None)
    email_address: Optional[str] = field(default=None)
    group: Optional[bool] = field(default=None)
    household: Optional[bool] = field(default=None)
    middle_name: Optional[str] = field(default=None)
    suffixcodeid: Optional[str] = field(default=None)
    phone: Optional[str] = field(default=None)
    prospectmanager: Optional[str] = field(default=None)


search = SearchConstituentsParams(classof=1901, name="John Doe")
print(search)
