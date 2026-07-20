#!/usr/bin/env python3
"""
Insert or update one paper's row in the tracker CSV (two-row-header format:
a title row, then the real header row, then data) from a JSON payload.

Why JSON-in, not CLI flags: field text contains quotes, commas, and
newlines that are fragile to pass as shell arguments.

Usage:
    python csv_writer.py <csv_path> <row_json_path>

JSON payload example:
{
  "Paper Title": "Transit Deserts and the Right to Mobility",
  "Author(s)": "Smith et al.",
  "Year": "2020",
  "Journal or Proceedings": "Journal of Transport Geography",
  "DOI or URL": "https://doi.org/10.xxxx/xxxx",
  "Sub-theme": "Transit deserts",
  "Central claim": "...",
  "Key concepts or framework": "...",
  "Who is centered": "...",
  "Value foreclosed (community value left out)": "...",
  "Relevance to argument": "...",
  "Gap or limitation": "...",
  "Quotable moment": "\"...\" (p. 4).",
  "Synthesis paragraph": "..."
}

Matching is done on "Paper Title" (case-insensitive, whitespace-trimmed).
Only keys present in the JSON are written — other columns on an existing
row are preserved. Any field containing an em dash character is rejected
outright so the row is never written with one.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

COLUMNS = [
    "Paper Title",
    "Author(s)",
    "Year",
    "Journal or Proceedings",
    "DOI or URL",
    "Sub-theme",
    "Central claim",
    "Key concepts or framework",
    "Who is centered",
    "Value foreclosed (community value left out)",
    "Relevance to argument",
    "Gap or limitation",
    "Quotable moment",
    "Synthesis paragraph",
]

EM_DASH = "\u2014"


def load(csv_path: Path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    title_row = reader[0]
    header_row = reader[1]
    data_rows = reader[2:]
    dict_rows = [dict(zip(header_row, row)) for row in data_rows]
    return title_row, header_row, dict_rows


def save(csv_path: Path, title_row, header_row, dict_rows):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(title_row)
        writer.writerow(header_row)
        for row in dict_rows:
            writer.writerow([row.get(col, "") for col in header_row])


def check_em_dash(payload: dict):
    offenders = [k for k, v in payload.items() if isinstance(v, str) and EM_DASH in v]
    if offenders:
        print(
            f"ERROR: em dash (\u2014) found in field(s): {offenders}. "
            "Rewrite using a comma, colon, period, or 'and' instead, then retry.",
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("row_json_path", type=Path)
    args = parser.parse_args()

    if not args.csv_path.exists():
        print(f"ERROR: {args.csv_path} does not exist. Run init_csv.py first.", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(args.row_json_path.read_text(encoding="utf-8"))

    if "Paper Title" not in payload or not payload["Paper Title"].strip():
        print("ERROR: JSON payload must include a non-empty 'Paper Title'.", file=sys.stderr)
        sys.exit(1)

    unknown_keys = [k for k in payload if k not in COLUMNS]
    if unknown_keys:
        print(f"ERROR: unknown column(s): {unknown_keys}\nValid columns: {COLUMNS}", file=sys.stderr)
        sys.exit(1)

    check_em_dash(payload)

    title_row, header_row, rows = load(args.csv_path)

    target_key = payload["Paper Title"].strip().lower()
    existing_idx = None
    for i, row in enumerate(rows):
        if row.get("Paper Title", "").strip().lower() == target_key:
            existing_idx = i
            break

    if existing_idx is not None:
        rows[existing_idx].update({k: str(v) for k, v in payload.items()})
        action = "Updated"
    else:
        new_row = {col: "" for col in header_row}
        new_row.update({k: str(v) for k, v in payload.items()})
        rows.append(new_row)
        action = "Added"

    save(args.csv_path, title_row, header_row, rows)
    print(f"{action} row for '{payload['Paper Title']}' in {args.csv_path}")


if __name__ == "__main__":
    main()
