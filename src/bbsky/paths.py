import os
from pathlib import Path


def getenv_path(key: str, default: Path) -> Path:
    value = os.getenv(key)
    return Path(value) if value else default


BBSKY_HOME_DIR = getenv_path("BBSKY_HOME_DIR", (Path.home() / ".bbsky").resolve())
BBSKY_CONFIG_DIR = getenv_path("BBSKY_CONFIG_DIR", BBSKY_HOME_DIR / "config")
BBSKY_CACHE_DIR = getenv_path("BBSKY_CACHE_DIR", BBSKY_HOME_DIR / "cache")
BBSKY_CONFIG_FILE = BBSKY_CONFIG_DIR / "config.json"
BBSKY_TOKEN_FILE = BBSKY_CACHE_DIR / "token.json"
