#!/bin/bash
#
# Thesis Data Validation Test Runner
# ==================================
#
# Runs all data integrity tests and generates a report.
#
# Usage:
#   ./run_tests.sh              # Run all tests
#   ./run_tests.sh --json       # Output as JSON
#   ./run_tests.sh --verbose    # Verbose mode
#   ./run_tests.sh --quick      # Quick validation (subset)
#
# Exit codes:
#   0 = All tests passed
#   1 = Error-level tests failed
#   2 = Critical tests failed
#

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../../.." && pwd)"
PYTHON="/opt/homebrew/bin/python3.11"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_DIR="$SCRIPT_DIR/logs"
REPORT_FILE="$LOG_DIR/test_report_$TIMESTAMP.txt"
JSON_FILE="$LOG_DIR/test_report_$TIMESTAMP.json"

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parse arguments
VERBOSE=""
JSON_OUTPUT=""
QUICK_MODE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --verbose|-v)
            VERBOSE="--verbose"
            shift
            ;;
        --json|-j)
            JSON_OUTPUT="--json-output"
            shift
            ;;
        --quick|-q)
            QUICK_MODE="1"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Create log directory
mkdir -p "$LOG_DIR"

# Header
echo -e "${BLUE}======================================${NC}"
echo -e "${BLUE}  THESIS DATA VALIDATION TEST SUITE  ${NC}"
echo -e "${BLUE}======================================${NC}"
echo ""
echo "Timestamp: $(date)"
echo "Python: $PYTHON"
echo "Log directory: $LOG_DIR"
echo ""

# Check Python
if [ ! -f "$PYTHON" ]; then
    echo -e "${RED}ERROR: Python not found at $PYTHON${NC}"
    exit 1
fi

# Check data files exist
echo -e "${BLUE}Checking data files...${NC}"
DATA_DIR="$REPO_ROOT/data/processed"

if [ ! -f "$DATA_DIR/thesis_panel_v3.nc" ]; then
    echo -e "${RED}ERROR: thesis_panel_v3.nc not found${NC}"
    exit 1
fi

if [ ! -f "$DATA_DIR/vagueness_timeseries.parquet" ]; then
    echo -e "${RED}ERROR: vagueness_timeseries.parquet not found${NC}"
    exit 1
fi

if [ ! -f "$DATA_DIR/features_all.parquet" ]; then
    echo -e "${RED}ERROR: features_all.parquet not found${NC}"
    exit 1
fi

echo -e "${GREEN}All data files found${NC}"
echo ""

# Run tests
echo -e "${BLUE}Running data integrity tests...${NC}"
echo ""

if [ -n "$JSON_OUTPUT" ]; then
    $PYTHON "$SCRIPT_DIR/test_data_integrity.py" $VERBOSE $JSON_OUTPUT > "$JSON_FILE" 2>&1
    EXIT_CODE=$?
    cat "$JSON_FILE"
else
    $PYTHON "$SCRIPT_DIR/test_data_integrity.py" $VERBOSE 2>&1 | tee "$REPORT_FILE"
    EXIT_CODE=${PIPESTATUS[0]}
fi

echo ""

# Summary
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}======================================${NC}"
    echo -e "${GREEN}  ALL TESTS PASSED                   ${NC}"
    echo -e "${GREEN}======================================${NC}"
elif [ $EXIT_CODE -eq 1 ]; then
    echo -e "${YELLOW}======================================${NC}"
    echo -e "${YELLOW}  TESTS FAILED (ERROR LEVEL)         ${NC}"
    echo -e "${YELLOW}======================================${NC}"
else
    echo -e "${RED}======================================${NC}"
    echo -e "${RED}  TESTS FAILED (CRITICAL)            ${NC}"
    echo -e "${RED}======================================${NC}"
fi

echo ""
echo "Report saved to: $REPORT_FILE"
echo ""

exit $EXIT_CODE
