# UDMA: Autonomous Vehicles, Community Mobility & Mobility as Social Service

A literature review and qualitative-coding pipeline for an academic paper arguing that
autonomous vehicles (AVs) are community **infrastructure** that typically arrives without
community participation, carrying efficiency-driven engineering values that clash with three
community values: **equitable access**, **relational trust**, and **flexibility for variable
need**. The paper introduces **"Mobility as Social Service"** (mobility as an ongoing,
relational practice of equitable provisioning).

## What is in this repo today

- `Community & Equity Dimensions of Mobility Literature Review.csv` — the literature-review
  tracker (canonical output), one row per paper, 17 columns (14 core + 3 participatory-method
  columns), 39 papers recorded and verified.
- `crosscomp/` — the literature cross-comparison: 7 cross-cutting mechanisms, thesis-clause
  support per thread, who-is-centered counts, and `unified_lit_review.csv` (the merged rows of
  the four thread trackers, 82 papers with DOI, journal, and thread).
- `csvs/` — the four source thread trackers (Engineering & Safety, Equity, Food Justice,
  Participatory Design).
- `Codebook/` — the codebook pipeline (see below): source codebooks, build script, process
  record, and the finalized deliverable (Excel + Word + plain-English summary).
- `analysis/` — the 34-transcript qualitative analysis (synthesis, coding notes, workshops).
- `papers/` — source PDFs for the literature review.
- `.claude/skills/` — the extractor and verifier skills that populate and audit the tracker.

## The codebook (most recent addition)

The codebook turns the transcript and workshop findings (original transcript codebook, the
MaSS thesis codebook, the Capstone workshop map) into a **paper-findings architecture** that
also incorporates the four literature threads. Running `Codebook/process/build_codebook.py`
regenerates all outputs from a single source table, verifying quotes verbatim and every lit
citation to a real paper (author, year, DOI), with a strict no-em-dash rule.

- `Codebook/Output/Codebook_final.xlsx` — 7 sheets: README, Codebook (72 codes across 9
  findings areas A–I plus a method block M), 3 crosswalks (OG themes, MaSS codes, Capstone
  clusters), LitEvidenceMap (56 paper-level citations, one row per paper with DOI), PaperMap
  (domain → thesis clause → paper section).
- `Codebook/Output/Codebook_final.docx` — readable companion version.
- `Codebook/Output/Codebook_Plain_English_Summary.docx` — 1-page plain-English explanation of
  the process and what the literature added (17 new codes + new areas H and I).
- `Codebook/process/build_codebook.py` — the generator script (single source of truth).
- `Codebook/process/codebook_build.md` — the process record.

## What changed

Recent commits added the finalized codebook: re-organized the three transcript-era codebooks
into 9 findings domains, added 17 lit-derived codes (including two new literature-only domains:
H, the discourse the AV carries, from Engineering & Safety; and I, the charity model and digital
food system, from Food Justice), and resolved every mechanism citation to its actual paper row.
See `git log` for details.