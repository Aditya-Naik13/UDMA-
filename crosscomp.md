# Cross-Thread Literature Synthesis — Prompt for Claude Code

Paste everything below into Claude Code, after updating the four file paths
in Step 0 to match where your CSVs actually live.

---

## Context

This project has four independently-completed literature review trackers,
each covering a different thread of the same paper's argument. The paper's
thesis is:

> Autonomous vehicles are not simply transportation vehicles but
> infrastructure, yet they typically arrive in communities without those
> communities' input, carrying efficiency-driven values inherited from
> transportation engineering. In this case study, drawing on six co-design
> workshops with food pantry users, volunteers, system-level stakeholders,
> and experts, in which a speculative AV provocation surfaced how
> participants reasoned about mobility, we find that these efficiency-driven
> values are misaligned with the community concerns, equitable access,
> relational trust, flexibility for variable need, that actually govern
> mobility in this context. This misalignment reflects a broader pattern in
> how infrastructure-scale technologies arrive in communities without their
> participation in shaping what the technology is for. This paper
> introduces Mobility as Social Service, a concept grounded in this data
> that reframes mobility as an ongoing, relational practice of equitable
> provisioning, and offers concrete implications for designing AV-related
> infrastructure in social service contexts.

The four threads:

| Thread | Reviewer(s) | Focus |
|---|---|---|
| Engineering/Safety-dominant AV discourse | Amy, Saanvi | How AV development and HCI's AV literature have primarily framed the technology through efficiency, optimization, safety, and trust-in-automation metrics. Names specifically what's centered: engineers, regulators, urban planning, throughput/safety metrics. |
| Community/Equity dimensions of mobility and transportation infrastructure | Shashi, Aditya | Transportation equity and mobility justice literature showing mobility access has long been unevenly distributed, and infrastructure arriving without community participation has historical precedent of reproducing exclusion. |
| Food insecurity / food justice context | Joy, Crystal | Why food pantries specifically. Food justice literature (food apartheid, critiques of charity-model assistance, dignity and stigma in aid contexts) grounding why this site reveals justice-oriented mobility concerns distinctly. |
| Participatory/speculative design as method | Mariya | Why workshops plus a speculative AV provocation was the right approach to elicit values around a not-yet-present technology. |

## Hard rules (carry these through every step)

- **No fabrication.** Every claim, mechanism tag, and thesis-clause support
  tag must trace back to an actual row's actual text in one of the four
  CSVs. If a row is ambiguous or doesn't clearly support something, mark it
  "unclear" rather than forcing a tag.
- **No em dash (—) anywhere** in any generated text, chart label, or file.
  Use a comma, colon, period, or "and" instead.
- **Cite as (Author, Year)** inline in the narrative, pulled directly from
  each row's Author(s) and Year columns.
- **Tag thread + reviewer(s) on first mention of that thread within a
  paragraph**, not on every sentence, e.g. "...(Equity, Shashi & Aditya)"
  the first time that thread's evidence appears in a paragraph, then just
  cite normally after that.
- Paraphrase paper content in your own words; only use text already present
  in a "Quotable moment" style column as an actual quotation, and keep any
  such quote short and attributed to its source row.

---

## Step 0: Load the four CSVs

```python
import pandas as pd

files = {
    "Engineering/Safety": {
        "path": "PATH_TO/Engineering_Safety_dominant_AV_discourse.csv",
        "reviewers": "Amy, Saanvi",
    },
    "Equity": {
        "path": "PATH_TO/Community___Equity_Dimensions_of_Mobility_Literature_Review.csv",
        "reviewers": "Shashi, Aditya",
    },
    "Food Justice": {
        "path": "PATH_TO/Food_insecurity_food_justice_context.csv",
        "reviewers": "Joy, Crystal",
    },
    "Participatory Method": {
        "path": "PATH_TO/Participatory_speculative_design_as_method.csv",
        "reviewers": "Mariya",
    },
}
```

Load each with `pandas.read_csv` (or `read_excel` if it's an .xlsx), skipping
the title row if one exists (row 0 may be a merged section title rather than
real headers, check for this the same way the two-row tracker format works:
title row, then header row, then data). Tag each resulting dataframe with a
`Thread` and `Reviewers` column before combining.

## Step 1: Compute the shared column schema

Do NOT hardcode which columns are shared. Compute it:

```python
common_columns = set(df1.columns) & set(df2.columns) & set(df3.columns) & set(df4.columns)
```

Build `unified_df` using only `common_columns` plus `Thread` and
`Reviewers`. Report which columns were dropped from each thread (the
"extra" columns, e.g. the Equity tracker's 3 extra columns) so nothing is
silently lost, just excluded from the cross-thread comparison.

Save this as `unified_lit_review.csv`.

## Step 2: Identify cross-cutting mechanisms

Read every row's available text columns (Sub-theme, Central claim, Key
concepts or framework, Relevance to argument, Who is centered, at minimum).
Identify 4 to 6 recurring mechanisms, patterns of exclusion, values, or
framing, that show up under different vocabulary in **at least two
different threads**. Do not report a mechanism that only appears in one
thread, that's a thread-specific finding, not a cross-cutting one.

For each mechanism, produce:
- A short name (2-5 words)
- A 1-sentence definition
- The list of supporting papers, each tagged with Thread, Reviewers,
  Author(s), Year

Save as `mechanisms.json`, structured like:
```json
{
  "mechanisms": [
    {
      "name": "Participation without power transfer",
      "definition": "...",
      "papers": [
        {"thread": "Equity", "reviewers": "Shashi, Aditya", "author": "Karner et al.", "year": 2020}
      ]
    }
  ]
}
```

## Step 3: Thesis-clause support matrix

Break the thesis paragraph into these component clauses (edit wording
slightly if a cleaner split emerges from the actual data, but keep this
list as the starting point):

1. AVs are infrastructure, not simply transportation vehicles
2. Infrastructure-scale technology typically arrives in communities without their input
3. AVs carry efficiency-driven values inherited from transportation engineering
4. Community concerns (equitable access, relational trust, flexibility for variable need) actually govern mobility in this context
5. Efficiency-driven values are misaligned with those community concerns
6. This misalignment reflects a broader pattern, not a one-off AV problem
7. Mobility as Social Service: mobility as an ongoing, relational practice of equitable provisioning

For every row in `unified_df`, assess whether it supports each clause:
`"direct"`, `"partial"`, or `"none"`, with a one-line reason. Do this by
actually reading the row's Central claim and Relevance to argument, not by
keyword matching.

Save as `thesis_clause_matrix.csv` with one row per paper and one column
per clause (values: direct/partial/none), plus a summary table
`thesis_clause_summary.csv` counting direct/partial supports per clause per
thread.

## Step 4: Narrative synthesis

Write 4 to 6 short paragraphs (150 to 250 words each), one per mechanism
identified in Step 2 (or grouped where two mechanisms clearly belong
together). Each paragraph should:
- Name the mechanism and state it plainly
- Cite at least 2 papers from at least 2 different threads supporting it,
  as (Author, Year), tagging thread + reviewers on first mention per thread
- Explicitly connect the mechanism to the relevant thesis clause(s) from
  Step 3
- End with why this cross-thread convergence strengthens the argument
  (i.e., why finding the same pattern independently in, say, the equity
  literature and the food justice literature is stronger evidence than
  either alone)

Save as `synthesis_narrative.md`.

## Step 5: Visuals

Build these with matplotlib (static PNGs are fine unless noted). Save all
to an `outputs/` folder.

**5a. Spider/radar chart** (`radar_chart.png`)
Axes = the 7 thesis clauses from Step 3. One line per thread. Value per
axis = percentage of that thread's papers tagged "direct" support for that
clause (from `thesis_clause_summary.csv`). This shows at a glance which
threads carry which parts of the argument, and where a clause is thin
across all four (a real gap worth knowing about before the paper is
written, not after).

**5b. Cross-thread mechanism heatmap** (`mechanism_heatmap.png`)
Rows = mechanisms from Step 2. Columns = the 4 threads. Cell value = count
of supporting papers. Use this to visually confirm which mechanisms are
genuinely cross-cutting (populated cells in 3+ threads) versus borderline
(only 2).

**5c. "Who is centered" comparison** (`who_is_centered.png`)
Stacked or grouped bar chart. For each thread, categorize each paper's
"Who is centered" text into a small number of buckets you define from the
actual data (e.g., "Engineers/technical experts", "Regulators/officials",
"Community members/residents", "Advocates/CBOs", "Researchers
synthesizing literature"). Plot bucket distribution per thread. This chart
should visually make the paper's own point: the Engineering/Safety thread
centers technical/regulatory actors while the other three threads
increasingly center affected communities and advocates.

**5d. Optional: publication timeline** (`timeline.png`)
Scatter or strip plot of Year (x-axis) by Thread (y-axis or color), one
point per paper. Useful for showing recency/currency of each literature
body in the paper's methods or lit review framing.

## Step 6: Final report

Assemble `final_report.md` containing, in this order:
1. The thesis paragraph (as given above)
2. The narrative synthesis from Step 4
3. Each visual, embedded with a 1-2 sentence caption explaining what it
   shows and how to read it
4. The thesis-clause summary table from Step 3
5. A short "gaps" section: which thesis clauses have the thinnest support
   across all four threads combined, and which mechanisms appear in only 2
   of 4 threads and might benefit from a stronger citation in a third

## Deliverables checklist

- [ ] `unified_lit_review.csv`
- [ ] `mechanisms.json`
- [ ] `thesis_clause_matrix.csv`
- [ ] `thesis_clause_summary.csv`
- [ ] `synthesis_narrative.md`
- [ ] `outputs/radar_chart.png`
- [ ] `outputs/mechanism_heatmap.png`
- [ ] `outputs/who_is_centered.png`
- [ ] `outputs/timeline.png` (optional)
- [ ] `final_report.md`

Report back after each major step (Steps 1-2, Step 3, Step 4, Step 5-6)
rather than running everything silently, so mistakes in mechanism-naming or
clause-tagging can be caught before they propagate into the visuals and
narrative.
