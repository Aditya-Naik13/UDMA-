# Amy's codebook section: INFRA_FRAME, EFF_VALUE, MISALIGNMENT, PROVOCATION, BREAKDOWN (DRAFT v3)

Owner: Amy (Engineering & Safety-dominant AV Discourse thread)
Status: draft for review. Nothing here has been written into the team file `MaSS_Codebook_with_subcodes.xlsx`.
Review workbook: `MaSS_Codebook_with_subcodes_Amy_review.xlsx`, rebuilt from this file with `python3 Codebook/process/build_amy_review.py`. Edit this file, not the workbook.

## What this section of the codebook has to show

This section covers the codes under four key concepts:

| Key concept (Column A) | Codes | Link to the paper |
|---|---|---|
| AVs are not simply transportation vehicles but infrastructure | `INFRA_FRAME` | Thesis clause C1 |
| efficiency-driven values inherited from transportation engineering | `EFF_VALUE` | Thesis clause C3 |
| efficiency-driven values are distant from community concerns | `MISALIGNMENT` | Thesis clause C5 |
| speculative AV provocation surfaced how participants reasoned about mobility | `PROVOCATION`, `BREAKDOWN` | The method: how our findings were produced |

The claim behind each, in one line:

> INFRA_FRAME: An AV is not one car or one ride. It becomes part of the shared systems a community depends on (transit networks, funding, rules, places), so who shapes it matters.

> EFF_VALUE and MISALIGNMENT: The efficiency-driven values AVs inherit from transportation engineering are distant from what the community needs, especially equitable access. The gap is whose efficiency gets counted: the system's or the community's.

> PROVOCATION and BREAKDOWN: A speculative AV, a technology participants have never used, worked as a conversation starter that surfaced how they reason about mobility. The moments where it did not land are data, not failures.

On efficiency (since v2): AV design counts the system's efficiency (vehicles per hour, boxes per shift, cost per delivery). Community members count efficiency in their own lives (not missing work, not waiting for hours, not standing in the cold). The claim is not "efficiency versus community," it is "efficiency for whom."

What the evidence base looks like (from `crosscomp/thesis_clause_summary.csv`, `who_is_centered_counts.csv`, and the transcripts):

- C1 (AVs are infrastructure) rests on the Engineering & Safety thread: 14 of 17 papers support it directly or partly (6 directly). The other threads barely touch it: Equity 1 of 39, Participatory Method 3 of 11, Food Justice 1 of 15.
- C3 (efficiency values): 17 of 17 Engineering & Safety papers support it directly or partly (12 directly).
- C5 (misalignment): only 9 of 17, and only 1 directly. The engineering literature describes the efficiency values but rarely names the gap itself.
- 0 of the 17 Engineering & Safety papers center community members or residents (9 center engineers, 4 regulators, 4 researchers).
- A real AV prompt appears in only 4 sources: the Hope and Ministries of Love focus groups, Workshop 1 (design team), and Workshop 3 (stakeholders). None of the 29 AI interview transcripts contains one. The Participatory Method thread (11 papers) grounds the provocation method.

**What this means for coding:** `INFRA_FRAME` and `EFF_VALUE` can lean on the literature. `MISALIGNMENT`, `PROVOCATION`, and `BREAKDOWN` have to be shown through the transcripts. One finding to keep in view: community members framed the AV as a personal ride, not as infrastructure. The infrastructure framing in our transcripts comes from stakeholders and the design team.

## How to tell the codes apart

| Code | What the passage shows | Quick test |
|---|---|---|
| `INFRA_FRAME` | **The system.** The AV or mobility as part of networks, funding, rules, and places that last for years. | "Is this about one ride, or about the system the ride belongs to?" |
| `EFF_VALUE` | **The system's efficiency.** A goal, measure, or design choice framed as moving more, faster, cheaper, with fewer people, measured from the system's side. | "What is this system trying to maximize?" |
| `MISALIGNMENT > COMMUNITY_EFFICIENCY` | **The community's efficiency.** What saves or costs a person their own time, effort, money, or strain. | "What does getting help cost this person in their day?" |
| `JUST_ACCESS` (teammate's code) | **The need.** Someone can or cannot get to the service at all. | "Who can't get there, and why?" |
| `MISALIGNMENT` | **The gap.** The system's efficiency costs someone their access or their own efficiency, or the two clearly pull in opposite directions. | "Whose efficiency does this choice count, and whose does it ignore?" |
| `PROVOCATION` | **The reasoning.** What people say, imagine, or ask because they were given the AV prompt. | "Would they have said this without the AV prompt?" |
| `BREAKDOWN` | **The pushback.** The prompt does not land as posed: resistance, conditions, a redirect to another fix, or a reframed question. | "Did they accept the question as asked, or change it?" |

A single excerpt often gets several of these. Apply `MISALIGNMENT` only when the passage links the two sides. Two separate observations that happen to sit next to each other do not count. `MISALIGNMENT` can be calm; `BREAKDOWN` is a live reaction to the prompt. The same excerpt can carry both.

## Summary of proposed subcodes

| Parent | Subcode | Status | Literature | Transcripts |
|---|---|---|---|---|
| `INFRA_FRAME` | `NETWORK_LINK` | **New** | Medium | Strong (stakeholders) |
| `INFRA_FRAME` | `EXISTING_SYSTEM` | **New** | Medium | Strong (includes community) |
| `INFRA_FRAME` | `FUNDING_OWNERSHIP` | **New** | Weak (one paper) | Strong (stakeholders) |
| `INFRA_FRAME` | `GOVERNANCE_REGIME` | **New** | Strong | Medium (stakeholders) |
| `INFRA_FRAME` | `AV_AS_FACILITY` | **New** | Medium | Strong (design team) |
| `INFRA_FRAME` | `LONG_TERM_RESHAPE` | **New** | Strong | Weak (one board note) |
| `INFRA_FRAME` | `EFFICIENCY_SURPLUS` | Existing, definition reworded | Food Justice thread | None found yet |
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
| `PROVOCATION` | `REASON_FROM_GAP` | **New** | Medium | Strong |
| `PROVOCATION` | `IMAGINED_USE` | **New** | Medium | Strong |
| `PROVOCATION` | `AV_AS_PROMPT` | **New** | Strong | Medium |
| `PROVOCATION` | `REPLACEMENT_LENS` | **New** | Medium | Weak (one quote) |
| `BREAKDOWN` | `LOW_TECH_REDIRECT` | **New** | Medium | Strong |
| `BREAKDOWN` | `CONDITIONS_SET` | **New** | Medium | Medium |
| `BREAKDOWN` | `SOLUTION_SKEPTICISM` | **New** | Medium | Medium (stakeholders) |
| `BREAKDOWN` | `RELATIONAL_REFRAME` | **New** | Medium | Strong (stakeholders) |
| `BREAKDOWN` | `FRICTION_MANAGED` | Existing, definition reworded | Strong | Literature only |

Locator format follows the `JUST_ACCESS` rows: `(source, timestamp or line, speaker, role)`. Every quote below was checked word for word against the raw transcript files in `transcripts/`. ★ marks a quote I suggest using as the main example. Workshop 1 notes are either a raw idea from the team or an HMW ("How might we") prompt written by the facilitator; the locator says which. Workshop 3 notes are a synthesis map of the stakeholder board with contributor names omitted.

---

# Parent code: INFRA_FRAME

**Key concept (Column A):** AVs are not simply transportation vehicles but infrastructure

**Status:** Reworded

**Literature strength:** Strong (Engineering & Safety thread)

**Transcript strength:** Medium (mostly stakeholders and design team)

**Current definition:** Treats the AV as infrastructure-scale reshaping daily life/dependency long-term vs. a one-off consumer product.

**Proposed definition:** The passage treats an AV not as a single car or a single ride, but as part of the shared systems a community depends on: transit networks, funding and ownership, rules and agencies, and the places and services people use. Like a bus line, it is built once, shapes daily life for years, and decides who gets served, so who designs it matters.

**Include when:** The AV, or mobility generally, is described as part of a larger system: connected to transit lines or a service network, paid for or owned through public or nonprofit funding, governed by rules and agencies, standing in for missing facilities, or changing places and habits over time.

**Exclude when:**
- The AV is treated as a single ride or trip with no systemic framing (for example, a car that drives you "like the Uber"). Code `PROVOCATION > REASON_FROM_GAP` or `IMAGINED_USE` instead.
- Community care networks are described as infrastructure with no technology or system link: code `CARE_INFRA`.

**Coding note:** In our transcripts, community members framed the AV as a personal ride, not as infrastructure (Plaud Hope, 00:47:10). The infrastructure framing came from stakeholders (Workshop 3) and the design team (Workshop 1). Treat that as a finding: the "AV as infrastructure" claim rests on the literature and the institutional side, while community members reason about mobility trip by trip and about the bus system they already use. Also: at Plaud Hope 00:54:18 it is the facilitator, not a participant, who calls community care "infrastructure"; do not code it as participant evidence.

**Literature:** Thesis clause C1. Engineering & Safety thread: 14 of 17 papers support C1 directly or partly (6 directly: Hicks, Kingsley, and Isett 2025; London and Danks 2018; Robles and Mallinson 2024; Pimenta, Kamruzzaman, and Currie 2023; Park, Jang, and Ko 2024; Lu et al. 2020). Other threads: Equity 1 of 39 (Bahman et al. 2026), Participatory Method 3 of 11 (Van Wynsberghe and Guimarães Pereira 2022 directly), Food Justice 1 of 15 (Deener 2017, partly).

**Feedback:**

---

### INFRA_FRAME > NETWORK_LINK

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong (stakeholders)

**Proposed definition:** The AV is understood as one link in a larger mobility network, filling a gap between existing pieces (a bus stop and the pantry, a transit line and a home), not as a stand-alone vehicle. Its value depends on what it connects to.

**Include when:** An AV or service idea is positioned relative to transit lines, stops, routes, the first and last mile, or other services.

**Exclude when:** A personal ride with no connection to a wider network (`PROVOCATION > REASON_FROM_GAP`).

**Example quotes:**
1. ★ "Microtransit: a key idea is using small AV's as micro transit shuttles to solve the first and last mile problem, connecting locations like food pantries to main public transit lines" (transcript_workshop3, line 97, stakeholder board, cluster: Micro transit)
2. ★ "Microtransit: busstop 1 mile away from pantry. AV can drop off user to the pantry to fill the walking gap" (transcript_workshop3, line 96, stakeholder board, cluster: Micro transit)
3. "AV implementation idea by MPO: pantry opens at a particular time, we can do inter-shuttling with bigger shuttles, substitute BRT line" (transcript_workshop3, line 100, stakeholder board, cluster: Micro transit)
4. "Last mile challenge → possible ecosystem like Uber pickups. Connect all notification, ring, door bell" (transcript_workshop3, line 126, stakeholder board, cluster: Last mile)

**Literature:** Pimenta, Kamruzzaman, and Currie 2023 (AV effects on cities depend on how the vehicles are owned and operated: shared AVs tend to support denser centers, private AVs tend to encourage sprawl); Lu et al. 2020 and Park et al. 2024 (AVs evaluated as part of a road network and its lanes, though only for capacity); Bahman et al. 2026 (Equity thread: AV deployment as a planning and policy matter that needs proactive planning, community engagement, and adaptive governance; the tracker notes only the abstract and introduction were readable).

**Why it matters:** Pairs with `MISALIGNMENT > CAPACITY_NOT_ACCESS`. The engineering papers model the network for flow; the stakeholders model it for getting someone from the bus stop to the pantry.

**Feedback:**

---

### INFRA_FRAME > EXISTING_SYSTEM

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong (includes community)

**Proposed definition:** An AV would enter a mobility system that already decides who gets where: bus routes, stop locations, fares, funding rules, and federal programs. The barrier is how the system is set up, not the people using it.

**Include when:** A passage locates a mobility barrier in how an existing system is designed, funded, or run.

**Exclude when:** The barrier is described with no system behind it. Use the `JUST_ACCESS` subcodes (for example `TRANSPORT_UNAVAILABLE`, `TRIP_COST`).

**Example quotes:**
1. ★ "Challenges for shepherd is not people but how the system is set (federal program creates challenges)" (transcript_workshop3, line 108, stakeholder board, cluster: limitations of macro transit)
2. ★ "you know i understand the bus system needs supported by you know people paying for it but i also you know they also need to figure out something like you know because not everybody can afford the bus and stuff" (Plaud Ministries of Love, 00:49:19, Speaker 7, client)
3. "And that's one of the big things we're talking about tonight, is our bus system on 16th and Poulson. They don't have no bus stop there." (Old Bethel interview, 41:44, community weaver)
4. "MPO route depends on numbers of houses, schools, and other essential infrastructure" (transcript_workshop3, line 42, stakeholder board, cluster: Route design)

**Literature:** Deener 2017 (Food Justice thread: food deserts were produced by "infrastructural exclusion," a path-dependent reorganization of food distribution that no single actor decided); Hicks et al. 2025 and Robles and Mallinson 2024 (AV policy is made inside existing networks of state agencies, consultants, and industry groups).

**Why it matters:** The strongest community-side evidence for C1's logic. Community members do reason at the system level, about the bus system they already depend on, even though they did not frame the AV that way.

**Feedback:**

---

### INFRA_FRAME > FUNDING_OWNERSHIP

**Status:** New

**Literature strength:** Weak (one paper)

**Transcript strength:** Strong (stakeholders)

**Proposed definition:** Who pays for, owns, and sponsors mobility shapes what it is for. The AV is talked about the way infrastructure is financed: bought with grants, sponsored by a pantry network, or pushed by automakers' interest in adoption. Meanwhile, mobility itself is underfunded as a service.

**Include when:** Grants, budgets, sponsors, ownership, or funding gaps for mobility or for the AV.

**Exclude when:** The cost of a trip falls on the person using it (`JUST_ACCESS > TRIP_COST`).

**Related coding:** Also apply `EFF_VALUE > ADOPTION_AS_SUCCESS` when funding is tied to adoption (the same board loop links adoption to automakers' interest).

**Example quotes:**
1. ★ "Transportation funding gap: a poll of non profits revealed that while transportation is a top client barrier it receives disproportionately low and restricted funding. It is often bundled as a need with grants for other areas rather than being funded as a primary service" (transcript_workshop3, line 23, stakeholder board, cluster: Funding & decision criteria)
2. ★ "AV purchased by non profits by seeking federal grant like how IHN provides grant for refrigerators" (transcript_workshop3, lines 89 to 90, stakeholder board annotation, cluster: Current Infrastructure)
3. "IHN pantry sponsors AV" (transcript_workshop3, line 81, stakeholder board, cluster: Current Infrastructure)

**Literature:** Robles and Mallinson 2024 (state AV policy spreads through shared intergovernmental organizations and industry groups such as the Autonomous Vehicle Industry Association). Thin in our thread; Bahman et al. 2026 may add more once read in full.

**Why it matters:** Quote 1 is a stakeholder-side version of our claim: transportation is a top barrier but is not funded as a primary service. Quote 2 shows the AV imagined as pantry equipment, like a refrigerator, which is a different idea of ownership than a transit service.

**Feedback:**

---

### INFRA_FRAME > GOVERNANCE_REGIME

**Status:** New

**Literature strength:** Strong

**Transcript strength:** Medium (stakeholders)

**Proposed definition:** The AV is something to be governed over time, like infrastructure: regulated in stages, monitored after deployment, steered by agencies and committees. The key question is who sits at the table when the rules are made.

**Include when:** Regulation, policy, planning agencies, committees, approval, or monitoring of AVs or mobility services.

**Exclude when:** The passage is only about whether the community had a say. Use `INPUT_PART_ABSENT` or `INPUT_PART_PRESENT`; use both codes when a governance body and community participation are discussed together.

**Example quotes:**
1. ★ "MPO has a Serve committee which has users of both transit users and micro transit users representing the community" (transcript_workshop3, line 99, stakeholder board, cluster: Micro transit)
2. "Within MPO, reluctancy & hesitancy within midwest about AVs. Also lack of knowledge + understanding about the technology in general" (transcript_workshop3, line 29, stakeholder board, cluster: Awareness)

**Literature:** London and Danks 2018 (an AV's competence depends on its operating conditions and keeps changing after deployment through software updates, so they propose staged approval and post-market monitoring, like drug regulation); Hicks et al. 2025 (states gather AV advice in an "expert" mode and a "convening" mode, both routed through officials, consultants, and industry); Robles and Mallinson 2024 (policy learning among state agencies and industry groups); Bahman et al. 2026 (adaptive governance).

**Why it matters:** London and Danks show an AV is never "finished": it keeps changing after it arrives. That is the infrastructure argument for why community participation has to be ongoing, which is the Mobility as Social Service idea of mobility as an ongoing, relational practice.

**Feedback:**

---

### INFRA_FRAME > AV_AS_FACILITY

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong (design team)

**Proposed definition:** The AV is imagined as a stand-in for community infrastructure that is missing, not only as transport: a mobile pantry, cold storage, a shared space where neighbors gather, or a communications hub.

**Include when:** An idea casts the AV as a facility, space, or service platform that a pantry or neighborhood lacks.

**Exclude when:** The AV only moves people or goods from one place to another (`PROVOCATION > IMAGINED_USE`).

**Example quotes:**
1. ★ "Refrigerated AV unit for pantries who cannot store for large quantities. Meat + Produce" (transcript_workshop1, line 156, design team board, raw idea, cluster: Food Logistics)
2. ★ "AV would have time in an area to wait for neighbors there." (transcript_workshop1, line 108, design team board, raw idea, cluster: Mobile Common Places)
3. "How might we envision AV as modular system to solve lacking infrastructure to enhance service accessibility" (transcript_workshop1, line 30, design team board, HMW prompt written by the facilitator, cluster: Modular AV)
4. "How might we envision AV's as a central communications between pantry, banks, neighbor and logistics" (transcript_workshop1, line 47, design team board, HMW prompt written by the facilitator, cluster: Communication)

**Literature:** Deener 2017 (Food Justice thread: food distribution as a sociotechnical infrastructure); Baumann, Caldwell, Bar, and Stokes 2018 (Participatory Method thread: "infrastructures of the imagination," the idea that a community's capacity to picture and steer its own technological future can be built up like infrastructure).

**Why it matters:** A clear contrast: the design team imagined the AV as a facility; community members imagined it as a ride. Code both so the difference is visible.

**Feedback:**

---

### INFRA_FRAME > LONG_TERM_RESHAPE

**Status:** New

**Literature strength:** Strong

**Transcript strength:** Weak (one board note)

**Proposed definition:** Once in place, AVs change streets, land use, and habits over years, and early choices lock in. The effects land unevenly, depending on who owns and runs the vehicles.

**Include when:** Long-term change to places, land use, travel habits, or dependence, or decisions that will be hard to undo.

**Exclude when:** Short-term effects of a single trip or pilot.

**Example quotes:**
1. "Infrastructure development to adopt AV serviced ecosystem" (transcript_workshop3, line 83, stakeholder board, cluster: Current Infrastructure)

**Literature:** Pimenta et al. 2023 (shared AVs support denser centers and private AVs encourage sprawl; no reviewed study asked whether freed parking could go to community-defined uses such as affordable housing); Park et al. 2024 (converting an existing expressway lane to AV-only); Deener 2017 ("path-dependent" reorganization of food distribution); London and Danks 2018 (an AV's competence keeps changing after deployment).

**Why it matters:** Literature-led for now. Pimenta's gap (nobody asked what communities would do with freed space) is a direct opening for the paper's participation argument.

**Feedback:**

---

### INFRA_FRAME > EFFICIENCY_SURPLUS

**Status:** Reworded

**Literature strength:** Food Justice thread

**Transcript strength:** None found yet

**Current definition:** An efficiency-led reorganization of the food system severed the residents it no longer served, and is the structural context a pantry sits inside.

**Proposed definition:** Some neighborhoods lack good food access because the food system was redesigned over many years to run more efficiently, and that redesign left them behind. No single person decided to cut them off; it built up from many efficiency decisions. Food pantries exist partly to fill the gap those decisions left.

**Include when:** A passage explains *why* a neighborhood lacks food access by pointing to how the food system or its stores, warehouses, or delivery routes were reorganized over time (for example, stores closing or moving because it was cheaper or more efficient).

**Exclude when:**
- The passage only says there is no store nearby, with no explanation of how that came about: code `JUST_ACCESS`.
- The passage describes a reorganization that did not leave anyone worse off.

**Related coding:** Also apply `EFF_VALUE` (the efficiency logic behind the redesign) and `MISALIGNMENT` (the system got more efficient while some communities lost access).

**Literature:** Mechanism 3: Deener 2017 (Food Justice thread: food deserts were not caused by residents' choices or by neighborhoods declining, but by "infrastructural exclusion": a long reorganization of food distribution that cut urban residents off from the stores they relied on. In his words, "the reorganization of spatial and material interdependence into a semi-autonomous and path-dependent force," meaning the changes built on each other until they became hard to reverse).

**Why it matters:** An illustration of the idea (not data from our study): a grocery chain closes small neighborhood stores and opens large suburban ones near highways, because that is cheaper per customer. The chain becomes more efficient; residents without a car lose their store. This subcode shows the pantry sitting inside an infrastructure history, not as a stand-alone charity, and it is the same `EFF_VALUE` logic our thread studies, playing out over decades. No transcript quote yet; literature-only for now.

**Feedback:**

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

**Coding note:** Always record *whose* logic it is: the literature, the design team (Workshop 1; note whether it is a raw idea or a facilitator's HMW prompt), stakeholders (Workshop 3), or an institution as described by a client or weaver. In our transcripts the efficiency logic shows up most clearly in the design team's own ideas and in the pantries' own rules, not in an AV vendor. That supports C6 (a broader pattern, not a one-off AV problem).

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
2. "How might AVs enhance route optimization?" (transcript_workshop1, line 89, design team board, HMW prompt written by the facilitator, cluster: Workforce Optimization)
3. "How might AVs optimize deliveries?" (transcript_workshop1, line 70, design team board, HMW prompt written by the facilitator, cluster: Integrated Logistics)

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
1. ★ "Anticipate the needs of food pantry when threshold is met → place order → got to pick up order • no communication between people" (transcript_workshop1, line 142, design team board, raw idea, cluster: Food Supply Demand)
2. ★ "How might we use AVs to reduce driver needs so manpower can focus on logistics/other business needs" (transcript_workshop1, line 90, design team board, HMW prompt written by the facilitator, cluster: Workforce Optimization)
3. "AV can anticipate the shortage of food. No communication from human" (transcript_workshop1, line 46, design team board, raw idea, cluster: Communication)
4. "Removes the dependence on truck drivers availability and skill set → able to operate at all hours" (transcript_workshop1, line 100, design team board, raw idea, cluster: Expanding operational hours)
5. "Senior citizens are lonely, become friends with AV" (transcript_workshop1, line 173, design team board, raw idea, cluster: Logistics)

**Counter-voice (code with `MISALIGNMENT`, `JUST_TRUST`, or `BREAKDOWN > RELATIONAL_REFRAME`):**
- "Delivery person might be the only point of human contact the home bound people might have" (transcript_workshop3, line 122, stakeholder board, cluster: Home Bound)
- "Indygo: home delivery might be the only personal interaction" (transcript_workshop3, line 159, stakeholder board, cluster: Social service meaning relational engagement not transactional)
- "Maintaining the human relation" (transcript_workshop3, line 162, stakeholder board, cluster: Social service meaning relational engagement not transactional)
- "How might we ensure there is a human element/touch with AVs used as a social service for those they serve → delivery" (transcript_workshop1, line 183, design team board, HMW prompt written by the facilitator; a minority theme in the same workshop)

**Literature:** Nordhoff, Stapel, van Arem, and Happee 2020 (the human safety steward was disguised so riders would experience the shuttle as fully driverless); Zoellick et al. 2019 (riders said the human safety operator shaped their experience, but the researchers treated this as a confound to control rather than something to design around).

**Why it matters for equitable access:** If the driver or volunteer is also the one who knows, checks on, or helps the client, removing them can remove access. Since v3 this is partly evidenced: Workshop 3 stakeholders say a delivery may be a homebound person's only human contact. That is the stakeholders' view; no homebound client was interviewed.

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
3. "Should have some sort of face verification to ensure food is handed to the right person" (transcript_workshop1, line 38, design team board, raw idea, cluster: Privacy)

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

# Parent code: PROVOCATION

**Key concept (Column A):** speculative AV provocation surfaced how participants reasoned about mobility

**Status:** Reworded

**Literature strength:** Strong (Participatory Method thread)

**Transcript strength:** Medium (only 4 sources contain an AV prompt)

**Current definition:** Any participant response reasoning, imagining, questioning directly triggered by the speculative AV concept.

**Proposed definition:** Anything participants say, imagine, or ask because they were given the speculative AV prompt: a driverless car that "somebody can donate" to the community, or the AV concept on a workshop board. The AV is a conversation starter, not the subject. The code records how people reason about mobility when handed a technology that does not exist in their lives yet.

**Include when:** The response follows directly from an AV prompt or an AV concept on a workshop board.

**Exclude when:**
- General mobility talk not tied to the AV prompt.
- Reactions to the AI interviewer. None of the 29 AI interview transcripts contains an AV prompt.

**Coding note:** Record how the prompt was worded, because the wording shapes the answers. In the Hope focus group the facilitator first introduced driverless vehicles as automation "replacing our labor force" (Plaud Hope, 00:26:08), and later as a car that can "run 24 hours seven days" and that "somebody can donate" to the community (00:46:44). Also record the speaker's role: community members, stakeholders, and the design team reasoned very differently.

**Literature:** Participatory Method thread: Liao and Muller 2019 (when a technology is not yet part of everyday life, participatory design fictions are the way to surface values about it); Van Wynsberghe and Guimarães Pereira 2022 (the AV works as a "MacGuffin," a device that sets the story in motion so people imagine alternatives); Omori and Lim 2025 and Wong et al. 2017 (speculative artifacts provoke value reflection; Wong calls them "values levers").

**Feedback:**

---

### PROVOCATION > REASON_FROM_GAP

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong

**Proposed definition:** Participants answer the AV prompt by naming a gap in their own mobility today: no license, a bus stop too far away, the cold. They reason from their current life, not from the technology.

**Include when:** The response to the prompt describes a current mobility gap the AV might fill.

**Exclude when:** A use is imagined with no current gap named (`IMAGINED_USE`).

**Related coding:** Also apply `MISALIGNMENT > IDEAL_VS_ACTUAL_TRAVELER` or `CAPACITY_NOT_ACCESS` when the gap shows who the current system leaves out, and `COMMUNITY_EFFICIENCY` for cold or waiting.

**Example quotes:**
1. ★ "I think I would take a car. You know why? Why? Because I don't know how to drive. I've never had a license." (Plaud Hope, 00:47:10, Speaker 7, client, the first answer to the driverless-car prompt)
2. ★ "I think it would be used because it's a lot of bus stops and a lot of times the bus stops to your destination is not close." (Plaud Hope, 00:47:41, Speaker 8, client)
3. "So I believe that they would utilize it, especially in the wintertime because it's cold." (Plaud Hope, 00:47:50, Speaker 8, client)

**Literature:** Severs, Wu, Diels, Harrow, Singleton, and Winsor 2022 (transport-excluded people hold specific needs that mainstream AV design misses; journey mapping exposes where their mobility breaks down); Van Wynsberghe and Guimarães Pereira 2022 (citizens redefine mobility on their own terms).

**Why it matters:** Shows the provocation worked as intended: a technology no one had used pulled out real, current gaps.

**Feedback:**

---

### PROVOCATION > IMAGINED_USE

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong

**Proposed definition:** Participants say what they would do with an AV. Record whether the imagined use moves people (rides to the pantry, rides for homebound neighbors) or moves goods (delivery, pickup, logistics). The split is itself a finding.

**Include when:** A concrete use is proposed for the AV.

**Exclude when:** The AV is imagined as a facility or space rather than a vehicle (`INFRA_FRAME > AV_AS_FACILITY`).

**Example quotes:**
1. ★ "If a car could drive me when I say put the address in, like the Uber, I could put the address in and I'll just sit there and go, la, listen to my music, dance, and the car just be rolling on where I'm going." (Plaud Hope, 00:47:10, Speaker 7, client) [moves people]
2. ★ "Targeted use case with beta volunteers: moving people with food, or move people to food" (transcript_workshop3, line 70, stakeholder board, cluster: Emergency Box) [both]
3. "Shepherd: AV - more useful to bringing people. More useful to design it so it can be served right out of pantry" (transcript_workshop3, line 68, stakeholder board, cluster: Emergency Box) [moves people]
4. "Using AV's to pick up people instead of food" (transcript_workshop1, line 175, design team board, raw idea, cluster: Logistics) [moves people]
5. "AV over here can help with smaller logistic - pick up of food (e.g. from community gardens, urban farms, roof top gardens)" (transcript_workshop1, line 57, design team board, raw idea, cluster: Community Resource Connection) [moves goods]

**Literature:** Severs et al. 2022 (transport-excluded participants generate their own solutions for a technology they have never used); Baumann et al. 2018 (residents author their own scenarios about future technology instead of researchers authoring them).

**Why it matters:** Workshop 1 leaned heavily toward moving goods (logistics), while community members imagined rides. Which one an idea serves is a direct read of whose needs the AV is imagined for.

**Feedback:**

---

### PROVOCATION > AV_AS_PROMPT

**Status:** New

**Literature strength:** Strong

**Transcript strength:** Medium

**Proposed definition:** The AV prompt opens a conversation about how the community already gets by, and the talk soon leaves the vehicle behind. Code the moment the conversation turns, and code its content with `VALUES`, `PRACTICES`, or `CARE_INFRA` as well.

**Include when:** Within the AV discussion, participants shift to existing practices, needs, or values (how lines and weather work, who picks up for whom). Record whether the shift came from participants or from a facilitator's follow-up question.

**Exclude when:** The talk was never connected to an AV prompt.

**Example quotes:**
1. ★ "It just depends on if it's bad weather, and if that's the case, you know, common sense will tell you don't even try to go, because if you can't get out, they ain't getting out." (Plaud Hope, 00:48:01, Speaker 8, client, after the facilitator asked whether pantries are open in winter)
2. "Yeah, but you're in the car for those who have vehicles. There's maybe two or three people that you'll see standing out there, but for the most part, this pantry, you're in the vehicle." (Plaud Hope, 00:48:13, Speaker 8, client)

**Literature:** Van Wynsberghe and Guimarães Pereira 2022 (the AV as a "MacGuffin": the prompt matters because of the conversation it starts, not as the subject); Omori and Lim 2025 (a speculative prototype provokes reflection on values rather than an opinion of a product); Wong et al. 2017 (speculative artifacts as "values levers").

**Why it matters:** Supports the method claim: the AV prompt was useful less for what people thought of AVs than for what it opened up about their lives.

**Feedback:**

---

### PROVOCATION > REPLACEMENT_LENS

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Weak (one quote)

**Proposed definition:** Participants read the AV through what automation has already done in their lives: a person at a counter, or a job, replaced by a machine.

**Include when:** A response links AVs or automation to people being replaced at work or in a service.

**Exclude when:** The statement comes from the facilitator (Plaud Hope, 00:26:08 and 00:53:35). That is prompt wording, not participant evidence.

**Related coding:** Also apply `EFF_VALUE > HUMAN_REMOVED` when the replaced person was part of the service.

**Example quotes:**
1. ★ "White Castle now white castle has an automated things not even nobody taking your order you walk up and she's like hi I'm Julia your assistant please say your order when you're ready." (Plaud Hope, 00:26:48, Speaker 8, client, right after the facilitator described driverless vehicles as automation replacing jobs)

**Literature:** Tan, Soh, Zhang, Lee, Meng, Sen, and Lee 2025 (Participatory Method thread: social service practitioners fear a new technology threatens the human core of their work, a concern that surfaced only through participatory workshops).

**Why it matters:** The answer was primed by how the facilitator framed the prompt, so treat it as evidence of how participants connect AVs to automation they already know, not as an unprompted fear.

**Feedback:**

---

# Parent code: BREAKDOWN

**Key concept (Column A):** speculative AV provocation surfaced how participants reasoned about mobility

**Status:** Reworded

**Literature strength:** Strong (Participatory Method thread)

**Transcript strength:** Strong

**Current definition:** A specific live moment of resistance, confusion, redirection, or reframing in response to the AV concept code the content of the pushback.

**Proposed definition:** A specific moment when the AV prompt does not land the way it was asked: a participant pushes back, sets conditions, switches to a different fix, or reframes the question. Code what the pushback is about. These moments are treated as data, not as failures of the session: they show where the community's values and the technology's assumptions do not fit.

**Include when:** Live resistance, conditions, redirection, or reframing in response to the AV prompt or concept.

**Exclude when:** Calm, neutral clarifying questions with no resistance or reframing (code `PROVOCATION` only).

**Coding note:** Also apply `MISALIGNMENT` when the pushback names a value gap. `MISALIGNMENT` can be calm and reflective; `BREAKDOWN` is the live reaction. The same excerpt can carry both.

**Literature:** Forlano and Mathew 2014 (design "friction": deliberate moments of disagreement, resistance, and reframing are where embedded values become visible and contestable). Mechanism 5, "Friction as signal, not noise": Forlano and Mathew 2014; Klaever et al. 2025; Agrawaal et al. 2024; Nordhoff et al. 2020; Engelbutzeder et al. 2023.

**Feedback:**

---

### BREAKDOWN > LOW_TECH_REDIRECT

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong

**Proposed definition:** Asked about an AV, participants switch to a simpler fix that already exists: bus passes, vouchers, cheaper fares. The redirect says the problem is affordability and reach, not the lack of a new vehicle.

**Include when:** An AV prompt is answered, or followed in the same exchange, by a low-tech or existing-system alternative.

**Exclude when:** A low-tech suggestion is made with no AV prompt in the exchange (`JUST_ACCESS > TRIP_COST`).

**Related coding:** Also apply `MISALIGNMENT > CAPACITY_NOT_ACCESS` when the redirect implies a new vehicle would not fix reach or cost.

**Example quotes:**
1. ★ "Bus vouchers. Yeah, bus vouchers would be good for people, too." (Plaud Hope, 00:48:32, Speaker 8, client, in the discussion that followed the driverless-car prompt)
2. ★ "what's the sense in having a public transportation if you still can't afford the public transportation" (Plaud Ministries of Love, 00:49:50, Speaker 7, client, right after the AV discussion)
3. Context: "But, you know, it would be good to pass out some bus passes sometimes, you know, to different people." (Plaud Ministries of Love, 00:48:11, Speaker 3, client). Said just before the AV prompt (00:48:17), so the low-tech fix was already on the table when the AV was introduced.

**Literature:** Van Wynsberghe and Guimarães Pereira 2022 (AVs are being built to solve a different problem than the mobility problem people actually have).

**Feedback:**

---

### BREAKDOWN > CONDITIONS_SET

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Medium

**Proposed definition:** Participants accept the AV only under conditions they define themselves: what it may be used for, where it may go, who may ride. They turn "would it help?" into "only if we decide how it is used."

**Include when:** A yes comes with limits or rules set by the participants.

**Exclude when:** A plain yes or no with no conditions (`PROVOCATION` only).

**Related coding:** The `JUST_ACCESS` teammate coded Plaud Ministries of Love 00:48:34 as `JUST_ACCESS > CONDITIONALITY` and `BREAKDOWN`. Here the conditions are set by the community rather than imposed on it; see open question 10.

**Example quotes:**
1. ★ "I think it would, but it would have to be on issues, you know. what reason are they going to the grocery store or they just run into someone's house because you got to be careful with that" (Plaud Ministries of Love, 00:48:34, Speaker 3, client, answering the AV prompt)
2. ★ "destination see where the destination goes yeah limit the destinations to like pantries and" (Plaud Ministries of Love, 00:49:14, Speaker 3, client). Note: the transcript's speaker turns break mid-sentence between 00:49:07 and 00:49:19, so who said which part is uncertain.

**Literature:** Baumann et al. 2018 (community storytelling builds a community's capacity to shape its own technological future instead of having that future imposed on it).

**Why it matters:** The community did not reject the AV; it governed it. This links `BREAKDOWN` to the participation argument (`INPUT_PART_PRESENT`, in a hypothetical form).

**Feedback:**

---

### BREAKDOWN > SOLUTION_SKEPTICISM

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Medium (stakeholders)

**Proposed definition:** Pushback on the AV as a general answer: it cannot serve everyone, it is not "the next big solution," or institutions are reluctant to adopt it at all.

**Include when:** Doubt that the AV fits the people or the context, or reluctance to adopt it.

**Exclude when:** Doubt about one specific feature (code the feature's topic instead).

**Example quotes:**
1. ★ "AV cannot be designed for everyone. It's not the next big solution." (transcript_workshop3, line 149, stakeholder board, cluster: People centered). Also coded under `MISALIGNMENT > IDEAL_VS_ACTUAL_TRAVELER`.
2. "Indy Go AV can't serve singular person." (transcript_workshop3, line 109, stakeholder board, cluster: limitations of macro transit)
3. "Within MPO, reluctancy & hesitancy within midwest about AVs." (transcript_workshop3, line 29, stakeholder board, cluster: Awareness)

**Literature:** Van Wynsberghe and Guimarães Pereira 2022 (the mismatch between what the industry builds AVs for and the mobility problem people have).

**Feedback:**

---

### BREAKDOWN > RELATIONAL_REFRAME

**Status:** New

**Literature strength:** Medium

**Transcript strength:** Strong (stakeholders)

**Proposed definition:** Participants reframe the AV question from logistics to relationships: the service only works if it keeps the human contact, which for a homebound person may be the only contact they have.

**Include when:** Pushback that the AV must keep, or be designed around, a human relationship.

**Exclude when:** Trust in a known person is described with no AV prompt (`JUST_TRUST` only).

**Related coding:** Also apply `JUST_TRUST`. These quotes are the counter-voice to `EFF_VALUE > HUMAN_REMOVED`.

**Example quotes:**
1. ★ "AV barrier: it needs to be intentional about the relation" (transcript_workshop3, line 160, stakeholder board, cluster: Social service meaning relational engagement not transactional)
2. ★ "Delivery person might be the only point of human contact the home bound people might have" (transcript_workshop3, line 122, stakeholder board, cluster: Home Bound)
3. "Indygo: home delivery might be the only personal interaction" (transcript_workshop3, line 159, stakeholder board, cluster: Social service meaning relational engagement not transactional)
4. "How might we ensure there is a human element/touch with AVs used as a social service for those they serve → delivery" (transcript_workshop1, line 183, design team board, HMW prompt written by the facilitator)

**Literature:** Tan et al. 2025 (threats to the human core of social service work surface in participatory workshops); Forlano and Mathew 2014.

**Feedback:**

---

### BREAKDOWN > FRICTION_MANAGED

**Status:** Reworded

**Literature strength:** Strong

**Transcript strength:** Literature only

**Current definition:** The AV field reads the same friction one thread treats as data, pedestrians testing a shuttle, stepping in front of it, pressing the emergency button, as distrust to manage, up to flagging non-compliant users to police.

**Proposed definition:** How the AV field responds when people push back on the technology (pedestrians testing a shuttle, stepping in front of it, pressing the emergency button). The field takes the pushback seriously, but treats the technology's goal as settled: the question is only how to get people to accept it, not whether and why to do it at all. So it changes the people (educating them, redesigning the vehicle so they comply, sanctioning them, up to flagging non-compliant road users to police) so the technology can go ahead as planned. Our study lets pushback change the plan itself: what the technology is for and how it is designed. The difference is who adapts to whom: the people to the technology, or the technology to the people.

**Include when:** A literature or institutional response treats the technology's goal as settled and tries to bring people around to it (through education, redesign for compliance, or sanctions).

**Exclude when:** The response lets the pushback change what the technology is for or how it is designed. Code the pushback itself under the other `BREAKDOWN` subcodes.

**Related coding:** Also apply `MISALIGNMENT` when the institutional response reveals a value-level gap.

**Literature:** Mechanism 5: Nordhoff et al. 2020 versus Forlano and Mathew 2014. Nordhoff does propose redesigning the vehicle, but toward compliance: making road users behave the way the shuttle needs. Forlano and Mathew treat friction as where people's values become visible and open to debate.

**Why it matters:** A quick test for coders: does the response ask only how to get people to accept the technology, or also whether and why to do it at all? Only "how to get people to accept it" means `FRICTION_MANAGED`. Two illustrations on our own transcripts (the field's reading is hypothetical; our reading is what the draft codes):
- "limit the destinations to like pantries and" (Plaud Ministries of Love, 00:49:14, Speaker 3, client). Managed: explain the safety features so the community accepts the vehicle as planned. Read as a signal: the community wants to decide how the vehicle is used in its neighborhood, so the plan changes (`CONDITIONS_SET`).
- "Bus vouchers. Yeah, bus vouchers would be good for people, too." (Plaud Hope, 00:48:32, Speaker 8, client). Managed: people do not yet understand what an AV offers. Read as a signal: the real problem is affordability and reach, not the lack of a new vehicle (`LOW_TECH_REDIRECT`).

**Note:** Response to the team comment asking whether this code is needed. Recommendation: keep it as a literature-only contrast code. It does not code participants' distrust, so it does not need a boycott-level example in the transcripts. It codes how the field responds to friction. The contrast between people adapting to the technology and the technology adapting to people is what lets the paper argue that our method treats breakdown as data, and it connects to the paper's claim that AVs arrive without community input: managing friction is one way that happens even when people are technically heard. If the team prefers fewer codes, it could move under `EFF_VALUE` as a system logic. See open question 9.

**Feedback:**

---

## Decision log

1. **v2 (Nov 1):** `EFFICIENCY_SERVES` replaced by `MISALIGNMENT > COMMUNITY_EFFICIENCY` (Amy's decision). Reason: efficiency in AV design is system-centered; the community's efficiency is rooted in daily life, so the "counter-evidence" quotes are really community-defined efficiency. The stakeholder microtransit idea (transcript_workshop3, line 97) was dropped from this code because it is a design proposal, not a description of daily-life efficiency.
2. **v2 (Nov 1):** `EFF_VALUE` and `MISALIGNMENT` parent definitions reworded around "whose efficiency gets counted." `BURDEN_SHIFTED` reworded as "the system gains efficiency by spending the community's."
3. **v2 (Nov 1):** "Quick." (sec-Participant 13 SP) moved from an `EFF_VALUE` exclusion example to a `COMMUNITY_EFFICIENCY` example. The Hope winter quote moved from a `SAFETY_ENG` "possible contrast" to `COMMUNITY_EFFICIENCY`.
4. **v3 (Nov 5):** Added Amy's other codes: `INFRA_FRAME`, `PROVOCATION`, and `BREAKDOWN`, with reworded definitions and new subcodes. The six new `INFRA_FRAME` subcodes answer the team file's placeholder row "Add more subcodes from lit defining AV as infrastructure."
5. **v3 (Nov 5):** Workshop 1 locators now say whether a note is a raw idea or an HMW prompt written by the facilitator. The transcript's own legend says HMW prompts are facilitator-authored, so they are weaker evidence of what the team itself proposed.
6. **v3 (Nov 5):** `HUMAN_REMOVED` gap partly filled: Workshop 3 stakeholders say a delivery may be a homebound person's only human contact (lines 122 and 159).
7. **v3 (Nov 5):** The review workbook now shows the team's "Concerns and Comments" next to each code, and the Full Codebook sheet keeps that column.
8. **v3 (Nov 5):** `EFFICIENCY_SURPLUS` rewritten in plain language (Amy's request): simpler definition, include and exclude rules a coder can apply to a transcript, and an everyday illustration labeled as not being study data.
9. **v3 (Nov 5):** `FRICTION_MANAGED` reworded around who adapts to whom (Amy's framing): the field asks only how to get people to accept the technology, not whether and why to do it at all. Added a coder test and two transcript illustrations. Earlier wording ("the opposite of how our study reads friction") made the difference sound like negative versus positive tone, which it is not.
10. **v3 (Nov 5):** Files renamed now that the section covers more than two codes: the draft is `Amy_review_draft.md`, the workbook is `MaSS_Codebook_with_subcodes_Amy_review.xlsx`, and the builder is `build_amy_review.py`.

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
7. **How many `INFRA_FRAME` subcodes:** Six new subcodes may be more than coders need. Possible trims: fold `FUNDING_OWNERSHIP` into `GOVERNANCE_REGIME`, and keep `LONG_TERM_RESHAPE` as literature-only. Which do you want to keep?
8. **Community framed the AV as a ride:** Community members never framed the AV as infrastructure; stakeholders and the design team did. Report this as a finding (C1 rests on the literature and the institutional side), or look for more community evidence first?
9. **`FRICTION_MANAGED`:** The team asked whether it is needed. Keep it as a literature-only contrast code (recommended), move it under `EFF_VALUE`, or drop it?
10. **`CONDITIONS_SET` vs `CONDITIONALITY`:** For Plaud Ministries of Love 00:48:34, are these conditions the community sets (`CONDITIONS_SET`) or conditions imposed on the community (`CONDITIONALITY`)? Worth agreeing with your `JUST_ACCESS` teammate.
11. **Questions back to the researchers:** "So where is all this going to go when you get done with it." (Plaud Hope, 00:52:19, Speaker 8, client). Should participants asking what happens to their input get its own subcode? It relates to `INPUT_PART_ABSENT > DEMOTIVATION_Ill_TREATMENT` and to Barendregt et al. 2024 (participatory futuring often treats publics as data sources rather than authors of the future).
