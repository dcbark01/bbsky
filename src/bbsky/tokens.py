import json
from pathlib import Path
from typing import Any

import click
from attrs import asdict, define

from bbsky.paths import BBSKY_TOKEN_FILE


@define(slots=True, frozen=True)
class OAuth2Token:
    """User Access Credentials for Blackbaud Sky API"""

    access_token: str
    refresh_token: str
    expires_in: int
    refresh_token_expires_in: int
    token_type: str
    environment_id: str
    environment_name: str
    legal_entity_id: str
    legal_entity_name: str
    user_id: str
    email: str
    family_name: str
    given_name: str
    mode: str

    def __str__(self):
        token_trunc = self.access_token[:4] + "..." + self.access_token[-4:]
        return (
            f"Access Token: {token_trunc} (expires in {self.expires_in} seconds) | Refresh Token: {self.refresh_token}"
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "OAuth2Token":
        return cls(**data)

    @classmethod
    def load(cls, input_file: Path) -> "OAuth2Token":
        """Load the token from a file."""
        return cls(**json.loads(input_file.read_text()))

    @classmethod
    def from_cache(cls) -> "OAuth2Token":
        """Load the token from the default cache file."""
        return cls.load(BBSKY_TOKEN_FILE)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def save(self, output_file: Path) -> None:
        """Save the token to a file."""
        output_file.write_text(json.dumps(self.to_dict(), indent=4))

    def to_cache(self) -> None:
        """Save the token to the default cache file."""
        self.save(BBSKY_TOKEN_FILE)


@click.group()
def cli():
    """CLI for Blackbaud token management."""
    pass


@click.command()
@click.option("-t", "--token-file", default=BBSKY_TOKEN_FILE, type=click.Path())
def show(token_file: Path) -> None:
    """Show the current token."""

    # Check if the token file exists
    if not token_file.exists():
        click.echo("No token found.")
        return

    token = OAuth2Token.load(token_file)
    click.echo(f"Token for {token.email}: {str(token)}")


@click.command()
@click.option("-t", "--token-file", default=BBSKY_TOKEN_FILE, type=click.Path())
def purge(token_file: Path) -> None:
    """Purge the current token."""

    # Check if the token file exists
    if not token_file.exists():
        click.echo("No token found.")
        return

    # Confirm with the user
    token = OAuth2Token.load(token_file)
    click.echo(f"Current token: {str(token)}")

    if click.confirm("Are you sure you want to purge the current token?"):
        token_file.unlink()
        click.echo("Token purged.")
    else:
        click.echo("Aborted. Token not purged.")


cli.add_command(show)
cli.add_command(purge)
