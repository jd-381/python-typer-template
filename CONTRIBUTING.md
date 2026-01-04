# Contributing to Python CLI Template

Thank you for your interest in contributing to the Python CLI Template! This guide will help you get started with development and testing.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package manager
- [act](https://github.com/nektos/act) - GitHub Actions local runner (for testing workflows)

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

To run the template CLI without installing it globally:

```bash
uv run template-cli [command]
```

For example:
```bash
uv run template-cli hello --name World
uv run template-cli mail fetch
```

```bash
make install
```

This will install the `template-cli` tool globally to `~/.local/bin`. Once installed, you can test it:

```bash
template-cli hello --name World
```

You should see:

```
Hello World
```

**Note:** If the command isn't found, make sure `~/.local/bin` is in your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Initialize Repository Workflow

The **Initialize Repository** workflow is a critical part of this template. We use `act` to test it locally before pushing changes.

The workflow will:

1. Rename the package directory
2. Update all configuration files
3. Update imports in all Python files
4. Run linting and formatting
5. Run the test suite

**⚠️ Important:** This workflow is destructive when testing locally - it will modify files in your working directory. To safely test your changes, create a separate git worktree from your branch.

### Using Git Worktrees for Safe Testing

```bash
# Create a test-init-branch worktree in the /tmp directory
git worktree add /tmp test-init-branch

# Navigate to the worktree
cd /tmp

# Run the initialization workflow with act
make test-init
# Or with custom inputs:
act workflow_dispatch \
  --input package_name=custom_package \
  --input cli_name=custom-cli \
  --workflows .github/workflows/initialize-repository.yml

# Inspect the changes made by the workflow
git status
git diff

# When done, return to main directory and clean up
cd ../python-cli-template
git worktree remove ../test-init
git branch -D test-init-branch  # Delete the test branch if no longer needed
```

```bash
# Quick test with default inputs
make test-init

# Or test with custom inputs
act workflow_dispatch \
  --input package_name=custom_package \
  --input cli_name=custom-cli \
  --workflows .github/workflows/initialize-repository.yml
```



If any step fails, the workflow has a bug that needs to be fixed.





**Why use worktrees?**
- Isolates destructive changes to a separate directory
- Keeps your main development environment clean
- Allows you to easily compare before/after states
- Can be quickly deleted when testing is complete

**Recommended workflow:**
1. Make changes to the initialization workflow in your main working directory
2. Create a worktree for testing
3. Run `act` in the worktree to test the destructive changes
4. Verify the workflow completed successfully and files were updated correctly
5. Clean up the worktree
6. Commit your workflow changes in the main directory

### Testing Other Workflows

```bash
# Test CI workflow (runs on pull requests)
act pull_request

# Test on push events
act push

# List all workflows
act -l
```

### Troubleshooting act

**Issue: Docker errors or missing tools**
- Try using a larger image: `act -P ubuntu-latest=catthehacker/ubuntu:full-latest`
- Or pull the latest image: `docker pull catthehacker/ubuntu:act-latest`

**Issue: Workflow fails on git operations**
- act runs in a clean container, so git operations may behave differently
- Use `--container-architecture linux/amd64` if you're on Apple Silicon

**Issue: Secrets not available**
- Create `.secrets` file with: `GITHUB_TOKEN=your_token_here`
- Or use: `act --secret GITHUB_TOKEN=your_token`

**Note:** The `.actrc` file in the repository root contains default configuration for act, using `catthehacker/ubuntu:act-latest` image with verbose output enabled.

### Understanding the Initialization Workflow

The workflow in [.github/workflows/initialize-repository.yml](.github/workflows/initialize-repository.yml) performs these critical operations:

1. **Validation** - Ensures package_name uses underscores, cli_name is valid
2. **Package Renaming** - Renames `template_package/` to user's package name
3. **Configuration Updates** - Updates Makefile and pyproject.toml
4. **Import Updates** - Updates all Python imports across the codebase
5. **Version Update** - Updates the `version()` call in main.py to use the distribution name
6. **Validation Checks** - Runs lint, format, and test to ensure everything works

**Common Issues to Watch For:**
- Forgetting to update a reference to `template_package` or `template-package`
- Not handling the underscore-to-hyphen conversion for distribution names
- Missing imports in new files
- Not testing that the package metadata is accessible after initialization

**Best Practices:**
1. Always test the initialization workflow locally before pushing changes
2. Test with different package names (with/without underscores)
3. Verify the workflow produces a working CLI application
4. Run `make lint && make format && make test` after workflow completes

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
| `make init` | Test initialization workflow locally with act |
| `make upgrade` | Reinstall CLI tool (clears cache and forces fresh install) |
| `make validate` | Run lint, format, and test |

## Development Workflow

### For Template Changes

1. Make your changes to the template
2. Test the initialization workflow: `make test-init`
3. Verify the initialized project works correctly
4. Run validation: `make validate` (runs lint, format, and test)
5. Ensure all checks pass before submitting a PR

### For Documentation Changes

1. Update relevant documentation files
2. If you modified workflow behavior, update [.github/workflows/README.md](.github/workflows/README.md)
3. If you changed the template structure, update both README.md and TEMPLATE_README.md
4. Test that the documentation matches the actual behavior

### For Workflow Changes

Any changes to `.github/workflows/initialize-repository.yml` MUST be tested with `act` before pushing:

```bash
make test-init
```

Common workflow changes:
- Adding new files to rename/update
- Changing validation logic
- Updating the initialization steps
- Modifying output messages

## Project Structure

```
.
├── template_package/                      # Template package (gets renamed)
│   ├── commands/                    # CLI command modules
│   ├── common/                      # Shared utilities
│   ├── models/                      # Data models
│   └── main.py                      # CLI entry point
├── tests/                           # Test suite
├── .github/
│   ├── workflows/
│   │   ├── initialize-repository.yml  # Main initialization workflow
│   │   ├── ci.yml                     # CI workflow
│   │   └── README.md                  # Workflow testing guide
│   └── setup-branch-protection.sh   # Branch protection setup script
├── .pre-commit-config.yaml          # Pre-commit hooks configuration
├── pyproject.toml                   # Project configuration
├── Makefile                         # Development commands
├── README.md                        # Template repository documentation
├── TEMPLATE_README.md               # README for initialized projects
├── CONTRIBUTING.md                  # This file - for template contributors
├── TEMPLATE_CONTRIBUTING.md         # CONTRIBUTING for initialized projects
├── USAGE.md                         # Generated CLI documentation
└── uv.lock                          # Locked dependencies
```

## Testing Strategy

### Unit Tests
- Test individual commands and services
- Located in `tests/test_*.py`
- Run with `make test`

### Integration Tests
- The initialization workflow itself serves as an integration test
- Tests that all pieces work together after template instantiation
- Run with `make test-init`

### Pre-commit Hooks
- Automatic checks before each commit
- Ensures code quality standards
- Validates documentation is up to date

## Code Style

This project uses Ruff for both linting and formatting with a line length of 120 characters. The configuration is in `pyproject.toml`.



## Questions?

If you have questions or need help:
1. Look at existing issues and PRs for similar problems
2. Open a new issue with your question

Thank you for contributing! 🎉
