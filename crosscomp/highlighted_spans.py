"""User-added yellow highlights from the reviewed final_report.docx (as of
2026-08-06 11:33), extracted so they can be preserved verbatim and
re-applied when the report is rebuilt with the Food Justice thread folded
in. Keyed by mechanism number (1-6, matching synthesis_narrative.md /
step6_final_report.py section order). Each value is an ordered list of
exact substrings that must remain, unmodified, inside that mechanism's
paragraph text."""

HIGHLIGHTS = {
    1: [
        "Formal participation shows up across all threads as a process that collects community input without transferring power over the final decision",
        "70 interested citizens to about 30 hand-picked representatives,",
        "performative equity",
        "public legitimacy route almost entirely through officials, consultants, and industry task-force members.",
        "participatory futuring generally includes mostly experts, and that even when publics are involved, the process is often not designed to empower them.",
    ],
    2: [
        "researchers measure and tune rather than something built relationally over time",
        "manufacturers can cultivate acceptance, routing the relational and societal bases of trust they find back to brand strategy rather than community authority.",
        "residents' non-participation directly to prior negative experiences, including one participant's public humiliation by a mayor, that taught them their input would not be needed",
    ],
    3: [
        "never ask who is traveling or why.",
        "people appearing only as anonymous origin-destination trip counts",
        "deep-learning allocation formula the authors themselves say lacks the community engagement needed to capture residents' actual perspectives.",
        "autonomous vehicles are being built to solve a different problem than the mobility problem people actually have",
    ],
    4: [
        "AV policy advice is written almost exclusively by “credentialed insiders,” state agency staff, legislative staff, and university researchers",
        "reduce travelers to anonymous vehicle-flow counts with no rider or community stakeholder anywhere in the model.",
        "synthesized entirely from published research rather than older travelers' own accounts,",
        "vulnerable groups as subjects appearing in literature rather than as participants in it.",
        "futuring research overwhelmingly includes experts and professionals instead of affected publics",
    ],
    5: [
        "argue that “design friction,” deliberately built-in disagreement, is not a flaw in a participatory process but the exact mechanism through which embedded values become visible and contestable.",
        "hitting similar friction against jargon-heavy planning tools.",
    ],
    6: [
        "describe a Bay Area coalition whose self-built regional transportation and land use scenario outperformed the metropolitan planning organization's",
    ],
}
