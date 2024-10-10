import json
import os
from pathlib import Path
from typing import Any

from attrs import define

from bbsky.abstractions import URL, structure, unstructure


@define(frozen=True, slots=True)
class AppCredentials:
    """
    Blackbaud app authentication credentials

    See this URL for helpful troubleshooting tips:
    https://developer.blackbaud.com/skyapi/docs/authorization/common-auth-issues

    client_id: str - Your Blackbaud client ID (should be same as app ID)
    client_secret: str - Your Blackbaud client secret (should be same as app secret)
    redirect_uri: URL - The URL you've pre-configured for the application
    """

    client_id: str
    client_secret: str
    redirect_uri: URL

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return structure(data, cls)

    @classmethod
    def from_env(cls):
        return cls.from_dict(
            {
                "client_id": os.environ["BLACKBAUD_CLIENT_ID"],
                "client_secret": os.environ["BLACKBAUD_CLIENT_SECRET"],
                "redirect_uri": os.environ["BLACKBAUD_REDIRECT_URI"],
            }
        )

    @classmethod
    def from_json_file(cls, path: Path):
        return cls.from_dict(json.loads(Path(path).read_text()))

    def to_dict(self):
        return unstructure(self)

    def to_json_file(self, path: Path):
        Path(path).write_text(json.dumps(self.to_dict(), indent=4))
