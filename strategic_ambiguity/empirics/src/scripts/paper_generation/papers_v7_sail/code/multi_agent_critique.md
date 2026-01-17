# Multi-Agent Critique Workflow

## Quick Reference Prompt

```
make [N] agents with [EXPERTISE] and critique capability and quickly roam around
the [ARTIFACTS] in [PATH] to elicit [M] critiques. based on the gathered critiques
across each agent, list top [K] and update them to enhance [QUALITY_CRITERIA]
```

## Proven Configurations

### Figure Design Audit (Thesis)
```
make 10 agents with world class figure designer and critique capability and quickly
roam around the figures in ./img to elicit 100 critiques. list top 20 and update
them to enhance consistency and data ink ratio
```

### Code Security Review
```
make 8 agents with senior security engineer and audit capability and quickly roam
around the source files in ./src to elicit 80 security concerns. list top 15 and
fix them to enhance OWASP compliance
```

### Documentation Quality
```
make 6 agents with technical writer and clarity assessment capability and quickly
roam around the docs in ./docs to elicit 60 readability issues. list top 12 and
update them to enhance beginner-friendliness
```

### API Design Review
```
make 8 agents with API architect and REST convention audit capability and quickly
roam around the endpoints in ./routes to elicit 80 design issues. list top 16 and
fix them to enhance consistency and discoverability
```

## Parameter Tuning Guide

| Parameter | Range | Notes |
|-----------|-------|-------|
| N (agents) | 5-15 | More = diverse perspectives, diminishing returns >15 |
| M (total critiques) | N × 10 | ~10 critiques per agent is sustainable |
| K (top items) | M × 0.2 | Act on top 20% for impact |

## Quality Criteria Examples

| Domain | Criteria |
|--------|----------|
| Figures | consistency, data ink ratio, color semantics, accessibility |
| Code | maintainability, test coverage, SOLID principles |
| Docs | completeness, accuracy, beginner-friendliness |
| API | RESTfulness, consistency, versioning, error handling |

## Output Artifacts

When running this workflow, expect:
1. **Style guide** - Unified standards (e.g., `thesis_figure_style.py`)
2. **Fix script** - Automated corrections (e.g., `fix_critical_figures.py`)
3. **Consolidated list** - Top K prioritized issues
4. **Updated artifacts** - Fixed figures/code/docs

## GitHub Issue Reference
https://github.com/hyunjimoon/tolzul/issues/22
