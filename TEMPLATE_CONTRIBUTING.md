# Contributing

This guide will help you get started with development.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) python package manager

## Development Setup

Install dependencies and set up git hooks:

```bash
make deps
```

This will:

- Install runtime dependencies (Typer)
- Install development dependencies (pytest, ruff, typer-cli, pre-commit)
- Set up pre-commit git hooks

The pre-commit hooks will automatically:

- Format code with Ruff
- Lint code with Ruff
- Run the test suite
- Generate documentation (fails if `USAGE.md` was edited manually)

## Available Make Commands

The project uses a [Makefile](Makefile) to simplify common development tasks. Run `make` to see all available commands.

### Quick Reference

| Command | Description |
|---------|-------------|
| `make deps` | Install dependencies and set up git hooks |
| `make docs` | Generate CLI usage documentation to `USAGE.md` |
| `make format` | Format code with Ruff formatter |
| `make github` | Configure GitHub branch protection rules (requires GitHub CLI) |
| `make hooks` | Install pre-commit git hooks for automatic quality checks |
| `make install` | Install CLI tool globally to `~/.local/bin` |
| `make lint` | Check code with Ruff linter (without modifying files) |
| `make test` | Run test suite with pytest |
| `make upgrade` | Reinstall CLI tool (clears cache and forces fresh install) |
| `make validate` | Run lint, format, and test |

### Command Details

#### `make docs`

Generates comprehensive CLI documentation using Typer CLI. The output is written to `USAGE.md` and includes:

- All commands and subcommands
- Command descriptions and help text
- Available options and arguments
- Usage examples

**Example:**

```bash
make docs
```

#### `make format`

Formats all Python code in the project using Ruff. This modifies files in-place to conform to the configured style guide.

**Example:**

```bash
make format
```

#### `make github`

Configures GitHub branch protection rules for the `main` branch. This command:

- Requires GitHub CLI (`gh`) to be installed and authenticated
- Requires all CI checks to pass before merging
- Blocks force pushes and branch deletion
- Enables automatic branch deletion after merge

**Example:**

```bash
make github
```

**Note:** This is optional but recommended for team projects.

#### `make hooks`

Installs pre-commit hooks that automatically run before each commit. The hooks will:

- Check code formatting with Ruff
- Run linting checks
- Validate your changes before committing

**Example:**

```bash
make hooks
```

**Important:** Run this once after cloning the repository.

**Note:** If the documentation hook fails, it means USAGE.md is out of date (or edited manually). Stage the updated file and commit again:

```bash
git add USAGE.md
git commit -m "Your message"
```

To skip hooks temporarily (not recommended):

```bash
git commit --no-verify
```

#### `make install`

Installs your CLI tool globally using `uv tool install`. The tool will be available in `~/.local/bin`.

**Example:**

```bash
make install

# Then use your CLI
my-cli hello --name World
```

**Note:** If the command isn't found, add `~/.local/bin` to your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

#### `make lint`

Runs Ruff linter to check for code quality issues without modifying files. Use this to validate code before committing.

**Example:**

```bash
make lint
```

#### `make test`

Runs the entire test suite using pytest. Includes all tests in the `tests/` directory.

**Example:**

```bash
make test

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_hello.py
```

#### `make upgrade`

Reinstalls the CLI tool with `--force --reinstall` flags. Use this when:

- You've made changes to the CLI and want to test them
- The installed version is out of sync with your code
- You need to clear cached installations

**Example:**

```bash
make upgrade
```

## Development Workflow

1. Make your changes
2. Write tests
3. Run validation: `make validate` (runs lint, format, and test)
4. Ensure all tests pass before submitting a PR

## Running the CLI During Development

To run the CLI without installing it globally:

```bash
uv run my-cli [command]
```

For example:

```bash
uv run my-cli hello --name World
uv run my-cli mail fetch
```

## Writing Tests

Tests use pytest and Typer's `CliRunner` for testing CLI commands. See the `tests/` directory for examples:

- `test_hello.py` - Tests for the hello command
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
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── pyproject.toml          # Project configuration
├── Makefile                # Development commands
├── README.md               # User documentation
├── USAGE.md                # Generated CLI documentation
└── uv.lock                 # Locked dependencies
```

## Questions?

If you have questions or need help, please open an issue on GitHub.
