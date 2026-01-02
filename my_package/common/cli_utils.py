import logging
from typing import Annotated

import typer

from .logger_utils import yellow


def validate_user_input_comma_list(input: str | None) -> list[str] | None:
    if input is None:
        return None
    if isinstance(input, list):
        if len(input) == 1 and "," in input[0]:
            return [part.strip() for part in input[0].split(",")]
        return input


def validate_user_input_debug(input: bool) -> bool:
    if input:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug(f"{yellow('Debug mode enabled')}")
    return input


DEBUG_OPTION = Annotated[bool, typer.Option("--debug", help="Print debug messages", callback=validate_user_input_debug)]
