import logging
from logging import Logger
from typing import Annotated

import typer

from ..common.cli_utils import DEBUG_OPTION, validate_user_input_comma_list
from ..common.logger_utils import cyan

LOGGER = logging.getLogger(__name__)

app = typer.Typer(invoke_without_command=True, no_args_is_help=False)


class GreetingService:
    def __init__(self, greeting: str, logger: Logger):
        self._greeting: str = greeting
        self._logger: Logger = logger

    def greet(self, names: list[str]) -> None:
        self._logger.debug(f"Using greeting {cyan(self._greeting)}")
        for name in names:
            print(f"{self._greeting} {name}")


@app.callback()
def main(
    names: Annotated[
        list[str],
        typer.Option("--names", "-n", help="Comma-separated list of names", callback=validate_user_input_comma_list),
    ],
    greeting: Annotated[str, typer.Option("--greeting", "-g", help="Greeting")] = "Hello",
    debug: DEBUG_OPTION = False,
) -> None:
    try:
        svc: GreetingService = GreetingService(greeting, LOGGER)
        svc.greet(names)
    except Exception as e:
        LOGGER.error(e)
        raise typer.Exit(code=1)
