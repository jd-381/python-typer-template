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

### 2. Initialize Your Project

Initialize your project using the GitHub Actions workflow:

1. Go to your new repository's **Actions** tab on GitHub
2. Select the **Initialize Repository** workflow
3. Click the **Run workflow** button
4. Enter your project's inputs:
   - **Package name**: Python module name with underscores (e.g., `weather_fetcher`)
   - **CLI name**: Command-line executable name, use hyphens for multi-word (e.g., `weatherf` or `we-fe`)
5. Click **Run workflow**
6. Wait for the job to finish and the success summary to appear

The workflow will:
- Validate your inputs (prevents running twice)
- Rename the package directory
- Update all configuration files
- Update all test imports
- Run linting, formatting, and tests
- Commit and push the changes
- Display a summary with next steps at the top of the workflow run page

**You must retain the underscore and hyphen naming conventions.** This template follows [PEP 8](https://peps.python.org/pep-0008/) naming conventions (underscores for Python modules/packages) and [PEP 508](https://peps.python.org/pep-0508/) distribution naming (hyphens for package names).

### 3. Validate Your Setup

After the workflow completes, pull the changes to your local repository:

```bash
# Pull the changes made by the workflow
git pull

# Install dependencies
uv sync --dev

make hooks
make lint
make format
make test
```

Install the CLI and run a command:

```bash
# Install your CLI
make install

# Run greet command using your CLI name
my-cli greet --names World
```

If the command prints `Hello World`, your setup is complete!

> **Note:** Replace `my-cli` with your actual CLI name that you chose during initialization.

**Optional: Configure GitHub Branch Protection**

Branch protection is optional but recommended to enforce CI checks before merging. See [SETUP.md](.github/SETUP.md).


```bash
# Requires GitHub CLI
make github
```

This opinionated command will:
   - Require all CI checks to pass (Lint, Format Check, Test, Documentation)
   - Block force pushes and branch deletion
   - Enable automatic branch deletion after merge

If not configured, the pre-commit hooks will still enforce the CI checks.

### 4. Build Your CLI

Now you're ready to customize your CLI application:

1. Modify or delete example commands in `<your_package_name>/commands/`
2. Update `<your_package_name>/main.py` to register your new commands
3. Write tests in `tests/`
4. Run tests: `make test`
5. Generate `USAGE.md` documentation: `make docs`
6. Update the `CONTRIBUTING.md` with your project details
7. Replace this `README.md` with the `TEMPLATE_README.md` (rename `TEMPLATE_README.md` to `README.md` and customize it for your project)