#!/usr/bin/env python3
"""Step 6: assemble final_report.docx (the presentable deliverable) and
final_report.md (the git-tracked plain-text version)."""
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = "/Users/adityanaik/Documents/Work/UDMA-/crosscomp"
OUT = f"{BASE}/outputs"

INK = RGBColor(0x0b, 0x0b, 0x0b)
SECONDARY = RGBColor(0x52, 0x51, 0x4e)
MUTED = RGBColor(0x89, 0x87, 0x81)
BLUE = RGBColor(0x2a, 0x78, 0xd6)

THESIS = ("Autonomous vehicles are not simply transportation vehicles but infrastructure, yet they "
    "typically arrive in communities without those communities' input, carrying efficiency-driven "
    "values inherited from transportation engineering. In this case study, drawing on six co-design "
    "workshops with food pantry users, volunteers, system-level stakeholders, and experts, in which a "
    "speculative AV provocation surfaced how participants reasoned about mobility, we find that these "
    "efficiency-driven values are misaligned with the community concerns, equitable access, relational "
    "trust, flexibility for variable need, that actually govern mobility in this context. This "
    "misalignment reflects a broader pattern in how infrastructure-scale technologies arrive in "
    "communities without their participation in shaping what the technology is for. This paper "
    "introduces Mobility as Social Service, a concept grounded in this data that reframes mobility as "
    "an ongoing, relational practice of equitable provisioning, and offers concrete implications for "
    "designing AV-related infrastructure in social service contexts.")

CLAUSES_ORDERED = [
    ("C1_AVs_are_infrastructure", "1. AVs are infrastructure, not simply transportation vehicles"),
    ("C2_arrives_without_input", "2. Infrastructure-scale technology typically arrives in communities without their input"),
    ("C3_efficiency_values", "3. AVs carry efficiency-driven values inherited from transportation engineering"),
    ("C4_community_concerns_govern", "4. Community concerns (equitable access, relational trust, flexibility for variable need) actually govern mobility in this context"),
    ("C5_misalignment", "5. Efficiency-driven values are misaligned with those community concerns"),
    ("C6_broader_pattern", "6. This misalignment reflects a broader pattern, not a one-off AV problem"),
    ("C7_mobility_as_social_service", "7. Mobility as Social Service: mobility as an ongoing, relational practice of equitable provisioning"),
]

def set_cell_shading(cell, hex_color):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    cell._tc.get_or_add_tcPr().append(shd)

def add_caption(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.italic = True
    run.font.size = Pt(9.5)
    run.font.color.rgb = SECONDARY
    return p

doc = Document()

# ---- base style ----
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)
style.font.color.rgb = INK
style.paragraph_format.space_after = Pt(8)

# ---- Title ----
title = doc.add_heading("Cross-Thread Literature Synthesis", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub.add_run("Mobility as Social Service: synthesis across Engineering/Safety, Equity, and Participatory Method threads")
r.font.size = Pt(13)
r.font.color.rgb = SECONDARY
r.italic = True

note = doc.add_paragraph()
note.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = note.add_run("Food Justice thread skipped this pass. 67 papers: 17 Engineering/Safety (Amy, Saanvi), "
                 "39 Equity (Shashi, Aditya), 11 Participatory Method (Mariya).")
r.font.size = Pt(10)
r.font.color.rgb = MUTED
doc.add_page_break()

# ---- 1. Thesis ----
doc.add_heading("The Thesis", level=1)
p = doc.add_paragraph(THESIS)
p.paragraph_format.space_after = Pt(12)

# ---- 2. Narrative synthesis ----
doc.add_heading("Cross-Cutting Mechanisms: Narrative Synthesis", level=1)
doc.add_paragraph(
    "Six mechanisms recurred across at least two of the three threads, identified by reading each "
    "paper's Sub-theme, Central claim, Key concepts, Who is centered, and Relevance to argument "
    "directly, not by keyword matching. Four appear in all three threads; two appear in two."
).italic = True

sections = [
    ("1. Participation without power transfer",
     "Formal participation shows up across all three threads as a process that collects community input without transferring power over the final decision. In the Equity literature (Shashi & Aditya), this has a long institutional history: Pinski et al. (2024) find California's funded, explicitly inclusive community needs assessments reproduce the same representation gaps as conventional public meetings, and Bailey et al. (2012) document a Virginia DOT advisory committee that shrank from nearly 70 interested citizens to about 30 hand-picked representatives, a process the agency circulated as a model of good practice. McCullough et al. (2024) name the pattern directly, distinguishing performative equity, which claims inclusion without redistributing decision-making power, from authentic equity, which does. The Engineering/Safety literature (Amy & Saanvi) shows the same mechanism from the regulator's side: Hicks, Kingsley, and Isett (2025) find that even AV policy processes explicitly convened to build public legitimacy route almost entirely through officials, consultants, and industry task-force members. The Participatory Method literature (Mariya) confirms this is not specific to transportation: Barendregt, Bendor, and van Eekelen (2024) find participatory futuring generally includes mostly experts, and that even when publics are involved, the process is often not designed to empower them. This supports clause 2 (infrastructure arrives without input) and clause 5 (efficiency values misaligned with community concerns). Finding the same failure mode independently in AV policy, decades of transportation equity cases, and a general HCI review rules out the explanation that this is one field's quirk or one agency's bad faith."),
    ("2. Trust reduced to a calibratable metric",
     "Trust recurs across the threads as something researchers measure and tune rather than something built relationally over time. In the Engineering/Safety literature (Amy & Saanvi), trust in automated vehicles is operationalized almost entirely as a scalar to calibrate: Kraus, Scholz, Stiegemeier, and Baumann (2020) model trust as a value that climbs and dips with system performance and can be shielded from dips through advance disclosure, while Lee and Kolodge (2020) reverse-engineer trust from survey comments specifically so manufacturers can cultivate acceptance, routing the relational and societal bases of trust they find back to brand strategy rather than community authority. The Equity literature (Shashi & Aditya) treats trust as a governing community concern instead: Bailey et al. (2010) find a persistent Arnstein Gap, where surveyed professionals report public involvement working better than the public itself experiences, and Klaever et al. (2025) trace Berlin residents' non-participation directly to prior negative experiences, including one participant's public humiliation by a mayor, that taught them their input would not be heeded. The Participatory Method literature (Mariya) shows what changes when trust is treated relationally instead: Tan et al. (2025) find co-design workshops with frontline social service workers reliably surface exactly the relational-trust concerns standard requirements-gathering misses. That the same reduction appears in a driving simulator, a Berlin street-redesign process, and a healthcare AI workshop shows this is a general property of how technical systems get evaluated, not an incidental feature of one domain."),
    ("3. Efficiency optimization crowds out purpose",
     "The literature repeatedly organizes evaluation around network-level efficiency metrics that never ask who is traveling or why. In the Engineering/Safety thread (Amy & Saanvi), this is close to universal within the throughput sub-theme: Lu, Tettamanti, Hörcher, and Varga (2020) model urban traffic capacity gains from automated vehicles with people appearing only as anonymous origin-destination trip counts, and Park, Jang, and Ko (2024) evaluate exclusive AV lanes purely by the automation share needed to maximize network efficiency. The Equity thread (Shashi & Aditya) documents the same reduction applied to equity itself: Cha et al. (2020) solve transit-stop placement as a pure spatial coverage problem with, by the authors' own account, no role for transport-disadvantaged residents in defining need, and Chen et al. (2025) model infrastructure-investment equity with a deep-learning allocation formula the authors themselves say lacks the community engagement needed to capture residents' actual perspectives. The Participatory Method thread (Mariya) names the resulting mismatch directly: Van Wynsberghe and Guimarães Pereira (2022) argue autonomous vehicles are being built to solve a different problem than the mobility problem people actually have, discovered only once citizens were given room to define the problem themselves. This supports clause 3 and clause 5 most sharply because it shows the same optimization logic applied unreflectively even inside research explicitly framed around equity."),
    ("4. Credentialed experts centered, communities counted",
     "Across the literature, the default answer to “who is centered” is the credentialed professional or researcher synthesizing data, not the resident whose mobility the system shapes. In the Engineering/Safety thread (Amy & Saanvi), Hicks, Kingsley, and Isett (2025) find AV policy advice is written almost exclusively by “credentialed insiders,” state agency staff, legislative staff, and university researchers, while Lu et al. (2020) reduce travelers to anonymous vehicle-flow counts with no rider or community stakeholder anywhere in the model. The Equity thread (Shashi & Aditya) shows the identical default inside research meant to serve underserved groups: Zhang et al.'s (2024) systematic review of elderly transport inclusion is synthesized entirely from published research rather than older travelers' own accounts, Jeghers et al. (2024) interview transportation professionals about mobility-vulnerable populations rather than those populations themselves, and Di Ruocco (2025) reviews vulnerable groups as subjects appearing in literature rather than as participants in it. The Participatory Method thread (Mariya) confirms this is a field-wide pattern rather than a transportation-specific one: Barendregt, Bendor, and van Eekelen (2024) find participatory futuring research overwhelmingly includes experts and professionals instead of affected publics. This directly supports clause 2 and clause 4: infrastructure keeps arriving without community input partly because research and policy are built, by default, around whose voice already counts as expertise."),
    ("5. Friction as signal, not noise",
     "A smaller but pointed pattern appears where resistance, confusion, or breakdown in an encounter with a technology or process becomes the moment a community's actual values surface, if the people running the process are willing to read it that way. The Participatory Method thread (Mariya) names this explicitly: Forlano and Mathew (2014) argue that “design friction,” deliberately built-in disagreement, is not a flaw in a participatory process but the exact mechanism through which embedded values become visible and contestable. The Equity thread (Shashi & Aditya) shows the same dynamic inside a real planning process: Klaever et al. (2025) find Berlin residents' withdrawal from official participatory venues, following experiences like public humiliation by a mayor, revealed exactly the trust deficit the process claimed to fix, while Agrawaal et al. (2024) find Canadian advocates hitting similar friction against jargon-heavy planning tools. The Engineering/Safety thread (Amy & Saanvi) offers a mirror image: Nordhoff, Stapel, van Arem, and Happee (2020) describe pedestrians and cyclists “testing” an automated shuttle, stepping in front of it or pressing its emergency button, and find the field's response is to read this as distrust or a problem to manage, up to flagging non-compliant road users to police, rather than as informative signal. Together these support clause 4 and clause 5: the same friction one thread treats as the richest available data about community values, another treats as noise to engineer away."),
    ("6. Community-led alternatives outperform agency defaults",
     "The literature also contains a more hopeful, cross-thread finding: when residents or community organizations are resourced to build their own alternative rather than only react to one, it can match or beat the agency or industry default on its own terms. In the Equity thread (Shashi & Aditya), Karner et al. (2020) describe a Bay Area coalition whose self-built regional transportation and land use scenario outperformed the metropolitan planning organization's preferred alternative on the agency's own environmental review and won funding concessions, alongside a Fresno community-led needs assessment that won a dedicated grant program. Gomes et al. (2026) find that reinterpreting the 15-Minute City model collaboratively with citizens, rather than applying it as a fixed template, surfaced priorities, trust in transit reliability and safe pedestrian access, that top-down planning had missed. The Participatory Method thread (Mariya) supplies the mechanism for why this works at the design stage: Severs et al. (2022) find participatory workshops with transport-excluded groups produce real, usable design insight for shared autonomous vehicle interiors, and Sörries, Leimstädtner, and Müller-Birn (2024) show a structured workshop method reliably converting vulnerable stakeholders' values into concrete design requirements. This bears most directly on clause 5 and clause 7: both threads independently show that closing the gap between efficiency-driven defaults and community concerns is achievable, not merely diagnostic, which is exactly the constructive claim the paper's Mobility as Social Service reframing depends on."),
]

for heading, body in sections:
    doc.add_heading(heading, level=2)
    doc.add_paragraph(body)

doc.add_page_break()

# ---- 3. Visuals ----
doc.add_heading("Visuals", level=1)

doc.add_heading("Thesis-clause support by thread", level=2)
doc.add_picture(f"{OUT}/radar_chart.png", width=Inches(5.8))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
add_caption(doc, "Share of each thread's papers giving DIRECT support to each of the 7 thesis clauses. "
                  "Engineering/Safety peaks only on efficiency-driven values and AVs-as-infrastructure; Equity "
                  "and Participatory Method both peak on community concerns governing mobility and misalignment, "
                  "the two clauses Engineering/Safety barely touches.")

doc.add_heading("Cross-thread mechanism heatmap", level=2)
doc.add_picture(f"{OUT}/mechanism_heatmap.png", width=Inches(5.8))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
add_caption(doc, "Count of papers per mechanism per thread. The top four mechanisms are populated in all three "
                  "threads (genuinely cross-cutting); the bottom mechanism, community-led alternatives, is Equity- "
                  "and Participatory-only, with zero Engineering/Safety support.")

doc.add_heading("Who is centered, by thread", level=2)
doc.add_picture(f"{OUT}/who_is_centered.png", width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
add_caption(doc, "Engineering/Safety centers engineers, regulators, and researchers exclusively (0% community "
                  "members). Equity centers community members and advocates in 61% of its papers. Participatory "
                  "Method centers community members and frontline practitioners in 54%. Participatory Method has "
                  "no Who-is-centered column; its buckets are inferred from Central claim and Relevance to "
                  "argument text and flagged as such.")

doc.add_heading("Publication timeline", level=2)
doc.add_picture(f"{OUT}/timeline.png", width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
add_caption(doc, "Optional. Equity is the oldest and most continuous body of evidence (2010 to 2026); "
                  "Engineering/Safety and Participatory Method are both concentrated in the last 8 years.")

doc.add_page_break()

# ---- 4. Thesis-clause summary table ----
doc.add_heading("Thesis-Clause Summary Table", level=1)
doc.add_paragraph("Percent of each thread's papers giving DIRECT support to each clause (n_papers in parentheses).").italic = True

summary = pd.read_csv(f"{BASE}/thesis_clause_summary.csv")
threads = ["Engineering/Safety", "Equity", "Participatory Method"]
n_papers = {t: summary[summary.Thread == t].iloc[0]["n_papers"] for t in threads}

table = doc.add_table(rows=1, cols=4)
table.style = "Light Grid Accent 1"
table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr = table.rows[0].cells
hdr[0].text = "Thesis clause"
for i, t in enumerate(threads):
    hdr[i + 1].text = f"{t} (n={n_papers[t]})"
for cell in hdr:
    for p in cell.paragraphs:
        for r in p.runs:
            r.bold = True

for code, label in CLAUSES_ORDERED:
    row = table.add_row().cells
    row[0].text = label
    for i, t in enumerate(threads):
        pct = summary[(summary.Thread == t) & (summary.Clause == code)].iloc[0]["pct_direct"]
        row[i + 1].text = f"{pct:.0f}%"
        row[i + 1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_page_break()

# ---- 5. Gaps ----
doc.add_heading("Gaps", level=1)

doc.add_heading("Thinnest thesis clauses across all three threads combined", level=2)
doc.add_paragraph(
    "Two clauses are markedly thinner than the rest once all 67 papers are pooled: "
    "clause 1 (AVs are infrastructure, not simply vehicles), only 11.9% direct / 26.9% direct-or-partial, "
    "and clause 7 (Mobility as Social Service), only 10.4% direct / 38.8% direct-or-partial. "
    "This is expected rather than alarming: clause 1 is inherently AV-specific, and the Equity thread "
    "(39 of the 67 papers) is almost entirely about existing, non-AV transportation infrastructure, so "
    "it can rarely speak to AVs directly. Clause 7 is the paper's own novel contribution; by definition, "
    "existing literature was not written to evidence a concept this paper is introducing. Neither gap is "
    "a weakness in the literature review so much as a reminder that clauses 1 and 7 will need to be carried "
    "primarily by the paper's own workshop data and argument, not by secondary literature. If either needs "
    "more secondary support, the Engineering/Safety thread (which alone reaches 35% partial-or-direct on "
    "clause 1) and papers explicitly proposing ongoing, relational models (Karner et al. 2020's transportation "
    "justice framework; Wander et al. 2026's Universal Basic Mobility) are the strongest existing anchors for "
    "clause 7 and are worth leaning on harder in the write-up."
)

doc.add_heading("Mechanisms present in only 2 of 3 threads", level=2)
doc.add_paragraph(
    "Community-led alternatives outperform agency defaults is well evidenced in the Equity thread (Karner "
    "et al. 2020, Gomes et al. 2026, Pineo et al. 2026) and the Participatory Method thread (Baumann et al. "
    "2018, Severs et al. 2022, Sörries et al. 2024), but has zero support in Engineering/Safety, whose "
    "papers are almost entirely diagnostic rather than solution-oriented. This is not necessarily a gap to "
    "fill: the Engineering/Safety literature may simply not contain constructive, community-led counter-"
    "examples because that is not what the sub-field studies. Worth flagging to Amy and Saanvi in case a "
    "relevant paper was screened out rather than genuinely absent from the field."
)

doc.add_heading("Thread not yet included", level=2)
doc.add_paragraph(
    "The Food Justice thread (Joy, Crystal) was skipped this pass at the user's request. Given the paper's "
    "case study is set in a food pantry, re-running Steps 1 through 6 once that tracker is available is "
    "likely to change both the mechanism list and the clause 4 and clause 7 numbers more than any other "
    "single addition would."
)

doc.save(f"{BASE}/final_report.docx")
print("Saved final_report.docx")
