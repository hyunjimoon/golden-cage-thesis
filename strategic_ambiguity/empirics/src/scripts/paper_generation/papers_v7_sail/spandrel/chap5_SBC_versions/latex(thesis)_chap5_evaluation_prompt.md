# Ch5 Cross-Evaluation Prompt

## Task
Evaluate the following 4 versions of Chapter 5 and rank them from best (1) to worst (4).

## Evaluation Criteria (score 1-5 each)
- **C1 (Flow)**: Logical progression between sections, smooth transitions
- **C2 (Practitioner Utility)**: Actionable guidance for founders/investors
- **C3 (Three Principles Clarity)**: Clear distinction between What/How to grow/How to fund
- **C4 (Fast Ion Integration)**: How well the Fast Ion case illustrates the "sequence matters" lesson
- **C5 (Prose Quality)**: Simple language, minimal bullet points, readable paragraphs

## Versions to Evaluate

### Version A (Claude)
- Introduction explains three decisions in prose paragraphs
- Fast Ion case: emphasizes "sequence matters" lesson
- Funding Ladder explained as three rungs in prose
- Conclusion summarizes each principle with its key case

### Version B (DeepSeek)
- Introduction uses enumerate list for three decisions
- Fast Ion case: included with sequence lesson
- Uses more bullet points (itemize/enumerate)
- Concise conclusion with What/How/Fund framing

### Version C (Gemini)
- Introduction: most reader-friendly explanation
- Fast Ion case: strongest emphasis on "governance design" implication
- Best narrative flow and transitions
- Most detailed boundary conditions in conclusion

### Version D (Synthesized)
- Combines: Gemini's narrative flow + Claude's prose style + DeepSeek's conciseness
- Introduction: three decisions in flowing prose
- Fast Ion: emphasizes sequence + governance homogeneity
- Balanced use of tables and prose
- Comprehensive conclusion with boundary conditions

## Your Output Format

| Criterion | A (Claude) | B (DeepSeek) | C (Gemini) | D (Synthesized) |
|:--|:--:|:--:|:--:|:--:|
| C1 Flow | /5 | /5 | /5 | /5 |
| C2 Practitioner | /5 | /5 | /5 | /5 |
| C3 Three Principles | /5 | /5 | /5 | /5 |
| C4 Fast Ion | /5 | /5 | /5 | /5 |
| C5 Prose | /5 | /5 | /5 | /5 |
| **Total** | /25 | /25 | /25 | /25 |

**Ranking**: 1st: _, 2nd: _, 3rd: _, 4th: _

**Brief justification** (2-3 sentences):
