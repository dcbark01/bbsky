import json
import os
from functools import wraps
from pathlib import Path
from typing import Any, Callable

import click
from attrs import define

from .data_cls import URL, structure, unstructure
from .paths import BBSKY_CONFIG_DIR, BBSKY_CONFIG_FILE


def ensure_config_dir(func: Callable[..., Any]) -> Callable[..., Any]:
    """Ensure the config directory exists, and create it if it doesn't."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        BBSKY_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        return func(*args, **kwargs)

    return wrapper


@define(frozen=True, slots=True)
class SkyConfig:
    """
    Blackbaud app authentication credentials

    See this URL for helpful troubleshooting tips:
    https://developer.blackbaud.com/skyapi/docs/authorization/common-auth-issues

    client_id: str - Your Blackbaud client ID (should be same as app ID)
    client_secret: str - Your Blackbaud client secret (should be same as app secret)
    redirect_uri: URL - The URL you've pre-configured for the application
    subscription_key: str - Your Blackbaud subscription key
    """

    client_id: str
    client_secret: str
    redirect_uri: URL
    subscription_key: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SkyConfig":
        return structure(data, cls)

    @classmethod
    def from_env(cls) -> "SkyConfig":
        return cls.from_dict(
            {
                "client_id": os.environ["BLACKBAUD_CLIENT_ID"],
                "client_secret": os.environ["BLACKBAUD_CLIENT_SECRET"],
                "redirect_uri": os.environ["BLACKBAUD_REDIRECT_URI"],
                "subscription_key": os.environ["BLACKBAUD_SUBSCRIPTION_KEY"],
            }
        )

    @classmethod
    def from_json_file(cls, path: Path) -> "SkyConfig":
        return cls.from_dict(json.loads(Path(path).read_text()))

    @classmethod
    def from_stored_config(cls) -> "SkyConfig":
        return cls.from_json_file(BBSKY_CONFIG_FILE)

    def to_dict(self) -> dict[str, Any]:
        return unstructure(self)

    def to_json_file(self, path: Path) -> None:
        Path(path).write_text(json.dumps(self.to_dict(), indent=4))


@click.group()
def cli():
    """Create and manage Blackbaud Sky API config."""
    pass


@click.command()
@click.option("--client-id", prompt="Client ID")
@click.option("--client-secret", prompt="Client Secret")
@click.option("--redirect-uri", prompt="Redirect URI")
@click.option("--subscription-key", prompt="Subscription Key")
@click.option("--output", type=click.Path(), default=BBSKY_CONFIG_FILE)
@click.pass_context
@ensure_config_dir
def create(
    context: click.Context, client_id: str, client_secret: str, redirect_uri: str, subscription_key: str, output: Path
) -> None:
    """Create a new Blackbaud Sky API config."""
    config = SkyConfig(client_id, client_secret, URL(redirect_uri), subscription_key)
    config.to_json_file(output)
    click.echo(f"Config saved to {output}")


@click.command()
@click.option("-i", "--input_path", type=click.Path(), default=BBSKY_CONFIG_FILE)
@click.option("-f", "--fmt", type=click.Choice(["json", "env"]), default="json")
@click.pass_context
def show(
    context: click.Context,
    input_path: Path,
    fmt: str,
) -> None:
    """Show the current Blackbaud Sky API config."""
    input_path = Path(input_path)
    config = SkyConfig.from_json_file(input_path)
    if fmt == "json":
        click.echo(json.dumps(config.to_dict(), indent=4))
    elif fmt == "env":
        click.echo(f"export BLACKBAUD_CLIENT_ID={config.client_id}")
        click.echo(f"export BLACKBAUD_CLIENT_SECRET={config.client_secret}")
        click.echo(f"export BLACKBAUD_REDIRECT_URI={config.redirect_uri}")
        click.echo(f"export BLACKBAUD_SUBSCRIPTION_KEY={config.subscription_key}")


@click.command()
@click.option("-i", "--input_path", type=click.Path(), default=BBSKY_CONFIG_FILE)
@click.option("--client-id", prompt="Client ID")
@click.option("--client-secret", prompt="Client Secret")
@click.option("--redirect-uri", prompt="Redirect URI")
@click.option("--subscription-key", prompt="Subscription Key")
@click.pass_context
@ensure_config_dir
def update(
    context: click.Context,
    input_path: Path,
    client_id: str,
    client_secret: str,
    redirect_uri: str,
    subscription_key: str,
) -> None:
    """Update the current Blackbaud Sky API config."""
    input_path = Path(input_path)
    config = SkyConfig(client_id, client_secret, URL(redirect_uri), subscription_key)
    config.to_json_file(input_path)
    click.echo(f"Config updated at {input_path}")


@click.command()
@click.option("-i", "--input_path", type=click.Path(), default=BBSKY_CONFIG_FILE)
@click.pass_context
def purge(
    context: click.Context,
    input_path: Path,
) -> None:
    """Delete the current Blackbaud Sky API config."""
    input_path = Path(input_path)
    if click.confirm(f"Are you sure you want to delete the current config '{input_path}'?"):
        if input_path.exists():
            input_path.unlink()
            click.echo(f"Config deleted at {input_path}")
        else:
            click.echo(f"Config not found at {input_path}. Nothing to delete.")
    else:
        click.echo("Aborted.")


cli.add_command(create)
cli.add_command(show)
cli.add_command(update)
cli.add_command(purge)
