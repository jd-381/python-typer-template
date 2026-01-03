# Python Typer Template

A production-ready template for building Python CLI applications with [Typer](https://typer.tiangolo.com/).

## Features

- ✅ Modern Python project structure with [uv](https://github.com/astral-sh/uv)
- ✅ Example CLI commands with subcommands
- ✅ Comprehensive test suite with pytest
- ✅ Code quality tools (Ruff for linting and formatting)
- ✅ Pre-commit hooks for automatic quality checks
- ✅ GitHub Actions CI/CD workflow (lint, format, test, docs)
- ✅ Branch protection configuration
- ✅ Auto-generated usage documentation with Typer CLI
- ✅ Makefile for common development tasks

## Getting Started

### 1. Create Your Repository from This Template

1. Click the `Use this template` button at the top of this repository
2. Choose `Create a new repository` then a repository name (e.g., `my-package`)
3. Clone your new repository locally then set it up for development:

```bash
# Install dependencies
uv sync --dev

# Set up pre-commit hooks
make hooks
```

4. Optional: Configure GitHub Branch Protection
   - Branch protection is **optional but recommended** to enforce CI checks before merging. See [SETUP.md](.github/SETUP.md).
   - This will:
      - Require all CI checks to pass (Lint, Format Check, Test, Documentation)
      - Block force pushes and branch deletion
      - Enable automatic branch deletion after merge

```bash
# Configure branch protection (requires GitHub CLI)
make github
```

### 2. Customize Your Project

Rename the package and CLI in the following locations to match your project, where:
- `my_package` should be the name of the package and Python module directory (e.g., `weather_fetcher`)
- `my-cli` should be the executable name that users type in the terminal (e.g., `weatherf`)

**You must retain the underscore and hyphen naming conventions.** This template follows [PEP 8](https://peps.python.org/pep-0008/) naming conventions (underscores for Python modules/packages) and [PEP 508](https://peps.python.org/pep-0508/) distribution naming (hyphens for package names).

#### **Package Directory**

Rename the root project directory to your package name:

```bash
mv my_package weather_fetcher
```

#### `Makefile`

Update `Makefile` variables to your package and CLI name:

```makefile
PACKAGE_NAME = my_package -> weather_fetcher
CLI_NAME = my-cli -> weatherf
```

#### `pyproject.toml`

Update the following project settings to your package and CLI name:

```toml
[project]
name = "my-package" -> "weather-fetcher"

[project.scripts]
my-cli = "my_package.main:app" -> 
weatherf = "weather_fetcher.main:app" 

[tool.hatch.build.targets.wheel]
packages = ["my_package"] -> ["weather_fetcher"]
```

#### **Tests** `tests/*`

Update import statements in `tests/` to your package name:

```python
# test_greet.py
# test_mail.py
from my_package.main import app ->
from weather_fetcher.main import app

# test_services.py
from my_package.commands.greet import GreetingService ->
from weather_fetcher.commands.greet import GreetingService

from my_package.commands.mail import MailService ->
from weather_fetcher.commands.mail import MailService
```

### 3. Validate Your Setup

Run tests to ensure everything is renamed correctly:

```bash
make lint
make format
make test
```

All tests should pass! If they fail, check that you've updated all package and CLI names consistently.

Next, test the actual CLI installation:

```bash
# Install your CLI
make install

# Run a command
weatherf greet --names World
```

If the command prints `Hello World`, your setup is complete!

### 4. Build Your CLI

1. Modify or delete example commands in `my_package/commands/`
2. Update `my_package/main.py` to register your commands
3. Write tests in `tests/`
4. Run tests: `make test`
5. Generate usage documentation: `make docs`
6. Update this `README.md` (below example) and `CONTRIBUTING.md` with your proj

### 5. Clean Up Template Instructions

**Delete everything above this line**

<------------------------------------------------>

# My Package

A brief description of what your CLI does.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package manager

## Installation

Install this CLI tool globally:

```bash
make install
```

Expected output:
```
my-cli installed successfully
```

The CLI will be installed to `~/.local/bin`. Make sure this directory is in your `$PATH`:

```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export PATH="$HOME/.local/bin:$PATH"
```

## Usage

See the [usage documentation](./USAGE.md) for all available commands and options.

### Quick Start

```bash
# Example command
my-cli greet --names Alice,Bob

# Get help
my-cli --help
```

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup and guidelines.