# EFF_VALUE and MISALIGNMENT: refined definitions and subcodes (DRAFT v2)

Owner: Amy (Engineering & Safety-dominant AV Discourse thread)
Status: draft for review. Nothing here has been written into the team file `MaSS_Codebook_with_subcodes.xlsx`.
Review workbook: `MaSS_Codebook_with_subcodes_EFF_MISALIGNMENT_review.xlsx`, rebuilt from this file with `python3 Codebook/process/build_eff_misalignment_review.py`. Edit this file, not the workbook.

## What this section of the codebook has to show

Our research claim for this thread, in one line:

> The efficiency-driven values that AVs inherit from transportation engineering are distant from (in a gap with) what the community needs, especially **equitable access**.

The sharper version, since v2: the gap is **whose efficiency gets counted**. AV design counts the system's efficiency (vehicles per hour, boxes per shift, cost per delivery). Community members count efficiency in their own lives (not missing work, not waiting for hours, not standing in the cold). The claim is not "efficiency versus community," it is "efficiency for whom."

This maps onto two thesis clauses:

| Clause | Text | Code |
|---|---|---|
| C3 | AVs carry efficiency-driven values inherited from transportation engineering. | `EFF_VALUE` |
| C5 | Efficiency-driven values are misaligned with community concerns. | `MISALIGNMENT` |

What the evidence base looks like (from `crosscomp/thesis_clause_summary.csv` and `who_is_centered_counts.csv`):

- The Engineering & Safety papers support C3 very strongly: 17 of 17 papers support it directly or partly (12 directly).
- They support C5 much more weakly: 9 of 17, and only 1 directly. The engineering literature describes the efficiency values but rarely names the gap itself.
- 0 of the 17 papers center community members or residents (9 center engineers, 4 regulators, 4 researchers).

**What this means for coding:** `EFF_VALUE` can lean on the literature. `MISALIGNMENT` mostly has to be shown through the transcripts, where community members and stakeholders run into the efficiency logic. That is why every `MISALIGNMENT` subcode below needs transcript quotes, not only citations.

## One rule to tell the codes apart

| Code | What the passage shows | Quick test |
|---|---|---|
| `EFF_VALUE` | **The system's efficiency.** A goal, measure, or design choice framed as moving more, faster, cheaper, with fewer people, measured from the system's side. | "What is this system trying to maximize?" |
| `MISALIGNMENT > COMMUNITY_EFFICIENCY` | **The community's efficiency.** What saves or costs a person their own time, effort, money, or strain. | "What does getting help cost this person in their day?" |
| `JUST_ACCESS` (teammate's code) | **The need.** Someone can or cannot get to the service at all. | "Who can't get there, and why?" |
| `MISALIGNMENT` | **The gap.** The system's efficiency costs someone their access or their own efficiency, or the two clearly pull in opposite directions. | "Whose efficiency does this choice count, and whose does it ignore?" |

A single excerpt often gets several of these. Apply `MISALIGNMENT` only when the passage links the two sides. Two separate observations that happen to sit next to each other do not count.

## Summary of proposed subcodes

| Parent | Subcode | Status | Literature | Transcripts |
|---|---|---|---|---|
| `EFF_VALUE` | `THROUGHPUT` | Existing, definition reworded | Strong | Medium |
| `EFF_VALUE` | `HUMAN_REMOVED` | **New** | Medium | Strong (mostly design team) |
| `EFF_VALUE` | `ADOPTION_AS_SUCCESS` | **New** | Strong | Medium (stakeholders) |
| `EFF_VALUE` | `VERIFY_TO_COUNT` | **New** | Medium | Strong |
| `EFF_VALUE` | `SAFETY_ENG` | Existing, definition reworded | Strong | Weak (no direct quote yet) |
| `EFF_VALUE` | `TRUST_METRIC` | Existing, kept as is | Strong | Contrast only (see `JUST_TRUST`) |
| `EFF_VALUE` | `ACCESS_AS_EFF` | Existing (Food Justice thread), kept as is | Food Justice | Excluded by its own rule |
| `MISALIGNMENT` | `COMMUNITY_EFFICIENCY` | **New** (replaces `EFFICIENCY_SERVES`) | Medium (Equity, Food Justice threads) | Strong |
| `MISALIGNMENT` | `IDEAL_VS_ACTUAL_TRAVELER` | Existing in `MaSS_New_Codes.md`, now grounded | Strong | Strong |
| `MISALIGNMENT` | `CAPACITY_NOT_ACCESS` | **New** | Strong | Medium |
| `MISALIGNMENT` | `BURDEN_SHIFTED` | **New** | Medium | Strong |
| `MISALIGNMENT` | `ACCESS_DEFERRED` | **New** | Strong | Weak (one quote) |

Locator format follows the `JUST_ACCESS` rows: `(source, timestamp or line, speaker, role)`. Every quote below was checked word for word against the raw transcript files in `transcripts/`. ★ marks a quote I suggest using as the main example.

---

# Parent code: EFF_VALUE

**Key concept (Column A):** efficiency-driven values inherited from transportation engineering

**Status:** Reworded

**Literature strength:** Strong

**Transcript strength:** Medium

**Current definition:** Invokes efficiency logic: speed, optimized routing, throughput, scheduling precision, automation-as-improvement.

**Proposed definition:** System-centered efficiency. The passage judges a vehicle, service, or system by how much it moves, how fast, and at what cost, measured from the system's side (vehicles per hour, boxes per shift, cost per delivery). Taking people out of the process (drivers, staff, choices, conversations) is treated as an improvement. Who is traveling, and why, is not part of what gets measured.

**Include when:** A goal, measure, or design idea is framed in terms of speed, volume, capacity, cost, automation, or a safety or trust score, from the system's point of view.

**Exclude when:**
- A vehicle or technology is mentioned with no efficiency framing.
- A community member describes what saves their own time, effort, or strain. That is community-defined efficiency: code `MISALIGNMENT > COMMUNITY_EFFICIENCY`. Example: "Quick." (sec-Participant 13 SP, 15:17:25; translated, answering what would make a new program easier to try).

**Coding note:** Always record *whose* logic it is: the literature, the design team (Workshop 1), stakeholders (Workshop 3), or an institution as described by a client or weaver. In our transcripts the efficiency logic shows up most clearly in the design team's own ideas and in the pantries' own rules, not in an AV vendor. That supports C6 (a broader pattern, not a one-off AV problem).

**Literature:** Thesis clause C3. Engineering & Safety thread: 17 of 17 papers support C3 directly or partly (12 directly). 0 of 17 papers center community members.

**Feedback:**

---

### EFF_VALUE > THROUGHPUT

**Status:** Reworded

**Literature strength:** Strong

**Transcript strength:** Medium

**Current definition:** The Engineering/Safety literature organizes evaluation around network throughput, capacity, and automation share, with people appearing only as trip counts.

**Proposed definition:** Success means more vehicles, trips, deliveries, or boxes moved through the same road or service. People appear only as counts (trips, flow, volume), not as individuals with destinations or reasons.

**Include when:** A model, plan, or practice is justified by capacity, flow, volume served, route optimization, or penetration rate.

**Exclude when:** The passage names a trade-off in terms of specific people affected (code `BURDEN_SHIFTED` or `CAPACITY_NOT_ACCESS` instead).

**Example quotes:**
1. ★ "Now we just put it in the box and move on. Because like I said, the volume got so much from 100 to 350, 400, we couldn't just keep letting them stay in there and we'd be in there until six o'clock at night" (Old Bethel interview, 15:03, community weaver, describing why the pantry stopped letting clients shop)
2. "How might AVs enhance route optimization?" (transcript_workshop1, line 89, design team board, cluster: Workforce Optimization)
3. "How might AVs optimize deliveries?" (transcript_workshop1, line 70, design team board, cluster: Integrated Logistics)

**Literature:** Mechanism 3 (Efficiency optimization crowds out purpose): Lu, Tettamanti, Hörcher, and Varga 2020 (network capacity rises about 16% to 24% at full automation; people appear only as vehicle flow and trip counts); Park, Jang, and Ko 2024 (an AV-only lane improves efficiency only above about 20% to 30% AV share; travelers are anonymous origin-destination trips); Pimenta, Kamruzzaman, and Currie 2023 (communities appear only as aggregate statistics).

**Why it matters for equitable access:** Quote 1 is not about AVs. It shows the same throughput logic already running inside the pantry. Pair it with `BURDEN_SHIFTED`: the pantry's efficiency went up while clients lost the ability to choose their food.

**Feedback:**

---

### EFF_VALUE > HUMAN_REMOVED

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong (mostly design team)

**Proposed definition:** Removing a person from the process (driver, staff, volunteer, or the conversation itself) is counted as a gain in its own right: lower cost, longer hours, fewer errors. Whatever else that person did for the people being served is not counted.

**Include when:** Automation is valued *because* it replaces or reduces human involvement, or communication between people is designed out.

**Exclude when:** The passage is about reducing physical injury or overwork for staff and volunteers without removing them from contact with clients (still `EFF_VALUE`, but not this subcode). If the passage is about what the human relationship means to the client, also code `JUST_TRUST`.

**Example quotes:**
1. ★ "How might we use AVs to reduce driver needs so manpower can focus on logistics/other business needs" (transcript_workshop1, line 90, design team board, cluster: Workforce Optimization)
2. ★ "Anticipate the needs of food pantry when threshold is met → place order → got to pick up order • no communication between people" (transcript_workshop1, line 142, design team board, cluster: Food Supply Demand)
3. "AV can anticipate the shortage of food. No communication from human" (transcript_workshop1, line 46, design team board, cluster: Communication)
4. "Removes the dependence on truck drivers availability and skill set → able to operate at all hours" (transcript_workshop1, line 100, design team board, cluster: Expanding operational hours)
5. "Senior citizens are lonely, become friends with AV" (transcript_workshop1, line 173, design team board, cluster: Logistics)

**Counter-voice (code with `MISALIGNMENT` or `JUST_TRUST`):**
- "Maintaining the human relation" (transcript_workshop3, line 162, stakeholder board, cluster: Social service meaning relational engagement not transactional)
- "How might we ensure there is a human element/touch with AVs used as a social service for those they serve → delivery" (transcript_workshop1, line 183, design team board, a minority voice in the same workshop)

**Literature:** Nordhoff, Stapel, van Arem, and Happee 2020 (the human safety steward was disguised so riders would experience the shuttle as fully driverless); Zoellick et al. 2019 (riders said the human safety operator shaped their experience, but the researchers treated this as a confound to control rather than something to design around).

**Why it matters for equitable access:** If the driver or volunteer is also the one who helps carry, waits, or knows the client, removing them can remove access. Gap: no transcript quote yet shows this directly for a driver. `CARE_INFRA` evidence may supply it.

**Feedback:**

---

### EFF_VALUE > ADOPTION_AS_SUCCESS

**Status:** New

**Literature strength:** Strong

**Transcript strength:** Medium (stakeholders)

**Proposed definition:** Success is measured by whether people accept, trust, or start using the technology (acceptance scores, intention to use, adoption rate), not by whether anyone's trip or load actually got easier.

**Include when:** A study, plan, or board note treats uptake, acceptance, or "successful integration" as the goal or the return on investment.

**Exclude when:** Uptake is measured as a means to check whether a need was met (for example, checking whether homebound clients actually got their food).

**Example quotes:**
1. ★ "Biggest ROI of AV as a social service is the adoption rate of AV" (transcript_workshop3, line 84, stakeholder board, cluster: Current Infrastructure), with the board's arrow from "Automaker" annotated "More AV adoption / Serving Automakers interest in building infrastructure" (transcript_workshop3, lines 184 to 185)

**Counter-voice (code with `MISALIGNMENT > COMMUNITY_EFFICIENCY`):**
- The discussion "questions traditional financial ROI for public good projects, suggesting a need for new metrics that measure the 'weights of burden' and capture the ultimate benefit to the end user" (transcript_workshop3, line 61, stakeholder board, cluster: ROI). Note: this is the board's summary of a discussion; only "weights of burden" is a direct phrase.

**Literature:** Zoellick et al. 2019 (field study built on standard acceptance, trust, and intention-to-use scales, and found those scales do not hold together cleanly); Lee and Kolodge 2020 (survey comments mined for what makes drivers accept the technology, so manufacturers can cultivate acceptance); Palatinus et al. 2022 (acceptance measured as an individual physiological and affective state, using UTAUT2); Nordhoff et al. 2020 (perceived safety engineered as the precondition for "successful integration").

**Why it matters for equitable access:** If success means adoption, the system succeeds by reaching the people easiest to convert, not the people who most need a ride. The stakeholders' "weights of burden" is the community's alternative measure of success.

**Feedback:**

---

### EFF_VALUE > VERIFY_TO_COUNT

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong

**Proposed definition:** To be easy to run and audit, the system needs every person to be checked and counted: show ID, appear in person, pass a face check, be detected by sensors. People who cannot show up or be checked fall out of the system.

**Include when:** A rule, idea, or technology exists to verify, count, or track the person being served, and is justified by order, fraud prevention, or efficiency.

**Exclude when:** The passage is about being judged as *deserving* or expected to show gratitude. That is the teammate's `JUST_ACCESS > CONDITIONALITY`. A passage can carry both.

**Example quotes:**
1. ★ "We have a 98-year-old neighbor. She can't get out and get this. But then you can't take it to her because the person has to be here to get the benefits." (Plaud Hope, 00:19:42, Speaker 8, client)
2. "Cuz they got a card, everybody's got a card, their number, show their ID, move on." (Old Bethel interview, 14:46, community weaver)
3. "Should have some sort of face verification to ensure food is handed to the right person" (transcript_workshop1, line 38, design team board, cluster: Privacy)

**Literature:** Nordhoff et al. 2020 (proposed responses to pedestrians who test the shuttle include having the vehicle's sensors flag non-compliant road users to police); Kooijman, Happee, and de Winter 2019 (future work imagines vehicles reading pedestrians' posture to infer their intention).

**Why it matters for equitable access:** Quote 1 is the clearest case in the corpus. The in-person rule makes the count reliable, and the person who cannot travel is excluded *by design*. Also apply `MISALIGNMENT > IDEAL_VS_ACTUAL_TRAVELER`.

**Feedback:**

---

### EFF_VALUE > SAFETY_ENG

**Status:** Reworded

**Literature strength:** Strong

**Transcript strength:** Weak (no direct quote yet)

**Current definition:** Safety or acceptance is operationalized as a measurable, tunable system property, such as take-over time, perceived safety, or acceptance scores.

**Proposed definition:** Safety is treated as a number the vehicle has to hit (take-over time, crossing speed, perceived-safety score), measured mostly on typical test drivers in simulators. Two things are left out: whether a particular person feels safe enough to use it, and who is put at risk without choosing to be.

**Include when:** A study converts safety into a system measure, a model input, or an optimization target.

**Exclude when:** The passage is about feeling safe in a social sense (neighborhood, weather, being known). Code that as community concern, not `SAFETY_ENG`.

**Example quotes:**
- None found yet. Community talk about safety in our transcripts is social, not technical. Suggest keeping this as a literature-only subcode unless a quote turns up.

**Literature:** Mechanism 3: Zhang, de Winter, Varotto, Happee, and Martens 2019 (meta-analysis of 129 take-over studies, 4,556 participants, almost all working-age drivers in simulators); Pedroff 2025 (crossing initiation time as the main safety and efficiency outcome); Kooijman et al. 2019 (walking speed used as a safety index); Nordhoff et al. 2020 (perceived safety assembled from vehicle cues to be engineered); London and Danks 2018 (safety as a certification problem; pedestrians and neighbors never opted in).

**Feedback:**

---

### EFF_VALUE > TRUST_METRIC

**Status:** Kept

**Literature strength:** Strong

**Transcript strength:** Contrast only

**Current definition:** Trust is measured and tuned as an individual psychological score rather than built and sustained through an ongoing relationship.

**Proposed definition:** (Kept as is.) Plain-language version, if wanted: Trust is treated as a score to raise or "calibrate" in a lab so that people use the vehicle correctly, not as something built by knowing and being known.

**Include when:** Trust-in-automation studies that model, score, or calibrate trust. Contrast with `JUST_TRUST`, which concerns relational trust.

**Exclude when:** Relational trust or being known (`JUST_TRUST`).

**Literature:** Mechanism 2: Kraus, Scholz, Stiegemeier, and Baumann 2020; Lee and Kolodge 2020; Alkurdi and Alsaid 2025 (over 90% of the 80 reviewed studies rely on simulators and self-report surveys); Zoellick et al. 2019; Tan et al. 2025 (contrast).

**Note:** This one sits closer to the `JUST_TRUST` owner's work than to equitable access. Suggest leaving it as is and coordinating with them.

**Feedback:**

---

### EFF_VALUE > ACCESS_AS_EFF

**Status:** Kept

**Literature strength:** Food Justice thread

**Transcript strength:** Excluded by its own rule

**Current definition:** Digital food platforms judge access against an efficiency standard instead of a procedural-inclusion or recognition one.

**Proposed definition:** (Kept as is; the Food Justice thread owns this subcode.)

**Include when:** Lit claims that platforms or systems treat access as optimization. Also apply `JUST_ACCESS`; add `MISALIGNMENT` when a value gap is explicit.

**Exclude when:** Digital-only pantry rules in the transcripts.

**Literature:** Mechanism 3: Joassart-Marcelli, Bosco, and McFadden 2026; Deener 2017.

**Note:** Because its exclusion rule makes it literature-only, the transcript quotes about phones and online-only systems sit under `MISALIGNMENT > IDEAL_VS_ACTUAL_TRAVELER` instead. See open question 3.

**Feedback:**

---

# Parent code: MISALIGNMENT

**Key concept (Column A):** efficiency-driven values are distant from community concerns

**Status:** Reworded

**Literature strength:** Weak in our thread

**Transcript strength:** Strong

**Current definition:** A named/implied value-level gap between efficiency-driven logic and community-grounded values (can be calm, reflective, not necessarily a live reaction). `MaSS_New_Codes.md` version: A gap between what an efficiency-driven system is built to optimise and what the community needs or values. The gap may be stated outright or implied, and expressed calmly or in reaction.

**Proposed definition:** A gap in whose efficiency gets counted. Efficiency-driven design counts the system's efficiency (move more, faster, cheaper, with fewer people). Community members count efficiency in their own lives (time, effort, money, strain) and in whether they can get where they need to go at all. Code it when the passage shows both sides, or clearly implies one: the system logic, and the person, need, or community-defined efficiency it leaves out.

**Include when:** The passage connects a system efficiency choice to an access cost or a cost in someone's daily life, or shows the two pulling in opposite directions. It can be calm and reflective.

**Exclude when:**
- There is confusion or pushback, but no value gap is articulated: code `BREAKDOWN` only.
- An access barrier is described with no system logic behind it: code `JUST_ACCESS` only.

**Coding note:** Rule of thumb: `EFF_VALUE` = the system's efficiency; `COMMUNITY_EFFICIENCY` = the community's efficiency; `JUST_ACCESS` = the need; `MISALIGNMENT` = the gap between them.

**Literature:** Thesis clause C5. Engineering & Safety thread: only 9 of 17 papers support C5 directly or partly (1 directly). The engineering literature describes the efficiency values but rarely names the gap, so `MISALIGNMENT` has to be shown mainly through the transcripts.

**Feedback:**

---

### MISALIGNMENT > COMMUNITY_EFFICIENCY

**Status:** New

**Literature strength:** Medium (Equity, Food Justice threads)

**Transcript strength:** Strong

**Proposed definition:** Efficiency as community members define it, rooted in daily life: what saves or costs a person their own time, effort, money, or strain when getting help (not missing work, not waiting for hours, not standing in the cold, not facing a crowd). It is measured from the person's life, not from the system. Coding it alongside system-centered efficiency (`EFF_VALUE`) shows whose efficiency a design counts.

**Include when:** A client, weaver, or stakeholder describes what makes getting help quick, easy, or worth the trip in terms of their own time, effort, money, or strain. Code it whether a feature delivers that (drive-through, appointment slot) or fails to (an afternoon lost to a lottery, Saturday-only hours).

**Exclude when:**
- The issue is whether the person can get there at all (no ride, no route, cannot afford it): code `JUST_ACCESS` (for example `TRANSPORT_UNAVAILABLE`, `TRIP_COST`).
- The efficiency is measured from the system's side (boxes per shift, vehicles per hour): code `EFF_VALUE`.
- The praise is for a relationship or a person, not for saved time or effort: code `JUST_TRUST`.

**Related coding:** When a system efficiency gain costs community efficiency, also code `BURDEN_SHIFTED`. When the same feature fits one person's life and fails another's (an appointment slot for a fixed-shift worker versus Saturday-only hours for families who work then), code both excerpts here so the contrast is visible.

**Example quotes:**
1. ★ "My appointment time." / "That I don't have to miss work." (sec-Participant 16, 15:53:59 and 15:54:21, on why visiting after work works well). Efficiency measured as protecting her paycheck.
2. ★ "Having the sense of not being around a lot of people and being able to just drive through." (sec-Participant 05, 15:55:08, on what makes the trip manageable). Efficiency measured as less social strain.
3. "Quick." (sec-Participant 13 SP, 15:17:25; translated, answering what would make a new program easier to try). Efficiency measured as the person's own time.
4. "So I believe that they would utilize it, especially in the wintertime because it's cold." (Plaud Hope, 00:47:50, Speaker 8, client, answering the driverless-car prompt). Efficiency measured as bodily cost.
5. Community efficiency lost: "So you can be the first ones in line and not get out." (Plaud Ministries of Love, 00:22:13, Speaker 7, client, on a pantry lottery). Double-code with `BURDEN_SHIFTED`.

**Counter-voice (a community-defined measure, from stakeholders):**
- New metrics that measure the "weights of burden" and capture the ultimate benefit to the end user (transcript_workshop3, line 61, stakeholder board, cluster: ROI)

**Literature:** Brenton, Tindall, Glanz, and Virudachalam 2025 (Food Justice thread: "minimised access and preparation burden" is one of six components of a high-dignity food assistance experience); Levine 2024 (Equity thread: intersectionality as "overlapping identities shaping distinct travel burdens"). Contrast from our thread: Park et al. 2024 does not count new trips by people who could not previously drive, so the efficiency that matters most to non-drivers is outside the model.

**Why it matters for equitable access:** It turns the argument from "efficiency versus community" into "efficiency for whom." The community is not against efficiency; it measures efficiency from a different place. Coding note: when reporting counts, report `COMMUNITY_EFFICIENCY` separately from the other `MISALIGNMENT` subcodes, because some of its excerpts describe a fit (drive-through, appointment slot) rather than a gap.

**Feedback:**

---

### MISALIGNMENT > IDEAL_VS_ACTUAL_TRAVELER

**Status:** Reworded

**Literature strength:** Strong

**Transcript strength:** Strong

**Current definition:** (From `MaSS_New_Codes.md`; not yet in the xlsx.) A system is designed around an imagined typical traveler whose circumstances differ from those of the people who actually rely on it.

**Proposed definition:** The system is designed and tested for a typical user: a working-age person who drives, owns a phone, keeps a steady schedule, and can stand in line and carry boxes. The people who actually rely on the service do not match that picture, so the design fails them.

**Include when:** A passage shows the gap between who the system assumes and who actually shows up (or cannot show up).

**Exclude when:** A person describes their own barrier with no assumed user behind it (code `JUST_ACCESS` subcodes such as `PHYSICAL_MOBILITY_LIMIT`).

**Example quotes:**
1. ★ "I think I would take a car. You know why? Why? Because I don't know how to drive. I've never had a license." (Plaud Hope, 00:47:10, Speaker 7, client, answering the driverless-car prompt)
2. ★ "They expect me to do things I'm not physically capable of." (sec-Participant 14, 15:21:45, answering what makes them hesitant to use job coaching or financial help)
3. "But if you go to the community cupboards online, on your phone, a lot of people have smartphones." (Plaud Ministries of Love, 00:23:13, Speaker 3, client), set against "not everybody has the phone." (Plaud Ministries of Love, 00:45:16, Speaker 3, client)
4. "He said, there's no paper application? I said, no, I haven't seen one in years." (Old Bethel interview, 01:27:21, community weaver)
5. "AV cannot be designed for everyone. It's not the next big solution." and "All personas are not the same. They have different needs" (transcript_workshop3, lines 149 to 150, stakeholder board, cluster: People centered)
6. "Homebound people miss out on transportation ideations" (transcript_workshop3, line 123, stakeholder board, cluster: Home Bound)

**Literature:** Zhang et al. 2019 (all 129 studies used ordinary working-age drivers; no data on elderly drivers, disabled drivers, or non-drivers); Lee and Kolodge 2020 (every respondent was a driver); Kraus et al. 2020 (young, mostly student samples); Kooijman et al. 2019 (24 mostly young students); Zoellick et al. 2019 (self-selected, young sample); Peng, Wu, Qie, and Iwaki 2022 (older adults framed as a population to test and screen for driving performance, not as riders to serve).

**Why it matters for equitable access:** The strongest bridge between the engineering literature and the transcripts. The literature tests on the "ideal traveler," and the transcripts show the people outside that picture. Quote 1 matters doubly: a non-driver sees an AV as a way *in*, the opposite of the driver-centered literature.

**Feedback:**

---

### MISALIGNMENT > CAPACITY_NOT_ACCESS

**Status:** New

**Literature strength:** Strong

**Transcript strength:** Medium

**Proposed definition:** More capacity or a faster network does not mean more people can reach what they need. The system gets better at moving trips that already happen, while the trip a person cannot make stays impossible.

**Include when:** A passage shows a gap between system performance (capacity, routes, coverage) and whether a person can actually reach a destination.

**Exclude when:** The passage questions *what the technology is for* or who decided its purpose. That is `PURPOSE_EXCLUSION`.

**Example quotes:**
1. ★ "I think it would be used because it's a lot of bus stops and a lot of times the bus stops to your destination is not close." (Plaud Hope, 00:47:41, Speaker 8, client, answering the driverless-car prompt)
2. "So, because that's one of the biggest obstacles, bless you, is the transportation to the pantry." (Old Bethel interview, 42:34, community weaver, on the missing bus stop near the pantry)

**Literature:** Mechanism 3: Lu et al. 2020 (models capacity under fixed demand and says nothing about who travels, why, or whether higher throughput translates into access); Park et al. 2024 (assumes travel patterns stay fixed and does not count new trips by people who could not previously drive); Pimenta et al. 2023 (no reviewed study asked whether freed parking could go to community-defined uses).

**Why it matters for equitable access:** The most direct statement of our thread's claim. The engineering literature measures the network; the community measures whether they can get there.

**Feedback:**

---

### MISALIGNMENT > BURDEN_SHIFTED

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong

**Proposed definition:** The system gains efficiency by spending the community's. An efficiency gain for the system is paid for by the person using it: more waiting, more travel, more carrying, fewer choices. The system's numbers improve while the person's day gets harder.

**Include when:** The passage ties a cost in someone's time, effort, money, or choice to an efficiency choice by the system (batching, rationing, fixed slots, boxes, lanes).

**Exclude when:** The burden is described with no system choice behind it. Use the teammate's `JUST_ACCESS > TRIP_COST` or `CARRY_BURDEN`, or `COMMUNITY_EFFICIENCY`, instead.

**Example quotes:**
1. ★ "Now we just put it in the box and move on. Because like I said, the volume got so much from 100 to 350, 400, we couldn't just keep letting them stay in there" (Old Bethel interview, 15:03, community weaver). The pantry gained speed, and clients lost the ability to choose. Double-code with `THROUGHPUT`.
2. ★ "And so you can be sitting there at two o'clock. They don't even open in the doors until like three thirty and they don't even start until four. So you can be the first ones in line and not get out." (Plaud Ministries of Love, 00:22:13, Speaker 7, client, on a pantry that replaced first-come-first-served with a "card shuffler")
3. "Time is a factor - beyond 9-5. Food pantry works on Saturday mornings - many families work at that time" (transcript_workshop3, line 129, stakeholder board, cluster: Time (End Users))

**Literature:** Park et al. 2024 (below about 20% to 30% AV share, an AV-only lane sits underused while human-driven traffic is squeezed into fewer lanes and congestion worsens: the cost of the efficiency bet falls on non-AV users). Food Justice thread: Deener 2017 (efficiency-led reorganization of the food system), already linked through `INFRA_FRAME > EFFICIENCY_SURPLUS`.

**Why it matters for equitable access:** This is the core misalignment pattern once efficiency is split into system and community efficiency: one is bought with the other. Overlaps with `JUST_FLEXIBILITY` for fixed slots and hours; see open question 1.

**Feedback:**

---

### MISALIGNMENT > ACCESS_DEFERRED

**Status:** New

**Literature strength:** Strong

**Transcript strength:** Weak (one quote)

**Proposed definition:** Access or equity is noticed but set aside: moved into the limitations section, called "future work," or made to wait behind another study, while efficiency and safety go first.

**Include when:** An access or equity concern is acknowledged and then explicitly postponed or ranked as less important.

**Exclude when:** Access is never mentioned at all. That absence is evidence for `EXPERTS_CENTERED` or the thread-level counts, not this code.

**Example quotes:**
1. ★ "I want to have them do a little, they always do a sustainability study. Okay, yeah, they gotta do a study. Gotta do a study. Feasibility, sustainability, gotta do it." (Old Bethel interview, 42:11, community weaver, on asking IndyGo for a bus stop near the pantry), followed by "So we're waiting on that" (same timestamp)

**Literature:** Lee and Kolodge 2020 (availability, privacy, and fairness explicitly set aside as less salient than safety; the authors concede that dispatch algorithms may be biased against certain socioeconomic groups but file this under future concerns); Zhang et al. 2019 (no data on elderly, disabled, or non-drivers, named only as a limitation); Park et al. 2024 (new trips by people who could not previously drive named only as a limitation); Pimenta et al. 2023.

**Why it matters for equitable access:** A pattern specific to the Engineering & Safety thread. The literature does not deny access matters; it keeps postponing it. Strong for the literature section, thin in the transcripts.

**Feedback:**

---

## Decision log

1. **v2 (Nov 1):** `EFFICIENCY_SERVES` replaced by `MISALIGNMENT > COMMUNITY_EFFICIENCY` (Amy's decision). Reason: efficiency in AV design is system-centered; the community's efficiency is rooted in daily life, so the "counter-evidence" quotes are really community-defined efficiency. The stakeholder microtransit idea (transcript_workshop3, line 97) was dropped from this code because it is a design proposal, not a description of daily-life efficiency.
2. **v2 (Nov 1):** `EFF_VALUE` and `MISALIGNMENT` parent definitions reworded around "whose efficiency gets counted." `BURDEN_SHIFTED` reworded as "the system gains efficiency by spending the community's."
3. **v2 (Nov 1):** "Quick." (sec-Participant 13 SP) moved from an `EFF_VALUE` exclusion example to a `COMMUNITY_EFFICIENCY` example. The Hope winter quote moved from a `SAFETY_ENG` "possible contrast" to `COMMUNITY_EFFICIENCY`.

## Evidence corrections found while checking quotes

These are corrections to how three quotes appear in `analysis/synthesis.md`. Worth knowing before anyone reuses them.

1. **"it's not fair for all of us to be dominated, replaced by all this kind of technology conversation"** (Plaud Hope, 00:53:02 to 00:53:35) is spoken by **Speaker 2, the facilitator**, not a participant. Speaker 8 responds "Oh, yeah, it's horrible." Left out of this draft. If used, attribute it to the facilitator.
2. **Workshop 1's cost question is cut off in the synthesis.** The full board note continues: "...to improve the distribution efficiency **and have workforce capacity to fulfill other social services needs**" (transcript_workshop1, line 94). The team framed efficiency as a way to free people up for social services, which softens the "efficiency only" reading. Not used as a main example for that reason.
3. **"it would be good to have someone who can assist us... Quick."** (cited as sec-participant-13-sp, 15:17:25) is stitched together. At 15:17:25 the client says only "Quick." The "assist us" wording is not in that turn. The draft uses "Quick." alone.

## Open questions for you

1. **Scope:** Should `MISALIGNMENT` subcodes stay focused on equitable access, or also cover gaps with relational trust and flexibility? `BURDEN_SHIFTED` and `COMMUNITY_EFFICIENCY` already overlap with `JUST_FLEXIBILITY` (fixed slots, Saturday hours).
2. **`VERIFY_TO_COUNT` vs `CONDITIONALITY`:** Your teammate used the Hope in-person-pickup context under `CONDITIONALITY`. Keep both codes (the system needs to count people vs. the person is judged as deserving), or merge?
3. **`ACCESS_AS_EFF` exclusion rule:** Should we ask the Food Justice owner to drop the "digital-only pantry rules in the transcripts" exclusion, so the phone and online-only quotes can live there instead of under `IDEAL_VS_ACTUAL_TRAVELER`?
4. **`SAFETY_ENG` and `TRUST_METRIC`:** Fine as literature-only subcodes, or should I search harder for transcript examples?
5. **Literature quotes:** The literature entries summarize the tracker rows. Do you want verbatim, page-cited quotes from the papers for the Source column? (That needs the PDFs, which are not all in `papers/`.)
6. **`COMMUNITY_EFFICIENCY` and `JUST_ACCESS`:** Is the boundary clear enough (community efficiency = what it costs a person in their day; `JUST_ACCESS` = whether they can get there at all), or should we check it with your `JUST_ACCESS` teammate?
