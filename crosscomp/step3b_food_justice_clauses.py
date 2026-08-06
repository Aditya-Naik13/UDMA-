#!/usr/bin/env python3
"""Tag the 15 Food Justice papers against the 7 thesis clauses (reusing the
CLAUSES definitions and matrix-building logic from step3_clauses.py), and
append them to the existing 67-row thesis_clause_matrix.csv without
re-tagging the other 3 threads."""
import pandas as pd
import json

FJ = "Food Justice"
d = "direct"; p = "partial"; n = "none"
TAGS = {}

def t(author, year, **kw):
    TAGS[(FJ, author, year)] = kw

t("Lindemann, Alvial, & Alter", 2026,
  C1=(n,"Not about AVs"), C2=(p,"Political abandonment and deindustrialization as structural exclusion, not a single infrastructure-arrival event"),
  C3=(n,"No efficiency-values framing; racial capitalism framing instead"), C4=(d,"Community-driven visions for food sovereignty and resilience, elicited via listening sessions, are central"),
  C5=(p,"Implied misalignment between corporate food regime and community-defined needs"), C6=(d,"Connects to global racial capitalism and deindustrialization, a broad historical pattern beyond this one valley"),
  C7=(p,"Food sovereignty and resilience are relational and community-defined, food domain analog rather than mobility itself"))

t("Gripper, Nethery, Cowger, White, Kawachi, & Adamkiewicz", 2022,
  C1=(n,"Not about AVs"), C2=(n,"Not about infrastructure-technology arrival; documents existing spatial pattern"),
  C3=(n,"Not applicable"), C4=(d,"Urban agriculture as collective agency and community resistance is a direct community-concerns finding"),
  C5=(n,"Not a misalignment case; a positive counter-response finding"), C6=(p,"Pattern of community garden response to food apartheid, food-domain specific"),
  C7=(p,"Community gardens as ongoing, community-authored provisioning, food-domain analog to Mobility as Social Service"))

t("Murray, Gale, Adams, & Dalton", 2023,
  C1=(n,"Not about AVs"), C2=(n,"Scoping review of concepts, not a documented arrival-without-input case"),
  C3=(n,"Not applicable"), C4=(d,"Own text: acknowledges community participation and agency as critical for transformative change"),
  C5=(n,"Conceptual review, no specific misalignment case"), C6=(p,"Field-level review across five themes, food-domain specific"),
  C7=(n,"No relational-provisioning framing beyond noting participation as a theme"))

t("Cresswell Riol & Connelly", 2023,
  C1=(n,"Not about AVs"), C2=(d,"Colonization destroyed Maori food sovereignty; charity used to depoliticize hunger without community's own terms"),
  C3=(n,"Not an efficiency-values framing; a neoliberal/colonial critique instead"), C4=(p,"Argues food insecurity requires looking past neoliberal critique to deeper community history"),
  C5=(d,"Own text: charity's normalization vs the deeper structural needs it obscures"), C6=(d,"Colonialism and capitalism as deep historical roots, explicitly broader than any one policy"),
  C7=(n,"Historical/genealogical, not a relational-provisioning proposal itself"))

t("Engelbutzeder, Bollmann, Berns, Landwehr, Randell, & Wulf", 2023,
  C1=(n,"Not about AVs"), C2=(n,"Not about arrival without input; describes an active community negotiation process"),
  C3=(n,"Not applicable"), C4=(d,"Community building in food sharing depends on negotiating community-held conceptions of fairness"),
  C5=(n,"Not a misalignment case; documents ongoing negotiation rather than an imposed mismatch"), C6=(n,"Single local context (Siegen, Germany), not framed as a broader pattern"),
  C7=(d,"Food sharing as an ongoing, ICT-mediated relational practice negotiating fairness is close to the food-domain analog of Mobility as Social Service"))

t("Talhouk, Montague, Ghattas, Araujo-Soares, Ahmad, & Balaam", 2022,
  C1=(n,"Not about AVs"), C2=(n,"Documents coping strategies, not a specific arrival-without-input case"),
  C3=(n,"Not applicable"), C4=(d,"Adaptation, navigation, negotiation, and sharing are refugees' own community-held coping practices"),
  C5=(n,"Not a misalignment case"), C6=(n,"Single refugee community in rural Lebanon, limited generalizability per own text"),
  C7=(p,"Technology supporting resource sharing and new practices is a relational, ongoing provisioning concept in the food domain"))

t("Joassart-Marcelli, Bosco, & McFadden", 2026,
  C1=(n,"Not about AVs"), C2=(d,"Platforms reproduce individualized, market-based logics rather than being shaped by community-defined procedural inclusion"),
  C3=(d,"Own text: treats access as an efficiency problem, a direct efficiency-values framing, though for food platforms not transportation engineering"),
  C4=(d,"Judges platforms against recognition, redistribution, and procedural inclusion as the standard communities need"),
  C5=(d,"Own text: platforms fall short of food justice's recognition/redistribution/procedural-inclusion standard by optimizing for efficiency instead"),
  C6=(d,"Extends the food apartheid critique of food desert language into digital solutionism broadly, a named broader pattern"),
  C7=(p,"Names what provisioning should look like (recognition, redistribution, procedural inclusion) but the paper is critique-focused rather than proposing the ongoing relational model itself"))

t("Deener", 2017,
  C1=(p,"Frames food distribution as sociotechnical infrastructure explicitly, though not transportation/AV infrastructure"),
  C2=(d,"Own text: infrastructural exclusion severed residents from retail systems through decisions no single actor made, without their input"),
  C3=(d,"Path-dependent reorganization of distribution systems prioritizing efficiency of the retail network over resident access"),
  C4=(p,"Residents' historical dependence on retail systems is documented, though the paper is historical/structural rather than centering residents' present-day voice"),
  C5=(d,"Distribution system's path-dependent logic vs. residents' severed access is a clear structural misalignment"),
  C6=(d,"Explicitly a broader, non-food-specific claim about infrastructural exclusion as a general urban-inequality mechanism"),
  C7=(n,"Historical/structural analysis, not a relational-provisioning proposal"))

t("Shaker, Grineski, Collins, & Flores", 2023,
  C1=(n,"Not about AVs"), C2=(d,"Redlining-era lending policy shaped present-day access without residents' input, decades before the fact"),
  C3=(p,"Federal lending policy as a technical/actuarial logic overriding community need"), C4=(p,"Documents who bears the access gap, quantitatively rather than through resident voice"),
  C5=(d,"Historical racist policy vs. present-day residents' access needs is a clear structural misalignment"), C6=(d,"Explicit historical throughline from 1930s HOLC grading to present, a broad non-food-specific mechanism"),
  C7=(n,"Quantitative structural study, no relational-provisioning framing"))

t("Prost, Crivellaro, Haddon, & Comber", 2018,
  C1=(n,"Not about AVs"), C2=(p,"Argues HCI should design for systems change rather than individual behavior, implying current tools do not"),
  C3=(n,"Not an efficiency-values framing; argues for expanding past health/sustainability framing"), C4=(d,"Food democracy: who can participate in a food system depends on who can reach and shape it"),
  C5=(n,"Programmatic/agenda-setting paper, not a documented misalignment case"), C6=(p,"HCI-wide argument, food-domain specific though framed as generalizable design principle"),
  C7=(d,"Food democracy as social/economic justice and democratic governance in food systems closely parallels ongoing, relational, equitable provisioning"))

t("Cresswell Riol & Connelly", 2025,
  C1=(n,"Not about AVs"), C2=(d,"Charity system's conditionality was built and imposed on recipients without their voice in its design"),
  C3=(n,"Not an efficiency-values framing; a neoliberal-welfare critique"), C4=(d,"Argues dignity, autonomy, and choice, not just material sufficiency, are what should govern assistance"),
  C5=(d,"Own text: growth of food charity reframes insecurity as personal failing and undermines dignity via surveillance, enforced gratitude, and stigma"),
  C6=(d,"Frames this as reflecting broader neoliberal erosion of welfare generally, not specific to any one program"), C7=(p,"Argues for autonomy/choice/political voice in assistance, food-domain analog to relational provisioning"))

t("Brenton, Tindall, Glanz, & Virudachalam", 2025,
  C1=(n,"Not about AVs"), C2=(n,"Proposes a positive design framework rather than documenting an arrival-without-input case"),
  C3=(n,"Not applicable"), C4=(d,"Six components of a high-dignity food assistance experience are explicitly community/recipient-centered design criteria"),
  C5=(n,"Constructive framework paper, not itself a documented misalignment case"), C6=(p,"General dignity-in-assistance framework, food-domain specific"),
  C7=(d,"Dignity as a designable property of an ongoing service, including minimizing access burden, closely parallels Mobility as Social Service in the food domain"))

t("Boling & Cervini", 2023,
  C1=(n,"Not about AVs"), C2=(p,"Argues food decisions are treated as private/individual when they are properly public and systemically caused"),
  C3=(n,"Not an efficiency-values framing"), C4=(d,"Own text: food problems should be framed as collective matters demanding public remedy"),
  C5=(p,"Implies misalignment between individual-behavior framing and the actually public, systemic nature of the problem"), C6=(d,"General public-values argument extending beyond food specifically"),
  C7=(n,"Argumentative/philosophical, not a relational-provisioning proposal itself"))

t("Heitlinger, Houston, Taylor, & Catlow", 2021,
  C1=(n,"Not about AVs"), C2=(p,"Argues food system governance values need reconfiguring, implying current systems were not community-shaped"),
  C3=(p,"Critiques 'optimising distribution' as the current default logic to be moved past"), C4=(d,"Co-design surfaces communities' own alternative value regimes for the food system"),
  C5=(d,"Own text: contrasts reconfiguring embedded values against optimising distribution within existing values"), C6=(p,"HCI/food-domain specific framing, though the co-design-surfaces-values claim generalizes"),
  C7=(d,"Explicitly proposes co-design to reconfigure values in food system governance, a close food-domain parallel to Mobility as Social Service"))

t("Reese", 2019,
  C1=(n,"Not about AVs"), C2=(d,"Structural disinvestment shaped Black neighborhoods' food access without residents' input into that disinvestment"),
  C3=(n,"Not an efficiency-values framing; anti-Blackness and disinvestment framing instead"), C4=(d,"Residents' own everyday practices of self-reliance are framed as active agency, not passive lack"),
  C5=(d,"Deficit framings like 'food desert' misdescribe residents' actual strategic navigation of an unjust system"), C6=(d,"Own text: conceptual source underlying food apartheid framing broadly, explicitly general beyond one city"),
  C7=(p,"Self-reliance as ongoing strategic navigation is relational and agentive, a food-domain conceptual precursor"))

with open("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/_step3_fj.json", "w") as f:
    json.dump({f"{k[0]}|{k[1]}|{k[2]}": v for k, v in TAGS.items()}, f, indent=2, ensure_ascii=False)
print(f"Food Justice rows tagged: {len(TAGS)}")

CLAUSES = {
    "C1_AVs_are_infrastructure": "AVs are infrastructure, not simply transportation vehicles",
    "C2_arrives_without_input": "Infrastructure-scale technology typically arrives in communities without their input",
    "C3_efficiency_values": "AVs carry efficiency-driven values inherited from transportation engineering",
    "C4_community_concerns_govern": "Community concerns (equitable access, relational trust, flexibility for variable need) actually govern mobility in this context",
    "C5_misalignment": "Efficiency-driven values are misaligned with those community concerns",
    "C6_broader_pattern": "This misalignment reflects a broader pattern, not a one-off AV problem",
    "C7_mobility_as_social_service": "Mobility as Social Service: mobility as an ongoing, relational practice of equitable provisioning",
}

unified = pd.read_csv("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/unified_lit_review.csv")
fj_rows = unified[unified["Thread"] == "Food Justice"]

# Match by (year, first-author-lastname) since the tag keys use short-form
# author names while unified_lit_review.csv has the full author strings.
def lastname_key(author_str, year):
    first_author = str(author_str).split(",")[0].split("&")[0].strip()
    last = first_author.split()[-1]
    return (last.lower(), int(float(year)))

tags_by_lastname = {}
for (thread, author, year), tags in TAGS.items():
    tags_by_lastname[lastname_key(author, year)] = tags

new_matrix_rows = []
missing = []
for _, row in fj_rows.iterrows():
    lk = lastname_key(row["Author(s)"], row["Year"])
    tags = tags_by_lastname.get(lk)
    if tags is None:
        missing.append((row["Author(s)"], row["Year"]))
        continue
    out = {"Thread": row["Thread"], "Reviewers": row["Reviewers"], "Author(s)": row["Author(s)"],
           "Year": lk[1], "Paper Title": row["Paper Title"]}
    for code in CLAUSES:
        short = code.split("_")[0]
        out[code] = tags[short][0]
        out[code + "_reason"] = tags[short][1]
    new_matrix_rows.append(out)

if missing:
    print("MISSING KEYS:", missing)

existing_matrix = pd.read_csv("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/thesis_clause_matrix.csv")
new_matrix_df = pd.DataFrame(new_matrix_rows)
combined = pd.concat([existing_matrix, new_matrix_df], ignore_index=True)
combined.to_csv("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/thesis_clause_matrix.csv", index=False)
print(f"thesis_clause_matrix.csv now has {len(combined)} rows (was {len(existing_matrix)}, added {len(new_matrix_df)})")

# ---- Rebuild thesis_clause_summary.csv across all 4 threads ----
summary_rows = []
for thread in combined["Thread"].unique():
    sub = combined[combined["Thread"] == thread]
    n_papers = len(sub)
    for code, clause_text in CLAUSES.items():
        counts = sub[code].value_counts()
        summary_rows.append({
            "Thread": thread, "Clause": code, "Clause_text": clause_text,
            "n_papers": n_papers,
            "n_direct": int(counts.get("direct", 0)),
            "n_partial": int(counts.get("partial", 0)),
            "n_none": int(counts.get("none", 0)),
            "pct_direct": round(100 * counts.get("direct", 0) / n_papers, 1),
            "pct_direct_or_partial": round(100 * (counts.get("direct", 0) + counts.get("partial", 0)) / n_papers, 1),
        })
summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/thesis_clause_summary.csv", index=False)
print(f"thesis_clause_summary.csv rebuilt: {len(summary_df)} rows")
print(summary_df.pivot(index="Clause", columns="Thread", values="pct_direct"))
