# Agent Prompt: Transcript Coding and Synthesis Against the Five Anchor Questions

Paste this whole document to a fresh agent. It is self-contained. Do not
skip the background section; the anchor questions only make sense against
the project's argument.

---

## 1. Your mission

We have spent about a year researching how a food pantry system works as
community mobility infrastructure. We now have a corpus of transcripts
(facilitated workshops / focus groups and AI-agent interviews with pantry
clients and stakeholders). Your job is to read every transcript closely
through five fixed analytical lenses ("anchor questions"), then produce a
synthesis that anchors our findings in what people actually said.

You will work in **two stages**:

1. **Per-transcript coding notes.** One transcript at a time, you produce a
   structured notes file that codes passages into the five buckets, with
   verbatim quotes and locators.
2. **Cross-cutting synthesis.** After all transcripts are coded, you write a
   single synthesis document organized by the five anchor questions, pulling
   the strongest evidence from across the corpus under each, and mapping the
   findings back to the paper's framework.

Do not start stage 2 until stage 1 is complete for every in-scope transcript.

---

## 2. Background: the argument this feeds

The team is writing an academic paper arguing that mobility infrastructure
(originally autonomous vehicles, extended here to the food pantry system)
typically arrives in communities **without community participation**, and
carries **efficiency-driven engineering values** that clash with community
values. The paper names three community values that top-down mobility
systems tend to foreclose:

- **Equitable access**: everyone can actually reach and use the service,
  regardless of income, disability, language, documentation status, digital
  access, or where they live.
- **Relational trust**: the service is built on known people and ongoing
  relationships, not anonymous transactions or verification regimes.
- **Flexibility for variable need**: the service bends to fluctuating,
  uneven, hard-to-schedule need instead of forcing need into fixed slots,
  quotas, and eligibility categories.

The paper introduces **"Mobility as Social Service" (MaSS)**: the idea that
mobility infrastructure should be designed and governed like a social
service that is accountable to the community it serves, rather than as an
efficiency-optimized product delivered to it.

The food pantry is the empirical site because it *is* a mobility system:
people, food, and care all have to move, and the same tensions show up.

You are not here to defend this argument. You are here to find where the
transcripts support it, complicate it, or contradict it, in participants'
own words.

---

## 3. The five anchor questions (the coding framework)

These five categories were set by the research lead as the coding scheme for
every transcript. Code each relevant passage into one or more of them.

### 1. Values
**Guiding question:** What social-relational values operate within the food
pantry system? For example trust, flexibility, dignity, mutual care,
reciprocity, respect, belonging. What values characterize and govern the
pantry ecosystem, both the stated ones and the ones visible in how people
describe their experience?

**Coding guidance:** Look for what people treat as important, what they
praise or resent, what makes an interaction feel good or humiliating. Values
can be named outright ("they treat you with dignity") or implied by a story.
Capture both client-side values and staff/organizer-side values.

### 2. Capabilities and Constraints
**Guiding question:** What existing **capabilities** (positive assets, e.g.
resilience, local knowledge, social networks, resourcefulness, care work
already being done) do community leaders and pantry clients hold? What
**systemic / infrastructural conditions** (time, childcare, income,
transportation, health, work schedules, documentation, language, technology
access) constrain them from fully using those capabilities?

**Coding guidance:** This is drawn from mobility-justice literature.
"Capability" means innate capacity and existing strength, **not** a deficit.
Do not code someone's hardship as a capability, and do not frame a
constraint as a personal failing. The pattern to capture is:
*person has capacity X → condition Y blocks them from exercising it*.

### 3. Meanings and Practices
**Guiding question:** What does **mobility** mean to food pantry users and
stakeholders? How do they actually **practice** mobility: what do they move
(people, goods, care, information, money) and how (walking, driving,
borrowing rides, buses, delivery, carrying for others, coordinating pickups
for neighbors)?

**Coding guidance:** Capture both the meaning ("getting to the pantry means
I can look my kids in the eye") and the concrete practice ("I pick up for
three other families on my street"). Note improvised, informal, and
care-driven mobility, not just trips to the pantry.

### 4. Misalignment
**Guiding question:** Where do **top-down, efficiency-driven values**
(around trust, time, negotiation, scheduling, verification, eligibility,
standardization) diverge from **community values and meanings**?

**Coding guidance:** This is the crux for the paper. Look for friction
between how the system is run and what the community needs or values:
appointment systems that ignore variable need, ID/proof requirements that
break trust, "one visit per month" rules, intake forms, hours that assume a
9-to-5 absence, routing/location decisions made without input, technology
that assumes a smartphone and data plan. Code the tension explicitly:
*system does X for efficiency / legibility → community experiences it as a
loss of value Y*. (Note: earlier team passes marked some of this with brown
highlighting in the source files. Do not rely on the highlighting; code
misalignment from the text itself.)

### 5. Provocation
**Guiding question:** How did participants react to the **speculative AV /
future-mobility workshop prompts**? What concrete **design implications**
emerge from reframing AV infrastructure as a mobility-related social
service?

**Coding guidance:** Some transcripts contain speculative prompts (imagined
autonomous vehicles, future delivery, automation, "what if the pantry came
to you"). Code participant reactions to those: enthusiasm, fear, skepticism,
conditions they'd attach, who they think it would help or exclude. **Many
transcripts will contain no such material.** When a transcript has none,
record "No provocation material in this transcript" in the notes and move
on. Do not invent reactions. If a transcript has a reaction to technology,
automation, or an imagined future service that is not a formal AV prompt,
you may code it here but label it clearly as adjacent, not a direct response
to a speculative prompt.

---

## 4. The corpus

### Location
All transcripts live under `transcripts/` in this repo. The team will add
more files there over time, including the facilitated AV/speculative
workshop transcripts and older "community-weaver" transcripts. **Before you
start, list the current contents of `transcripts/` and build your own
in-scope file list.** In scope: every transcript of a workshop, focus group,
or interview. Out of scope: summary images (`.jpeg`), the quant analysis
spreadsheet (`AI interviews metrics.xlsx`), and any non-transcript file.

### Known structure as of writing (verify, do not assume it is still current)
- `transcripts/Focus Groups/` : facilitated "Insight Box" workshop sessions.
  - `Plaud Hope_Food_Pantry-transcript.txt`
  - `Plaud Ministries of Love transcript.txt`
  - `Old Bethel Interview Transcript.docx`
- `transcripts/AI Interviews/` : interviews conducted by an AI agent ("Alex")
  with pantry clients, organized by site.
  - `SEC/Participant NN/Participant NN.docx` (about 22 files; `SP` in a
    folder name indicates a Spanish-language interview)
  - `Hope/Participant NN Hope/Participant NN Hope.docx` (about 6 files)
  - `Ministries of Love/Quincey AI shashi.docx`

### Transcript formats (each needs different handling)
The corpus is inconsistent. Detect the format per file:

| Format | Looks like | Locator to record |
|---|---|---|
| Focus-group `.txt` | `00:04:13 Speaker 2` on its own line, then text | `file, 00:04:13, Speaker 2` |
| Hope interview `.docx` | `Alex • 09:08:11` / `Interviewee • 09:08:23` then text | `file, 09:08:23, Interviewee` |
| SEC interview `.docx` | `Interviewer: ...` / `Interviewee: ...` inline, no timestamps | `file, turn N, Interviewee` (count turns from the top) |
| Old Bethel `.docx` | `04:15` on its own line, no speaker label | `file, 04:15` |
| Anything else | (inspect) | timestamp if present, else `paragraph N` |

### Extracting text
- This is macOS. `pdftotext`, `textutil`, and Python `python-docx` are
  available. (The repo's CLAUDE.md says "Windows / PowerShell"; that note is
  stale, ignore it for this task.)
- `.txt`: read directly.
- `.docx`: extract with `python-docx` (iterate `document.paragraphs`, keep
  non-empty `.text`) or `textutil -convert txt "file.docx" -output -`.
  Prefer `python-docx` because it preserves paragraph breaks between
  speaker turns cleanly.
- Read the **entire** transcript before coding it. Do not code from the
  first page.

### Anonymization (hard rule)
- Never write a participant's real name, even if it appears in the
  transcript. Use `Participant`, `Interviewee`, `Client`, `Staff`,
  `Organizer`, `Facilitator`, or the speaker label the transcript uses
  (`Speaker 4`).
- Keep the site name (Hope, SEC / Southeast Community Pantry, Ministries of
  Love, Old Bethel) and the file name; those are not sensitive.
- If a quote contains a third person's name, replace it with `[name]` inside
  the quote and note that you did.
- Redact any other direct identifier that appears in a quote (phone number,
  address, employer) as `[redacted]`.

---

## 5. Evidence and attribution rules (hard rules)

These carry over from the project's literature-review discipline.

1. **No fabrication.** Every coded point traces to text you actually read in
   that transcript. Do not code what a participant "probably" felt or what a
   person in that situation "would" say. If it is not in the transcript, it
   does not go in the notes.
2. **Verbatim quotes.** Every quote is copied character for character.
   Preserve the participant's grammar and word choice. Mark any omission
   inside a quote with `...` and never let the omission change the meaning.
   Do not clean up or "fix" a quote.
3. **Source and locator on every quote.** Format:
   `"quote" (file name, locator, speaker role)` using the locator column in
   the table above. A claim in the synthesis with no locatable quote behind
   it does not belong in the synthesis.
4. **No em dash (`—`) anywhere in your output files.** Use a comma, colon,
   period, or "and". (This is house style for the project's written
   deliverables. It does not apply to text you are quoting verbatim; if a
   transcript contains an em dash, keep it inside the quote.)
5. **Attribute borrowed words.** If a participant is quoting someone else
   (a caseworker, a sign, a rule they were told), make clear in your framing
   that these are reported words, not the participant's own position.
6. **Represent disagreement.** If participants at the same site say opposite
   things, code both. Do not average them into a single tidy finding.
7. **Uncertainty is allowed.** If a passage is ambiguous, code it and say
   why it is ambiguous. Do not force it into a clean bucket.

---

## 6. Stage 1: per-transcript coding notes

### Process
Work through your in-scope file list **one transcript at a time**. For each:

1. Extract the full text.
2. Detect the format and locator scheme.
3. Read the whole thing.
4. Fill the template below into
   `analysis/coding-notes/<slug>.md`, where `<slug>` is a short safe name,
   e.g. `sec-participant-01`, `focus-group-hope`, `old-bethel`.
5. Move to the next transcript. Do not hold more than one transcript's full
   text in working memory at a time.

### Per-transcript notes template

```markdown
# Coding notes: <transcript name>

- Source file: <relative path>
- Site: <Hope | SEC | Ministries of Love | Old Bethel | other>
- Type: <Insight Box workshop | AI-agent interview | other>
- Language: <English | Spanish | other>
- Format / locator scheme: <e.g. "docx, Name • HH:MM:SS">
- Participants present: <count and roles, no names>
- Read in full: <yes>

## 1. Values
- <finding stated plainly>
  - "verbatim quote" (file, locator, role)
- ...

## 2. Capabilities and Constraints
- Capability: <asset the person holds>
  - "quote" (file, locator, role)
- Constraint: <systemic condition blocking it>
  - "quote" (file, locator, role)
- Capability/constraint pair: <person can X but Y blocks them>
  - "quote" (file, locator, role)

## 3. Meanings and Practices
- Meaning of mobility: <what moving / getting there means to them>
  - "quote" (file, locator, role)
- Practice of mobility: <what they move and how>
  - "quote" (file, locator, role)

## 4. Misalignment
- Tension: <system does X for efficiency / legibility> vs <community value or
  meaning Y that this costs>
  - Which of the three community values is at stake: <equitable access |
    relational trust | flexibility for variable need | other, name it>
  - "quote" (file, locator, role)
- ...
- If none found: "No clear misalignment surfaced in this transcript."

## 5. Provocation
- Speculative prompt present: <yes / no>
- If yes, participant reaction: <summary>
  - "quote" (file, locator, role)
  - Conditions or concerns they attached: <...>
  - Who they thought it would help or exclude: <...>
- If no: "No provocation material in this transcript."

## Cross-bucket notes
- Passages that resist the five buckets, surprising moments, anything the
  synthesis should not lose. Quote them.

## Coder uncertainty
- Ambiguous passages and why. Anything you suspect is transcription error.
```

### Self-check before saving each notes file
- Every quote has a file, a locator, and a role.
- No real participant names anywhere.
- No em dash outside a verbatim quote.
- You read the whole transcript, not an excerpt.
- Capabilities are framed as assets, not hardships.
- Misalignment entries name the specific value at stake.
- You did not invent a provocation reaction to fill the section.

---

## 7. Stage 2: cross-cutting synthesis

After every in-scope transcript has a notes file, write
`analysis/synthesis.md`. Read across all the notes files (not the raw
transcripts again) to build it.

### Structure

```markdown
# Transcript Synthesis: Five Anchor Questions

## About this document
- Corpus: <N transcripts: breakdown by site and type>
- Method: two-stage coding (per-transcript notes in analysis/coding-notes/,
  then this synthesis). Anchor questions set by the research lead.
- Date range of fieldwork if known.
- Caveats: <language coverage, sample skew, transcription quality, any site
  under-represented>.

## 1. Values
- 3 to 6 findings. Each finding is a claim in one sentence, then 2 to 4
  supporting quotes from different transcripts with locators, then a short
  paragraph on what the pattern means and where it does not hold.
- Note which values are client-side, which are organizer-side, and where
  they conflict.

## 2. Capabilities and Constraints
- Same shape. Organize as: capabilities the community already holds, then
  the systemic constraints that blunt them, then the specific
  capability/constraint pairs that recur across transcripts.

## 3. Meanings and Practices
- Same shape. Separate "what mobility means" from "how mobility is
  practiced". Highlight informal and care-driven mobility (picking up for
  others, coordinating rides) as its own finding if the evidence supports
  it.

## 4. Misalignment
- Same shape. This is the most important section for the paper. Each finding
  names: the efficiency / legibility logic on the system side, the community
  value or meaning it costs, and which of the three framework values
  (equitable access, relational trust, flexibility for variable need) it
  maps to. Rank findings by how much evidence stands behind them.

## 5. Provocation
- Only the transcripts with speculative material. Summarize the range of
  reactions, the conditions participants attached, and the equity concerns
  they raised. If coverage is thin, say so directly and do not overreach.

## Design implications (tentative)
- Derived mainly from anchor 5, informed by anchors 1 to 4.
- Frame every item as a provisional hypothesis for the team to debate, not a
  settled specification. Use "The transcripts suggest ..." / "One
  implication to test ...".
- For each: the implication, the transcript evidence it rests on, and what
  would confirm or kill it.

## Mapping to the paper framework
- One section, at the end, mapping the emergent findings back to:
  - Equitable access: <which findings, which quotes>
  - Relational trust: <...>
  - Flexibility for variable need: <...>
  - Mobility as Social Service: <where the transcripts support or complicate
    the idea that the pantry mobility system should be governed as an
    accountable social service>
  - Community participation: <evidence about whether the system was built
    with or without community input, and what that cost>
- Be explicit where the transcripts complicate or contradict the framework.
  A finding that cuts against the argument is more valuable than one more
  confirmation.

## Open questions and gaps
- What the corpus cannot answer. What a next round of fieldwork should ask.
```

### Synthesis quality bar
- Every finding rests on at least two transcripts unless it is explicitly
  flagged as a single-source observation worth keeping.
- Quotes in the synthesis are copied from the notes files with their
  locators intact.
- No finding is stated more confidently than the evidence allows.
- Contradictory evidence is shown, not smoothed.
- Design implications are all marked tentative.
- No real names. No em dash outside verbatim quotes.

---

## 8. Output file layout

```
analysis/
  transcript-synthesis-agent-prompt.md   (this file)
  coding-notes/
    <one .md per transcript>
  synthesis.md                            (stage 2 deliverable)
```

Create `analysis/coding-notes/` if it does not exist.

---

## 9. Workflow checklist

1. List `transcripts/` and build the in-scope file list. Report it back
   before coding.
2. For each in-scope transcript: extract, read in full, code into the
   template, save to `analysis/coding-notes/`, then stop and move to the
   next. One at a time.
3. When all are coded, write `analysis/synthesis.md` from the notes files.
4. Report: how many transcripts coded, which anchor questions turned out
   thin, where the corpus has gaps, and any files you could not read.

## 10. Stop conditions (ask the team, do not guess)

- A transcript is unreadable or looks truncated or corrupted.
- A file's format does not match anything in the table and you cannot
  establish a reliable locator scheme.
- You find no speculative material in any transcript and anchor 5 would be
  empty across the whole corpus.
- The in-scope count is far from what you expected (for example the
  workshop transcripts the team mentioned are not present).
- Two sites tell opposite stories and you are unsure whether that is a real
  finding or a coding error.
