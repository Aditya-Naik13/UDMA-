"""
Review-workbook builder for the EFF_VALUE and MISALIGNMENT codebook section.

Source of truth: Codebook/Output/EFF_VALUE_MISALIGNMENT_draft.md (edit that, not the xlsx).
Context:         Codebook/Output/MaSS_Codebook_with_subcodes.xlsx (team file, read only).

Run:  python3 Codebook/process/build_eff_misalignment_review.py
Output:
  Codebook/Output/MaSS_Codebook_with_subcodes_EFF_MISALIGNMENT_review.xlsx

Checks run on every build:
  - no em dash in any field written from the draft (build fails)
  - every quoted transcript phrase is found verbatim in transcripts/ (warns)
  - the draft's summary table lists the same codes as its sections (warns)
"""

import glob
import math
import os
import re
import sys
import zipfile
from copy import copy

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Codebook/
REPO = os.path.dirname(BASE)
DRAFT = os.path.join(BASE, "Output", "EFF_VALUE_MISALIGNMENT_draft.md")
TEAM_XLSX = os.path.join(BASE, "Output", "MaSS_Codebook_with_subcodes.xlsx")
OUT = os.path.join(BASE, "Output", "MaSS_Codebook_with_subcodes_EFF_MISALIGNMENT_review.xlsx")
OWNED_PARENTS = ("EFF_VALUE", "MISALIGNMENT")

NAVY, LIME, SUBBLUE = "1F4E78", "C3FF65", "EEF4FA"
NEW_FILL, REWORDED_FILL, KEPT_FILL = "FFF2CC", "FCE4D6", "E2EFDA"
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(top=THIN, bottom=THIN, left=THIN, right=THIN)
HFONT = Font(name="Arial", size=11, bold=True, color="FFFFFF")
BFONT = Font(name="Arial", size=10)
BOLD = Font(name="Arial", size=10, bold=True)
WRAP = Alignment(wrap_text=True, vertical="top")

FIELD_KEYS = [
    ("key concept", "kc"),
    ("status", "status"),
    ("literature strength", "ls"),
    ("transcript strength", "ts"),
    ("current definition", "current"),
    ("proposed definition", "proposed"),
    ("definition", "proposed"),
    ("include when", "include"),
    ("exclude when", "exclude"),
    ("related coding", "related"),
    ("example quotes", "quotes"),
    ("counter-voice", "counter"),
    ("literature", "lit"),
    ("why it matters", "why"),
    ("coding note", "why"),
    ("note", "why"),
    ("feedback", None),
]


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

def clean(text):
    text = text.replace("`", "")
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", text)
    return text


def join_block(lines):
    """Join field lines, putting a blank line between numbered list items."""
    out = []
    for ln in lines:
        s = ln.rstrip()
        if not s:
            continue
        if re.match(r"^\d+\.\s", s) and out:
            out.append("")
        out.append(clean(s))
    return "\n".join(out).strip()


def field_key(label):
    low = label.lower()
    for prefix, key in FIELD_KEYS:
        if low.startswith(prefix):
            return key, label
    return "why", label


def parse_draft(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    doc = {"title": clean(lines[0].lstrip("# ").strip()), "codes": [], "lists": {}, "intro": [], "summary_table": []}
    code, field, buf, label = None, None, [], None
    section = None
    list_items = None

    def flush_field():
        nonlocal field, buf, label
        if code is not None and field:
            text = join_block(buf)
            if field == "counter":
                text = clean(label) + ":\n" + text
                code["quotes"] = (code.get("quotes", "") + "\n\n" + text).strip()
            elif field in ("why", "proposed") and code.get(field):
                code[field] += "\n\n" + text
            else:
                code[field] = text
        field, buf, label = None, [], None

    for ln in lines[1:]:
        m_parent = re.match(r"^# Parent code:\s*(\w+)", ln)
        m_sub = re.match(r"^### (\w+) > (\w+)", ln)
        m_h2 = re.match(r"^## (.+)", ln)
        if m_parent or m_sub or m_h2 or ln.strip() == "---":
            flush_field()
            if code is not None:
                doc["codes"].append(code)
                code = None
            if m_parent:
                code = {"parent": m_parent.group(1), "sub": ""}
            elif m_sub:
                code = {"parent": m_sub.group(1), "sub": m_sub.group(2)}
            if m_h2:
                section = m_h2.group(1).strip()
                list_items = None
            elif m_parent or m_sub:
                section = None
            continue

        if code is not None:
            m_field = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", ln)
            if m_field:
                flush_field()
                field, label = field_key(m_field.group(1))
                buf = [m_field.group(2)] if m_field.group(2) else []
            elif field:
                buf.append(ln)
            continue

        if section is None:
            continue
        if section.lower().startswith(("decision log", "evidence corrections", "open questions")):
            m_item = re.match(r"^(\d+)\.\s+(.*)", ln)
            if m_item:
                list_items = doc["lists"].setdefault(section, [])
                list_items.append(clean(m_item.group(2)))
            elif ln.strip() and list_items:
                list_items[-1] += " " + clean(ln.strip())
        elif section.lower().startswith("summary"):
            if ln.startswith("|") and not re.match(r"^\|\s*-", ln):
                cells = [clean(c.strip()) for c in ln.strip("|").split("|")]
                if cells[0] != "Parent":
                    doc["summary_table"].append(cells)
        else:
            doc["intro"].append((section, ln))

    flush_field()
    if code is not None:
        doc["codes"].append(code)
    return doc


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_no_em_dash(doc):
    bad = []
    for c in doc["codes"]:
        for k, v in c.items():
            if isinstance(v, str) and "\u2014" in v:
                bad.append(f"{c['parent']} > {c['sub'] or '(parent)'}: {k}")
    if bad:
        sys.exit("Em dash found in draft fields (not allowed):\n  " + "\n  ".join(bad))


def docx_text(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = re.sub(r"</w:p>", "\n", xml)
    return re.sub(r"<[^>]+>", "", xml)


def normalize(s):
    s = (s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
          .replace("&amp;", "&").replace("&apos;", "'").replace("&quot;", '"'))
    s = re.sub(r"[\"']", "", s)
    return re.sub(r"\s+", " ", s).lower().strip()


def load_corpus():
    texts = []
    for p in glob.glob(os.path.join(REPO, "transcripts", "**", "*"), recursive=True):
        if p.endswith(".txt"):
            texts.append(open(p, encoding="utf-8", errors="replace").read())
        elif p.endswith(".docx"):
            texts.append(docx_text(p))
    return normalize("\n".join(texts))


def check_quotes(doc):
    corpus = load_corpus()
    missing = []
    for c in doc["codes"]:
        for field in ("quotes", "exclude"):
            for q in re.findall(r"\"([^\"]+)\"", c.get(field, "")):
                for part in q.split("..."):
                    part = part.strip(" .")
                    if len(part) < 12:
                        continue
                    if normalize(part) not in corpus:
                        missing.append(f"{c['parent']} > {c['sub'] or '(parent)'}: \"{part}\"")
    for m in missing:
        print("WARNING quote not found verbatim in transcripts/:", m)
    return missing


def check_summary(doc):
    in_table = {(row[0], row[1]) for row in doc["summary_table"] if len(row) > 1}
    in_sections = {(c["parent"], c["sub"]) for c in doc["codes"] if c["sub"]}
    for p, s in sorted(in_sections - in_table):
        print(f"WARNING {p} > {s} has a section but is missing from the summary table")
    for p, s in sorted(in_table - in_sections):
        print(f"WARNING {p} > {s} is in the summary table but has no section")


# ---------------------------------------------------------------------------
# Workbook helpers
# ---------------------------------------------------------------------------

def fill(color):
    return PatternFill("solid", fgColor=color)


def status_fill(status):
    s = (status or "").lower()
    if s.startswith("new"):
        return NEW_FILL
    if s.startswith("reworded"):
        return REWORDED_FILL
    if s.startswith("kept"):
        return KEPT_FILL
    return "FFFFFF"


def est_height(cells, line_h=13, pad=8, cap=409):
    lines = 1
    for text, width in cells:
        if not text:
            continue
        n = sum(max(1, math.ceil(len(p) / max(1, width * 1.15))) for p in str(text).split("\n"))
        lines = max(lines, n)
    return min(cap, lines * line_h + pad)


def write_header(ws, headers, widths):
    for i, (h, w) in enumerate(zip(headers, widths), 1):
        c = ws.cell(1, i, h)
        c.font, c.fill, c.border = HFONT, fill(NAVY), BORDER
        c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
        ws.column_dimensions[c.column_letter].width = w
    ws.row_dimensions[1].height = 32


def write_rows(ws, rows, widths, start=2):
    for i, row in enumerate(rows, start=start):
        for j, v in enumerate(row, 1):
            c = ws.cell(i, j, v)
            c.font, c.alignment, c.border = BFONT, WRAP, BORDER
        ws.row_dimensions[i].height = est_height([(v, widths[j]) for j, v in enumerate(row)])


def label(code):
    return code["sub"] or "(parent definition)"


# ---------------------------------------------------------------------------
# Sheets
# ---------------------------------------------------------------------------

def build_start_here(wb, doc, team_codes):
    ws = wb.active
    ws.title = "Start Here"
    widths = [30, 62, 40, 18, 26]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + i)].width = w
    ws.sheet_view.showGridLines = False
    r = 1

    def text_row(text, font=BFONT, height=None):
        nonlocal r
        c = ws.cell(r, 1, text)
        c.font, c.alignment = font, WRAP
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        ws.row_dimensions[r].height = height or est_height([(text, sum(widths))])
        r += 1

    def heading(text):
        nonlocal r
        r += 1
        text_row(text, Font(name="Arial", size=11, bold=True, color=NAVY), 18)

    def table(rows, fills=None):
        nonlocal r
        for j, h in enumerate(rows[0], 1):
            c = ws.cell(r, j, h)
            c.font, c.fill, c.border = HFONT, fill(NAVY), BORDER
            c.alignment = Alignment(wrap_text=True, vertical="center")
        ws.row_dimensions[r].height = 20
        r += 1
        for k, row in enumerate(rows[1:]):
            for j, v in enumerate(row, 1):
                c = ws.cell(r, j, v)
                c.font, c.alignment, c.border = BFONT, WRAP, BORDER
                if fills and fills[k] and j == fills[k][0]:
                    c.fill = fill(fills[k][1])
            ws.row_dimensions[r].height = est_height([(v, widths[j]) for j, v in enumerate(row)])
            r += 1

    text_row(doc["title"], Font(name="Arial", size=14, bold=True, color=NAVY), 24)
    text_row("Built from Codebook/Output/EFF_VALUE_MISALIGNMENT_draft.md by "
             "Codebook/process/build_eff_misalignment_review.py. Edit the draft, then rebuild. "
             "The team file MaSS_Codebook_with_subcodes.xlsx is read, never changed.")

    current, pending_table = None, []
    for section, ln in doc["intro"] + [("__end__", "")]:
        if section != current or not ln.startswith("|"):
            if pending_table:
                table(pending_table)
                pending_table = []
        if section != current and section != "__end__":
            heading(section)
            current = section
        s = ln.strip()
        if not s or section == "__end__":
            continue
        if s.startswith("|"):
            if not re.match(r"^\|\s*-", s):
                pending_table.append([clean(c.strip()) for c in s.strip("|").split("|")])
        elif s.startswith(">"):
            text_row(clean(s.lstrip("> ")), BOLD)
        elif s.startswith("- "):
            text_row("\u2022 " + clean(s[2:]))
        elif not s.startswith(("Owner:", "Status:", "Review workbook:")):
            text_row(clean(s))

    heading("Color legend")
    for name, desc, col in [
        ("New", "New subcode proposed in this draft", NEW_FILL),
        ("Reworded", "Existing code with a plain-language rewrite", REWORDED_FILL),
        ("Kept", "Existing code kept as is", KEPT_FILL),
        ("Parent row", "Parent code (same lime green as the team file)", LIME),
        ("Subcode row", "Subcode (same light blue as the team file)", SUBBLUE),
    ]:
        a = ws.cell(r, 1, name)
        a.fill, a.font, a.border = fill(col), BOLD, BORDER
        b = ws.cell(r, 2, desc)
        b.font, b.border = BFONT, BORDER
        r += 1

    heading("Sheets in this file")
    table([["Sheet", "What it is"],
           ["Review", "The main sheet. One row per code: before vs. proposed definition, include and exclude rules, "
                      "verified quotes, literature, gaps, evidence strength, and two columns for your decision and feedback."],
           ["Full Codebook", "The whole team codebook in its original 7 columns, with the EFF_VALUE and MISALIGNMENT "
                             "blocks replaced by this draft. Use it to see how the section fits with the other codes."],
           ["Decision Log", "Decisions already made, and what changed because of them."],
           ["Quote Corrections", "Quotes in analysis/synthesis.md that do not match the raw transcripts."],
           ["Open Questions", "Decisions still needed, with a column for your answer."],
           ["Notes for Coders", "The team's coder notes, plus a short added section for these two codes."]])

    heading("How to give feedback")
    text_row("On the Review sheet, pick Keep / Revise / Merge / Drop in 'Your decision' (dropdown) and write comments "
             "in 'Your feedback'. Answer the Open Questions sheet. The next version is built from your notes.")

    heading("Summary of proposed codes")
    rows = [["Parent", "Subcode", "Status", "Literature", "Transcripts"]]
    fills = []
    for c in doc["codes"]:
        rows.append([c["parent"], label(c), c.get("status", ""), c.get("ls", ""), c.get("ts", "")])
        fills.append((3, status_fill(c.get("status"))))
    table(rows, fills)


def build_review(wb, doc):
    ws = wb.create_sheet("Review")
    headers = ["Parent code", "Subcode", "Status", "Current definition (before)", "Proposed definition (plain language)",
               "Include when", "Exclude when", "Example quotes (\u2605 = main example; verified against raw transcripts)",
               "Literature grounding", "Why it matters / notes", "Evidence: literature", "Evidence: transcripts",
               "Your decision", "Your feedback"]
    widths = [16, 24, 13, 38, 44, 34, 38, 70, 52, 42, 14, 16, 14, 40]
    write_header(ws, headers, widths)
    for i, c in enumerate(doc["codes"], start=2):
        include = c.get("include", "")
        if c.get("related"):
            include += "\n\nRelated coding: " + c["related"]
        vals = [c["parent"], label(c), c.get("status", ""), c.get("current") or "(new, no previous definition)",
                c.get("proposed", ""), include, c.get("exclude", ""), c.get("quotes", ""), c.get("lit", ""),
                c.get("why", ""), c.get("ls", ""), c.get("ts", ""), None, None]
        base = SUBBLUE if c["sub"] else LIME
        for j, v in enumerate(vals, 1):
            cell = ws.cell(i, j, v)
            cell.font, cell.alignment, cell.border = BFONT, WRAP, BORDER
            if j in (1, 2):
                cell.fill, cell.font = fill(base), BOLD
            elif j == 3:
                cell.fill = fill(status_fill(c.get("status")))
            elif j == 4:
                cell.font = Font(name="Arial", size=10, italic=True, color="595959")
        ws.row_dimensions[i].height = est_height([(v, widths[j]) for j, v in enumerate(vals)])
    last = len(doc["codes"]) + 1
    dv = DataValidation(type="list", formula1='"Keep,Revise,Merge,Drop"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"M2:M{last}")
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:N{last}"


def build_full_codebook(wb, doc, team):
    tws = team["Codebook"]
    ws = wb.create_sheet("Full Codebook")
    headers = [tws.cell(1, c).value for c in range(1, 8)] + ["Change status"]
    widths = [42, 25.3, 28, 56, 40, 64, 50, 14]
    write_header(ws, headers, widths)
    key_concepts = {}
    for r in range(2, tws.max_row + 1):
        if tws.cell(r, 2).value in OWNED_PARENTS and tws.cell(r, 3).value is None:
            key_concepts[tws.cell(r, 2).value] = tws.cell(r, 1).value

    def status_cell(row, text, color=None, bold=False):
        c = ws.cell(row, 8, text)
        c.font = Font(name="Arial", size=9, bold=bold, color=None if color else "808080")
        c.border, c.alignment = BORDER, WRAP
        if color:
            c.fill = fill(color)

    def copy_team_row(src, dst, with_status=True):
        for c in range(1, 8):
            s, d = tws.cell(src, c), ws.cell(dst, c, tws.cell(src, c).value)
            d.font, d.fill, d.border, d.alignment = copy(s.font), copy(s.fill), copy(s.border), copy(s.alignment)
        ws.row_dimensions[dst].height = tws.row_dimensions[src].height
        if with_status:
            status_cell(dst, "Unchanged")

    def write_code(c, dst):
        definition = c.get("proposed", "")
        if c.get("include"):
            definition += "\n\nInclude when: " + c["include"]
        if c.get("related"):
            definition += "\n\nRelated coding: " + c["related"]
        if c["sub"] and c.get("why"):
            definition += "\n\nNote: " + c["why"]
        kc = key_concepts.get(c["parent"]) or c.get("kc", "")
        vals = [kc, c["parent"], c["sub"] or None, definition, c.get("exclude", ""),
                c.get("quotes") if c["sub"] else None, c.get("lit") if c["sub"] else None]
        base = SUBBLUE if c["sub"] else LIME
        for j, v in enumerate(vals, 1):
            cell = ws.cell(dst, j, v)
            cell.font, cell.alignment, cell.border, cell.fill = BFONT, WRAP, BORDER, fill(base)
            if j == 2:
                cell.font = BOLD
            if j == 3 and v:
                cell.font = Font(name="Arial", size=10, bold=True, color=NAVY)
        ws.row_dimensions[dst].height = est_height([(v, widths[j]) for j, v in enumerate(vals)])
        status_cell(dst, c.get("status", ""), status_fill(c.get("status")), bold=True)

    dst, written, legend_rows = 2, set(), []
    for src in range(2, tws.max_row + 1):
        a, b = tws.cell(src, 1).value, tws.cell(src, 2).value
        if a is None and b is None:
            continue
        if a is None and b in ("Main Code", "Subcode"):
            legend_rows.append(src)
            continue
        if b in OWNED_PARENTS:
            if b not in written:
                for c in doc["codes"]:
                    if c["parent"] == b:
                        write_code(c, dst)
                        dst += 1
                written.add(b)
            continue
        copy_team_row(src, dst)
        dst += 1
    ws.freeze_panes = "D2"
    ws.auto_filter.ref = f"A1:H{dst - 1}"
    dst += 1
    for src in legend_rows:
        copy_team_row(src, dst, with_status=False)
        dst += 1


def build_list_sheet(wb, title, items, answer_header):
    ws = wb.create_sheet(title)
    widths = [5, 100] + ([50] if answer_header else [])
    write_header(ws, ["#", "Item"] + ([answer_header] if answer_header else []), widths)
    rows = [[i, t] + ([None] if answer_header else []) for i, t in enumerate(items, 1)]
    write_rows(ws, rows, widths)
    ws.freeze_panes = "A2"


def build_notes(wb, team):
    sws = team["Notes for Coders"]
    ws = wb.create_sheet("Notes for Coders")
    ws.column_dimensions["A"].width = sws.column_dimensions["A"].width
    n = 1
    for r in range(1, sws.max_row + 1):
        s, d = sws.cell(r, 1), ws.cell(n, 1, sws.cell(r, 1).value)
        d.font, d.fill, d.alignment, d.border = copy(s.font), copy(s.fill), copy(s.alignment), copy(s.border)
        n += 1
    added = [
        "",
        "EFF_VALUE AND MISALIGNMENT (added in the review draft):",
        "EFF_VALUE = the system's efficiency. COMMUNITY_EFFICIENCY = the community's efficiency. JUST_ACCESS = the need. "
        "MISALIGNMENT = the gap between them: whose efficiency a choice counts, and whose it ignores.",
        "Apply MISALIGNMENT only when the passage links the system logic to a cost in access or in someone's daily life; "
        "two separate observations side by side do not count.",
        "Record whose logic it is: literature, design team (Workshop 1), stakeholders (Workshop 3), or an institution "
        "described by a client or weaver.",
        "A client describing what saves their own time, effort, or strain is COMMUNITY_EFFICIENCY, not EFF_VALUE.",
        "Report COMMUNITY_EFFICIENCY counts separately from other MISALIGNMENT subcodes: some excerpts describe a fit, "
        "not a gap.",
    ]
    for i, t in enumerate(added):
        c = ws.cell(n, 1, t)
        c.font = Font(name="Arial", size=10, bold=(i == 1), color=NAVY if i == 1 else None)
        c.alignment = Alignment(wrap_text=True)
        if i:
            c.fill = fill(NEW_FILL)
        n += 1


def main():
    doc = parse_draft(DRAFT)
    check_no_em_dash(doc)
    check_summary(doc)
    missing = check_quotes(doc)
    team = load_workbook(TEAM_XLSX)

    wb = Workbook()
    build_start_here(wb, doc, team)
    build_review(wb, doc)
    build_full_codebook(wb, doc, team)
    lists = doc["lists"]
    pick = lambda prefix: next((v for k, v in lists.items() if k.lower().startswith(prefix)), [])
    build_list_sheet(wb, "Decision Log", pick("decision log"), None)
    build_list_sheet(wb, "Quote Corrections", pick("evidence corrections"), "Your note")
    build_list_sheet(wb, "Open Questions", pick("open questions"), "Your answer")
    build_notes(wb, team)
    wb.active = 1
    wb.save(OUT)
    print(f"Wrote {os.path.relpath(OUT, REPO)}: {len(doc['codes'])} codes, "
          f"{len(missing)} unverified quote fragment(s).")


if __name__ == "__main__":
    main()
