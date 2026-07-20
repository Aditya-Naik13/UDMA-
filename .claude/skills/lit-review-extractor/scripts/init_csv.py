#!/usr/bin/env python3
"""
Initialize the literature review tracker CSV with headers derived from
references/research_questions.md.

Usage:
    python init_csv.py <csv_path> [--rq-file <path>]

Safe to re-run: if the CSV already exists, does nothing (won't clobber data).
"""
import argparse
import csv
import re
import sys
from pathlib import Path

DEFAULT_RQ_FILE = Path(__file__).parent.parent / "references" / "research_questions.md"

FIXED_COLUMNS = [
    "Paper_ID",
    "Paper_Name",
    "Authors",
    "Year",
    "Journal",
    "DOI_Link",
]

TRAILING_COLUMNS = [
    "Interesting_Perspective",
    "RQs_Not_Addressed",
    "Status",
    "Date_Reviewed",
]


def parse_rq_ids(rq_file: Path) -> list[str]:
    """Extract RQ labels like RQ1, RQ2... from the research questions markdown file."""
    text = rq_file.read_text(encoding="utf-8")
    ids = re.findall(r"^\s*(?:\*\*)?RQ(\d+)", text, flags=re.MULTILINE)
    if not ids:
        raise ValueError(
            f"No 'RQ<number>' patterns found in {rq_file}. "
            "Each research question should start a line with e.g. 'RQ1.'"
        )
    # de-duplicate, preserve order
    seen = []
    for n in ids:
        label = f"RQ{n}"
        if label not in seen:
            seen.append(label)
    return seen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--rq-file", type=Path, default=DEFAULT_RQ_FILE)
    parser.add_argument("--force", action="store_true", help="Overwrite existing CSV")
    args = parser.parse_args()

    if args.csv_path.exists() and not args.force:
        print(f"{args.csv_path} already exists — leaving it alone. Use --force to overwrite.")
        sys.exit(0)

    rq_columns = parse_rq_ids(args.rq_file)
    headers = FIXED_COLUMNS + rq_columns + TRAILING_COLUMNS

    args.csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(args.csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

    print(f"Initialized {args.csv_path} with columns:\n  " + "\n  ".join(headers))


if __name__ == "__main__":
    main()
