#!/usr/bin/env python3
"""Step 2: cross-cutting mechanisms, hand-identified by reading Sub-theme,
Central claim, Key concepts, Who is centered, and Relevance to argument
across all 67 rows in the 3 loaded threads (Food Justice skipped this pass).
Every paper listed here was read directly; none are keyword-matched."""
import json

R = {"Engineering/Safety": "Amy, Saanvi", "Equity": "Shashi, Aditya", "Participatory Method": "Mariya"}

def p(thread, author, year):
    return {"thread": thread, "reviewers": R[thread], "author": author, "year": year}

mechanisms = [
    {
        "name": "Participation without power transfer",
        "definition": "Formal public involvement processes solicit community input through meetings, committees, or task forces, but rarely give that input binding influence over the final decision.",
        "papers": [
            p("Equity", "Pinski et al.", 2024),
            p("Equity", "Bailey et al.", 2012),
            p("Equity", "Karner et al.", 2020),
            p("Equity", "McCullough et al.", 2024),
            p("Equity", "van Holstein et al.", 2020),
            p("Equity", "Klaever et al.", 2025),
            p("Engineering/Safety", "Hicks, Kingsley, & Isett", 2025),
            p("Participatory Method", "Barendregt, Bendor, & van Eekelen", 2024),
        ],
    },
    {
        "name": "Trust reduced to a calibratable metric",
        "definition": "Trust in a system, whether an automated vehicle or a public agency, is measured and reported as an individual psychological score to be tuned rather than built and sustained through an ongoing relationship.",
        "papers": [
            p("Engineering/Safety", "Lee & Kolodge", 2020),
            p("Engineering/Safety", "Kraus, Scholz, Stiegemeier, & Baumann", 2020),
            p("Engineering/Safety", "Alkurdi & Alsaid", 2025),
            p("Engineering/Safety", "Zoellick, Kuhlmey, Schenk, Schindel, & Bluher", 2019),
            p("Equity", "Bailey et al.", 2010),
            p("Equity", "Klaever et al.", 2025),
            p("Equity", "Nakshi et al.", 2025),
            p("Participatory Method", "Tan, Soh, Zhang, Lee, Meng, Sen, & Lee", 2025),
        ],
    },
    {
        "name": "Efficiency optimization crowds out purpose",
        "definition": "Evaluation centers on network throughput, response time, or model fit, leaving unexamined who is actually traveling, why, and whether the optimized system serves their purpose.",
        "papers": [
            p("Engineering/Safety", "Park, Jang, & Ko", 2024),
            p("Engineering/Safety", "Lu, Tettamanti, Hörcher, & Varga", 2020),
            p("Engineering/Safety", "Zhang, de Winter, Varotto, Happee, & Martens", 2019),
            p("Engineering/Safety", "Pimenta, Kamruzzaman, & Currie", 2023),
            p("Equity", "Cha et al.", 2020),
            p("Equity", "Chen et al.", 2025),
            p("Equity", "Zhang et al.", 2024),
            p("Participatory Method", "Van Wynsberghe & Guimarães Pereira", 2022),
        ],
    },
    {
        "name": "Credentialed experts centered, communities counted",
        "definition": "The default 'who is centered' in both engineering-safety and top-down equity research is the professional, official, or researcher synthesizing data, not the resident whose mobility the system actually shapes.",
        "papers": [
            p("Engineering/Safety", "Hicks, Kingsley, & Isett", 2025),
            p("Engineering/Safety", "Lu, Tettamanti, Hörcher, & Varga", 2020),
            p("Engineering/Safety", "Robles & Mallinson", 2024),
            p("Equity", "Zhang et al.", 2024),
            p("Equity", "Jeghers et al.", 2024),
            p("Equity", "Chen et al.", 2025),
            p("Equity", "Di Ruocco", 2025),
            p("Participatory Method", "Barendregt, Bendor, & van Eekelen", 2024),
        ],
    },
    {
        "name": "Friction as signal, not noise",
        "definition": "Moments of resistance, confusion, or breakdown in an encounter with a technology or process, rather than smooth agreement, are where a community's actual values and their misalignment with imposed values become visible, if the people running the process choose to read them that way.",
        "papers": [
            p("Participatory Method", "Forlano & Mathew", 2014),
            p("Equity", "Klaever et al.", 2025),
            p("Equity", "Agrawaal et al.", 2024),
            p("Engineering/Safety", "Nordhoff, Stapel, van Arem, & Happee", 2020),
        ],
    },
    {
        "name": "Community-led alternatives outperform agency defaults",
        "definition": "When residents or community-based organizations are resourced to build their own plan, scenario, or design rather than only reacting to one, the resulting alternative can match or outperform the agency or industry default on the sponsor's own terms.",
        "papers": [
            p("Equity", "Karner et al.", 2020),
            p("Equity", "Gomes et al.", 2026),
            p("Equity", "Pineo et al.", 2026),
            p("Participatory Method", "Baumann, Caldwell, Bar, & Stokes", 2018),
            p("Participatory Method", "Severs, Wu, Diels, Harrow, Singleton, & Winsor", 2022),
            p("Participatory Method", "Sörries, Leimstädtner, & Müller-Birn", 2024),
        ],
    },
]

with open("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/mechanisms.json", "w") as f:
    json.dump({"mechanisms": mechanisms}, f, indent=2, ensure_ascii=False)

for m in mechanisms:
    threads = sorted({pp["thread"] for pp in m["papers"]})
    print(f"{m['name']}: {len(m['papers'])} papers across {len(threads)} threads ({', '.join(threads)})")
