# Cross-Thread Literature Synthesis

*Mobility as Social Service: synthesis across Engineering/Safety, Equity, Participatory Method, and Food Justice threads.*
*82 papers across all four threads: 17 Engineering/Safety (Amy, Saanvi), 39 Equity (Shashi, Aditya), 11 Participatory Method (Mariya), 15 Food Justice (Joy, Crystal).*

The presentable version of this report is `final_report.docx`, which also preserves the yellow highlights added by hand to an earlier 3-thread review pass (see `highlighted_spans.py` for the exact preserved phrases). This file is the git-tracked plain-text companion; see `outputs/` for the source PNGs.

## The Thesis

> Autonomous vehicles are not simply transportation vehicles but infrastructure, yet they typically arrive in communities without those communities' input, carrying efficiency-driven values inherited from transportation engineering. In this case study, drawing on six co-design workshops with food pantry users, volunteers, system-level stakeholders, and experts, in which a speculative AV provocation surfaced how participants reasoned about mobility, we find that these efficiency-driven values are misaligned with the community concerns, equitable access, relational trust, flexibility for variable need, that actually govern mobility in this context. This misalignment reflects a broader pattern in how infrastructure-scale technologies arrive in communities without their participation in shaping what the technology is for. This paper introduces Mobility as Social Service, a concept grounded in this data that reframes mobility as an ongoing, relational practice of equitable provisioning, and offers concrete implications for designing AV-related infrastructure in social service contexts.

## Cross-Cutting Mechanisms: Narrative Synthesis

See `synthesis_narrative.md` for the full seven-paragraph synthesis, reproduced in full inside `final_report.docx`:

1. Participation without power transfer (4 threads)
2. Trust reduced to a calibratable metric (3 threads: Engineering/Safety, Equity, Participatory Method)
3. Efficiency optimization crowds out purpose (4 threads)
4. Credentialed experts centered, communities counted (4 threads)
5. Friction as signal, not noise (4 threads)
6. Community-led alternatives outperform agency defaults (3 threads: Equity, Participatory Method, Food Justice)
7. Dignity as a designable, structural property (2 threads: Equity, Food Justice), new, unlocked only once the Food Justice thread was added

## Visuals

- `outputs/radar_chart.png`: Share of each thread's papers giving DIRECT support to each of the 7 thesis clauses, now with a 4th line for Food Justice.
- `outputs/mechanism_heatmap.png`: Count of papers per mechanism per thread, now 7 rows x 4 columns.
- `outputs/who_is_centered.png`: Who is centered, by thread. Food Justice splits roughly 47% community members / 53% researchers synthesizing literature; both Participatory Method's and Food Justice's buckets are inferred from Central claim/Relevance text, since neither tracker has a Who-is-centered column.
- `outputs/timeline.png` (optional): Publication year by thread, now with Food Justice's 2017-2026 range added.

Color note: the 4th thread (Food Justice) uses the dataviz skill's documented fixed-order yellow slot, validated with the skill's checker for adjacent-pair CVD safety (radar lines, heatmap, stacked bar) in both light and dark modes. The timeline is a scatter, where the skill's checker confirms no 4th hue holds up under an all-pairs read; kept anyway because thread identity there is already carried redundantly by row position and the y-axis label, not by hue alone.

## Thesis-Clause Summary

Percent of each thread's papers giving DIRECT support to each clause. Full per-paper detail in `thesis_clause_matrix.csv`; counts in `thesis_clause_summary.csv`.

| Thesis clause | Engineering/Safety (n=17) | Equity (n=39) | Participatory Method (n=11) | Food Justice (n=15) |
|---|---|---|---|---|
| 1. AVs are infrastructure, not simply transportation vehicles | 35% | 3% | 9% | 0% |
| 2. Infrastructure-scale technology typically arrives in communities without their input | 12% | 59% | 27% | 40% |
| 3. AVs carry efficiency-driven values inherited from transportation engineering | 71% | 23% | 9% | 13% |
| 4. Community concerns actually govern mobility in this context | 0% | 82% | 73% | 80% |
| 5. Efficiency-driven values are misaligned with those community concerns | 6% | 82% | 27% | 47% |
| 6. This misalignment reflects a broader pattern, not a one-off AV problem | 0% | 85% | 9% | 53% |
| 7. Mobility as Social Service: ongoing, relational, equitable provisioning | 0% | 13% | 18% | 27% |

## Gaps

**Thinnest clauses overall (all 82 papers pooled):** clause 1 (AVs as infrastructure, 9.8% direct / 23.2% direct-or-partial) and clause 7 (Mobility as Social Service, 13.4% direct / 43.9% direct-or-partial). Both improved slightly after Food Justice was added (clause 7's direct-or-partial rose from 38.8% to 43.9%, mostly on the strength of the dignity literature) but neither closed. Expected rather than alarming: clause 1 is AV-specific and 61 of 82 papers (Equity plus Food Justice) are about existing, non-AV systems; clause 7 is the paper's own new concept, which existing literature was not written to evidence. Both clauses will still need to lean on the paper's own workshop data. Strongest existing anchors: Engineering/Safety for clause 1 (35% partial-or-direct); Karner et al. (2020) and Wander et al. (2026) from Equity plus Prost et al. (2018), Heitlinger et al. (2021), and Brenton et al. (2025) from Food Justice for clause 7.

**Mechanisms in fewer than 4 threads:** Trust reduced to a calibratable metric has no Food Justice support (no paper there frames trust itself as a metric to calibrate, so none was forced in). Community-led alternatives outperform agency defaults still has zero Engineering/Safety support, likely reflecting what that sub-field studies rather than a screening gap, worth a quick check with Amy and Saanvi. Dignity as a designable, structural property, the mechanism Food Justice unlocked, currently has only Equity and Food Justice support; worth watching whether the paper's own food-pantry workshop data eventually supplies a third thread's worth of direct evidence.

**Highlighted-content preservation:** the user's manual yellow highlights from the prior 3-thread review pass (20 phrases across mechanisms 1-6) were preserved verbatim in the updated paragraph text and re-applied in `final_report.docx`; see `highlighted_spans.py` for the exact list.

**Workbook highlight (Food Justice source, unresolved):** 6 of the 14 rows in the Food Justice source workbook's main sheet are shaded cream in the original file; the user clarified this question was about the docx highlights, not the source workbook, so the meaning of that xlsx shading is still unconfirmed. It is carried forward as a `WorkbookHighlighted` boolean column on the Food Justice frame in `thread_frames.pkl` rather than silently dropped, in case it turns out to matter later.

## Deliverables

- [x] `unified_lit_review.csv` (82 rows)
- [x] `mechanisms.json` (7 mechanisms)
- [x] `thesis_clause_matrix.csv` (82 rows)
- [x] `thesis_clause_summary.csv` (28 rows: 7 clauses x 4 threads)
- [x] `synthesis_narrative.md` (7 paragraphs)
- [x] `outputs/radar_chart.png`
- [x] `outputs/mechanism_heatmap.png`
- [x] `outputs/who_is_centered.png`
- [x] `outputs/timeline.png` (optional, included)
- [x] `final_report.md` (this file)
- [x] `final_report.docx` (presentable deliverable, with highlights preserved)
