#!/bin/bash
# Script to configure branch protection rules using GitHub CLI
# Requires: gh CLI (https://cli.github.com/)
# Usage: ./setup-branch-protection.sh

set -e

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
BRANCH="main"

echo "Setting up branch protection for $REPO on branch $BRANCH..."

# Enable branch protection
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO/branches/$BRANCH/protection" \
  --input - <<EOF
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["Lint", "Format Check", "Test", "Documentation"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "lock_branch": false,
  "allow_fork_syncing": false,
  "required_linear_history": false,
  "require_signed_commits": false
}
EOF

echo "✓ Branch protection configured successfully!"
echo ""
echo "Settings applied:"
echo "  - Require PR before merging"
echo "  - Require status checks: Lint, Format Check, Test, Documentation"
echo "  - Require code owner reviews"
echo "  - Require conversation resolution"
echo "  - Enforce for admins"
echo "  - Block force pushes and deletions"
