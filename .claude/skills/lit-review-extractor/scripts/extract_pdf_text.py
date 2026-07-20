#!/usr/bin/env python3
"""
Extract text from a PDF, page by page, with explicit page-number markers.

This exists so that when an answer is written into the CSV tracker, the
page number cited can be checked against real output instead of guessed.

Usage:
    python extract_pdf_text.py <pdf_path> [--out <txt_path>]

If --out is omitted, prints to stdout.
Requires poppler-utils (pdftotext) to be installed.
"""
import argparse
import subprocess
import sys
from pathlib import Path


def extract(pdf_path: Path) -> str:
    # -layout preserves reading order better than default mode.
    # pdftotext inserts a form-feed (\f) between pages.
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext failed on {pdf_path}: {result.stderr}")

    pages = result.stdout.split("\f")
    # Trailing empty page from final \f
    if pages and pages[-1].strip() == "":
        pages = pages[:-1]

    out = []
    for i, page_text in enumerate(pages, start=1):
        out.append(f"\n===== PAGE {i} =====\n")
        out.append(page_text.strip())
        out.append("\n")
    return "".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf_path", type=Path)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    if not args.pdf_path.exists():
        print(f"ERROR: file not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    text = extract(args.pdf_path)

    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"Wrote {len(text)} chars to {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
