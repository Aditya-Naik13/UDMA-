#!/usr/bin/env python3
"""
Insert or update one paper's row in the tracker CSV from a JSON file.

Why JSON-in, not CLI flags: RQ answers contain quotes, commas, and newlines.
Passing that through shell arguments is fragile and error-prone. Write the
row data to a small JSON file first, then call this script.

Usage:
    python csv_writer.py <csv_path> <row_json_path>

The JSON file should look like:
{
  "Paper_ID": "smith2020",
  "Paper_Name": "Transit Deserts and the Right to Mobility",
  "Authors": "Smith, J.; Doe, A.",
  "Year": "2020",
  "Journal": "Journal of Transport Geography",
  "DOI_Link": "https://doi.org/10.xxxx/xxxx",
  "RQ1": "Not addressed in this paper.",
  "RQ2": "Finding: <1-2 sentence answer>. Quote: \"<short supporting quote>\" (p. 4).",
  "Interesting_Perspective": "...",
  "RQs_Not_Addressed": "RQ5, RQ8",
  "Status": "Reviewed",
  "Date_Reviewed": "2026-07-13"
}

Only keys present in the JSON are written/updated — existing values for
other columns on that row are preserved. Matching is done on Paper_ID.
Any RQ column not present in the JSON and not already in the CSV is left
blank, NOT auto-filled — this script never invents content.
"""
import argparse
import csv
import json
import sys
from pathlib import Path


def load_rows(csv_path: Path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    return fieldnames, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("row_json_path", type=Path)
    args = parser.parse_args()

    if not args.csv_path.exists():
        print(f"ERROR: {args.csv_path} does not exist. Run init_csv.py first.", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(args.row_json_path.read_text(encoding="utf-8"))

    if "Paper_ID" not in payload or not payload["Paper_ID"]:
        print("ERROR: JSON payload must include a non-empty 'Paper_ID'.", file=sys.stderr)
        sys.exit(1)

    fieldnames, rows = load_rows(args.csv_path)

    unknown_keys = [k for k in payload if k not in fieldnames]
    if unknown_keys:
        print(f"ERROR: unknown column(s) not in CSV header: {unknown_keys}\n"
              f"Valid columns: {fieldnames}", file=sys.stderr)
        sys.exit(1)

    paper_id = payload["Paper_ID"]
    existing_idx = None
    for i, row in enumerate(rows):
        if row.get("Paper_ID") == paper_id:
            existing_idx = i
            break

    if existing_idx is not None:
        rows[existing_idx].update({k: str(v) for k, v in payload.items()})
        action = "Updated"
    else:
        new_row = {col: "" for col in fieldnames}
        new_row.update({k: str(v) for k, v in payload.items()})
        rows.append(new_row)
        action = "Added"

    with open(args.csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"{action} row for Paper_ID='{paper_id}' in {args.csv_path}")


if __name__ == "__main__":
    main()
