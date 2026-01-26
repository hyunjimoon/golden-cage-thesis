#!/bin/bash
#
# THESIS SELF-AUDIT LOOP
# ======================
# Automated thesis quality sweep with GitHub integration.
#
# Usage:
#   ./thesis_audit_loop.sh              # Run once (manual trigger)
#   ./thesis_audit_loop.sh --schedule   # Install daily schedule (launchd)
#   ./thesis_audit_loop.sh --unschedule # Remove schedule
#
# What it does:
#   1. Analyzes thesis chapters, figures, tables, bibliography
#   2. Collects 30+ improvements from evaluator perspective
#   3. Creates GitHub issue with prioritized findings
#   4. Creates branch with suggested fixes
#   5. Opens PR for your review
#

set -e

# Configuration
THESIS_DIR="/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/papers_v7_sail"
REPO_ROOT="/Users/hyunjimoon/tolzul"
PLIST_NAME="com.thesis.audit"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
LOG_DIR="$THESIS_DIR/.audit_logs"
MIN_IMPROVEMENTS=30

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# Create launchd plist for scheduling
install_schedule() {
    local interval="${1:-10800}"  # Default 3 hours (10800 seconds)
    local hours=$((interval / 3600))

    log "Installing schedule (runs every ${hours} hours)..."

    mkdir -p "$(dirname "$PLIST_PATH")"

    cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>$THESIS_DIR/code/thesis_audit_loop.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>${interval}</integer>
    <key>StandardOutPath</key>
    <string>${LOG_DIR}/audit.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_DIR}/audit_error.log</string>
    <key>WorkingDirectory</key>
    <string>${THESIS_DIR}</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

    launchctl unload "$PLIST_PATH" 2>/dev/null || true
    launchctl load "$PLIST_PATH" 2>/dev/null || launchctl bootstrap gui/$(id -u) "$PLIST_PATH"
    success "Audit scheduled every ${hours} hours (runs immediately, then repeats)"
    echo "  Logs: $LOG_DIR/"
    echo "  To run manually: ./thesis_audit_loop.sh"
    echo "  To stop: ./thesis_audit_loop.sh --unschedule"
}

uninstall_schedule() {
    log "Removing schedule..."
    launchctl unload "$PLIST_PATH" 2>/dev/null || launchctl bootout gui/$(id -u)/$PLIST_NAME 2>/dev/null || true
    rm -f "$PLIST_PATH"
    success "Schedule removed"
}

# Main audit function
run_audit() {
    log "Starting thesis self-audit..."

    # Setup
    mkdir -p "$LOG_DIR"
    TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
    BRANCH_NAME="audit/${TIMESTAMP}"
    ISSUE_FILE="$LOG_DIR/issue_${TIMESTAMP}.md"

    cd "$REPO_ROOT"

    # Check for uncommitted changes
    if [[ -n $(git status --porcelain) ]]; then
        warn "Uncommitted changes detected. Stashing..."
        git stash push -m "audit-stash-${TIMESTAMP}"
        STASHED=true
    fi

    # Create audit branch from main
    log "Creating branch: $BRANCH_NAME"
    git checkout main
    git pull origin main
    git checkout -b "$BRANCH_NAME"

    # Run Claude audit
    log "Running Claude analysis (this may take a few minutes)..."

    AUDIT_PROMPT="You are a rigorous MIT PhD thesis evaluator. Audit this thesis comprehensively.

SCAN these files:
- All .tex files in: $THESIS_DIR/
- All figures in: $THESIS_DIR/img/
- All tables in: $THESIS_DIR/table/
- Bibliography: $THESIS_DIR/golden_cage.bib

COLLECT exactly $MIN_IMPROVEMENTS improvements across these categories:

## CRITICAL (fix before submission) - aim for 5+
- Statistical errors, wrong numbers, inconsistent data
- Missing citations, broken references
- Logical contradictions

## IMPORTANT (significantly improves quality) - aim for 10+
- Unclear arguments, weak transitions
- Figure/table issues (labels, captions, readability)
- Missing definitions, undefined acronyms

## MINOR (polish) - aim for 15+
- Grammar, typos, formatting
- Redundant text, wordiness
- Style inconsistencies

For each improvement, provide:
1. File and line number (if applicable)
2. Current text/issue
3. Suggested fix
4. Category (CRITICAL/IMPORTANT/MINOR)

After listing all improvements, CREATE FIXES for the top 10 most impactful issues by editing the actual files.

Output format for the issue:
\`\`\`markdown
# Thesis Audit Report - [DATE]

## Summary
- Critical: X issues
- Important: Y issues
- Minor: Z issues

## Critical Issues
### 1. [Title]
- **File**: path/to/file.tex:LINE
- **Issue**: description
- **Fix**: suggested correction

[continue for all issues...]

## Commits in this PR
- [list of fixes applied]
\`\`\`"

    # Run claude and capture output
    claude --print "$AUDIT_PROMPT" > "$ISSUE_FILE" 2>&1 || {
        error "Claude analysis failed. Check $ISSUE_FILE for details."
        git checkout main
        git branch -D "$BRANCH_NAME" 2>/dev/null || true
        [[ "$STASHED" == "true" ]] && git stash pop
        exit 1
    }

    # Check if any changes were made
    if [[ -z $(git status --porcelain) ]]; then
        warn "No fixes were applied. Creating issue only."
        git checkout main
        git branch -D "$BRANCH_NAME"

        # Create issue without PR
        gh issue create \
            --title "📋 Thesis Audit Report - $(date '+%Y-%m-%d %H:%M')" \
            --body-file "$ISSUE_FILE" \
            --label "audit,thesis"

        [[ "$STASHED" == "true" ]] && git stash pop
        success "Issue created (no fixes to PR)"
        exit 0
    fi

    # Commit changes
    log "Committing fixes..."
    git add -A
    git commit -m "$(cat <<EOF
🔍 Thesis audit fixes - $(date '+%Y-%m-%d')

Automated improvements from thesis self-audit loop.
See linked issue for full report.

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"

    # Push branch
    log "Pushing branch..."
    git push -u origin "$BRANCH_NAME"

    # Create issue
    log "Creating GitHub issue..."
    ISSUE_URL=$(gh issue create \
        --title "📋 Thesis Audit Report - $(date '+%Y-%m-%d %H:%M')" \
        --body-file "$ISSUE_FILE" \
        --label "audit,thesis")

    ISSUE_NUM=$(echo "$ISSUE_URL" | grep -oE '[0-9]+$')

    # Create PR
    log "Creating pull request..."
    PR_URL=$(gh pr create \
        --title "🔍 Thesis Audit Fixes - $(date '+%Y-%m-%d')" \
        --body "$(cat <<EOF
## Automated Thesis Audit

This PR contains fixes identified by the thesis self-audit loop.

### Related Issue
Closes #${ISSUE_NUM}

### Review Checklist
- [ ] Reviewed all changes
- [ ] Verified fixes are correct
- [ ] No unintended modifications

### How to Review
1. Check the linked issue for full audit report
2. Review each commit
3. Approve or request changes

---
🤖 Generated by thesis_audit_loop.sh
EOF
)" \
        --base main \
        --head "$BRANCH_NAME")

    # Return to main
    git checkout main
    [[ "$STASHED" == "true" ]] && git stash pop

    success "Audit complete!"
    echo ""
    echo "  📋 Issue: $ISSUE_URL"
    echo "  🔀 PR: $PR_URL"
    echo "  📁 Log: $ISSUE_FILE"
    echo ""
    echo "Review the PR when ready, then merge or close."
}

# Handle arguments
case "${1:-}" in
    --schedule)
        # Default: every 3 hours for crunch time
        install_schedule 10800
        ;;
    --hourly)
        install_schedule 3600
        ;;
    --daily)
        install_schedule 86400
        ;;
    --unschedule)
        uninstall_schedule
        ;;
    --help|-h)
        echo "Usage: $0 [OPTIONS]"
        echo ""
        echo "Options:"
        echo "  (none)        Run audit once"
        echo "  --schedule    Every 3 hours (crunch mode - DEFAULT)"
        echo "  --hourly      Every hour (intensive)"
        echo "  --daily       Every 24 hours (maintenance)"
        echo "  --unschedule  Remove schedule"
        echo "  --help        Show this help"
        echo ""
        echo "For submission crunch: ./thesis_audit_loop.sh --schedule"
        ;;
    *)
        run_audit
        ;;
esac
