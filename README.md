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

1. Click the **Use this template** button at the top of this repository
2. Choose **Create a new repository** then enter a repository name (e.g., `my-package`)

### 2. Initialize Your Project

Initialize your project using the GitHub Actions workflow:

1. Go to your new repository's **Actions** tab on GitHub
2. Select the **Initialize Repository** workflow
3. Click the **Run workflow** button
4. Enter your project's inputs:
   - **Package name**: Python module name with underscores (e.g., `mail_fetcher`)
   - **CLI name**: Command-line executable name, use hyphens for multi-word (e.g., `ma-fe`)
5. Click **Run workflow**
6. Wait for the job to finish and the success summary to appear

The workflow will:

- Validate your inputs (prevents running twice)
- Rename the package directory
- Update all configuration files
- Update all imports
- Run linting, formatting, and tests
- Commit and push the changes
- Display a summary with next steps at the top of the workflow run page

**You must retain the underscore and hyphen naming.** This template follows [PEP 8](https://peps.python.org/pep-0008/) naming conventions (underscores for Python modules/packages) and [PEP 508](https://peps.python.org/pep-0508/) distribution naming (hyphens for package names).

### 3. Validate Your Setup

After the workflow completes, set up your local repository for development (either clone or pull the workflow's changes):

```bash
# Install dependencies and set up git hooks
make deps

# Validate initialization
make validate
```

Install the CLI and run a command:

```bash
# Installs to ~/.local/bin
make install

# Run hello command
# Replace my-cli with your CLI name chosen during initialization
my-cli hello --name World
```

If the command prints `Hello World`, your setup is complete!

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

_If not configured, the pre-commit hooks will still enforce the CI checks._

### 4. Build Your CLI

Now you're ready to customize your CLI application. See [TEMPLATE_CONTRIBUTING.md](TEMPLATE_CONTRIBUTING.md) for a detailed developer workflow.

High-level next steps:

1. Write new commands in `<your_package_name>/commands/`
2. Register your new commands in `<your_package_name>/main.py`
3. Write tests in `tests/`
4. Run validation: `make validate` (runs lint, format, and test)
5. Generate `USAGE.md` documentation: `make docs`
6. Replace `CONTRIBUTING.md` with `TEMPLATE_CONTRIBUTING.md` (remove template-specific content)
7. Update `TEMPLATE_README.md` with your project details
8. Replace this `README.md` with `TEMPLATE_README.md`