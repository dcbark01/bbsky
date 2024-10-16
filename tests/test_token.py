import json
from pathlib import Path
from typing import Any

import pytest
from _pytest.monkeypatch import MonkeyPatch

from bbsky.tokens import OAuth2Token


@pytest.fixture
def valid_token_dict() -> dict[str, Any]:
    return {
        "access_token": "test_access_token",
        "refresh_token": "test_refresh_token",
        "expires_in": 3600,
        "refresh_token_expires_in": 7200,
        "token_type": "Bearer",
        "environment_id": "env_id",
        "environment_name": "env_name",
        "legal_entity_id": "entity_id",
        "legal_entity_name": "entity_name",
        "user_id": "user_id",
        "email": "user@example.com",
        "family_name": "Doe",
        "given_name": "John",
        "mode": "test_mode",
    }


@pytest.fixture
def valid_token(valid_token_dict: dict[str, Any]) -> OAuth2Token:
    return OAuth2Token.from_dict(valid_token_dict)


def test_token_from_dict(valid_token_dict: dict[str, Any], valid_token: OAuth2Token):
    assert valid_token.access_token == valid_token_dict["access_token"]
    assert valid_token.refresh_token == valid_token_dict["refresh_token"]
    assert valid_token.expires_in == valid_token_dict["expires_in"]
    assert valid_token.refresh_token_expires_in == valid_token_dict["refresh_token_expires_in"]
    assert valid_token.token_type == valid_token_dict["token_type"]
    assert valid_token.environment_id == valid_token_dict["environment_id"]
    assert valid_token.environment_name == valid_token_dict["environment_name"]
    assert valid_token.legal_entity_id == valid_token_dict["legal_entity_id"]
    assert valid_token.legal_entity_name == valid_token_dict["legal_entity_name"]
    assert valid_token.user_id == valid_token_dict["user_id"]
    assert valid_token.email == valid_token_dict["email"]
    assert valid_token.family_name == valid_token_dict["family_name"]
    assert valid_token.given_name == valid_token_dict["given_name"]
    assert valid_token.mode == valid_token_dict["mode"]


def test_token_to_dict(valid_token: OAuth2Token, valid_token_dict: dict[str, Any]):
    result = valid_token.to_dict()
    assert result == valid_token_dict


def test_token_save_load(tmp_path: Path, valid_token: OAuth2Token):
    token_file = tmp_path / "token.json"
    valid_token.save(token_file)
    loaded_token = OAuth2Token.load(token_file)
    assert loaded_token == valid_token


def test_token_from_cache(monkeypatch: MonkeyPatch, tmp_path: Path, valid_token: OAuth2Token):
    token_file = tmp_path / "token.json"
    valid_token.save(token_file)
    monkeypatch.setattr("bbsky.tokens.BBSKY_TOKEN_FILE", token_file)
    cached_token = OAuth2Token.from_cache()
    assert cached_token == valid_token


def test_token_save_to_cache(monkeypatch: MonkeyPatch, tmp_path: Path, valid_token: OAuth2Token):
    token_file = tmp_path / "token.json"
    monkeypatch.setattr("bbsky.tokens.BBSKY_TOKEN_FILE", token_file)
    valid_token.to_cache()
    assert token_file.exists()
    cached_token = OAuth2Token.load(token_file)
    assert cached_token == valid_token


def test_token_load_file_not_found():
    with pytest.raises(FileNotFoundError):
        OAuth2Token.load(Path("non_existent_file.json"))


def test_token_load_invalid_json(tmp_path: Path):
    invalid_json_file = tmp_path / "invalid.json"
    invalid_json_file.write_text("{ invalid json }")
    with pytest.raises(json.JSONDecodeError):
        OAuth2Token.load(invalid_json_file)
