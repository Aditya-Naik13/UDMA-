#!/usr/bin/env python3
"""
One-time helper for the participatory-columns task: pair each of the 39
existing tracker rows with the PDF in papers/ it most likely came from.

This is a direct adaptation of
.claude/skills/lit-review-verifier/scripts/build_review_queue.py's matching
algorithm (same normalize/tokenize/score/greedy-assignment approach), with
two changes:
  1. The header-row index is fixed: the live tracker CSV currently has ONE
     header row (not the two-row title+header format some of the skill
     scripts assume), so header_row = reader[0], data_rows = reader[1:].
  2. The known renamed duplicate of the Pinski "Bridging the gap" paper is
     excluded from candidate PDFs, same as build_review_queue.py excludes
     the stray resume.

Usage:
    python map_titles_to_pdfs.py <papers_dir> <csv_path> > title_pdf_map.tsv

Output (stdout), one row per line:
    <confidence>\t<csv_row_title>\t<pdf_path_or_NO MATCH>

confidence is HIGH / LOW / NONE. Any LOW/NONE row must be resolved by hand
(open the PDF and confirm) before it's used to drive extraction.
"""
import csv
import re
import subprocess
import sys
from pathlib import Path

FIRSTPAGE_PAGES = 2

IGNORE_STEMS = {
    "adityanaik-resumep",
    "community needs assessments in transportation planning",
}

STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "for", "to", "in", "on", "with",
    "using", "from", "at", "as", "is", "are", "how", "do", "does", "main",
    "s2", "0", "1", "2", "preprint", "revised", "clean", "final", "ds1",
    "manuscript", "paper", "vol", "iss", "article",
}

HIGH_CONFIDENCE = 0.5
LOW_CONFIDENCE = 0.25


def normalize(s: str) -> set:
    tokens = set(re.findall(r"[a-z0-9]+", s.lower()))
    return tokens - STOPWORDS


def firstpage_tokens(pdf: Path) -> set:
    try:
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(FIRSTPAGE_PAGES), "-layout",
             str(pdf), "-"],
            capture_output=True, text=True, timeout=60,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return set()
    if result.returncode != 0:
        return set()
    return normalize(result.stdout)


def score(title_tokens: set, pdf_tokens: set) -> float:
    if not title_tokens:
        return 0.0
    return len(title_tokens & pdf_tokens) / len(title_tokens)


def main():
    if len(sys.argv) != 3:
        print("Usage: map_titles_to_pdfs.py <papers_dir> <csv_path>", file=sys.stderr)
        sys.exit(1)
    papers_dir = Path(sys.argv[1])
    csv_path = Path(sys.argv[2])

    if not papers_dir.exists():
        print(f"ERROR: {papers_dir} not found.", file=sys.stderr)
        sys.exit(1)
    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found.", file=sys.stderr)
        sys.exit(1)

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    header_row = reader[0]
    data_rows = [dict(zip(header_row, row)) for row in reader[1:]]
    titles = [r.get("Paper Title", "").strip() for r in data_rows]
    titles = [t for t in titles if t]

    pdfs = [p for p in sorted(papers_dir.glob("*.pdf"))
            if p.stem.lower() not in IGNORE_STEMS]
    print(f"# Scanning first {FIRSTPAGE_PAGES} page(s) of {len(pdfs)} PDF(s) "
          "for printed titles...", file=sys.stderr)
    pdf_tokens = {p: normalize(p.stem) | firstpage_tokens(p) for p in pdfs}

    title_tokens = {t: normalize(t) for t in titles}
    candidates = []
    for title in titles:
        for pdf in pdfs:
            sc = score(title_tokens[title], pdf_tokens[pdf])
            if sc >= LOW_CONFIDENCE:
                candidates.append((sc, title, pdf))
    candidates.sort(key=lambda c: c[0], reverse=True)

    assigned_title = {}
    used_pdfs = set()
    for sc, title, pdf in candidates:
        if title in assigned_title or pdf in used_pdfs:
            continue
        assigned_title[title] = (pdf, sc)
        used_pdfs.add(pdf)

    matched_pdfs = set(used_pdfs)
    lines = []
    high = low = none = 0
    for title in titles:
        pair = assigned_title.get(title)
        if pair is None:
            conf, target = "NONE", "NO MATCH"
            none += 1
        else:
            pdf, sc = pair
            conf = "HIGH" if sc >= HIGH_CONFIDENCE else "LOW"
            high += conf == "HIGH"
            low += conf == "LOW"
            target = str(pdf)
        lines.append(f"{conf}\t{title}\t{target}")

    print(f"# {len(titles)} rows in tracker, {len(pdfs)} candidate PDFs.",
          file=sys.stderr)
    print(f"# {high} HIGH, {low} LOW, {none} NONE confidence pairings.",
          file=sys.stderr)

    unmatched = [p for p in pdfs if p not in matched_pdfs]
    if unmatched:
        print(f"# {len(unmatched)} PDF(s) not paired to any row:", file=sys.stderr)
        for p in unmatched:
            print(f"#   {p}", file=sys.stderr)

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
