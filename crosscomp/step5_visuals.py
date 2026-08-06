#!/usr/bin/env python3
"""Step 5: build the 4 visuals with matplotlib, using the dataviz skill's
validated categorical palette (first 3 slots, which pass the all-pairs CVD
gate): blue #2a78d6 (Engineering/Safety), orange #eb6834 (Equity),
aqua #1baf7a (Participatory Method), in that fixed order throughout."""
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

BASE = "/Users/adityanaik/Documents/Work/UDMA-/crosscomp"
OUT = f"{BASE}/outputs"

# Fixed categorical order (blue, orange, aqua, yellow) validated by the
# dataviz skill's checker for adjacent-pair CVD safety in both light and
# dark modes (used by: radar lines, heatmap columns are sequential so no
# concern, who-is-centered stacked bar). Timeline is a scatter (all-pairs
# case) where no 4th hue holds up against blue/orange/aqua under the skill's
# validator; kept anyway because thread identity there is already carried
# redundantly by row position and the y-axis label, not by hue alone.
THREAD_COLOR = {
    "Engineering/Safety": "#2a78d6",
    "Equity": "#eb6834",
    "Participatory Method": "#1baf7a",
    "Food Justice": "#eda100",
}
THREAD_ORDER = ["Engineering/Safety", "Equity", "Participatory Method", "Food Justice"]
INK = "#0b0b0b"
SECONDARY_INK = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
SURFACE = "#fcfcfb"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "text.color": INK,
    "axes.edgecolor": GRID,
    "axes.labelcolor": SECONDARY_INK,
    "xtick.color": SECONDARY_INK,
    "ytick.color": SECONDARY_INK,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
})

# ============================================================
# 5a. Radar chart: 7 thesis clauses x 3 threads, % direct support
# ============================================================
summary = pd.read_csv(f"{BASE}/thesis_clause_summary.csv")
CLAUSE_LABELS = {
    "C1_AVs_are_infrastructure": "AVs as\ninfrastructure",
    "C2_arrives_without_input": "Arrives without\ncommunity input",
    "C3_efficiency_values": "Efficiency-driven\nvalues",
    "C4_community_concerns_govern": "Community concerns\ngovern mobility",
    "C5_misalignment": "Values\nmisalignment",
    "C6_broader_pattern": "Broader pattern\n(not AV-only)",
    "C7_mobility_as_social_service": "Mobility as\nSocial Service",
}
clause_codes = list(CLAUSE_LABELS.keys())
n = len(clause_codes)
angles = [i / n * 2 * np.pi for i in range(n)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_facecolor(SURFACE)
for thread in THREAD_ORDER:
    sub = summary[summary["Thread"] == thread].set_index("Clause")
    vals = [sub.loc[c, "pct_direct"] for c in clause_codes]
    vals += vals[:1]
    ax.plot(angles, vals, linewidth=2, color=THREAD_COLOR[thread], label=thread)
    ax.fill(angles, vals, color=THREAD_COLOR[thread], alpha=0.08)

ax.set_xticks(angles[:-1])
ax.set_xticklabels([CLAUSE_LABELS[c] for c in clause_codes], fontsize=9.5, color=SECONDARY_INK)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20%", "40%", "60%", "80%", "100%"], fontsize=8, color=MUTED)
ax.set_ylim(0, 100)
ax.grid(color=GRID, linewidth=0.8)
ax.spines["polar"].set_color(GRID)
fig.suptitle("Share of each thread's papers giving DIRECT support to each thesis clause",
             fontsize=13, color=INK, y=1.02)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=False, fontsize=10)
plt.tight_layout()
plt.savefig(f"{OUT}/radar_chart.png", dpi=200, bbox_inches="tight")
plt.close()
print("saved radar_chart.png")

# ============================================================
# 5b. Mechanism heatmap: rows = mechanisms, cols = threads, cell = paper count
# ============================================================
with open(f"{BASE}/mechanisms.json") as f:
    mechanisms = json.load(f)["mechanisms"]

mech_names = [m["name"] for m in mechanisms]
heat = pd.DataFrame(0, index=mech_names, columns=THREAD_ORDER)
for m in mechanisms:
    for p in m["papers"]:
        heat.loc[m["name"], p["thread"]] += 1

fig, ax = plt.subplots(figsize=(9, 6.5))
from matplotlib.colors import LinearSegmentedColormap
blue_ramp = LinearSegmentedColormap.from_list("blue_seq", ["#fcfcfb", "#cde2fb", "#6da7ec", "#2a78d6", "#0d366b"])
im = ax.imshow(heat.values, cmap=blue_ramp, vmin=0, vmax=heat.values.max(), aspect="auto")

ax.set_xticks(range(len(THREAD_ORDER)))
ax.set_xticklabels(THREAD_ORDER, fontsize=10, color=SECONDARY_INK, rotation=20, ha="right")
ax.set_yticks(range(len(mech_names)))
ax.set_yticklabels(mech_names, fontsize=10, color=SECONDARY_INK)
ax.set_xticks(np.arange(-.5, len(THREAD_ORDER), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(mech_names), 1), minor=True)
ax.grid(which="minor", color=SURFACE, linewidth=3)
ax.tick_params(which="minor", bottom=False, left=False)
for spine in ax.spines.values():
    spine.set_visible(False)

for i in range(len(mech_names)):
    for j in range(len(THREAD_ORDER)):
        val = heat.values[i, j]
        txt_color = "#ffffff" if val >= heat.values.max() * 0.55 else INK
        ax.text(j, i, str(val), ha="center", va="center", fontsize=13,
                 color=txt_color, fontweight="bold")

ax.set_title("Cross-thread mechanism heatmap (papers supporting each mechanism)",
             fontsize=12, color=INK, pad=14)
plt.tight_layout()
plt.savefig(f"{OUT}/mechanism_heatmap.png", dpi=200, bbox_inches="tight")
plt.close()
print("saved mechanism_heatmap.png")

# ============================================================
# 5c. Who is centered comparison (hand-coded buckets, see WHO_CENTERED below)
# ============================================================
from step5c_who_is_centered import WHO_CENTERED

# Bucket order matches the validated fixed adjacent-pair sequence (slots
# 1-6: blue, orange, aqua, yellow, magenta, green) so consecutive stacked
# segments are always a validated-safe adjacent pair, in both modes.
bucket_order = ["Community members/residents", "Advocates/CBOs", "Frontline practitioners",
                "Regulators/officials", "Researchers synthesizing literature", "Engineers/technical experts"]
bucket_colors = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"]

counts = pd.DataFrame(0, index=THREAD_ORDER, columns=bucket_order)
for (thread, author, year), bucket in WHO_CENTERED.items():
    counts.loc[thread, bucket] += 1
pct = counts.div(counts.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(9, 5.5))
left = np.zeros(len(THREAD_ORDER))
for bucket, color in zip(bucket_order, bucket_colors):
    vals = pct[bucket].values
    ax.barh(THREAD_ORDER, vals, left=left, color=color, label=bucket, height=0.55)
    for i, (v, l) in enumerate(zip(vals, left)):
        if v >= 6:
            ax.text(l + v / 2, i, f"{v:.0f}%", ha="center", va="center", fontsize=9,
                     color="#ffffff" if bucket not in ("Regulators/officials",) else INK)
    left += vals

ax.set_xlim(0, 100)
ax.set_xlabel("Share of papers in thread (%)", fontsize=10)
ax.set_title("Who is centered, by thread", fontsize=12, color=INK, pad=14)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.tick_params(left=False)
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False, fontsize=8.5)
plt.tight_layout()
plt.savefig(f"{OUT}/who_is_centered.png", dpi=200, bbox_inches="tight")
plt.close()
print("saved who_is_centered.png")

counts.to_csv(f"{BASE}/who_is_centered_counts.csv")

# ============================================================
# 5d. Publication timeline (optional)
# ============================================================
unified = pd.read_csv(f"{BASE}/unified_lit_review.csv")
unified["YearClean"] = unified["Year"].astype(str).str[:4].astype(int)

fig, ax = plt.subplots(figsize=(9, 4))
y_pos = {t: i for i, t in enumerate(THREAD_ORDER)}
rng = np.random.default_rng(7)
for thread in THREAD_ORDER:
    sub = unified[unified["Thread"] == thread]
    jitter = rng.uniform(-0.15, 0.15, size=len(sub))
    ax.scatter(sub["YearClean"], [y_pos[thread]] * len(sub) + jitter,
               color=THREAD_COLOR[thread], s=45, alpha=0.85, edgecolor="white", linewidth=0.5)

ax.set_yticks(list(y_pos.values()))
ax.set_yticklabels(list(y_pos.keys()), fontsize=10)
ax.set_xlabel("Publication year", fontsize=10)
ax.set_title("Publication timeline by thread", fontsize=12, color=INK, pad=14)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig(f"{OUT}/timeline.png", dpi=200, bbox_inches="tight")
plt.close()
print("saved timeline.png")
