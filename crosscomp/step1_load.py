#!/usr/bin/env python3
"""
Step 0-1: Load the three literature review trackers (Food Justice skipped
this pass, per user), normalize column-name mismatches between threads,
compute the shared schema, and save unified_lit_review.csv.
"""
import re
import pandas as pd
import openpyxl

BASE = "/Users/adityanaik/Documents/Work/UDMA-/csvs"

SOURCES = {
    "Engineering/Safety": {
        "path": f"{BASE}/Engineering & Safety-dominant AV Discourse Literature Review .xlsx",
        "reviewers": "Amy, Saanvi",
        "sheet": "in",
        "has_title_row": True,
    },
    "Equity": {
        "path": f"{BASE}/Community & Equity Dimensions of Mobility Literature Review.xlsx",
        "reviewers": "Shashi, Aditya",
        "sheet": None,
        "has_title_row": False,
    },
    "Participatory Method": {
        "path": f"{BASE}/Participatory or speculative design as method.xlsx",
        "reviewers": "Mariya",
        "sheet": None,
        "has_title_row": True,
    },
}


def normalize_colname(c):
    """Normalize for matching only: strip, drop trailing '?', lowercase."""
    return re.sub(r"\s+", " ", str(c).strip().rstrip("?").strip()).lower()


def load_thread(name, cfg):
    wb = openpyxl.load_workbook(cfg["path"], data_only=True)
    sheet = cfg["sheet"] or wb.sheetnames[0]
    header_row = 1 if cfg["has_title_row"] else 0
    df = pd.read_excel(cfg["path"], sheet_name=sheet, header=header_row)
    # Drop fully-empty columns/rows (e.g. merged-cell artifacts, stray "No" index col handled separately)
    df = df.dropna(axis=0, how="all")
    df = df[df["Paper Title"].notna()] if "Paper Title" in df.columns else df
    df["Thread"] = name
    df["Reviewers"] = cfg["reviewers"]
    return df


frames = {}
for name, cfg in SOURCES.items():
    df = load_thread(name, cfg)
    frames[name] = df
    print(f"{name}: {len(df)} papers, {len(df.columns)} columns")
    print(f"  columns: {list(df.columns)}")

# Build normalized -> canonical column name map (canonical = Equity's naming, our reference schema)
canonical_map = {}
for name, df in frames.items():
    for col in df.columns:
        if col in ("Thread", "Reviewers"):
            continue
        norm = normalize_colname(col)
        if norm not in canonical_map:
            canonical_map[norm] = col
# Prefer Equity's spelling as canonical where it exists
for col in frames["Equity"].columns:
    if col in ("Thread", "Reviewers"):
        continue
    canonical_map[normalize_colname(col)] = col

# Rename each frame's columns to canonical names
renamed = {}
for name, df in frames.items():
    rename_dict = {
        col: canonical_map[normalize_colname(col)]
        for col in df.columns
        if col not in ("Thread", "Reviewers")
    }
    renamed[name] = df.rename(columns=rename_dict)

# Compute shared column schema (normalized-name intersection, expressed via canonical names)
norm_sets = [
    {normalize_colname(c) for c in df.columns if c not in ("Thread", "Reviewers")}
    for df in renamed.values()
]
common_norm = set.intersection(*norm_sets)
common_columns = sorted(canonical_map[n] for n in common_norm)

print("\n=== COMMON COLUMNS (present in all 3 threads) ===")
for c in common_columns:
    print(" -", c)

print("\n=== DROPPED COLUMNS PER THREAD (thread-specific, excluded from unified table) ===")
dropped_report = {}
for name, df in renamed.items():
    thread_cols = {c for c in df.columns if c not in ("Thread", "Reviewers")}
    dropped = sorted(thread_cols - set(common_columns))
    dropped_report[name] = dropped
    print(f"{name}: {dropped}")

# Build unified_df
unified_cols = common_columns + ["Thread", "Reviewers"]
unified_frames = []
for name, df in renamed.items():
    sub = df[[c for c in unified_cols if c in df.columns]].copy()
    unified_frames.append(sub)
unified_df = pd.concat(unified_frames, ignore_index=True, sort=False)

out_path = "/Users/adityanaik/Documents/Work/UDMA-/crosscomp/unified_lit_review.csv"
unified_df.to_csv(out_path, index=False)
print(f"\nSaved {out_path} ({len(unified_df)} rows, {len(unified_df.columns)} columns)")

# Save per-thread full frames (with dropped columns retained) for later steps that need e.g. Who is centered
import pickle
with open("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/thread_frames.pkl", "wb") as f:
    pickle.dump(renamed, f)

# Save dropped-columns report
import json
with open("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/dropped_columns_report.json", "w") as f:
    json.dump(dropped_report, f, indent=2)
