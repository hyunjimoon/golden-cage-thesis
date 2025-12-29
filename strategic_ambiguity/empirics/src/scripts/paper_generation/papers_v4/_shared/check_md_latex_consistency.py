#!/usr/bin/env python3
"""
md vs latex 일관성 점검 스크립트
Usage: python check_md_latex_consistency.py
"""

import re
from pathlib import Path

# 경로 설정
BASE = Path(__file__).parent.parent
MD_DIR = BASE
LATEX_DIR = BASE / "latex"

# 점검할 핵심 요소
KEY_STATS = {
    "correlation": r"[ρρ]\s*\(?G,?\s*F\)?\s*=\s*-?[\d.]+",
    "p_value": r"p\s*[<>=]\s*[\d.]+",
    "sample_size": r"N\s*=\s*[\d,]+",
    "mover_survival": r"18[\d.]*%",
    "stayer_survival": r"9[\d.]*%",
    "mover_advantage": r"1\.8[0-9]*[×x]",
    "zoom_in": r"17[\d.]*%",
    "zoom_out": r"18[\d.]*%",
}

KEY_CITATIONS = [
    "Van den Steen",
    "Porter",
    "Ghemawat",
    "Camuffo",
    "Gans",
    "Stern",
    "Spence",
    "Agrawal",
]

def extract_stats(text, patterns):
    """텍스트에서 통계 추출"""
    results = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        results[name] = matches if matches else ["NOT FOUND"]
    return results

def extract_citations(text, names):
    """텍스트에서 인용 추출"""
    results = {}
    for name in names:
        # 다양한 형식 검색
        patterns = [
            rf"{name}\s*\(\d{{4}}\)",  # Name (YEAR)
            rf"\\citet{{\s*{name.lower()}\d*\s*}}",  # \citet{name}
            rf"\\citep{{\s*{name.lower()}\d*\s*}}",  # \citep{name}
            rf"\({name}[^)]*\d{{4}}\)",  # (Name et al., YEAR)
        ]
        found = False
        for p in patterns:
            if re.search(p, text, re.IGNORECASE):
                found = True
                break
        results[name] = "✓" if found else "✗"
    return results

def compare_files(md_path, latex_path):
    """두 파일 비교"""
    md_text = md_path.read_text() if md_path.exists() else ""
    latex_text = latex_path.read_text() if latex_path.exists() else ""

    print(f"\n{'='*60}")
    print(f"비교: {md_path.name} vs {latex_path.name}")
    print('='*60)

    # 통계 비교
    print("\n📊 핵심 통계:")
    md_stats = extract_stats(md_text, KEY_STATS)
    latex_stats = extract_stats(latex_text, KEY_STATS)

    for stat in KEY_STATS:
        md_val = md_stats[stat][0] if md_stats[stat] else "N/A"
        latex_val = latex_stats[stat][0] if latex_stats[stat] else "N/A"
        match = "✓" if md_val == latex_val else "⚠️"
        print(f"  {stat:20} | md: {md_val:15} | tex: {latex_val:15} | {match}")

    # 인용 비교
    print("\n📚 인용:")
    md_cites = extract_citations(md_text, KEY_CITATIONS)
    latex_cites = extract_citations(latex_text, KEY_CITATIONS)

    for name in KEY_CITATIONS:
        md_val = md_cites[name]
        latex_val = latex_cites[name]
        match = "✓" if md_val == latex_val else "⚠️"
        print(f"  {name:20} | md: {md_val} | tex: {latex_val} | {match}")

def main():
    print("🔍 md vs latex 일관성 점검")
    print("="*60)

    # I module
    compare_files(
        MD_DIR / "1_I_introduction" / "I1.md",
        LATEX_DIR / "introduction.tex"
    )

    # M module
    compare_files(
        MD_DIR / "2_M_movement" / "MG.md",
        LATEX_DIR / "paper_M.tex"
    )

    # V module
    compare_files(
        MD_DIR / "3_V_vagueness" / "VM.md",
        LATEX_DIR / "paper_V.tex"
    )

    print("\n" + "="*60)
    print("점검 완료. ⚠️ 표시 항목은 수동 확인 필요")

if __name__ == "__main__":
    main()
