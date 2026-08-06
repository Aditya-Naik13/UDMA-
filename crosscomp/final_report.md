# Cross-Thread Literature Synthesis

*Mobility as Social Service: synthesis across Engineering/Safety, Equity, and Participatory Method threads.*
*Food Justice thread skipped this pass. 67 papers: 17 Engineering/Safety (Amy, Saanvi), 39 Equity (Shashi, Aditya), 11 Participatory Method (Mariya).*

The presentable version of this report is `final_report.docx`. This file is the git-tracked plain-text companion; see `outputs/` for the source PNGs.

## The Thesis

> Autonomous vehicles are not simply transportation vehicles but infrastructure, yet they typically arrive in communities without those communities' input, carrying efficiency-driven values inherited from transportation engineering. In this case study, drawing on six co-design workshops with food pantry users, volunteers, system-level stakeholders, and experts, in which a speculative AV provocation surfaced how participants reasoned about mobility, we find that these efficiency-driven values are misaligned with the community concerns, equitable access, relational trust, flexibility for variable need, that actually govern mobility in this context. This misalignment reflects a broader pattern in how infrastructure-scale technologies arrive in communities without their participation in shaping what the technology is for. This paper introduces Mobility as Social Service, a concept grounded in this data that reframes mobility as an ongoing, relational practice of equitable provisioning, and offers concrete implications for designing AV-related infrastructure in social service contexts.

## Cross-Cutting Mechanisms: Narrative Synthesis

See `synthesis_narrative.md` for the full six-paragraph synthesis (Participation without power transfer; Trust reduced to a calibratable metric; Efficiency optimization crowds out purpose; Credentialed experts centered, communities counted; Friction as signal, not noise; Community-led alternatives outperform agency defaults), reproduced in full inside `final_report.docx`.

## Visuals

- `outputs/radar_chart.png`: Share of each thread's papers giving DIRECT support to each of the 7 thesis clauses.
- `outputs/mechanism_heatmap.png`: Count of papers per mechanism per thread.
- `outputs/who_is_centered.png`: Who is centered, by thread (Participatory Method's buckets are inferred from Central claim/Relevance text, since that thread's tracker has no Who-is-centered column).
- `outputs/timeline.png` (optional): Publication year by thread.

## Thesis-Clause Summary

Percent of each thread's papers giving DIRECT support to each clause. Full per-paper detail in `thesis_clause_matrix.csv`; counts in `thesis_clause_summary.csv`.

| Thesis clause | Engineering/Safety (n=17) | Equity (n=39) | Participatory Method (n=11) |
|---|---|---|---|
| 1. AVs are infrastructure, not simply transportation vehicles | 35% | 3% | 9% |
| 2. Infrastructure-scale technology typically arrives in communities without their input | 12% | 59% | 27% |
| 3. AVs carry efficiency-driven values inherited from transportation engineering | 71% | 23% | 9% |
| 4. Community concerns actually govern mobility in this context | 0% | 82% | 73% |
| 5. Efficiency-driven values are misaligned with those community concerns | 6% | 82% | 27% |
| 6. This misalignment reflects a broader pattern, not a one-off AV problem | 0% | 85% | 9% |
| 7. Mobility as Social Service: ongoing, relational, equitable provisioning | 0% | 13% | 18% |

## Gaps

**Thinnest clauses overall (all 67 papers pooled):** clause 1 (AVs as infrastructure, 11.9% direct / 26.9% direct-or-partial) and clause 7 (Mobility as Social Service, 10.4% direct / 38.8% direct-or-partial). Both are expected gaps rather than review failures: clause 1 is AV-specific and most of the corpus (the 39-paper Equity thread) is about existing, non-AV infrastructure; clause 7 is the paper's own new concept, which existing literature was not written to evidence. These two clauses will need to be carried primarily by the paper's own workshop data, not secondary literature. Strongest existing anchors if more support is needed: Engineering/Safety for clause 1 (35% partial-or-direct), and Karner et al. (2020) and Wander et al. (2026) for clause 7.

**Mechanisms in only 2 of 3 threads:** Community-led alternatives outperform agency defaults has zero Engineering/Safety support (that sub-field is almost entirely diagnostic, not solution-oriented). Worth a quick check with Amy and Saanvi in case a relevant paper was screened out rather than genuinely absent.

**Thread not yet included:** Food Justice (Joy, Crystal) was skipped this pass at the user's request. Given the paper's case study is set in a food pantry, adding that tracker and re-running Steps 1 to 6 is likely to shift the clause 4 and clause 7 numbers, and the mechanism list, more than any other single addition would.

## Deliverables

- [x] `unified_lit_review.csv`
- [x] `mechanisms.json`
- [x] `thesis_clause_matrix.csv`
- [x] `thesis_clause_summary.csv`
- [x] `synthesis_narrative.md`
- [x] `outputs/radar_chart.png`
- [x] `outputs/mechanism_heatmap.png`
- [x] `outputs/who_is_centered.png`
- [x] `outputs/timeline.png` (optional, included)
- [x] `final_report.md` (this file)
- [x] `final_report.docx` (presentable deliverable)
