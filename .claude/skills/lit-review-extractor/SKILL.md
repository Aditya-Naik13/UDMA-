---
name: lit-review-extractor
description: "Use this skill whenever the user wants to systematically read a folder of research paper PDFs against a fixed set of research questions and populate a literature review tracking CSV/spreadsheet. Triggers include: 'process these papers', 'fill in the lit review tracker', 'read these PDFs and answer our research questions', 'update the literature review CSV', mentions of a papers repo/folder plus a research-questions file, or any request to extract per-paper findings for a literature review in a structured, citable, non-fabricated way. Also use when asked to add new papers to an existing tracker, re-check an existing tracker's citations, or verify that RQ answers are actually grounded in the source PDFs. This is specifically for RIGOROUS, citation-grounded extraction — not for casual PDF summarization."
---

# Literature Review Extractor

Reads PDFs one at a time against a fixed list of research questions (RQs) and
writes short, page-cited answers into a tracking CSV. The entire point of
this skill is trustworthiness: every answer must be traceable to an actual
page and passage in the actual PDF. An empty or "not addressed" cell is
always preferable to a plausible-sounding invented one.

## Hard rule: no fabrication

This is the single most important constraint. Before writing anything into
the CSV:

- Every RQ answer must be grounded in text you actually read from the
  extracted PDF output (via `extract_pdf_text.py`), not from the paper's
  title, your general knowledge of the topic, or an assumption about what
  a paper "probably" says.
- Every answer must cite a page number that appears in that paper's
  extracted text (the `===== PAGE N =====` markers).
- If a paper does not address an RQ, write exactly: `Not addressed in this
  paper.` — do not stretch a tangential mention into a full answer, and do
  not leave the cell blank (blank looks unprocessed; "not addressed" is a
  confirmed finding).
- If you are uncertain whether a passage really answers the RQ, say so
  briefly rather than presenting it with false confidence.
- Never invent a DOI, year, author name, or journal. If metadata isn't on
  the PDF's first/last page, write `Not found` for that field rather than
  guessing — do not source it from memory of what a paper by that title
  "probably" is.
- Quotes must be copied character-for-character from the extracted text,
  kept short (roughly under 25 words), and attributed to a page number.

## Workflow

### 1. Setup (once per project)

Confirm three things exist, in this order:

1. `references/research_questions.md` — the RQ list. If the user hasn't
   customized this, use the default questions already in the file, but
   confirm with the user this is the right set before processing a whole
   batch of papers.
2. The papers folder (a repo/directory of PDFs the user has already
   downloaded).
3. The tracker CSV. If it doesn't exist yet:

```bash
python scripts/init_csv.py <path/to/tracker.csv>
```

This reads the RQ file and builds the header row automatically
(`Paper_ID, Paper_Name, Authors, Year, Journal, DOI_Link, RQ1...RQn,
Interesting_Perspective, RQs_Not_Addressed, Status, Date_Reviewed`). It
will refuse to overwrite an existing CSV unless `--force` is passed.

### 2. Determine which papers still need processing

Read the current CSV. Cross-reference `Paper_ID` values (or filenames) in
the CSV against PDFs in the papers folder. Only process PDFs that are
missing or whose `Status` is not `Reviewed`. This makes the workflow safely
resumable across sessions — never reprocess a paper marked `Reviewed`
unless the user explicitly asks for a re-check.

### 3. Process one paper at a time

For each unprocessed PDF:

**a. Extract the text with page markers:**

```bash
python scripts/extract_pdf_text.py <path/to/paper.pdf> --out /tmp/paper_text.txt
```

Then read `/tmp/paper_text.txt` (use `view` or a file read tool — do not
skim just the abstract). For long papers, at minimum read: title page,
abstract, introduction, and any sections whose headings plausibly relate to
the RQs, plus skim the rest for missed relevant passages. Don't answer an
RQ from the abstract alone if the full text has more specific support.

**b. Extract metadata** (title, authors, year, journal, DOI) from the first
page and/or the running header/footer. If a DOI isn't printed on the PDF,
check the filename/folder naming convention the user is using, but do not
fabricate one — leave `Not found` if genuinely absent.

**c. Answer each RQ.** For each RQ, decide: does this paper contain material
that actually speaks to it? If yes, write a cell in this format:

```
Finding: <1-2 sentence answer in your own words>. Quote: "<short exact quote>" (p. <N>).
```

If no, write: `Not addressed in this paper.`

**d. Note an interesting perspective** — one sentence on what's distinctive
or citable about this paper's angle, beyond the RQ answers (useful later for
the actual prose lit review, not just the table).

**e. Assign a `Paper_ID`** — short, unique, human-readable slug, e.g.
`lastname_year` (e.g. `sheller2018`). If a collision would occur, add a
letter suffix (`sheller2018b`).

**f. Write the row.** Build a small JSON payload with only the fields you
have real values for, save it, then:

```bash
python scripts/csv_writer.py <path/to/tracker.csv> /tmp/row_<paper_id>.json
```

This merges into the existing row if `Paper_ID` already exists, or appends
a new row — it never clobbers other columns you didn't touch, and it will
error out (not silently guess) if you reference a column name that isn't in
the CSV header.

Set `"Status": "Reviewed"` and `"Date_Reviewed"` (today's date) once all RQ
cells for that paper are filled or marked not-addressed.

### 4. Batch processing

When processing many papers, go through them sequentially rather than
trying to hold multiple papers' text in context at once — extract, read,
answer, write, then move to the next. After each paper, briefly tell the
user which paper was just processed and which RQs it did/didn't address,
so they can spot-check as you go rather than discovering an error 40 papers
later.

### 5. Spot-check on request

If the user asks you to verify a row (e.g. "check paper X's answer to
RQ4"), re-run `extract_pdf_text.py` on that PDF, locate the cited page, and
confirm the quote actually appears there verbatim. Report back plainly if
it doesn't match — don't quietly patch it without flagging the discrepancy.

## CSV schema reference

See `references/research_questions.md` for the live RQ list — it is the
source of truth for CSV columns. Fixed columns (always present):

| Column | Notes |
|---|---|
| `Paper_ID` | Unique slug, used as the merge key by `csv_writer.py` |
| `Paper_Name` | Full title as printed on the paper |
| `Authors` | `Last, F.; Last2, F2.` format |
| `Year` | Publication year |
| `Journal` | Journal/venue name |
| `DOI_Link` | Full DOI URL or direct link |
| `RQ1...RQn` | One column per research question — auto-generated |
| `Interesting_Perspective` | Free-text, one sentence |
| `RQs_Not_Addressed` | Comma-separated list, e.g. `RQ5, RQ8` |
| `Status` | `Reviewed` or blank/`Pending` |
| `Date_Reviewed` | ISO date |

## Updating the research questions

If the user wants to change the RQs mid-project, edit
`references/research_questions.md` directly (keep the `RQ<number>.` format
at the start of each entry). New RQ columns can be added to an already-populated
CSV by re-running `init_csv.py --force` against a *new* CSV path and manually
merging, or by editing the CSV header by hand and adding the column —
`csv_writer.py` will accept writes to any column present in the current
header. Do not silently retrofit old rows with guessed answers for a newly
added RQ; treat previously-`Reviewed` papers as needing a quick re-pass for
the new RQ only.
