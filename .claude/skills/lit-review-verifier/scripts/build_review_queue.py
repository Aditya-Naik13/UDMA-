#!/usr/bin/env python3
"""
Pair each row already recorded in the tracker CSV with the PDF in the papers
folder it most likely came from, so a reviewer can go paper by paper and
check the row against the actual source.

This is the inverse of the extractor's list_pending.py: that script asks
"which PDFs have no row yet"; this one asks "for each existing row, which PDF
should I re-read to verify it". Matching scores each row's title against the
UNION of a PDF's filename tokens and its first-page text tokens (the printed
title usually lives on page 1), because filenames here are often renamed to
short human labels that share few tokens with the full title. Even so, treat
the pairing as a first pass and confirm the PDF actually is the cited paper
before trusting a low-confidence match.

Usage:
    python build_review_queue.py <papers_dir> <csv_path>

Output (stdout), one row per line, stable order (CSV order):
    <confidence>  <csv_row_title>  =>  <pdf_path_or_NO MATCH>

confidence is HIGH / LOW / NONE. A summary and any unmatched PDFs are printed
to stderr so stdout stays a clean, parseable queue.
"""
import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

# Number of leading pages whose text we scan for the printed title.
FIRSTPAGE_PAGES = 2

# Filenames that are in the folder but are not research papers to review.
IGNORE_STEMS = {"adityanaik-resumep"}

# Tokens so common in paper filenames/titles that they add noise, not signal.
STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "for", "to", "in", "on", "with",
    "using", "from", "at", "as", "is", "are", "how", "do", "does", "main",
    "s2", "0", "1", "2", "preprint", "revised", "clean", "final", "ds1",
    "manuscript", "paper", "vol", "iss", "article",
}

HIGH_CONFIDENCE = 0.5
LOW_CONFIDENCE = 0.25


def normalize(s: str) -> set:
    """Lowercase alphanumeric tokens, stopwords removed."""
    tokens = set(re.findall(r"[a-z0-9]+", s.lower()))
    return tokens - STOPWORDS


def firstpage_tokens(pdf: Path) -> set:
    """Normalized tokens from the first few pages of the PDF (where the title
    is printed). Returns an empty set if pdftotext is unavailable or fails, so
    matching degrades gracefully to filename-only."""
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
    """Overlap as a fraction of the (smaller, more specific) title token set."""
    if not title_tokens:
        return 0.0
    return len(title_tokens & pdf_tokens) / len(title_tokens)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("papers_dir", type=Path)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    if not args.papers_dir.exists():
        print(f"ERROR: {args.papers_dir} not found.", file=sys.stderr)
        sys.exit(1)
    if not args.csv_path.exists():
        print(f"ERROR: {args.csv_path} not found.", file=sys.stderr)
        sys.exit(1)

    with open(args.csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    header_row = reader[1]
    data_rows = [dict(zip(header_row, row)) for row in reader[2:]]
    titles = [r.get("Paper Title", "").strip() for r in data_rows]
    titles = [t for t in titles if t]

    pdfs = [p for p in sorted(args.papers_dir.glob("*.pdf"))
            if p.stem.lower() not in IGNORE_STEMS]
    # Evidence per PDF = filename tokens UNION first-page text tokens.
    print(f"# Scanning first {FIRSTPAGE_PAGES} page(s) of {len(pdfs)} PDF(s) "
          "for printed titles...", file=sys.stderr)
    pdf_tokens = {p: normalize(p.stem) | firstpage_tokens(p) for p in pdfs}

    # Global one-to-one assignment: score every (title, pdf) pair, then assign
    # greedily from the highest score down, so each PDF goes to the title that
    # claims it most strongly and a displaced title falls back to its own
    # next-best (usually its true file) instead of stealing another's.
    title_tokens = {t: normalize(t) for t in titles}
    candidates = []
    for title in titles:
        for pdf in pdfs:
            sc = score(title_tokens[title], pdf_tokens[pdf])
            if sc >= LOW_CONFIDENCE:
                candidates.append((sc, title, pdf))
    candidates.sort(key=lambda c: c[0], reverse=True)

    assigned_title = {}   # title -> (pdf, score)
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
        lines.append(f"{conf}\t{title}\t=>\t{target}")

    print(f"# {len(titles)} rows in tracker, {len(pdfs)} candidate PDFs.",
          file=sys.stderr)
    print(f"# {high} HIGH, {low} LOW, {none} NONE confidence pairings.",
          file=sys.stderr)
    print("# Verify LOW/NONE rows against the CSV before trusting the pairing.",
          file=sys.stderr)

    unmatched = [p for p in pdfs if p not in matched_pdfs]
    if unmatched:
        print(f"# {len(unmatched)} PDF(s) not paired to any row "
              "(possibly unprocessed or a duplicate filename):", file=sys.stderr)
        for p in unmatched:
            print(f"#   {p}", file=sys.stderr)

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
