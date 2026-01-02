import logging

import typer
from rich.logging import RichHandler

from .commands.greet import app as greet
from .commands.mail import app as mail

logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[RichHandler(markup=True)])

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(greet, name="greet", help="No command example")
app.add_typer(mail, name="mail", help="Multiple command example")
