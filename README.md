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

1. Click the "Use this template" button at the top of this repository
2. Choose a repository name (e.g., `your-package`)
3. Clone your new repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/your-package.git
   cd your-package
   ```

**Then install dependencies:**

```bash
# Install dependencies
uv sync --dev

# Set up pre-commit hooks
make hooks
```

#### Optional: Configure GitHub Branch Protection

After pushing your repository to GitHub, set up branch protection rules to enforce CI checks:

```bash
# Configure branch protection (requires GitHub CLI)
make github
```

This will automatically configure your `main` branch to:
- Require pull requests before merging
- Require all CI checks to pass (Lint, Format Check, Test, Documentation)
- Require conversation resolution
- Block force pushes and deletions

**Optional: Enable Code Owner Reviews**

If working with a team, uncomment lines in [.github/CODEOWNERS](.github/CODEOWNERS) and replace `@your-github-username` with actual GitHub usernames to automatically request reviews from code owners.

### 2. Customize Your CLI

Rename the following to match your project:

#### **Package Directory**
```bash
# Package name (Python module directory)
mv my_package your_package
```

#### **Makefile** (`Makefile`)
```makefile
# Package name (Python module directory)
PACKAGE_NAME = your_package
# CLI executable name (what users type in terminal)
CLI_NAME = your-cli
```

#### **pyproject.toml**
```toml
[project]
name = "your-package"
description = "Your package description"

[project.scripts]
your-cli = "your_package.main:app"

[tool.hatch.build.targets.wheel]
packages = ["your_package"]
```

#### **Tests**
Update import statements in `tests/` to use your new package name:
```python
from your_package.main import app
from your_package.commands.greet import GreetingService
```

### 3. Validate Your Setup

Run tests to ensure everything is renamed correctly and working:

```bash
make format
make lint
make test
```

All tests should pass! If they fail, check that you've updated all package names consistently.

### 4. Build Your CLI

1. Modify or delete example commands in `your_package/commands/`
2. Update `your_package/main.py` to register your commands
3. Write tests in `tests/`
4. Run tests: `make test`
5. Generate documentation: `make docs`

### 5. Clean Up Template Instructions

✅ **Before you're done, complete this checklist:**
- [ ] Renamed `my_package` directory to your package name
- [ ] Updated `PACKAGE_NAME` and `CLI_NAME` in Makefile
- [ ] Updated package name, description, scripts, and wheel in pyproject.toml
- [ ] Updated test imports to use your package name
- [ ] Modified or deleted example commands
- [ ] Ran tests successfully with `make test`
- [ ] Generated documentation with `make docs`
- [ ] (Optional) Configured branch protection with `make github`
- [ ] (Optional) Updated `.github/CODEOWNERS` with team members
- [ ] Updated CONTRIBUTING.md with your project-specific contribution guidelines
- [ ] **Deleted everything above this line (including this checklist!)**

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

See the auto-generated [usage documentation](./USAGE.md) for all available commands and options.

### Quick Examples

```bash
# Example command
my-cli greet --names Alice,Bob

# Get help
my-cli --help
```

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup and guidelines.