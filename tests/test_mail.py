"""Tests for the mail commands."""

from typer.testing import CliRunner

from my_package.main import app

runner = CliRunner()


def test_mail_fetch():
    """Test fetching mail."""
    result = runner.invoke(app, ["mail", "fetch"])
    assert result.exit_code == 0
    assert "Mail" in result.stdout


def test_mail_delete_default():
    """Test deleting mail with default count."""
    result = runner.invoke(app, ["mail", "delete"])
    assert result.exit_code == 0
    assert "Deleted 1 messages" in result.stdout


def test_mail_delete_custom_count():
    """Test deleting mail with custom count."""
    result = runner.invoke(app, ["mail", "delete", "--count", "5"])
    assert result.exit_code == 0
    assert "Deleted 5 messages" in result.stdout


def test_mail_delete_short_option():
    """Test deleting mail with short option."""
    result = runner.invoke(app, ["mail", "delete", "-c", "3"])
    assert result.exit_code == 0
    assert "Deleted 3 messages" in result.stdout


def test_mail_error_command():
    """Test the error command exits with code 1."""
    result = runner.invoke(app, ["mail", "error"])
    assert result.exit_code == 1
