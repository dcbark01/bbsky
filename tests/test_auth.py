import json
from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

from bbsky.abstractions import URL
from bbsky.auth import AppCredentials


@pytest.fixture
def valid_credentials_dict() -> dict[str, str]:
    return {
        "client_id": "test_client_id",
        "client_secret": "test_client_secret",
        "redirect_uri": "https://example.com/callback",
    }


@pytest.fixture
def valid_credentials(valid_credentials_dict: dict[str, str]) -> AppCredentials:
    return AppCredentials.from_dict(valid_credentials_dict)


def test_app_credentials_from_dict(valid_credentials_dict: dict[str, str], valid_credentials: AppCredentials):
    assert valid_credentials.client_id == valid_credentials_dict["client_id"]
    assert valid_credentials.client_secret == valid_credentials_dict["client_secret"]
    assert valid_credentials.redirect_uri == URL(valid_credentials_dict["redirect_uri"])


def test_app_credentials_to_dict(valid_credentials: AppCredentials, valid_credentials_dict: dict[str, str]):
    result = valid_credentials.to_dict()
    assert result["client_id"] == valid_credentials_dict["client_id"]
    assert result["client_secret"] == valid_credentials_dict["client_secret"]
    assert result["redirect_uri"] == valid_credentials_dict["redirect_uri"]


def test_app_credentials_from_env(monkeypatch: MonkeyPatch, valid_credentials_dict: dict[str, str]) -> None:
    monkeypatch.setenv("BLACKBAUD_CLIENT_ID", valid_credentials_dict["client_id"])
    monkeypatch.setenv("BLACKBAUD_CLIENT_SECRET", valid_credentials_dict["client_secret"])
    monkeypatch.setenv("BLACKBAUD_REDIRECT_URI", valid_credentials_dict["redirect_uri"])

    credentials = AppCredentials.from_env()
    assert credentials.client_id == valid_credentials_dict["client_id"]
    assert credentials.client_secret == valid_credentials_dict["client_secret"]
    assert credentials.redirect_uri == URL(valid_credentials_dict["redirect_uri"])


def test_app_credentials_from_json_file(tmp_path: Path, valid_credentials_dict: dict[str, str]) -> None:
    json_file = tmp_path / "credentials.json"
    json_file.write_text(json.dumps(valid_credentials_dict))

    credentials: AppCredentials = AppCredentials.from_json_file(json_file)
    assert credentials.client_id == valid_credentials_dict["client_id"]
    assert credentials.client_secret == valid_credentials_dict["client_secret"]
    assert credentials.redirect_uri == URL(valid_credentials_dict["redirect_uri"])


def test_app_credentials_to_json_file(tmp_path: Path, valid_credentials: AppCredentials) -> None:
    json_file = tmp_path / "credentials.json"
    valid_credentials.to_json_file(json_file)
    assert json_file.exists()


def test_app_credentials_from_env_missing_env_var(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.delenv("BLACKBAUD_CLIENT_ID", raising=False)
    monkeypatch.setenv("BLACKBAUD_CLIENT_SECRET", "test_secret")
    monkeypatch.setenv("BLACKBAUD_REDIRECT_URI", "https://example.com/callback")

    with pytest.raises(KeyError):
        AppCredentials.from_env()


def test_app_credentials_from_json_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        AppCredentials.from_json_file(Path("non_existent_file.json"))


def test_app_credentials_from_json_file_invalid_json(tmp_path: Path) -> None:
    invalid_json_file = tmp_path / "invalid.json"
    invalid_json_file.write_text("{ invalid json }")

    with pytest.raises(json.JSONDecodeError):
        AppCredentials.from_json_file(invalid_json_file)
