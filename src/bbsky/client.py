from enum import Enum

import hishel
import httpx
from attrs import define, field

from bbsky.config import SkyConfig
from bbsky.constants import API_BASE_URL
from bbsky.crm_constituent_client.client import AuthenticatedClient
from bbsky.data_cls import URL
from bbsky.token import OAuth2Token


class NamedAPIs(str, Enum):
    """
    An enum of Blackbaud API products and their corresponding URL paths.

    See here:
    https://developer.blackbaud.com/skyapi/products

    """

    CONSTITUENTS = "crm-conmg"

    @classmethod
    def get_base_url(cls, api_name: str) -> URL:
        return API_BASE_URL / cls[api_name.upper()].value


@define(slots=False)
class SkyClient(AuthenticatedClient):
    """
    A Blackbaud Sky API client.
    """

    oauth_token: OAuth2Token = field(factory=OAuth2Token.from_cache)
    config: SkyConfig = field(factory=SkyConfig.from_stored_config)
    cache_client: hishel.CacheClient = hishel.CacheClient()
    token = field(default=None)

    def __attrs_post_init__(self) -> None:
        self.token = self.oauth_token.access_token

    def get_httpx_client(self) -> httpx.Client:
        """Get the underlying httpx.Client, constructing a new one if not previously set"""
        if self._client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            self._headers["Bb-Api-Subscription-Key"] = self.config.subscription_key
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                **self._httpx_args,
            )
        return self._client
