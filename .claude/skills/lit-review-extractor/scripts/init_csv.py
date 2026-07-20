#!/usr/bin/env python3
"""
Initialize the literature review tracker CSV in the fixed 14-column format
(matching the reference "Engineering & Safety-dominant AV discourse" CSV
layout): a title row, then a header row, then data rows.

Usage:
    python init_csv.py <csv_path> "<Section Title>"

Example:
    python init_csv.py tracker.csv "Community & Equity Dimensions of Mobility Literature Review"

Safe to re-run: won't overwrite an existing file unless --force is passed.
"""
import argparse
import csv
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


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("section_title", type=str)
    parser.add_argument("--force", action="store_true", help="Overwrite existing CSV")
    args = parser.parse_args()

    if args.csv_path.exists() and not args.force:
        print(f"{args.csv_path} already exists — leaving it alone. Use --force to overwrite.")
        sys.exit(0)

    args.csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(args.csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        title_row = [args.section_title] + [""] * (len(COLUMNS) - 1)
        writer.writerow(title_row)
        writer.writerow(COLUMNS)

    print(f"Initialized {args.csv_path} with title '{args.section_title}' and columns:\n  " + "\n  ".join(COLUMNS))


if __name__ == "__main__":
    main()
