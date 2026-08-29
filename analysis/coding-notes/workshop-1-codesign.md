# Coding notes: Workshop 1, TMF internal co-design session

- Source file: transcripts/Co design systhesis Transcripts/transcript_workshop1.txt
- Site: other (TMF internal team session, not a community site)
- Type: internal co-design workshop, first-level affinity map (raw, unsynthesized), compiled from FigJam board screenshots
- Language: English
- Format / locator scheme: clustered affinity map. Locator = `CLUSTER: <name>, [Idea]` or `[HMW]`. `[Idea]` = unattributed participant sticky, `[HMW]` = facilitator-authored prompt (Crystal Habib). No timestamps, no per-speaker attribution.
- Participants present: TMF team members (count not given); facilitator/notetaker named in file. No community members present.
- Read in full: yes

Note on use: this is the research/design team talking to itself about AVs, not
community data. Its main analytic value is as evidence of the efficiency-driven
engineering values the paper critiques, visible here in the team's own first
instincts, plus a minority of relational counter-currents. Treat every item as
a team idea, not a community view.

## 1. Values

- Efficiency, optimization, and cost reduction dominate the team's framing.
  Clusters are literally named for it and the verbs are extract, optimize,
  reduce, minimize, eliminate.
  - "How might we use AVs to reduce logistic company cost (labor, time, asset) to improve the distribution efficiency and have workforce capacity to fulfill other social services needs" (transcript_workshop1.txt, CLUSTER: Workforce Optimization (effect), [HMW])
  - "How might AVs optimize deliveries?" (transcript_workshop1.txt, CLUSTER: Integrated Logistics, [HMW])
  - "Avoid food going bad by quickly picking and delivering through real-time operation" (transcript_workshop1.txt, CLUSTER: Waste Reduction, [Idea])
- Removing the human from the loop is treated as a positive.
  - "AV can anticipate the shortage of food. No communication from human" (transcript_workshop1.txt, CLUSTER: Communication (features), [Idea])
  - "Anticipate the needs of food pantry when threshold is met, place order, got to pick up order, no communication between people" (transcript_workshop1.txt, CLUSTER: Food Supply Demand, [Idea])
  - "Removes the dependence on truck drivers availability and skill set, able to operate at all hours" (transcript_workshop1.txt, CLUSTER: Expanding operational hours (effect), [Idea])
- A relational minority current: some team members push back toward human
  contact, social connection, and the pantry as a place, not just a node.
  - "How might we ensure there is a human element/touch with AVs used as a social service for those they serve, delivery" (transcript_workshop1.txt, CLUSTER: Logistics / AV's + AI Robot + Human Touch point at delivery, [HMW])
  - "How might we envision food pantries as social hubs and logistical hubs to coordinate AVs as mobile pantries" (transcript_workshop1.txt, CLUSTER: Food Logistics (touch point), [HMW])
  - "How might we enhance the social service amenity at food banks when food distribution task is eased by AVs" (transcript_workshop1.txt, CLUSTER: Food Logistics (touch point), [HMW])
- Verification and control framed as a feature, with the burden on the client.
  - "Should have some sort of face verification to ensure food is handed to the right person" (transcript_workshop1.txt, CLUSTER: Privacy, [Idea])
  - "AV over here can contact Arthur till he answers and gives the access code so food can be delivered in hand" (transcript_workshop1.txt, CLUSTER: Logistics, [Idea])

## 2. Capabilities and Constraints

- Constraint the team names for the community: time poverty, information gaps,
  and being homebound or immobile.
  - "How might we design a moving spaces to solve neighbors service access issues (time constraint, information gap). Augmenting their capacity to enhance their well being" (transcript_workshop1.txt, CLUSTER: Community Resource Connection (effect), [HMW])
  - "How might AV help home bound neighbors come to the pantry" (transcript_workshop1.txt, CLUSTER: Home Bound Neighbors, [HMW])
  - "How might AV help neighbors with, time constraints, educational needs, career development" (transcript_workshop1.txt, CLUSTER: Neighbors with time constrain challenges (educational needs), [HMW])
- Constraint named for volunteers and the pantry workforce: aging volunteers,
  physical strain, cars and fuel paid out of pocket.
  - "AV over here can be used at each pantry for smaller orders so volunteers do not have to use their cars/manpower" (transcript_workshop1.txt, CLUSTER: Overuse of volunteer resource, [Idea])
  - "How might AVs help assist aging volunteers reach the pantry" (transcript_workshop1.txt, CLUSTER: Aging Volunteers, [HMW])
  - "AV can carry heavy loads reducing the change of injury and removing limitations" (transcript_workshop1.txt, CLUSTER: Physical Labor, [Idea])
- Constraint named for rural and under-served areas: missing infrastructure.
  - "HMW use modular AVs to address rural areas/places lacking modern infrastructure" (transcript_workshop1.txt, CLUSTER: Modular AV (features), [HMW])
- Coder note: the team frames these as problems for AVs to solve, not as
  capacities the community already exercises. Capability-as-asset framing is
  mostly absent from this transcript; the nearest is the recognition that
  volunteers and pantries already run the last mile with their own cars and
  labor.

## 3. Meanings and Practices

- Mobility is framed almost entirely as logistics: moving food, supplies, and
  labor efficiently between banks, pantries, and doors.
  - "Community AV that all pantries have access to for pantry to pantry transportation (volunteers, food, supplies)" (transcript_workshop1.txt, CLUSTER: Food Supply Demand, [Idea])
  - "AVs (road) can reach to common destination points and can launch 4-6 drones so it could deliver 2-3 items in one go." (transcript_workshop1.txt, CLUSTER: Modular AV (features), [Idea])
- A competing meaning surfaces in a few stickies: mobility as bringing people
  together and reaching people who are isolated.
  - "Using AV's to pick up people instead of food" (transcript_workshop1.txt, CLUSTER: Logistics, [Idea])
  - "AV would have time in an area to wait for neighbors there." (transcript_workshop1.txt, CLUSTER: Mobile Common Places (effect), [Idea])
  - "Can serve as emergency transportation while delivering food to senior citizen if they wanna visit a hospital or elsewhere" (transcript_workshop1.txt, CLUSTER: Accessibility? (for disabled people), Seniors, [Idea])
- Practice: the team repeatedly references an existing operator ("913") that
  already runs trucks and drivers, i.e. the current mobility practice they want
  to automate.
  - "913 has AV Trucks that handle the entire deliver process" (transcript_workshop1.txt, CLUSTER: Workforce Optimization (effect), [Idea])

## 4. Misalignment

- Tension: the team's default design logic is throughput and cost (optimize
  routes, cut drivers, run 24/7, no human communication) vs the relational and
  place-based value of the pantry that a minority of the same team keeps trying
  to protect.
  - Value at stake: relational trust, and secondarily the pantry as a community
    space.
  - "AV can anticipate the shortage of food. No communication from human" (transcript_workshop1.txt, CLUSTER: Communication (features), [Idea])
  - against: "How might we ensure there is a human element/touch with AVs used as a social service for those they serve, delivery" (transcript_workshop1.txt, CLUSTER: Logistics, [HMW])
- Tension: face verification and access codes to "ensure food is handed to the
  right person" vs a pantry norm of low-barrier, no-questions-asked help.
  - Value at stake: relational trust, and equitable access for anyone without
    the required device, face match, or ability to answer a call.
  - "Should have some sort of face verification to ensure food is handed to the right person" (transcript_workshop1.txt, CLUSTER: Privacy, [Idea])
- Tension: loneliness and companionship reframed as something a machine can
  supply, which treats a relational need as a logistics feature.
  - Value at stake: relational trust.
  - "Senior citizens are lonely, become friends with AV" (transcript_workshop1.txt, CLUSTER: Logistics, [Idea])
  - "AVs can be friends with senior citizens as they are alone and feel lonely" (transcript_workshop1.txt, CLUSTER: Logistics, [Idea])
- Coder note: this transcript is itself an artifact of the misalignment the
  paper describes. The efficiency framing is not imposed by an outside vendor
  here, it is the design team's own first response, which is a useful and
  slightly uncomfortable finding.

## 5. Provocation

- Speculative prompt present: yes. The entire session is a speculative AV
  brainstorm, though with the internal team rather than community members.
- Range of ideas generated:
  - AVs as mobile pantries and mobile common spaces that park and wait for
    neighbors. "AV over here is able to deliver food at door steps having a common area to park these devices" (transcript_workshop1.txt, CLUSTER: Mobile Common Places (effect), [Idea])
  - AVs as connective infrastructure linking farmers, food banks, pantries, and
    families. "Become 100% effective by having access to centralized information and connecting suppliers (farmers/food banks) with the users (food pantries/families)" (transcript_workshop1.txt, CLUSTER: Communication (features), [Idea])
  - AVs for people, not just food: rides to medical appointments, bringing
    homebound neighbors and aging volunteers to the pantry. "How might AV help home bound neighbors come to the pantry" (transcript_workshop1.txt, CLUSTER: Home Bound Neighbors, [HMW])
  - AVs to extend refrigeration and storage for pantries that lack space.
    "Refrigerated AV unit for pantries who cannot store for large quantities. Meat + Produce" (transcript_workshop1.txt, CLUSTER: Food Logistics (touch point), [Idea])
  - Modular AVs plus drones for last-mile and rural/infrastructure-poor areas.
    "How might drones/flight AVs to address last mile" (transcript_workshop1.txt, CLUSTER: Modular AV (features), [HMW])
- Conditions or concerns attached: privacy and data protection for pantry
  clients ("How might AV ensure data and user privacy of pantry clients",
  CLUSTER: Privacy, [HMW]); keeping a human element in the delivery; not losing
  the pantry as a social hub.
- Who the team thought it would help or exclude: named beneficiaries are
  seniors, homebound neighbors, disabled people, aging volunteers, rural
  residents, and time-poor working neighbors. No sticky explicitly names who
  would be excluded, which is itself a gap.

## Cross-bucket notes

- The clusters split cleanly into two families: operations and logistics
  (Workforce Optimization, Waste Reduction, Integrated Logistics, Food Supply
  Demand, Physical Labor, Expanding operational hours) which is the large
  majority, and people and place (Mobile Common Places, Home Bound Neighbors,
  Accessibility, Neighbors/Friends, food pantry as social hub) which is the
  minority. The synthesis can use this ratio as evidence of where the team's
  attention defaults.
- "How might we envision food pantry as a social hub/service" appears more than
  once, which suggests at least one team member kept reintroducing it against
  the logistics pull. (transcript_workshop1.txt, CLUSTER: Food Logistics (touch point), [HMW])
- "AV can help me be more productive" is a first-person sticky that reads as a
  facilitator or team member speaking, not a neighbor. (transcript_workshop1.txt, CLUSTER: Neighbors with time constrain challenges, [Idea])

## Coder uncertainty

- Several entries are marked "(?)" or "covered up" in the source, meaning the
  FigJam screenshot was partly illegible. Those are not quotable.
- Attribution: the file says [Idea] boxes are "direct, unattributed participant
  statements" but also that everything is filtered through one notetaker
  compiling screenshots. Treat [Idea] quotes as workshop content, not as a
  verified single speaker.
- "913" is an organization reference left unexplained in the transcript. Do not
  guess what it is in the synthesis.
- Because no community members were present, nothing here should be coded as a
  community value or a community capability. It is all team framing.
