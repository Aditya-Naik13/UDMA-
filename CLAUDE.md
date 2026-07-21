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
- `Community & Equity Dimensions of Mobility Literature Review.review.xlsx` —
  verifier output, green cells are suggested changes with a comment holding
  the original text and the reason. Untracked working file, not the
  deliverable.

## Current state

All 39 rows have been through one full verifier pass. **11 suggestions across
10 rows are still PENDING in the review workbook and have NOT been applied to
the CSV.** The CSV therefore still contains the four known defects listed
under "Known failure patterns". Applying accepted suggestions is a separate,
explicit step, do not assume it has happened.
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
- **No em dash (—) in any tracker field or suggestion.** `csv_writer.py` and
  `xlsx_suggest.py` hard-reject it. Use a comma, colon, period, or "and".
  Scope note: this applies to CSV/workbook content, not to prose in this file
  or in the skill docs, which do use em dashes. Do not copy their punctuation
  style into a row.
- **One paper at a time.** Extract → read → draft/check → write → stop. Do not
  batch multiple PDFs into context before writing.
- **The verifier never edits the canonical CSV.** It only writes the review
  workbook. Applying accepted suggestions back into the CSV is a separate,
  explicit step.
- Length caps are ceilings for the extractor, but guidance (not limits) for
  the verifier when an important omitted point justifies more words.

## Extractor checklist (first pass, while drafting a row)

Self-checks on your own output, before calling `csv_writer.py`:

1. **Grounding** every field traces to text read in THIS PDF, not the title,
   topic knowledge, or what a paper like this probably argues.
2. **Quote** copied character-for-character, page taken from a real
   `===== PAGE N =====` marker.
3. **Whose words is the quote?** Read the sentences around it. If it sits in
   the paper's own quotation marks or carries a trailing `(Author, Year, p. N)`,
   it is borrowed and the nested source must be named in the field. See
   "Known failure patterns" below, this is the single most common defect.
4. **Every specific is in the source.** Any number, count, sample size, or
   date you write must be greppable in the extracted text. Do not complete a
   plausible pattern (a committee that shrank "to about 30") from inference.
5. **Bibliographic** year, DOI, journal, author present on the PDF, else
   `Not found`. Never guess.
6. **Artifact vs citation** check what the PDF actually is. A preprint,
   author manuscript, or ScienceDirect page-print does not share pagination
   with the published article. If the row cites a published DOI but the pages
   come from a manuscript, say so in the quote field.
7. **Value foreclosed** one of the three community values, or honestly
   `None directly foreclosed` rather than forcing one.
8. **Relevance honesty** written against the section claim. If the fit is
   thin, say so plainly instead of inflating it.
9. **Synthesis written last**, and not a paraphrase of Central claim.
10. **Length caps** as ceilings, **no em dash**.

## Verifier checklist (second pass, row against PDF)

Ordered by yield from the first full pass. Default outcome is NO change.

1. Whose words is the quote (nested-quote check).
2. Is every specific number actually in the source.
3. Quote verbatim on the CITED page.
4. Does the quote survive truncation, or does it stop before the point.
5. Artifact vs citation (preprint/manuscript pagination).
6. Claim drift against abstract and conclusion.
7. Overstated fit in Relevance.
8. Material omission (changes how the paper reads, not wording taste).
9. Paywall caveat present and accurate.

## Known failure patterns (found in the first verifier pass)

29 of 39 rows were clean. The 11 findings clustered into four types, all of
which the extractor should now prevent at the source:

- **Nested quotes (3 rows)** the most common defect. Quotes recorded as the
  paper's own words that the paper was quoting from someone else
  (Al-Sharari 2022, Hendren 2020, TransitCenter 2022). Cited as-is, these
  misattribute another scholar's words.
- **Unsupported specific (1 row)** the most serious. A committee described as
  shrinking "to about 30 hand-picked representatives" when the paper states
  only that nearly 70 people attended and were asked to nominate one or two
  per organization. The number was plausible and absent from the source.
- **Manuscript/preprint pagination (2 rows)** page cites taken from an author
  manuscript while the row cites the published DOI.
- **Quote truncated before the point (2 rows)** verbatim but cut where the
  meaning starts ("They have priorities"), leaving nothing usable.

## PDF extraction pitfalls (cost real time, do not relearn)

- **Two-column layouts interleave under `-layout`.** Columns are joined on the
  same physical lines, so a quote can be split by unrelated text from the
  other column. A naive grep then reports "quote not found" for a quote that
  is really there. Search reading-order mode (`pdftotext` with no `-layout`)
  as well.
- **Hyphenated line breaks become spaces** (`displaced` extracts as
  `dis placed`), so exact-string search fails. Compare with whitespace removed
  before concluding a quote is wrong.
- **Never file a "quote not found" or a name correction from a failed pattern
  match alone.** Open the cited page and read it. Two near-miss false
  corrections in the first pass came from trusting a grep over the source
  (a line-wrapped quote, and the author `McCullogh`, which is correctly
  spelled that way and is not a typo of `McCullough`).

## Conventions

- Author(s): `Last` for a sole author, `Last et al.` for two or more. No
  initials, no spelled-out co-authors.
- The extractor caps fields; the verifier may exceed a cap only to add a
  materially important point.
- `papers/Community Needs Assessments in Transportation Planning.pdf` is a
  renamed duplicate of the Pinski "Bridging the gap" paper
  (`1-s2.0-S2590198224001003-main.pdf`), not a 40th unprocessed paper.

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
