# GitHub Configuration

This directory contains GitHub-specific configuration files.

## Files

### [workflows/ci.yml](workflows/ci.yml)
CI/CD pipeline that runs on every push and pull request:
- **Lint**: Code quality checks with Ruff
- **Format Check**: Ensures code is properly formatted
- **Test**: Runs the test suite
- **Documentation**: Verifies USAGE.md is up to date

### [setup-branch-protection.sh](setup-branch-protection.sh)
**Optional one-time script** to configure branch protection rules for the `main` branch using the GitHub CLI.

You can use this script for convenience, configure branch protection manually (see below), or add it to your Infrastructure as Code.

## Initial Setup

After cloning this repository:

```bash
# Install pre-commit hooks locally
make hooks
```

## Branch Protection (Optional)

Branch protection is **optional but recommended** to enforce CI checks before merging.

### Option 1: Automated Setup (requires GitHub CLI)

```bash
# One-time setup - requires admin access and GitHub CLI
make github
```

This will:
- Require all CI checks to pass (Lint, Format Check, Test, Documentation)
- Block force pushes and branch deletion
- Enable automatic branch deletion after merge

### Option 2: Manual Configuration

If you prefer to configure branch protection manually:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Branches**
3. Click **Add branch protection rule**
4. Set **Branch name pattern** to `main`
5. Enable:
   - ✅ Require status checks to pass before merging
     - Select: `Lint`, `Format Check`, `Test`, `Documentation`
   - ✅ Do not allow force pushes
6. Save changes

### Option 3: Infrastructure as Code

Manage branch protection alongside your other infrastructure using tools like Terraform (with the GitHub provider), Pulumi, or other IaC solutions.

## CI/CD in GitHub Actions

The workflow runs automatically on:
- Every push to `main`
- Every pull request to `main`

All checks must pass before code can be merged, preventing:
- Unformatted code
- Failing tests
- Outdated documentation
- Code quality issues

Even changes made via GitHub's web editor must pass these checks through a pull request.
