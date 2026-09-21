# Codebook build: process record

This file records how the finalized codebook (Codebook_final.xlsx, Codebook_final.docx) was derived. It is the process artifact requested for this step: finalize the codes by taking the transcript-era maps and coding them further and differently with the literature now in hand.

Build date: 2026-09-20

## 1. Decisions locked in the brainstorm

- Purpose: paper findings architecture, not a coding-ops manual alone.
- Architecture: a topic-interleaved single tree (a mix of stacking the OG spine with the MaSS overlay and merging by theme). Nine findings domains plus a method block.
- Lit reviews enter in three ways: lit-informed names for existing codes, new lit-derived codes, and an evidence-map column tying every lit-grounded code to a thread, authors, and mechanism.
- New lit-derived domains: H (the discourse the AV carries, from the Engineering/Safety thread) and I (the charity model and digital food system, from the Food Justice thread).
- Capstone ideation (C01-C18) sits inside domain F as contrast (design team), split into five idea families.
- Method block stays (M1 AI instrument, M2 workshop and Insight Box).
- Naming: tags plus prose titles.
- Example quotes are seeded from existing corpus quotes with real locators (no fabrication); L-only codes carry a note pointing to the LitEvidenceMap instead.
- The xlsx includes the paper map domains to thesis clauses to paper sections.

### The paper thesis (clauses C1 to C7)

1. AVs are infrastructure, not simply transportation vehicles.
2. Infrastructure-scale technology typically arrives in communities without their input.
3. AVs carry efficiency-driven values inherited from transportation engineering.
4. Community concerns (equitable access, relational trust, flexibility for variable need) actually govern mobility in this context.
5. Efficiency-driven values are misaligned with those community concerns.
6. This misalignment reflects a broader pattern, not a one-off AV problem.
7. Mobility as Social Service: mobility as an ongoing, relational practice of equitable provisioning.

## 2. Sources

- Codebook/Codebook.docx: the original transcript codebook, 10 themes with sub-themes and evidence.
- Codebook/MaSS_Codebook xlsx.xlsx: the 16 deductive thesis codes (INFRA_FRAME to CONSTRAINTS).
- Codebook/maps/Capstone Fall 2025 Map.md: 18 ideation clusters (C01-C18) from the team workshop. The PDF version is ignored; the md is canonical.
- Codebook/maps/AV_Related_Ideas_From_Workshop.docx: participant crazy-8s ideation (input to the families).
- analysis/synthesis.md and analysis/coding-notes: the 34-transcript analysis; the source of every seeded quote.
- crosscomp/mechanisms.json: 7 cross-cutting mechanisms with per-thread papers.
- crosscomp/unified_lit_review.csv: the merged rows of the four thread trackers; the build resolves every mechanism citation in mechanisms.json to its actual row (author, year, DOI, journal, thread) so the LitEvidenceMap sheet cites papers directly rather than through the mechanism.
- crosscomp/thesis_clause_summary.csv: clause support percentages per thread.
- crosscomp/who_is_centered_counts.csv: centered-actor counts per thread.
- csvs/: the four original thread trackers that unified_lit_review.csv merges (Community & Equity Dimensions, Engineering & Safety, Food Justice / Pinyun, Participatory or speculative design). They are the paper-level citation layer on top of mechanisms.json; no code was invented from them, they supply the verbatim author-year-DOI detail behind every lit-derived code.

## 3. Derivation decisions worth keeping

- The 16 MaSS codes map onto the new tree in a crosswalk; none is lost. CAPABILITIES becomes A5. CONSTRAINTS dissolve into the D codes that own the constraint. MISALIGNMENT expands into the ten D codes. BREAKDOWN becomes a flag inside F, not a top-level code.
- The OG 10 themes map onto the tree theme by theme (Crosswalk_OG); the themes survive as provenance, not as the hierarchy.
- The 18 Capstone clusters map onto the idea families (Crosswalk_Capstone) and stay visible as the design team's contrast inside domain F.
- The two new domains came from mechanism-level evidence, not single papers:
   - H exists because the Engineering/Safety thread centers throughput, safety-as-engineering, and trust-as-metric (mechanisms 2, 3, 4), and who_is_centered_counts.csv shows a 0 community / 17 expert-regulator-researcher split in that thread.
   - I exists because the Food Justice thread supplies the mechanism behind what the transcripts only show as symptoms: charity reframes hunger as personal failing (Cresswell Riol and Connelly), conditionality and enforced gratitude, access optimized as an efficiency problem (Joassart-Marcelli, Deener), and food-apartheid geography (Shaker, Gripper).
- Domain E gained three lit-derived codes the transcripts cannot produce alone: E7 consultation without power, E8 performative vs authentic equity, E9 negative political self-efficacy (with sec-participant-01 as the local echo).
- Domain G gained the dignity-as-structural-property code (G4) from mechanism 7 and the community-co-governor code (G5) from mechanism 6.
- Domain C gained C7 community-built alternatives outperform agency defaults (mechanism 6).

## 4. Provenance and no-fabrication rules applied

- Every seeded example quote is verbatim from analysis/synthesis.md or a coding note, with its real locator. The build script verifies each quote body against the corpus before writing.
- Quotes from the 5 Spanish interviews are English translations and are marked 'translated'.
- L-only codes carry no invented transcripts quote; they point to the LitEvidenceMap.
- Author-year citations in lit evidence come from mechanisms.json resolved to the actual rows of unified_lit_review.csv (author string, DOI, journal, thread); the build prints a warning for any mechanism citation it cannot resolve, and nothing was guessed.
- No em dash in any codebook field (validated by the build).

## 5. Verification

- Quote bodies checked against analysis/coding-notes and analysis/synthesis.md (script does this).
- Lit citations checked two ways: the resolver reports any mechanism citation it cannot match to a paper row, and the built LitEvidenceMap is audited for paragraphs/DOIs that look broken.
- Crosswalks: all 16 MaSS codes, all 18 Capstone clusters, and the 10 OG themes appear in their crosswalk sheets. Audit by cross-ref the CODE column names.
- Em-dash scan on every generated field.
- Paper map: each domain cites its clause numbers from thesis_clause_summary.csv.

## 6. Rebuild

    python3 Codebook/process/build_codebook.py

The script regenerates all three outputs from the single source table at the top of the file. Edit the table, not the spreadsheets.
