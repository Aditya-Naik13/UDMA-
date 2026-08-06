#!/usr/bin/env python3
"""Add the Food Justice thread (Joy, Crystal) to the existing 3-thread
unified table, reusing the already-loaded/tagged Engineering/Safety, Equity,
and Participatory Method frames rather than reloading them.

Food Justice source has 15 papers total: 14 in the 'Table 1' sheet plus one
orphaned row (Reese, 2019) sitting in a second sheet 'x' with no header row
and missing its Quotable moment / Synthesis paragraph fields, both left as
'Not provided in source tracker' per the no-fabrication rule rather than
invented.

Six of the 14 'Table 1' rows are shaded cream in the source workbook
(Lindemann et al. 2026, Gripper et al. 2022, Murray et al. 2023, Cresswell
Riol & Connelly 2023, Engelbutzeder et al. 2023, Talhouk et al. 2022); the
user did not specify what this marks, so it is recorded as a boolean flag
column (WorkbookHighlighted) without asserting a meaning, rather than
silently dropped or guessed at.
"""
import re
import json
import pickle
import pandas as pd
import openpyxl

BASE = "/Users/adityanaik/Documents/Work/UDMA-"
CSV_DIR = f"{BASE}/csvs"
OUT = f"{BASE}/crosscomp"

FJ_PATH = f"{CSV_DIR}/Food Justice Food Security Literature Review_Pinyun.xlsx"

def normalize_colname(c):
    return re.sub(r"\s+", " ", str(c).strip().rstrip("?").strip()).lower()

# ---- Load Table 1 (14 papers), detect highlighted rows ----
df_main = pd.read_excel(FJ_PATH, sheet_name="Table 1", header=0)
df_main = df_main.dropna(subset=["Paper Title"]).copy()

wb = openpyxl.load_workbook(FJ_PATH, data_only=True)
ws = wb["Table 1"]
highlighted_rows = set()
for r in range(2, 2 + len(df_main)):
    cell = ws.cell(row=r, column=2)  # Paper Title column
    if cell.fill and cell.fill.patternType == "solid" and cell.fill.fgColor.rgb == "FFFFF7E2":
        highlighted_rows.add(r)
df_main["WorkbookHighlighted"] = [ (2 + i) in highlighted_rows for i in range(len(df_main)) ]
df_main = df_main.drop(columns=["#"])

# ---- Load the orphaned 15th paper from sheet 'x' ----
x_row = pd.read_excel(FJ_PATH, sheet_name="x", header=None).iloc[0]
# Column order in sheet x (no header): Paper Title, Author(s), Year,
# Journal or Proceedings, DOI or URL, Sub-theme, [blank Summary],
# Central claim, Key concepts or framework, Relevance to argument, Gap or limitation
orphan = {
    "Paper Title": x_row[0],
    "Author(s)": x_row[1],
    "Year": x_row[2],
    "Journal or Proceedings": x_row[3],
    "DOI or URL": x_row[4],
    "Sub-theme": x_row[5],
    "Summary": None,
    "Central claim": x_row[7],
    "Key concepts or framework": x_row[8],
    "Relevance to argument": x_row[9],
    "Gap or limitation": x_row[10],
    "Quotable moment": "Not provided in source tracker",
    "Synthesis paragraph": "Not provided in source tracker",
    "WorkbookHighlighted": False,
}
df_orphan = pd.DataFrame([orphan])

df_fj = pd.concat([df_main, df_orphan], ignore_index=True)
df_fj["Thread"] = "Food Justice"
df_fj["Reviewers"] = "Joy, Crystal"

print(f"Food Justice: {len(df_fj)} papers loaded ({len(df_main)} from Table 1 + 1 orphaned)")
print(f"  Workbook-highlighted rows: {df_fj['WorkbookHighlighted'].sum()}")

# ---- Rename to canonical column names (reuse Step 1's mapping logic) ----
with open(f"{OUT}/thread_frames.pkl", "rb") as f:
    existing_frames = pickle.load(f)

canonical_map = {}
for name, df in existing_frames.items():
    for col in df.columns:
        if col in ("Thread", "Reviewers"):
            continue
        canonical_map[normalize_colname(col)] = col
# Equity's spelling stays canonical (matches Step 1 precedent)
for col in existing_frames["Equity"].columns:
    if col in ("Thread", "Reviewers"):
        continue
    canonical_map[normalize_colname(col)] = col

rename_dict = {}
for col in df_fj.columns:
    if col in ("Thread", "Reviewers", "WorkbookHighlighted"):
        continue
    norm = normalize_colname(col)
    rename_dict[col] = canonical_map.get(norm, col)
df_fj = df_fj.rename(columns=rename_dict)

existing_frames["Food Justice"] = df_fj
with open(f"{OUT}/thread_frames.pkl", "wb") as f:
    pickle.dump(existing_frames, f)

# ---- Recompute common columns across all 4 threads ----
norm_sets = [
    {normalize_colname(c) for c in df.columns if c not in ("Thread", "Reviewers", "WorkbookHighlighted")}
    for df in existing_frames.values()
]
common_norm = set.intersection(*norm_sets)
common_columns = sorted(canonical_map[n] for n in common_norm)
print("\nCommon columns across all 4 threads:", common_columns)

dropped_report = {}
for name, df in existing_frames.items():
    thread_cols = {c for c in df.columns if c not in ("Thread", "Reviewers", "WorkbookHighlighted")}
    dropped_report[name] = sorted(thread_cols - set(common_columns))
print("\nDropped columns per thread:")
for k, v in dropped_report.items():
    print(f"  {k}: {v}")

with open(f"{OUT}/dropped_columns_report.json", "w") as f:
    json.dump(dropped_report, f, indent=2)

# ---- Rebuild unified_lit_review.csv across all 4 threads ----
unified_cols = common_columns + ["Thread", "Reviewers"]
unified_frames = []
for name, df in existing_frames.items():
    sub = df[[c for c in unified_cols if c in df.columns]].copy()
    unified_frames.append(sub)
unified_df = pd.concat(unified_frames, ignore_index=True, sort=False)
unified_df.to_csv(f"{OUT}/unified_lit_review.csv", index=False)
print(f"\nSaved unified_lit_review.csv: {len(unified_df)} rows, {len(unified_df.columns)} columns")
print(unified_df["Thread"].value_counts())
