# Contributing to Python CLI Template

This guide will help you get started with development and testing.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package manager

## Development Setup

### Install Dependencies

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


### Validate Setup

```bash
make validate
```

This will:

- Check code with Ruff linter (`make lint`)
- Format code with Ruff formatter (`make format`)
- Run the test suite with pytest (`make test`)

This command runs all quality checks in sequence, ensuring your code is properly linted, formatted, and tested. It's the same set of checks that pre-commit hooks run, making it useful for verifying your setup or manually validating changes before committing.

### Testing The CLI

**During development**, use `uv run` to test your changes without installing:

```bash
uv run template-cli hello --name World
```

**To test the installed CLI**, use `make install`:

```bash
make install
```

This installs it globally to `~/.local/bin`. Once installed, you can run:

```bash
template-cli hello --name World
```

After making code changes, use `make upgrade` to reinstall with a fresh cache.

**Note:** If the command isn't found, make sure `~/.local/bin` is in your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Available Make Commands

Run `make` to see all available commands.

### Quick Reference

| Command | Description |
|---------|-------------|
| `make deps` | Install dependencies and set up git hooks |
| `make docs` | Generate CLI usage documentation to `USAGE.md` |
| `make format` | Format code with Ruff formatter |
| `make github` | Configure GitHub branch protection rules (requires GitHub CLI) |
| `make install` | Install CLI tool globally to `~/.local/bin` |
| `make lint` | Check code with Ruff linter (without modifying files) |
| `make test` | Run test suite with pytest |
| `make upgrade` | Reinstall CLI tool (clears cache and forces fresh install) |
| `make validate` | Run lint, format, and test |

## Project Structure

```
.
├── template_package/                 # Template package (gets renamed)
│   ├── commands/                     # CLI command modules
│   ├── common/                       # Shared utilities
│   ├── models/                       # Data models
│   └── main.py                       # CLI entry point
├── tests/                            # Test suite
├── .github/
│   ├── workflows/
│   │   ├── initialize-repository.yml # Main initialization workflow
│   │   ├── ci.yml                    # CI workflow
│   │   └── SETUP.md                  # Workflow testing guide
│   └── setup-branch-protection.sh    # Branch protection setup script
├── .pre-commit-config.yaml           # Pre-commit hooks configuration
├── pyproject.toml                    # Project configuration
├── Makefile                          # Development commands
├── README.md                         # Template repository documentation
├── TEMPLATE_README.md                # README for initialized projects
├── CONTRIBUTING.md                   # This file - for template contributors
├── TEMPLATE_CONTRIBUTING.md          # CONTRIBUTING for initialized projects
├── USAGE.md                          # Generated CLI documentation
└── uv.lock                           # Locked dependencies
```

## Testing Strategy

### Unit Tests

- Test individual commands and services
- Located in `tests/test_*.py`
- Run with `make test`

### Pre-commit Hooks

- Automatic checks before each commit
- Ensures code quality standards
- Validates documentation is up to date

## Code Style

This project uses Ruff for both linting and formatting. The configuration is in `pyproject.toml`.

## Questions?

If you have questions or need help:
1. Look at existing issues and PRs for similar problems
2. Open a new issue with your question

Thank you for contributing! 🎉
