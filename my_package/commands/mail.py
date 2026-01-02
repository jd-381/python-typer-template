import logging
from logging import Logger
from typing import Annotated

import typer

from ..common.cli_utils import DEBUG_OPTION
from ..models.mail import Mail, mail_data

LOGGER = logging.getLogger(__name__)

app = typer.Typer(invoke_without_command=False, no_args_is_help=True)


class MailService:
    def __init__(self, logger: Logger):
        self._logger: Logger = logger

    def delete(self, count: int) -> int:
        self._logger.info(f"Deleted {count} messages")
        remaining_messages: int = max(0, len(mail_data) - count)
        self._logger.debug(f"{remaining_messages} messages remain")
        return count

    def fetch(self) -> list[Mail]:
        self._logger.debug("Fetching mail")
        return mail_data


@app.command(name="delete", help="Delete mail")
def delete(
    count: Annotated[int, typer.Option("--count", "-c", help="Number of messages to delete")] = 1,
    debug: DEBUG_OPTION = False,
) -> None:
    try:
        svc: MailService = MailService(LOGGER)
        deleted: int = svc.delete(count)
        print(f"Deleted {deleted} messages")
    except Exception as e:
        LOGGER.error(e)
        raise typer.Exit(code=1)


@app.command(name="fetch", help="Fetch mail")
def fetch(debug: DEBUG_OPTION = False) -> None:
    try:
        svc: MailService = MailService(LOGGER)
        mail: list[Mail] = svc.fetch()
        for m in mail:
            print(m)
    except Exception as e:
        LOGGER.error(e)
        raise typer.Exit(code=1)


@app.command(name="error", help="Show example error")
def error() -> None:
    try:
        raise Exception("This is an example error message")
    except Exception as e:
        LOGGER.error(e)
        raise typer.Exit(code=1)
