#!/bin/bash
#
# 🎼 THESIS GENERATION PIPELINE - One Touch Execution
# ═══════════════════════════════════════════════════
#
# Usage:
#   ./run_thesis_pipeline.sh              # Full pipeline
#   ./run_thesis_pipeline.sh --quick      # Skip Stage 1 (use cached vagueness)
#   ./run_thesis_pipeline.sh --figures    # Only regenerate figures
#   ./run_thesis_pipeline.sh --dashboard  # Launch dashboard only
#
# Author: Claude Code
# Date: 2025-12-20

set -e  # Exit on error

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
SRC_DIR="$REPO_ROOT/src"
PAPERS_DIR="$SRC_DIR/scripts/paper_generation/papers_v3"
DATA_DIR="$REPO_ROOT/data"
LOG_DIR="$REPO_ROOT/logs"
PYTHON="/opt/homebrew/bin/python3.11"

# Pipeline state file for dashboard
STATE_FILE="$REPO_ROOT/.pipeline_state.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ═══════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

log_stage() {
    local stage=$1
    local status=$2
    local message=$3

    case $status in
        "start")
            echo -e "\n${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${CYAN}║${NC} ${YELLOW}STAGE $stage${NC}: $message"
            echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
            update_state "$stage" "running" "$message"
            ;;
        "done")
            echo -e "${GREEN}✓${NC} Stage $stage complete: $message"
            update_state "$stage" "complete" "$message"
            ;;
        "skip")
            echo -e "${BLUE}⏭${NC} Stage $stage skipped: $message"
            update_state "$stage" "skipped" "$message"
            ;;
        "fail")
            echo -e "${RED}✗${NC} Stage $stage failed: $message"
            update_state "$stage" "failed" "$message"
            ;;
    esac
}

update_state() {
    local stage=$1
    local status=$2
    local message=$3
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Create or update state file
    if [ ! -f "$STATE_FILE" ]; then
        echo '{"stages": {}, "last_run": null}' > "$STATE_FILE"
    fi

    # Update using Python for proper JSON handling
    $PYTHON -c "
import json
from pathlib import Path

state_file = Path('$STATE_FILE')
state = json.loads(state_file.read_text())
state['stages']['$stage'] = {
    'status': '$status',
    'message': '$message',
    'timestamp': '$timestamp'
}
state['last_run'] = '$timestamp'
state_file.write_text(json.dumps(state, indent=2))
"
}

check_python() {
    if ! command -v $PYTHON &> /dev/null; then
        echo -e "${RED}Error: Python 3.11 not found at $PYTHON${NC}"
        echo "Please install Python 3.11 or update PYTHON path in this script"
        exit 1
    fi
}

check_dependencies() {
    echo -e "${CYAN}Checking dependencies...${NC}"
    $PYTHON -c "import pandas, numpy, xarray, scipy, matplotlib" 2>/dev/null || {
        echo -e "${RED}Missing Python dependencies. Run: pip install pandas numpy xarray scipy matplotlib${NC}"
        exit 1
    }
    echo -e "${GREEN}✓${NC} All dependencies available"
}

# ═══════════════════════════════════════════════════════════════════════════
# PIPELINE STAGES
# ═══════════════════════════════════════════════════════════════════════════

stage_0_init() {
    log_stage 0 "start" "Initializing pipeline"

    # Create log directory
    mkdir -p "$LOG_DIR"

    # Initialize state
    echo '{
        "stages": {
            "0": {"status": "complete", "message": "Initialized"},
            "1": {"status": "pending", "message": "Vagueness scoring"},
            "2": {"status": "pending", "message": "Panel construction"},
            "3": {"status": "pending", "message": "Statistical analysis"},
            "4": {"status": "pending", "message": "Figure generation"},
            "5": {"status": "pending", "message": "Narrative assembly"},
            "6": {"status": "pending", "message": "PDF compilation"}
        },
        "last_run": "'$(date -u +"%Y-%m-%dT%H:%M:%SZ")'"
    }' > "$STATE_FILE"

    check_python
    check_dependencies

    log_stage 0 "done" "Pipeline initialized"
}

stage_1_vagueness() {
    log_stage 1 "start" "Computing vagueness scores (Description + Keywords)"

    cd "$REPO_ROOT"
    $PYTHON "$SRC_DIR/scripts/build_vagueness_timeseries.py" 2>&1 | tee "$LOG_DIR/stage1_vagueness.log"

    if [ -f "$DATA_DIR/processed/vagueness_timeseries.parquet" ]; then
        log_stage 1 "done" "vagueness_timeseries.parquet created"
    else
        log_stage 1 "fail" "Output file not created"
        exit 1
    fi
}

stage_2_panel() {
    log_stage 2 "start" "Building thesis panel (N=180,994)"

    cd "$REPO_ROOT"
    $PYTHON "$PAPERS_DIR/_shared/generate_thesis_nc_files.py" 2>&1 | tee "$LOG_DIR/stage2_panel.log"

    if [ -f "$DATA_DIR/processed/thesis_panel_v3.nc" ]; then
        log_stage 2 "done" "thesis_panel_v3.nc created"
    else
        log_stage 2 "fail" "Output file not created"
        exit 1
    fi
}

stage_3_stats() {
    log_stage 3 "start" "Computing statistics from data"

    cd "$REPO_ROOT"
    $PYTHON "$PAPERS_DIR/_shared/compute_thesis_stats.py" 2>&1 | tee "$LOG_DIR/stage3_stats.log"

    if [ -f "$REPO_ROOT/.thesis_stats.json" ]; then
        log_stage 3 "done" "Statistics saved to .thesis_stats.json (NO HARD-CODING!)"
    else
        log_stage 3 "fail" ".thesis_stats.json not created"
        exit 1
    fi
}

stage_4_figures() {
    log_stage 4 "start" "Generating thesis figures"

    cd "$REPO_ROOT"

    # Main thesis plots
    echo -e "${CYAN}  [4a] Main thesis plots...${NC}"
    $PYTHON "$PAPERS_DIR/generate_thesis_plots.py" 2>&1 | tee "$LOG_DIR/stage4a_plots.log"

    # Module T figures
    echo -e "${CYAN}  [4b] Module T figures...${NC}"
    $PYTHON "$PAPERS_DIR/4_T_commit2trap/generate_figures.py" 2>&1 | tee "$LOG_DIR/stage4b_T_figures.log"

    # Yearly decomposition figures
    echo -e "${CYAN}  [4c] Yearly decomposition figures...${NC}"
    $PYTHON "$PAPERS_DIR/4_T_commit2trap/generate_figures_by_year.py" 2>&1 | tee "$LOG_DIR/stage4c_yearly.log"

    # Count generated figures
    FIGURE_COUNT=$(find "$PAPERS_DIR" -name "fig_*.png" | wc -l | tr -d ' ')
    log_stage 4 "done" "$FIGURE_COUNT figures generated"
}

stage_5_narrative() {
    log_stage 5 "start" "Assembling narrative (113 lines)"

    # Check TOC files exist
    TOC_COUNT=$(find "$PAPERS_DIR" -name "toc*.md" | wc -l | tr -d ' ')

    if [ "$TOC_COUNT" -ge 5 ]; then
        log_stage 5 "done" "$TOC_COUNT TOC files ready"
    else
        log_stage 5 "skip" "Manual assembly required"
    fi
}

stage_6_pdf() {
    log_stage 6 "start" "Compiling PDF (requires pandoc)"

    # Check if pandoc is available
    if command -v pandoc &> /dev/null; then
        echo -e "${YELLOW}  PDF compilation not yet implemented${NC}"
        log_stage 6 "skip" "Future implementation"
    else
        log_stage 6 "skip" "pandoc not installed"
    fi
}

# ═══════════════════════════════════════════════════════════════════════════
# DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════

launch_dashboard() {
    log_stage "D" "start" "Launching pipeline dashboard"

    # Create dashboard HTML
    $PYTHON << 'DASHBOARD_SCRIPT'
import json
import webbrowser
from pathlib import Path
from datetime import datetime
import http.server
import socketserver
import threading

REPO_ROOT = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics")
STATE_FILE = REPO_ROOT / ".pipeline_state.json"
DASHBOARD_FILE = REPO_ROOT / ".pipeline_dashboard.html"

# Read state
if STATE_FILE.exists():
    state = json.loads(STATE_FILE.read_text())
else:
    state = {"stages": {}, "last_run": None}

# Generate dashboard HTML
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="5">
    <title>Thesis Pipeline Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #fff;
            padding: 2rem;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 2rem;
        }
        .pipeline {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 2rem;
            overflow-x: auto;
            padding: 1rem 0;
        }
        .stage {
            flex: 1;
            min-width: 150px;
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            position: relative;
            transition: all 0.3s ease;
        }
        .stage:hover { transform: translateY(-5px); }
        .stage::after {
            content: '→';
            position: absolute;
            right: -1rem;
            top: 50%;
            transform: translateY(-50%);
            color: #444;
            font-size: 1.5rem;
        }
        .stage:last-child::after { display: none; }
        .stage-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        .stage-name {
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .stage-status {
            font-size: 0.85rem;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            display: inline-block;
        }
        .pending { background: #444; }
        .running {
            background: linear-gradient(90deg, #f39c12, #e74c3c);
            animation: pulse 1.5s infinite;
        }
        .complete { background: #27ae60; }
        .failed { background: #e74c3c; }
        .skipped { background: #7f8c8d; }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        .ink-effect {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 200px;
            background: linear-gradient(to top,
                rgba(0,212,255,0.3) 0%,
                rgba(123,44,191,0.2) 50%,
                transparent 100%);
            animation: ink-spread 3s ease-out forwards;
            pointer-events: none;
        }
        @keyframes ink-spread {
            0% { height: 0; opacity: 0; }
            100% { height: 200px; opacity: 1; }
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }
        .stat-card {
            background: rgba(255,255,255,0.05);
            border-radius: 8px;
            padding: 1rem;
            text-align: center;
        }
        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            color: #00d4ff;
        }
        .stat-label { color: #888; font-size: 0.9rem; }
        .last-run {
            text-align: center;
            color: #666;
            margin-top: 2rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎼 Thesis Pipeline Dashboard</h1>
        <p class="subtitle">Raw Data → Statistics → Plots → 113 Lines → PDF</p>

        <div class="pipeline">
'''

stages_config = [
    ("0", "📦", "INIT", "Initialize"),
    ("1", "🔍", "VAGUE", "Vagueness Scoring"),
    ("2", "📊", "PANEL", "Panel Build"),
    ("3", "📈", "STATS", "Statistics"),
    ("4", "🎨", "PLOTS", "Figures"),
    ("5", "📝", "NARR", "Narrative"),
    ("6", "📄", "PDF", "Compile")
]

for stage_id, icon, name, label in stages_config:
    stage_state = state.get("stages", {}).get(stage_id, {"status": "pending", "message": label})
    status = stage_state.get("status", "pending")
    message = stage_state.get("message", label)

    html += f'''
            <div class="stage">
                <div class="stage-icon">{icon}</div>
                <div class="stage-name">{name}</div>
                <div class="stage-status {status}">{status.upper()}</div>
            </div>
'''

html += '''
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">180,994</div>
                <div class="stat-label">Companies in Panel</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">113</div>
                <div class="stat-label">Thesis Lines</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">-0.196</div>
                <div class="stat-label">ρ(G,E) Capital Paradox</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">4</div>
                <div class="stat-label">Mover Archetypes</div>
            </div>
        </div>
'''

last_run = state.get("last_run", "Never")
html += f'''
        <p class="last-run">Last updated: {last_run}</p>
    </div>
    <div class="ink-effect"></div>
</body>
</html>
'''

DASHBOARD_FILE.write_text(html)
print(f"Dashboard saved to: {DASHBOARD_FILE}")

# Open in browser
webbrowser.open(f"file://{DASHBOARD_FILE}")
print("Dashboard opened in browser")
DASHBOARD_SCRIPT

    echo -e "${GREEN}✓${NC} Dashboard launched"
}

# ═══════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════

print_summary() {
    echo -e "\n${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${NC}                   ${GREEN}PIPELINE COMPLETE${NC}                          ${CYAN}║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"

    echo -e "\n${YELLOW}Generated Files:${NC}"
    echo -e "  📊 Data:    $DATA_DIR/processed/thesis_panel_v3.nc"
    echo -e "  🎨 Figures: $(find "$PAPERS_DIR" -name "fig_*.png" | wc -l | tr -d ' ') PNG files"
    echo -e "  📝 TOCs:    $(find "$PAPERS_DIR" -name "toc*.md" | wc -l | tr -d ' ') markdown files"
    echo -e "  📋 Logs:    $LOG_DIR/"

    # Read statistics from computed JSON (NO HARD-CODING!)
    echo -e "\n${YELLOW}Key Statistics (from .thesis_stats.json):${NC}"
    if [ -f "$REPO_ROOT/.thesis_stats.json" ]; then
        $PYTHON << 'STATS_SCRIPT'
import json
from pathlib import Path

stats_file = Path("/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/.thesis_stats.json")
if stats_file.exists():
    stats = json.loads(stats_file.read_text())
    print(f"  N = {stats['N_total']:,} companies")
    print(f"  ρ(G, E) = {stats['rho_G_E']:+.3f}{stats['rho_G_E_sig']} (Funding Paradox)")
    print(f"  ρ(A, E) = {stats['rho_A_E']:+.3f}{stats['rho_A_E_sig']} (Fund2Cage)")
    print(f"  ρ(G, A) = {stats['rho_G_A']:+.3f}{stats['rho_G_A_sig']} (Adaptation→Growth)")
    print(f"  Movement advantage: {stats['movement_advantage']}× (moved={stats['success_rate_moved']:.1f}%, stayed={stats['success_rate_stayed']:.1f}%)")
else:
    print("  [Warning: .thesis_stats.json not found - run compute_thesis_stats.py]")
STATS_SCRIPT
    else
        echo -e "  ${RED}[Warning: .thesis_stats.json not found]${NC}"
        echo -e "  Run: python3.11 $PAPERS_DIR/_shared/compute_thesis_stats.py"
    fi

    echo -e "\n${YELLOW}Next Steps:${NC}"
    echo -e "  1. Review figures in papers_v3/*/fig_*.png"
    echo -e "  2. Update toc(x).md narratives if needed"
    echo -e "  3. Run: ./run_thesis_pipeline.sh --dashboard"

    echo -e "\n${GREEN}Done!${NC} Total time: $SECONDS seconds"
}

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

main() {
    local mode="${1:-full}"

    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║        🎼 THESIS GENERATION PIPELINE 🎼                      ║"
    echo "║     Raw Data → Statistics → Plots → 113 Lines → PDF         ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"

    case $mode in
        "--quick"|"-q")
            echo -e "${YELLOW}Quick mode: Skipping vagueness scoring${NC}"
            stage_0_init
            # Skip stage 1
            log_stage 1 "skip" "Using cached vagueness_timeseries.parquet"
            stage_2_panel
            stage_3_stats
            stage_4_figures
            stage_5_narrative
            stage_6_pdf
            print_summary
            launch_dashboard
            ;;
        "--figures"|"-f")
            echo -e "${YELLOW}Figures only mode${NC}"
            stage_0_init
            stage_4_figures
            print_summary
            launch_dashboard
            ;;
        "--dashboard"|"-d")
            launch_dashboard
            ;;
        "--help"|"-h")
            echo "Usage: ./run_thesis_pipeline.sh [OPTION]"
            echo ""
            echo "Options:"
            echo "  (none)      Full pipeline execution"
            echo "  --quick     Skip Stage 1 (use cached vagueness)"
            echo "  --figures   Only regenerate figures (Stage 4)"
            echo "  --dashboard Launch dashboard only"
            echo "  --help      Show this help"
            ;;
        *)
            # Full pipeline
            stage_0_init
            stage_1_vagueness
            stage_2_panel
            stage_3_stats
            stage_4_figures
            stage_5_narrative
            stage_6_pdf
            print_summary
            launch_dashboard
            ;;
    esac
}

main "$@"
