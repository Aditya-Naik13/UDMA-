---
name: lit-review-extractor
description: "Use this skill whenever the user wants to systematically read a folder of research paper PDFs and populate a literature review tracking CSV in the fixed 14-column format (Paper Title, Author(s), Year, Journal or Proceedings, DOI or URL, Sub-theme, Central claim, Key concepts or framework, Who is centered, Value foreclosed, Relevance to argument, Gap or limitation, Quotable moment, Synthesis paragraph). Triggers include: 'process these papers', 'fill in the lit review tracker', 'read these PDFs and add them to the CSV', mentions of a papers repo/folder plus a tracker CSV, or any request to extract per-paper findings for a literature review in a structured, citable, non-fabricated way. Also use when asked to add new papers to an existing tracker, re-check an existing tracker's citations, or verify a quote against the source PDF. This is specifically for RIGOROUS, citation-grounded extraction, one paper at a time, not for casual PDF summarization."
---

# Literature Review Extractor

Reads PDFs **one at a time** and writes a row per paper into a tracker CSV
using a fixed 14-column format. The point of this skill is trustworthiness
and consistency: every claim must trace back to an actual page in the actual
PDF, every row must read like it belongs next to the others, and no row
should balloon into a wall of text.

## Hard rules

**No fabrication.**
- Every column must be grounded in text actually read from the extracted
  PDF (via `extract_pdf_text.py`), never from the title alone, general
  knowledge of the topic, or a guess at what a paper "probably" argues.
- Quotable moment must be copied character-for-character from the
  extracted text and cite a real page number from the `===== PAGE N =====`
  markers.
- Never invent a DOI, year, author, or journal. If it's not on the PDF,
  write `Not found` rather than guessing.
- If a paper doesn't foreclose any of the three community values, write
  "None directly foreclosed" in that column rather than forcing one.

**No em dash (—), anywhere, in any field.** Before writing a row, scan your
own drafted text for this character. If you find one, rewrite that clause
with a comma, colon, period, or "and" instead of substituting a hyphen.
`csv_writer.py` will hard-reject any field containing one, so catching it
yourself first saves a retry.

**Keep it short.** See `references/column_style_guide.md` for exact
per-column word/character targets, calibrated from the reference CSV you
were given. Rows that run long are harder to scan and defeat the purpose
of a tracker. When in doubt, cut a clause rather than add one.

**Process exactly one paper at a time.** Do not read multiple PDFs into
context before writing anything. Do not draft several rows in your head
and then write them all at once. The sequence for every paper is: extract
→ read → draft the row → write it to the CSV → move on. This keeps each
paper's extraction grounded in what you just read rather than a blended
memory of several papers, and keeps context from filling up with PDF text
you no longer need once that paper's row is written.

## Setup (once per project)

1. Read `references/paper_context.md` — this is the working lens: the
   section's specific claim, the three community values, and the starting
   sub-theme examples (open-ended, not a fixed taxonomy).
2. Read `references/column_style_guide.md` — the length targets and style
   rules (including the no-em-dash rule).
3. If the tracker CSV doesn't exist yet:

```bash
python scripts/init_csv.py <path/to/tracker.csv> "Community & Equity Dimensions of Mobility Literature Review"
```

This writes the title row and the fixed 14-column header. Won't overwrite
an existing file unless `--force` is passed.

## Workflow, per paper

### 1. Get the queue

```bash
python scripts/list_pending.py <papers_dir> <path/to/tracker.csv>
```

This diffs the PDFs folder against what's already in the CSV (fuzzy title
match) and prints one pending PDF path per line to stdout, in a stable
order. Treat this as a first-pass filter, not a guarantee — if a match
looks wrong, check the CSV directly before assuming a paper is done.

**Take the first path from that list. Ignore the rest for now.**

### 2. Extract that one paper's text

```bash
python scripts/extract_pdf_text.py <path/to/paper.pdf> --out /tmp/paper_text.txt
```

Read `/tmp/paper_text.txt`. At minimum: title page, abstract, introduction,
and any section headings that plausibly relate to the working lens, plus a
skim of the rest for relevant passages you'd otherwise miss.

### 3. Draft the row against the working lens

For each column, go back to `references/paper_context.md`:

- **Sub-theme**: 2-5 words. Use one of the starting examples if it fits,
  or coin a new short label if it doesn't — this list is meant to grow.
- **Central claim**: what the paper actually argues, in the paper's own
  terms, not pre-filtered through our lens yet.
- **Key concepts or framework**: the paper's own vocabulary/framework, each
  concept defined in a half-sentence.
- **Who is centered**: whose perspective or expertise the paper's method
  and framing foreground.
- **Value foreclosed**: which of equitable access / relational trust /
  flexibility for variable need the paper's framing leaves out, or "None
  directly foreclosed."
- **Relevance to argument**: how this paper supports the section's
  specific claim (mobility access historically unevenly distributed,
  and/or infrastructure without participation reproduces exclusion) —
  see `paper_context.md` for exactly how to frame this. If the fit to
  that claim is thin or indirect, say so plainly and justify the paper's
  inclusion against the broader project instead of overstating the fit.
- **Gap or limitation**: what the paper doesn't address that our argument
  needs.
- **Quotable moment**: one exact short quote plus page number.
- **Synthesis paragraph**: write this LAST, after all other columns are
  filled — it should read as the 2-3 sentence takeaway you'd actually use
  when writing the prose lit review, not a repeat of Central claim.

Before moving to step 4, reread every field you just drafted and check for
an em dash. Fix any you find.

### 4. Write the row

```bash
cat > /tmp/row.json << 'EOF'
{
  "Paper Title": "...",
  "Author(s)": "...",
  ...
}
EOF
python scripts/csv_writer.py <path/to/tracker.csv> /tmp/row.json
```

Only include keys you have real values for. `csv_writer.py` merges into an
existing row (matched by Paper Title) or appends a new one, rejects unknown
column names, and rejects any field containing an em dash.

### 5. Report and stop

Tell the user which paper was just processed, its sub-theme, and a
one-line summary of what it contributes. **Then stop** — do not
automatically continue to the next paper in the same turn unless the user
has explicitly asked for a full batch run. This keeps a natural checkpoint
where the user can spot-check before more rows get written, and keeps each
paper's processing isolated from the last so context doesn't accumulate
across many PDFs' worth of extracted text.

If the user does ask for a full batch run, still process serially (one
extract → read → draft → write cycle per paper, discarding that paper's
extracted text before starting the next), and give a short progress note
after each paper rather than one bundled summary at the end.

## Spot-checking

If asked to verify a row, re-run `extract_pdf_text.py` on that PDF, find
the cited page, and confirm the quote matches verbatim. Report plainly if
it doesn't, don't quietly patch it without flagging the discrepancy.

## Reference files

- `references/paper_context.md` — the paper's full thesis (background),
  this section's specific claim (the working lens), the three community
  values, and starting sub-theme examples.
- `references/column_style_guide.md` — per-column length targets and style
  rules, including the no-em-dash rule.
