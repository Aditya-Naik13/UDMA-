---
name: lit-review-verifier
description: "Use this skill whenever the user wants to independently VERIFY or REVIEW an already-populated literature review tracker CSV against the source PDFs, rather than extract new rows from scratch. This is the reviewer counterpart to lit-review-extractor: it reads each paper, re-checks the existing row for accuracy (quotes, year, DOI, author, journal, faithful central claim, non-overstated relevance) and completeness (important points the row omitted), and records suggested corrections and additions as green-highlighted cells in a separate review workbook (.xlsx) without ever touching the canonical CSV. Triggers include: 'verify the tracker', 'review these rows for accuracy', 'check the CSV against the papers', 'audit the lit review', 'double-check the quotes and DOIs', 'is anything important missing from these rows'. Do NOT use this to create rows for papers that have no row yet, that is lit-review-extractor's job."
---

# Literature Review Verifier

A second, independent reviewer pass over a tracker CSV that
`lit-review-extractor` already populated. For each paper it re-reads the
source PDF, checks the existing row field by field, and proposes corrections
and additions. The point is trustworthiness: catch a quote that does not match
its cited page, a claim that drifted from the paper, a relevance line that
overstates a thin fit, a wrong year or DOI, or an important point the row
skipped, and surface each as a reviewable suggestion, not a silent edit.

## What makes this different from the extractor

- The extractor **writes rows into the CSV**. The verifier **never modifies
  the canonical CSV.** It writes suggestions to a separate review workbook
  `<tracker>.review.xlsx`, where each proposed change is a green-highlighted
  cell with a comment giving the original text and the reason. The user
  accepts or rejects from there.
- The extractor treats the length caps as hard ceilings. For the verifier
  the caps are **guidance, not limits**: when an important omitted point
  justifies it, a suggested field may exceed its cap. Prefer tight wording,
  but do not drop a materially important point just to stay under a cap.

## Hard rules

**No fabrication.** Every suggestion must be grounded in text actually read
from the extracted PDF, never from the title, general knowledge, or a guess.
A suggested quote must be copied character for character from the extracted
text and cite a real page from the `===== PAGE N =====` markers. Never
invent a DOI, year, author, or journal; if it is not on the PDF, the correct
suggestion is `Not found`.

**Verify before you suggest.** Do not propose a change unless you have
confirmed the existing value is wrong, imprecise, or incomplete against the
PDF you just read. A row that checks out gets **no** suggestions, and that is
a valid, expected outcome. Do not manufacture changes to look busy.

**No em dash (—), anywhere, in any suggested text.** `xlsx_suggest.py` hard
rejects any suggestion containing one. Use a comma, colon, period, or "and".
Scan your drafted suggestion before writing it.

**The canonical CSV is read-only.** Only `<tracker>.review.xlsx` is written.
If you ever find yourself about to edit the CSV, stop: that is the extractor's
job, not the verifier's.

**One paper at a time.** Extract, read, check, write suggestions, stop.
Do not read several PDFs into context before writing. This keeps each paper's
review grounded in what you just read and keeps context from filling with PDF
text you no longer need.

## Setup (once per project)

1. Confirm dependencies: `pdftotext` (poppler) and `openpyxl`
   (`python -m pip install openpyxl`).
2. Read the working lens and style targets, shared with the extractor:
   - `../lit-review-extractor/references/paper_context.md` — the section's
     specific claim, the three community values, the sub-theme examples.
   - `../lit-review-extractor/references/column_style_guide.md` — the length
     targets (treated here as guidance, not caps).
3. Read `references/review_checklist.md` — the per-column verification
     criteria and the verbatim-quote procedure.

## Workflow, per paper

### 1. Build / consult the review queue

```bash
python scripts/build_review_queue.py <papers_dir> <tracker.csv>
```

This pairs each CSV row with the PDF it most likely came from, scoring the
title against each PDF's filename plus its first-page text. Output columns:
`CONFIDENCE  <row title>  =>  <pdf path>`. Take the first row not yet
reviewed. For a `LOW` or `NONE` pairing, confirm the PDF really is the cited
paper (open its first page) before proceeding. Any PDF the summary lists as
unpaired is a possible unprocessed paper or a renamed duplicate; flag it to
the user rather than reviewing it as if it had a row.

### 2. Extract that one paper's text

```bash
python ../lit-review-extractor/scripts/extract_pdf_text.py <paper.pdf> --out /tmp/paper_text.txt
```

Read `/tmp/paper_text.txt`: title page, abstract, introduction, section
headings relevant to the lens, plus a skim for passages the row's claims
depend on. Note the page numbers of anything the existing row cites.

### 3. Check the existing row against the paper

Pull up the row's current values from the CSV and go field by field using
`references/review_checklist.md`. For each field decide: correct as is,
needs correction, or missing something important. Record only what changes.

### 4. Write suggestions to the review workbook

Build a suggestion JSON with only the fields that need changing:

```bash
cat > /tmp/suggestion.json << 'EOF'
{
  "Paper Title": "<exact title as it appears in the CSV>",
  "changes": {
    "Quotable moment": {
      "suggested": "\"...\" (p. 7).",
      "why": "Original cited p. 5; the phrase is on p. 7 in the extract."
    }
  }
}
EOF
python scripts/xlsx_suggest.py <tracker.csv> /tmp/suggestion.json
```

`xlsx_suggest.py` creates `<tracker>.review.xlsx` on first run and updates it
in place afterward, so a full pass accumulates every paper's suggestions in
one workbook. It matches the row by Paper Title, highlights each changed cell
green with a comment (`Original:` + `Why:`), leaves untouched cells and all
other rows alone, and rejects em dashes. If a paper checks out fully, either
skip the write or pass `"changes": {}` to record "reviewed, nothing to
change."

### 5. Report and stop

Tell the user which paper was reviewed and, in one or two lines, what you
suggested and why (or that it checked out clean). **Then stop** unless the
user asked for a full unattended batch. This gives a checkpoint to spot-check
suggestions before the next paper, and keeps each paper's review isolated.

If the user does ask for a full batch, still process serially (one extract,
read, check, write cycle per paper, discarding that paper's extracted text
before the next), with a short progress note after each paper.

## After the pass

The deliverable is `<tracker>.review.xlsx` with green suggestion cells. The
user reviews it and decides what to accept. Applying accepted suggestions
back into the canonical CSV is a separate, explicit step, do not do it as
part of the review.

## Reference files

- `references/review_checklist.md` — per-column verification criteria, the
  verbatim-quote check, the overstated-fit test, and the important-omission
  test.
- Shared with the extractor: `../lit-review-extractor/references/paper_context.md`
  (the lens) and `../lit-review-extractor/references/column_style_guide.md`
  (length targets, here treated as guidance).

## Scripts

- `scripts/build_review_queue.py` — pair each CSV row to its source PDF.
- `scripts/xlsx_suggest.py` — record one paper's suggestions into the review
  workbook (green cell plus comment), CSV untouched.
- Reused: `../lit-review-extractor/scripts/extract_pdf_text.py` — page-marked
  PDF text extraction.
