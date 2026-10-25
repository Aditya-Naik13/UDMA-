import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const inputPath = "/Users/adityanaik/Documents/Work/UDMA-/Codebook/MaSS_Codebook xlsx.xlsx";
const tempPath = "/private/tmp/MaSS_Codebook_completed.xlsx";
const previewDir = "/private/tmp/mass_codebook_previews_after";

const rows = [
  ["Key Concept (Abstract)", "Code Name", "Definition & Inclusion", "Exclusion Criteria", "Example / Coding Exemplar", "Source / Locator"],
  [
    "AVs are not simply transportation vehicles but infrastructure",
    "INFRA_FRAME",
    "Treats the AV as infrastructure-scale: reshaping daily life, service relationships, and dependency over time rather than functioning as a one-off consumer product.",
    "Treats an AV as a single ride or trip with no systemic framing.",
    "[Analytic exemplar] AV deployment is discussed as reorganizing long-term service relationships or neighborhood dependencies beyond a single trip.",
    "Paper argument / abstract. No direct transcript exemplar identified in Codebook_final.xlsx.",
  ],
  [
    "arrive without communities' input",
    "INPUT_PART_ABSENT",
    "Reflects that the speaker or community currently has no say in how mobility technology or services are designed and decided.",
    "Lacking a ride rather than lacking a say; code the former as CONSTRAINTS.",
    '"Neighbor have ideas imposed on them. Their needs are not accommodated"',
    "workshop-3-codesign, cluster: People centered, Input/decision making",
  ],
  [
    "arrive without communities' input",
    "CONSULT_NO_POWER",
    "Subcode of INPUT_PART_ABSENT. Formal involvement solicits input but leaves final authority unchanged; includes performative equity practices that do not redistribute decision-making power.",
    "No community input at all belongs to INPUT_PART_ABSENT alone. Binding community authority belongs to COGOVERN.",
    "[Literature-derived] No transcript exemplar identified; apply only when consultation is documented but influence remains non-binding.",
    "Pinski et al. 2024, https://doi.org/10.1016/j.trip.2024.101114; McCullough et al. 2024, https://doi.org/10.1177/03611981231193409",
  ],
  [
    "arrive without communities' input",
    "NEGATIVE_SELFEFF",
    "Subcode of INPUT_PART_ABSENT. Prior experiences of being ignored or humiliated teach people that participating will not matter, leading them to withdraw.",
    "General service distrust without a participation referent.",
    '"I don\'t know if somebody\'s going to actually listen or whatever"',
    "sec-participant-01, turn 21, Interviewee; Klaever et al. 2025, https://doi.org/10.1080/17450101.2024.2426554",
  ],
  [
    "arrive without communities' input",
    "EXPERTS_CENTERED",
    "Subcode of INPUT_PART_ABSENT. Credentialed professionals, officials, or researchers are centered as decision-makers instead of residents whose mobility the system shapes.",
    "Studies or processes in which residents hold meaningful decision authority.",
    "[Literature-derived] No transcript exemplar identified; use when the evidence specifies who is authorized to define the problem or solution.",
    "Hicks, Kingsley, and Isett 2025, https://doi.org/10.1093/polsoc/puae041",
  ],
  [
    "arrive without communities' input",
    "INPUT_PART_PRESENT",
    "A moment where participation shaped a decision, including a co-design workshop being documented as a rare instance.",
    'Hypothetical statements such as "it would be nice if we were asked" belong to INPUT_PART_ABSENT.',
    "[Process exemplar] The co-design session itself is the documented instance; no verbatim quote was recorded.",
    "Co-design workshop sessions and Capstone ideation. Log workshop ID and speaker role.",
  ],
  [
    "arrive without communities' input",
    "COGOVERN",
    "Subcode of INPUT_PART_PRESENT. Residents or community organizations act as co-governors or authors of the service, with resources and binding influence over design decisions. This includes the former COMMUNITY_BUILT concept.",
    "Consultation that gathers views without transferring authority.",
    '[Process exemplar] Design principle 11: "Build it with the community." No verbatim transcript quote was recorded.',
    "Karner et al. 2020, https://doi.org/10.1177/0885412220927691; Severs et al. 2022, https://doi.org/10.1145/3544999.3554787; Tan et al. 2025, https://doi.org/10.1145/3706599.3719736",
  ],
  [
    "efficiency-driven values inherited from transportation engineering",
    "EFF_VALUE",
    "Invokes efficiency or technical-performance logic: speed, optimized routing, throughput, scheduling precision, measurable system performance, or automation-as-improvement.",
    "Vehicle or technology mentions with no efficiency or technical-performance framing.",
    '"How might we use AVs to reduce logistic company cost (labor, time, asset) to improve the distribution efficiency and have workforce capacity to fulfill other social services needs"',
    "workshop-1-codesign, CLUSTER: Workforce Optimization (effect), HMW",
  ],
  [
    "efficiency-driven values inherited from transportation engineering",
    "THROUGHPUT",
    "Subcode of EFF_VALUE. Evaluation is organized around network throughput, capacity, automation share, penetration rate, or level of service, with people represented primarily as trips or counts.",
    "Trade-offs described through riders' lived experience rather than system capacity.",
    "[Literature-derived] No transcript exemplar; apply to model-level claims about capacity, penetration rate, or level of service.",
    "Lu et al. 2020, https://doi.org/10.1080/19427867.2019.1662561; Park et al. 2024, https://doi.org/10.3390/su16010026; Pimenta et al. 2023, https://doi.org/10.1080/01441647.2023.2189325",
  ],
  [
    "efficiency-driven values inherited from transportation engineering",
    "SAFETY_ENG",
    "Subcode of EFF_VALUE. Safety or acceptance is operationalized as a measurable, tunable system property, such as take-over time, perceived safety, or acceptance scores.",
    "Relational trust, lived access concerns, or an unmeasured account of feeling safe.",
    "[Literature-derived] No transcript exemplar; use only when safety or acceptance is explicitly converted into a system measure or optimization target.",
    "Zhang et al. 2019, https://doi.org/10.1016/j.trf.2019.04.020; Nordhoff et al. 2020, https://doi.org/10.1016/j.tra.2020.05.009; Zoellick et al. 2019, https://doi.org/10.1371/journal.pone.0215969",
  ],
  [
    "efficiency-driven values inherited from transportation engineering",
    "TRUST_METRIC",
    "Subcode of EFF_VALUE and contrast to JUST_TRUST. Trust is modeled, scored, or calibrated as an individual attitude toward automation rather than sustained through a relationship.",
    "Being known, listened to, or trusted by a person belongs to JUST_TRUST.",
    "[Literature-derived] No transcript exemplar; apply to studies that measure or calibrate trust in automation.",
    "Kraus et al. 2020, https://doi.org/10.1177/0018720819853686; Lee and Kolodge 2020, https://doi.org/10.1177/0018720819872672; Alkurdi and Alsaid 2025, https://doi.org/10.1177/10711813251369499",
  ],
  [
    "community concerns — equitable access",
    "JUST_ACCESS",
    "Frames equitable access: being able to reach services when needed despite rigid slots, geography, documentation, language, or cost.",
    'Generic statements such as "everyone should have a ride" with no access barrier specified.',
    '"Homebound people miss out on transportation ideations."',
    "workshop-3-codesign, cluster: Home Bound",
  ],
  [
    "community concerns — relational trust",
    "JUST_TRUST",
    "Frames relational trust toward a known person who recognizes and listens, rather than trust in a system or vehicle.",
    "Trust framed as technology reliability or a measured automation attitude belongs to EFF_VALUE or TRUST_METRIC.",
    '"here with them, they give you confidence, they listen to you... anything, they let me know through a message or text message or WhatsApp message."',
    "sec-participant-15-sp, 15:27:26; translated",
  ],
  [
    "community concerns — flexibility for variable need",
    "JUST_FLEXIBILITY",
    "Frames adaptability to variable or unpredictable need, including household size, timing, and one-time versus recurring need.",
    "Fixed scheduling described neutrally with no flexibility concern.",
    '"Whenever I have the opportunity, whenever I have the opportunity, chances to go."',
    "sec-participant-13-sp, 15:14:56; translated",
  ],
  [
    "efficiency-driven values are distant from community concerns",
    "MISALIGNMENT",
    "A named or implied value-level gap between efficiency-driven logic and community-grounded values; the statement may be calm or reflective.",
    "A live moment of confusion or pushback with no value gap articulated belongs to BREAKDOWN only.",
    '"not everybody has the phone."',
    "focus-group-ministries-of-love, 00:45:16, Speaker 3",
  ],
  [
    "misalignment reflects a broader pattern... without participation in shaping what the technology is for",
    "PURPOSE_EXCLUSION",
    "Questions or challenges not just how an AV is designed but why it exists, what success means, and who selected that goal.",
    "Questions about design details only, such as routing or hours.",
    '"Biggest ROI of AV as a social service is the adoption rate of AV"',
    "workshop-3-codesign, SECTION: How would AV works in terms of service?, cluster: Current Infrastructure",
  ],
  [
    "speculative AV provocation surfaced how participants reasoned about mobility",
    "PROVOCATION",
    "Any participant response—reasoning, imagining, questioning, or proposing conditions—directly triggered by the speculative AV concept.",
    "General mobility discussion not tied to the AV prompt.",
    '"I would take a car. You know why?... I don\'t know how to drive. I\'ve never had a license. If a car could drive me..."',
    "focus-group-hope, 00:47:10, Speaker 7",
  ],
  [
    "speculative AV provocation surfaced how participants reasoned about mobility",
    "BREAKDOWN",
    "A specific live moment of resistance, confusion, redirection, or reframing in response to the AV concept; code the content of the pushback.",
    "Calm or neutral clarifying questions with no resistance or reframing.",
    '"AV cannot be designed for everyone. It\'s not the next big solution."',
    "workshop-3-codesign, cluster: People centered, Personalized services",
  ],
  [
    "speculative AV provocation surfaced how participants reasoned about mobility",
    "FRICTION_MANAGED",
    "Subcode of BREAKDOWN. Institutions or AV researchers interpret resistance, testing, or noncompliance as distrust or a problem to manage rather than as evidence about the design.",
    "Friction treated as a meaningful signal that redirects design.",
    "[Literature-derived] No transcript exemplar; apply only when the institutional response to resistance is being analyzed.",
    "Nordhoff et al. 2020, https://doi.org/10.1016/j.tra.2020.05.009; Forlano and Mathew 2014, Journal of Urban Technology 21(4), 7–24",
  ],
  [
    "Mobility as Social Service — ongoing, relational practice of equitable provisioning",
    "VALUES",
    "Statements naming what should matter in mobility or aid: trust, dignity, mutual care, flexibility, fairness, and maintained human connection.",
    "Purely factual or logistical statements with no evaluative content.",
    '"Maintaining the human relation"',
    "workshop-3-codesign, cluster: Social service meaning relational engagement not transactional",
  ],
  [
    "Mobility as Social Service — ongoing, relational practice of equitable provisioning",
    "DIGNITY_STRUCT",
    "Subcode of VALUES. Dignity is treated as a concrete design property: minimizing burden, respecting autonomy, and avoiding stigma or discrimination.",
    "Dignity named only as a general value without a design or service condition.",
    '"they do not discriminate against you, they see you as another family united with the community."',
    "sec-participant-11-sp, 15:13:44; translated",
  ],
  [
    "Mobility as Social Service — ongoing, relational practice of equitable provisioning",
    "MEANINGS",
    "Statements about what mobility represents: independence, being seen, belonging, burden, care, progress, or human contact.",
    "Purely functional trip descriptions belong to PRACTICES.",
    '"striving to be someone better in life."',
    "sec-participant-15-sp, 15:30:03; translated",
  ],
  [
    "Mobility as Social Service — ongoing, relational practice of equitable provisioning",
    "PRACTICES",
    "Concrete descriptions of how people, goods, information, or care move: who drives, what is carried, and how routes and times are decided.",
    "Hypothetical or wished-for practices. Recurring unpaid redistribution systems may also receive INFORMAL_CARE_INFRASTRUCTURE.",
    '"I go, pick up my children from school, and at the same time, I pick up my food."',
    "sec-participant-11-sp, 15:13:20; translated",
  ],
  ["Additional top-level codes and their subcodes", null, null, null, null, null],
  [
    "Existing community infrastructure not named directly in the abstract",
    "INFORMAL_CARE_INFRASTRUCTURE",
    "An existing, unpaid, informal person, route, or network that repeatedly moves food, goods, care, or information for others and functions as real mobility or distribution infrastructure.",
    "A wished-for network; a one-off errand; an isolated skill or resource; or a mobility description with no redistribution to others.",
    '"That\'s why I\'m able to pick up stuff for other people who can\'t come, who don\'t have cars."',
    "focus-group-hope, 00:42:51, Speaker 8",
  ],
  [
    "Additional code from the original anchor-question list",
    "CONSTRAINTS",
    "Named systemic, infrastructural, or resource limits shaping mobility, including funding, geography, carrying burden, scheduling rigidity, staffing, or eligibility rules.",
    "General complaints with no identifiable structural cause.",
    '"the most challenging part is going back because I have the bags."',
    "ministries-of-love-interview-walker, 01:46, Speaker 2",
  ],
  [
    "Additional code from the original anchor-question list",
    "CONDITIONALITY",
    "Subcode of CONSTRAINTS. Access to help depends on demonstrating eligibility or deservingness, accepting monitoring, or performing gratitude.",
    "A neutral identification rule with no barrier or deservingness logic; use the broader CONSTRAINTS code if the mechanism is unspecified.",
    "[Literature-derived] No transcript exemplar identified; use only when deservingness or conditional access is explicit.",
    "Cresswell Riol and Connelly 2025, https://doi.org/10.1111/gec3.70054",
  ],
];

const notes = [
  "Codebook Notes — AV / Food Pantry Co-Design Workshops",
  "",
  "ORDER: The Codebook sheet follows the paper argument in Column A and expands each abstract concept",
  "into its parent code and any retained subcodes. Codes remain non-mutually-exclusive.",
  "",
  "VISUAL STRUCTURE:",
  "Gray = framing or additional-code blocks. Yellow = Mobility as Social Service synthesis block.",
  "Pale blue = a retained concept nested as a subcode of the parent code immediately above it.",
  "",
  "INFORMAL_CARE_INFRASTRUCTURE replaces the former CAPABILITIES code.",
  "Use it only for an existing, recurring unpaid route or network that serves others.",
  "An isolated skill, personal persistence, or a one-off favor is not sufficient.",
  "Apply PRACTICES as a second code when the passage also describes the concrete route or activity.",
  "",
  "A single excerpt can carry MULTIPLE codes from this list; the codes are not mutually exclusive.",
  "",
  "MISALIGNMENT vs. BREAKDOWN:",
  "MISALIGNMENT = a value-level gap is named or implied and may be calm or reflective.",
  "BREAKDOWN = an in-the-moment reaction such as confusion, pushback, or redirection.",
  "The same excerpt can carry both.",
  "",
  "JUST_ACCESS / JUST_TRUST / JUST_FLEXIBILITY are sub-codes of the broader justice-value moment.",
  "Apply as many as fit; do not force a single choice.",
  "",
  "PARTICIPATION HIERARCHY:",
  "CONSULT_NO_POWER includes the former PERF_VS_AUTH distinction when inclusion is claimed without power transfer.",
  "NEGATIVE_SELFEFF captures withdrawal after exclusion; EXPERTS_CENTERED captures who holds authority.",
  "COGOVERN includes the former COMMUNITY_BUILT concept when community authorship has binding influence.",
  "",
  "ENGINEERING VALUE HIERARCHY:",
  "THROUGHPUT, SAFETY_ENG, and TRUST_METRIC are subcodes of EFF_VALUE, not standalone top-level codes.",
  "SAFETY_ENG is literature-derived and should be used only for measurable or tunable safety/acceptance framing.",
  "TRUST_METRIC contrasts with relational trust in JUST_TRUST.",
  "",
  "CROSS-CODING RULES FOR MERGED CONCEPTS:",
  "ACCESS_AS_EFF = EFF_VALUE + JUST_ACCESS; add MISALIGNMENT when the value gap is explicit.",
  "EFFICIENCY_SURPLUS = INFRA_FRAME + EFF_VALUE + MISALIGNMENT.",
  "FRICTION_MANAGED remains a BREAKDOWN subcode; CONDITIONALITY remains a CONSTRAINTS subcode.",
  "",
  "EVIDENCE RULES:",
  "Column E contains either a verbatim excerpt, a process exemplar, or a clearly labeled analytic exemplar.",
  "Literature-only codes are explicitly labeled and cite sources in Column F; they are not transcript findings.",
  "Where no direct exemplar exists, the gap is stated rather than filled with an invented quote.",
  "Always log workshop or interview ID and speaker role with each coded excerpt.",
  "",
  "DROPPED AFTER ABSTRACT-FIT REVIEW:",
  "SURVEILLANCE, CHARITY_REFRAIM, and APARTHEID_GEO are not included as codes because they are peripheral",
  "to the stated paper argument. Relevant literature may still be used as background context.",
  "",
  "STATUS: Working codebook completed with examples, locators, literature sources, and hierarchy.",
  "The codebook still requires an inter-coder pilot before final use.",
];

const input = await FileBlob.load(inputPath);
const workbook = await SpreadsheetFile.importXlsx(input);
const sheet = workbook.worksheets.getItem("Codebook");
const notesSheet = workbook.worksheets.getItem("Notes for Coders");

for (const ref of ["A16:F16", "A25:F25"]) {
  try {
    sheet.unmergeCells(ref);
  } catch {
    // The range is not merged in this version of the workbook.
  }
}

sheet.getRange("A1:F80").clear({ applyTo: "all" });
sheet.getRange(`A1:F${rows.length}`).values = rows;
sheet.mergeCells("A25:F25");

const body = sheet.getRange(`A1:F${rows.length}`);
body.format = {
  fill: "#FFFFFF",
  font: { name: "Arial", size: 10, color: "#000000" },
  wrapText: true,
  verticalAlignment: "top",
  horizontalAlignment: "left",
  borders: { preset: "all", style: "thin", color: "#BFBFBF" },
};

sheet.getRange("A1:F1").format = {
  fill: "#1F4E78",
  font: { name: "Arial", size: 11, bold: true, color: "#FFFFFF" },
  wrapText: true,
  verticalAlignment: "center",
  horizontalAlignment: "center",
  borders: { preset: "all", style: "thin", color: "#BFBFBF" },
};

sheet.getRange("A2:F2").format.fill = "#E2E2E2";
sheet.getRange("A21:F24").format.fill = "#FFF2CC";
sheet.getRange("A25:F25").format = {
  fill: "#BFBFBF",
  font: { name: "Arial", size: 10, bold: true, italic: true, color: "#000000" },
  wrapText: true,
  verticalAlignment: "center",
  horizontalAlignment: "left",
  borders: { preset: "all", style: "thin", color: "#BFBFBF" },
};
sheet.getRange("A26:F27").format.fill = "#F2F2F2";

const subcodeRows = [4, 5, 6, 8, 10, 11, 12, 20, 22, 28];
for (const row of subcodeRows) {
  sheet.getRange(`A${row}:F${row}`).format.fill = "#DDEBF7";
  sheet.getRange(`B${row}`).format.font = { name: "Arial", size: 10, bold: true, color: "#1F4E78" };
}

sheet.getRange(`A2:A${rows.length}`).format.font = { name: "Arial", size: 10, italic: true, color: "#000000" };
sheet.getRange(`B2:B${rows.length}`).format.font = { name: "Arial", size: 10, bold: true, color: "#000000" };
for (const row of subcodeRows) {
  sheet.getRange(`B${row}`).format.font = { name: "Arial", size: 10, bold: true, color: "#1F4E78" };
}

sheet.getRange("A1:A28").format.columnWidth = 38;
sheet.getRange("B1:B28").format.columnWidth = 27;
sheet.getRange("C1:C28").format.columnWidth = 52;
sheet.getRange("D1:D28").format.columnWidth = 40;
sheet.getRange("E1:E28").format.columnWidth = 48;
sheet.getRange("F1:F28").format.columnWidth = 46;
body.format.autofitRows();
sheet.getRange("1:1").format.rowHeight = 28;
sheet.getRange("25:25").format.rowHeight = 24;

notesSheet.getRange("A1:A90").clear({ applyTo: "contents" });
notesSheet.getRange(`A1:A${notes.length}`).values = notes.map((value) => [value]);
const notesRange = notesSheet.getRange(`A1:A${notes.length}`);
notesRange.format = {
  font: { name: "Arial", size: 11, color: "#000000" },
  wrapText: true,
  verticalAlignment: "top",
  horizontalAlignment: "left",
};
notesSheet.getRange("A1").format.font = { name: "Arial", size: 11, bold: true, color: "#000000" };
for (const row of [6, 17, 25, 30, 35, 40, 46, 51]) {
  notesSheet.getRange(`A${row}`).format.font = { name: "Arial", size: 11, bold: true, color: "#000000" };
}
notesSheet.getRange(`A1:A${notes.length}`).format.columnWidth = 100;
notesRange.format.autofitRows();

const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(tempPath);
await fs.rename(tempPath, inputPath);

const verifyInput = await FileBlob.load(inputPath);
const verifyWorkbook = await SpreadsheetFile.importXlsx(verifyInput);
const structureCheck = await verifyWorkbook.inspect({
  kind: "sheet,region",
  sheetId: "Codebook",
  range: "A1:F28",
  maxChars: 18000,
  tableMaxRows: 35,
  tableMaxCols: 6,
  tableMaxCellChars: 260,
});
console.log("STRUCTURE CHECK");
console.log(structureCheck.ndjson);

const errorCheck = await verifyWorkbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});
console.log("ERROR CHECK");
console.log(errorCheck.ndjson);

await fs.mkdir(previewDir, { recursive: true });
for (const sheetName of ["Codebook", "Notes for Coders"]) {
  const preview = await verifyWorkbook.render({
    sheetName,
    autoCrop: "all",
    scale: 1.5,
    format: "png",
  });
  const safeName = sheetName.replaceAll(" ", "_");
  await fs.writeFile(`${previewDir}/${safeName}.png`, new Uint8Array(await preview.arrayBuffer()));
}
