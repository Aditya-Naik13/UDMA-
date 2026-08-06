#!/usr/bin/env python3
"""Update mechanisms.json with Food Justice support for the existing 6
mechanisms, plus one new mechanism (dignity as a designable, structural
property) that Food Justice unlocks and that also appears in the Equity
thread (Chapman et al. 2024). All additions read from the 15 Food Justice
papers directly, not keyword-matched."""
import json

with open("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/mechanisms.json") as f:
    data = json.load(f)
mechanisms = {m["name"]: m for m in data["mechanisms"]}

FJ = "Food Justice"
R = "Joy, Crystal"

def p(author, year):
    return {"thread": FJ, "reviewers": R, "author": author, "year": year}

# ---- Existing mechanism 1: Participation without power transfer ----
mechanisms["Participation without power transfer"]["papers"].extend([
    p("Cresswell Riol & Connelly", 2025),
    p("Joassart-Marcelli, Bosco, & McFadden", 2026),
])

# ---- Existing mechanism 3: Efficiency optimization crowds out purpose ----
mechanisms["Efficiency optimization crowds out purpose"]["papers"].extend([
    p("Joassart-Marcelli, Bosco, & McFadden", 2026),
    p("Deener", 2017),
])

# ---- Existing mechanism 4: Credentialed experts centered, communities counted ----
mechanisms["Credentialed experts centered, communities counted"]["papers"].extend([
    p("Murray, Gale, Adams, & Dalton", 2023),
    p("Shaker, Grineski, Collins, & Flores", 2023),
])

# ---- Existing mechanism 5: Friction as signal, not noise ----
mechanisms["Friction as signal, not noise"]["papers"].extend([
    p("Engelbutzeder, Bollmann, Berns, Landwehr, Randell, & Wulf", 2023),
])

# ---- Existing mechanism 6: Community-led alternatives outperform agency defaults ----
mechanisms["Community-led alternatives outperform agency defaults"]["papers"].extend([
    p("Gripper, Nethery, Cowger, White, Kawachi, & Adamkiewicz", 2022),
    p("Prost, Crivellaro, Haddon, & Comber", 2018),
    p("Heitlinger, Houston, Taylor, & Catlow", 2021),
])

# Mechanism 2 (Trust reduced to a calibratable metric): no Food Justice paper
# makes this claim directly; left as a 3-thread mechanism rather than forcing
# a weak link.

# ---- NEW mechanism 7: Dignity as a designable, structural property ----
new_mechanism = {
    "name": "Dignity as a designable, structural property",
    "definition": "Whether a service preserves or strips a recipient's dignity is treated as a concrete, structural design property of the service itself, not an unavoidable side effect of receiving help.",
    "papers": [
        p("Cresswell Riol & Connelly", 2023),
        p("Cresswell Riol & Connelly", 2025),
        p("Brenton, Tindall, Glanz, & Virudachalam", 2025),
        {"thread": "Equity", "reviewers": "Shashi, Aditya", "author": "Chapman et al.", "year": 2024},
    ],
}

ordered = list(mechanisms.values())
ordered.insert(6, new_mechanism)  # place as mechanism 7, after the existing 6

with open("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/mechanisms.json", "w") as f:
    json.dump({"mechanisms": ordered}, f, indent=2, ensure_ascii=False)

for m in ordered:
    threads = sorted({pp["thread"] for pp in m["papers"]})
    print(f"{m['name']}: {len(m['papers'])} papers across {len(threads)} threads ({', '.join(threads)})")
