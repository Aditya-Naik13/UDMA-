#!/usr/bin/env python3
"""
Append the 3 participatory/co-design columns to the tracker CSV and fill
them in row by row. Deliberately standalone: does NOT import or modify
.claude/skills/lit-review-extractor/scripts/csv_writer.py or the verifier's
xlsx_suggest.py, both of which hardcode the original 14-column schema and
would reject these 3 new keys outright.

The live tracker CSV currently has ONE header row (no separate title row),
so this script treats reader[0] as the header, unlike csv_writer.py which
assumes a title row + header row.

Usage:
    # One-time: append the 3 new (empty) columns to every row.
    python append_columns.py --ensure-columns <csv_path>

    # Per paper: fill in the 3 new columns on an existing row, matched by
    # "Paper Title" (case-insensitive, whitespace-trimmed). Never creates a
    # new row; errors if no existing row matches.
    python append_columns.py <csv_path> <row_json_path>

JSON payload example:
{
  "Paper Title": "Bridging the gap: Do community needs assessments enhance public participation in transportation planning?",
  "Codesign/participatory method": "...",
  "What worked": "...",
  "What didn't work": "..."
}
"""
import argparse
import csv
import json
import sys
from pathlib import Path

NEW_COLUMNS = [
    "Codesign/participatory method",
    "What worked",
    "What didn't work",
]

EM_DASH = "—"


def load(csv_path: Path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    header_row = reader[0]
    data_rows = reader[1:]
    return header_row, data_rows


def save(csv_path: Path, header_row, data_rows):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header_row)
        writer.writerows(data_rows)


def ensure_columns(csv_path: Path):
    header_row, data_rows = load(csv_path)
    missing = [c for c in NEW_COLUMNS if c not in header_row]
    if not missing:
        print(f"No changes: {csv_path} already has all 3 new columns.")
        return
    new_header = header_row + missing
    pad = len(missing)
    new_rows = [row + [""] * pad for row in data_rows]
    save(csv_path, new_header, new_rows)
    print(f"Added column(s) {missing} to {csv_path} "
          f"({len(new_rows)} data rows padded).")


def check_em_dash(payload: dict):
    offenders = [k for k, v in payload.items() if isinstance(v, str) and EM_DASH in v]
    if offenders:
        print(
            f"ERROR: em dash (—) found in field(s): {offenders}. "
            "Rewrite using a comma, colon, period, or 'and' instead, then retry.",
            file=sys.stderr,
        )
        sys.exit(1)


def update_row(csv_path: Path, row_json_path: Path):
    payload = json.loads(row_json_path.read_text(encoding="utf-8"))

    if "Paper Title" not in payload or not payload["Paper Title"].strip():
        print("ERROR: JSON payload must include a non-empty 'Paper Title'.", file=sys.stderr)
        sys.exit(1)

    allowed_keys = set(NEW_COLUMNS) | {"Paper Title"}
    unknown_keys = [k for k in payload if k not in allowed_keys]
    if unknown_keys:
        print(f"ERROR: unknown column(s): {unknown_keys}\n"
              f"Valid keys: Paper Title + {NEW_COLUMNS}", file=sys.stderr)
        sys.exit(1)

    check_em_dash({k: v for k, v in payload.items() if k != "Paper Title"})

    header_row, data_rows = load(csv_path)
    missing = [c for c in NEW_COLUMNS if c not in header_row]
    if missing:
        print(f"ERROR: {csv_path} is missing column(s) {missing}. "
              "Run --ensure-columns first.", file=sys.stderr)
        sys.exit(1)

    col_idx = {name: header_row.index(name) for name in NEW_COLUMNS}
    title_idx = header_row.index("Paper Title")
    target_key = payload["Paper Title"].strip().lower()

    match_idx = None
    for i, row in enumerate(data_rows):
        if len(row) > title_idx and row[title_idx].strip().lower() == target_key:
            match_idx = i
            break

    if match_idx is None:
        print(f"ERROR: no existing row found for Paper Title "
              f"{payload['Paper Title']!r}. This script never creates new "
              "rows.", file=sys.stderr)
        sys.exit(1)

    row = data_rows[match_idx]
    if len(row) < len(header_row):
        row = row + [""] * (len(header_row) - len(row))
    for name in NEW_COLUMNS:
        if name in payload:
            row[col_idx[name]] = str(payload[name])
    data_rows[match_idx] = row

    save(csv_path, header_row, data_rows)
    print(f"Updated row for '{payload['Paper Title']}' in {csv_path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ensure-columns", action="store_true",
                         help="Append the 3 new (empty) columns to the CSV, then exit.")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("row_json_path", type=Path, nargs="?")
    args = parser.parse_args()

    if not args.csv_path.exists():
        print(f"ERROR: {args.csv_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    if args.ensure_columns:
        ensure_columns(args.csv_path)
        return

    if args.row_json_path is None:
        print("ERROR: row_json_path is required unless --ensure-columns is passed.",
              file=sys.stderr)
        sys.exit(1)

    update_row(args.csv_path, args.row_json_path)


if __name__ == "__main__":
    main()
