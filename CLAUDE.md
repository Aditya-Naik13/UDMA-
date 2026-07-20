# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A **literature review pipeline** for an academic paper arguing that
autonomous vehicles are community *infrastructure* that typically arrives
without community participation, carrying efficiency-driven engineering
values that clash with three community values: **equitable access**,
**relational trust**, and **flexibility for variable need**. The paper
introduces "Mobility as Social Service."

The concrete deliverable is a single tracker CSV, one row per paper, filled
rigorously from source PDFs and citation-grounded (no fabrication).

## Layout

- `Community & Equity Dimensions of Mobility Literature Review.csv` — the
  tracker (canonical output). Two-row header: a section-title row, then the
  14-column header, then one data row per paper. 39 papers recorded.
- `papers/` — source PDFs. Filenames are often renamed human labels that do
  not match the paper title. `AdityaNaik-ResumeP.pdf` is a stray résumé, not
  a research paper; skip it.
- `.claude/skills/lit-review-extractor/` — populates the tracker from PDFs.
- `.claude/skills/lit-review-verifier/` — independently reviews existing rows
  against the PDFs and proposes corrections.
- `Transportation Equity Lit Review Extractor.skill` — zip-packaged copy of
  the extractor skill for sharing/install.

## The 14 columns (fixed order)

Paper Title, Author(s), Year, Journal or Proceedings, DOI or URL, Sub-theme,
Central claim, Key concepts or framework, Who is centered, Value foreclosed
(community value left out), Relevance to argument, Gap or limitation,
Quotable moment, Synthesis paragraph.

Length targets per column live in
`.claude/skills/lit-review-extractor/references/column_style_guide.md`.

## The two skills

### `lit-review-extractor` — add new rows
Reads PDFs **one at a time** and writes a row per paper. Use when populating
the tracker or adding papers that have no row yet. Workflow: `list_pending.py`
→ `extract_pdf_text.py` → draft against the lens → `csv_writer.py` → stop.

### `lit-review-verifier` — review existing rows
The reviewer counterpart. Re-reads each paper, checks the existing row for
accuracy (quotes, year, DOI, author, journal, faithful claim, non-overstated
relevance) and completeness, and records suggestions as **green-highlighted
cells in a separate `<tracker>.review.xlsx`** without ever touching the CSV.
Workflow: `build_review_queue.py` → `extract_pdf_text.py` → check row against
`references/review_checklist.md` → `xlsx_suggest.py` → stop.

Both skills share the same lens (`paper_context.md`) and style guide, and both
reuse `extract_pdf_text.py` from the extractor.

## Hard rules (both skills)

- **No fabrication.** Every field traces to text actually read from the
  extracted PDF. Quotes are copied character-for-character with a real page
  number from the `===== PAGE N =====` markers. Never invent a DOI, year,
  author, or journal; write `Not found` instead.
- **No em dash (—) anywhere, in any field.** `csv_writer.py` and
  `xlsx_suggest.py` hard-reject it. Use a comma, colon, period, or "and".
- **One paper at a time.** Extract → read → draft/check → write → stop. Do not
  batch multiple PDFs into context before writing.
- **The verifier never edits the canonical CSV.** It only writes the review
  workbook. Applying accepted suggestions back into the CSV is a separate,
  explicit step.
- Length caps are ceilings for the extractor, but guidance (not limits) for
  the verifier when an important omitted point justifies more words.

## Conventions

- Author(s): `Last` for a sole author, `Last et al.` for two or more. No
  initials, no spelled-out co-authors.
- The extractor caps fields; the verifier may exceed a cap only to add a
  materially important point.

## Dependencies

- `pdftotext` (poppler) — PDF text extraction. Confirmed working (v4.00).
- `openpyxl` — review workbook generation (`python -m pip install openpyxl`).
- Python 3 for all scripts.

## Environment notes

- Windows; PowerShell is primary, Bash tool available for POSIX scripts.
- Script paths in `papers/` use spaces; quote them.
- The queue/pairing matcher scores paper titles against each PDF's filename
  **plus its first-page text**, because filenames are unreliable here. A PDF
  the queue reports as unpaired is likely unprocessed or a renamed duplicate,
  flag it rather than assuming it has a row.
