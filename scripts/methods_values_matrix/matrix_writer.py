#!/usr/bin/env python3
"""
Insert or update one paper's row in the Methods, Values, and Ideal-Traveler
Matrix CSV from a JSON payload.

This is a standalone writer for the second-pass matrix. It is deliberately
separate from the lit-review-extractor's csv_writer.py, which only knows the
original 14-column tracker schema.

Single header row, then one data row per paper. Matching is on "Paper Title"
(case-insensitive, whitespace-trimmed). Only keys present in the JSON are
written; other columns on an existing row are preserved. Any field containing
an em dash is rejected outright, same rule as the main tracker.

Usage:
    python matrix_writer.py <csv_path> <row_json_path>
    python matrix_writer.py <csv_path> --init      # write just the header row
"""
import argparse
import csv
import json
import sys
from pathlib import Path

COLUMNS = [
    "Paper Title",
    "Author(s)",
    "Year",
    "Study type / basis for inclusion",
    "Case setting",
    "Method(s), session by session",
    "Tools and artifacts",
    "Underlying principle of the method",
    "Provocation used to generate new ideas",
    "Who holds design authority",
    "What is being designed",
    "Values surfaced in the case",
    "Ideal traveler per decision-makers",
    "Actual travelers encountered",
    "Gap between the two",
    "Quotable moment",
    "Cross-comparison note (our synthesis)",
]

EM_DASH = "—"


def load(csv_path: Path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    if not reader:
        return list(COLUMNS), []
    header = reader[0]
    rows = [dict(zip(header, r)) for r in reader[1:]]
    return header, rows


def save(csv_path: Path, header, rows):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in rows:
            w.writerow([row.get(c, "") for c in header])


def check_em_dash(payload: dict):
    bad = [k for k, v in payload.items() if isinstance(v, str) and EM_DASH in v]
    if bad:
        print(
            f"ERROR: em dash (—) in field(s): {bad}. "
            "Use a comma, colon, period, or 'and' instead.",
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv_path", type=Path)
    p.add_argument("row_json_path", type=Path, nargs="?")
    p.add_argument("--init", action="store_true", help="write only the header row and exit")
    args = p.parse_args()

    if args.init:
        if args.csv_path.exists():
            print(f"ERROR: {args.csv_path} already exists, refusing to overwrite.", file=sys.stderr)
            sys.exit(1)
        with open(args.csv_path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(COLUMNS)
        print(f"Wrote header ({len(COLUMNS)} columns) to {args.csv_path}")
        return

    if not args.row_json_path:
        print("ERROR: need a row JSON path (or --init).", file=sys.stderr)
        sys.exit(1)
    if not args.csv_path.exists():
        print(f"ERROR: {args.csv_path} does not exist. Run with --init first.", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(args.row_json_path.read_text(encoding="utf-8"))

    if not payload.get("Paper Title", "").strip():
        print("ERROR: payload must include a non-empty 'Paper Title'.", file=sys.stderr)
        sys.exit(1)

    unknown = [k for k in payload if k not in COLUMNS]
    if unknown:
        print(f"ERROR: unknown column(s): {unknown}\nValid: {COLUMNS}", file=sys.stderr)
        sys.exit(1)

    check_em_dash(payload)

    header, rows = load(args.csv_path)
    for c in COLUMNS:
        if c not in header:
            header.append(c)

    key = payload["Paper Title"].strip().lower()
    idx = next((i for i, r in enumerate(rows) if r.get("Paper Title", "").strip().lower() == key), None)

    if idx is not None:
        rows[idx].update({k: str(v) for k, v in payload.items()})
        action = "Updated"
    else:
        new = {c: "" for c in header}
        new.update({k: str(v) for k, v in payload.items()})
        rows.append(new)
        action = "Added"

    save(args.csv_path, header, rows)
    print(f"{action} row for '{payload['Paper Title']}'")


if __name__ == "__main__":
    main()
