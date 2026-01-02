"""Tests for service classes."""

import logging

import pytest

from my_package.commands.greet import GreetingService
from my_package.commands.mail import MailService

logger = logging.getLogger(__name__)


def test_greeting_service_greet(capsys: pytest.CaptureFixture[str]) -> None:
    """Test GreetingService.greet method."""
    service = GreetingService("Hello", logger)
    service.greet(["Alice", "Bob"])

    captured = capsys.readouterr()
    assert "Hello Alice" in captured.out
    assert "Hello Bob" in captured.out


def test_mail_service_fetch() -> None:
    """Test MailService.fetch method."""
    service = MailService(logger)
    mail = service.fetch()

    assert isinstance(mail, list)
    assert len(mail) > 0
