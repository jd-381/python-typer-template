PACKAGE_NAME = template_package
CLI_NAME = template-cli

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make deps         - Install dependencies and set up git hooks"
	@echo "  make docs         - Generate CLI usage documentation"
	@echo "  make format       - Format code with Ruff"
	@echo "  make github       - Configure GitHub branch protection rules"
	@echo "  make install      - Install CLI tool globally"
	@echo "  make lint         - Check code with Ruff linter"
	@echo "  make test         - Run test suite with pytest"
	@echo "  make init         - Test initialization workflow locally with act"
	@echo "  make upgrade      - Reinstall CLI tool (clears cache)"
	@echo "  make validate     - Run lint, format, and test"

.DEFAULT_GOAL := help

.PHONY: deps
deps:
	uv sync --dev
	uv run pre-commit install

.PHONY: docs
docs:
	uv run typer $(PACKAGE_NAME).main utils docs --name $(CLI_NAME) --output USAGE.md

.PHONY: format
format:
	uv run ruff format .

.PHONY: github
github:
	@if ! command -v gh > /dev/null 2>&1; then \
		echo "Error: GitHub CLI (gh) is not installed"; \
		echo "Install it from: https://cli.github.com/"; \
		exit 1; \
	fi
	@echo "Configuring GitHub branch protection rules..."
	@./.github/setup-branch-protection.sh

.PHONY: install
install:
	uv tool install .
	@if which $(CLI_NAME) > /dev/null 2>&1; then \
		echo "$(CLI_NAME) installed successfully"; \
	else \
		echo "⚠️  $(CLI_NAME) installed but not in PATH"; \
		echo "   Add ~/.local/bin to your PATH:"; \
		echo "   export PATH=\"\$$HOME/.local/bin:\$$PATH\""; \
	fi

.PHONY: init
test-init:
	@if ! command -v act > /dev/null 2>&1; then \
		echo "Error: act is not installed"; \
		echo "Install it with: brew install act"; \
		echo "See: https://github.com/nektos/act"; \
		exit 1; \
	fi
	@echo "⚠️  WARNING: This workflow is DESTRUCTIVE!"
	@echo "   It will modify files in your repository."
	@echo ""
	@echo "Recommended: Run this in a git worktree for safe testing:"
	@echo "  git worktree add ../test-init test-init-branch"
	@echo "  cd ../test-init"
	@echo "  make test-init"
	@echo ""
	@read -p "Continue? (yes/NO): " confirm; \
	if [ "$$confirm" != "yes" ]; then \
		echo "Aborted."; \
		exit 1; \
	fi
	@echo ""
	@echo "Testing initialization workflow with act..."
	@echo "Package name: test_package"
	@echo "CLI name: test-cli"
	@echo ""
	act workflow_dispatch \
		--input package_name=test_package \
		--input cli_name=test-cli \
		--workflows .github/workflows/initialize-repository.yml

.PHONY: lint
lint:
	uv run ruff check .

.PHONY: test
test:
	uv run pytest

.PHONY: upgrade
upgrade:
	@echo "Reinstalling $(CLI_NAME)..."
	uv tool install --force --reinstall .

.PHONY: validate
validate:
	@echo "Running validation checks..."
	@$(MAKE) lint
	@$(MAKE) format
	@$(MAKE) test
	@echo "✓ All validation checks passed!"