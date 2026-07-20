#!/usr/bin/env python3
"""
List which PDFs in a papers folder have NOT yet been recorded in the
tracker CSV, so processing can proceed one paper at a time without the
model needing to hold the full "done vs not-done" state in its own context.

Usage:
    python list_pending.py <papers_dir> <csv_path>

Prints one PDF path per line, in a stable (alphabetical) order, that is
NOT yet matched to a "Paper Title" already recorded in the CSV. Matching
is fuzzy-loose (filename tokens vs. title words) since PDF filenames
rarely equal the exact paper title, so treat this as a first-pass filter,
not a guarantee — always sanity check against the CSV before assuming a
paper is done.
"""
import argparse
import csv
import re
import sys
from pathlib import Path


def normalize(s: str) -> set:
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("papers_dir", type=Path)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    if not args.papers_dir.exists():
        print(f"ERROR: {args.papers_dir} not found.", file=sys.stderr)
        sys.exit(1)
    if not args.csv_path.exists():
        print(f"ERROR: {args.csv_path} not found. Run init_csv.py first.", file=sys.stderr)
        sys.exit(1)

    with open(args.csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    header_row = reader[1]
    data_rows = [dict(zip(header_row, row)) for row in reader[2:]]

    done_titles = [row.get("Paper Title", "") for row in data_rows if row.get("Paper Title", "").strip()]
    done_token_sets = [normalize(t) for t in done_titles]

    pdfs = sorted(args.papers_dir.glob("*.pdf"))
    pending = []
    for pdf in pdfs:
        pdf_tokens = normalize(pdf.stem)
        is_done = False
        for done_tokens in done_token_sets:
            if not done_tokens:
                continue
            overlap = len(pdf_tokens & done_tokens) / max(1, len(done_tokens))
            if overlap > 0.5:
                is_done = True
                break
        if not is_done:
            pending.append(pdf)

    total = len(pdfs)
    remaining = len(pending)
    print(f"# {total - remaining}/{total} PDFs appear to already be in the tracker.", file=sys.stderr)
    print(f"# {remaining} pending. Process ONE at a time, in this order:", file=sys.stderr)
    for p in pending:
        print(p)


if __name__ == "__main__":
    main()
