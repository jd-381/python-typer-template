# Contributing

Thank you for your interest in contributing to this project! This guide will help you get started with development.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) python package manager

## Development Setup

1. Install dependencies:
```bash
uv sync --dev
```

This will install:
- Runtime dependencies (Typer)
- Development dependencies (pytest, ruff, typer-cli, pre-commit)

3. Set up git hooks:
```bash
make hooks
```

This installs pre-commit hooks that automatically run before each commit to:
- Format code with Ruff
- Lint code with Ruff
- Run the test suite
- Generate documentation (fails if USAGE.md needs updating)

## Available Make Commands

The project uses a Makefile to simplify common development tasks:

### Testing

```bash
make test
```
Runs the test suite using pytest. Tests are located in the `tests/` directory.

### Code Formatting

```bash
make format
```
Formats all Python code using Ruff formatter. This ensures consistent code style across the project.

### Linting

```bash
make lint
```
Checks code for style issues and potential errors using Ruff linter.

### Documentation

```bash
make docs
```
Generates CLI usage documentation in `USAGE.md` using Typer's built-in documentation generator.

### Git Hooks

```bash
make hooks
```
Installs pre-commit hooks that run automatically before each commit. The hooks will:
- Auto-format your code with Ruff
- Check for linting issues with Ruff
- Run the test suite
- Regenerate USAGE.md documentation

**Note:** If the documentation hook fails, it means USAGE.md is out of date. Stage the updated file and commit again:
```bash
git add USAGE.md
git commit -m "Your message"
```

To skip hooks temporarily (not recommended):
```bash
git commit --no-verify
```

### Installation

```bash
make install
```
Installs the CLI tool globally using `uv tool install`. The executable will be available as `my-cli` (or your custom CLI name).

### Upgrade

```bash
make upgrade
```
Reinstalls the CLI tool after clearing the uv cache. Use this when you've made changes to the code and `make install` isn't picking them up.

## Development Workflow

1. Make your changes
2. Format your code: `make format`
3. Check for linting issues: `make lint`
4. Run tests: `make test`
5. Ensure all tests pass before submitting a PR

## Running the CLI During Development

To run the CLI without installing it globally:

```bash
uv run my-cli [command]
```

For example:
```bash
uv run my-cli greet --names Alice,Bob
uv run my-cli mail fetch
```

## Writing Tests

Tests use pytest and Typer's `CliRunner` for testing CLI commands. See the `tests/` directory for examples:

- `test_greet.py` - Tests for the greet command
- `test_mail.py` - Tests for mail commands
- `test_services.py` - Unit tests for service classes

Example test structure:
```python
from typer.testing import CliRunner
from my_package.main import app

runner = CliRunner()

def test_example():
    result = runner.invoke(app, ["command", "--option", "value"])
    assert result.exit_code == 0
    assert "expected output" in result.stdout
```

## Code Style

This project uses Ruff for both linting and formatting with a line length of 120 characters. The configuration is in `pyproject.toml`.

## Project Structure

```
.
├── my_package/             # Main package
│   ├── commands/           # CLI command modules
│   ├── common/             # Shared utilities
│   ├── models/             # Data models
│   └── main.py             # CLI entry point
├── tests/                  # Test suite
├── pyproject.toml          # Project configuration
├── Makefile                # Development commands
└── README.md               # User documentation
```

## Questions?

If you have questions or need help, please open an issue on GitHub.
