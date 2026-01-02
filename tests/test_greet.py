"""Tests for the greet command."""

from typer.testing import CliRunner

from my_package.main import app

runner = CliRunner()


def test_greet_single_name():
    """Test greeting a single person."""
    result = runner.invoke(app, ["greet", "--names", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice" in result.stdout


def test_greet_multiple_names():
    """Test greeting multiple people."""
    result = runner.invoke(app, ["greet", "--names", "Alice,Bob,Charlie"])
    assert result.exit_code == 0
    assert "Hello Alice" in result.stdout
    assert "Hello Bob" in result.stdout
    assert "Hello Charlie" in result.stdout


def test_greet_custom_greeting():
    """Test using a custom greeting."""
    result = runner.invoke(app, ["greet", "--names", "Alice", "--greeting", "Hi"])
    assert result.exit_code == 0
    assert "Hi Alice" in result.stdout


def test_greet_short_options():
    """Test using short option flags."""
    result = runner.invoke(app, ["greet", "-n", "Alice", "-g", "Hey"])
    assert result.exit_code == 0
    assert "Hey Alice" in result.stdout
