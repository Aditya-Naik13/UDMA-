#!/usr/bin/env python3
"""Step 3: thesis-clause support matrix. Every row was tagged by reading its
Central claim and Relevance to argument (already read in full for all 67
rows in Step 2). Values: direct / partial / none, each with a one-line
reason grounded in the paper's actual content."""
import pandas as pd
import json

CLAUSES = {
    "C1_AVs_are_infrastructure": "AVs are infrastructure, not simply transportation vehicles",
    "C2_arrives_without_input": "Infrastructure-scale technology typically arrives in communities without their input",
    "C3_efficiency_values": "AVs carry efficiency-driven values inherited from transportation engineering",
    "C4_community_concerns_govern": "Community concerns (equitable access, relational trust, flexibility for variable need) actually govern mobility in this context",
    "C5_misalignment": "Efficiency-driven values are misaligned with those community concerns",
    "C6_broader_pattern": "This misalignment reflects a broader pattern, not a one-off AV problem",
    "C7_mobility_as_social_service": "Mobility as Social Service: mobility as an ongoing, relational practice of equitable provisioning",
}

# key = (Thread, Author(s), Year) exactly matching unified_lit_review.csv rows
# value = dict of clause_code -> (tag, reason)
d = "direct"; p = "partial"; n = "none"
TAGS = {}

def t(thread, author, year, **kw):
    TAGS[(thread, author, year)] = kw

ENG = "Engineering/Safety"
EQ = "Equity"
PM = "Participatory Method"

# ---------------- Engineering/Safety ----------------
t(ENG, "Hicks, D., Kingsley, G., & Isett, K.R.", 2025,
  C1=(d, "About AV policy reports and advisory infrastructure directly"),
  C2=(d, "Convening mode shows legitimacy-seeking AV policy still routes through officials, not communities"),
  C3=(p, "Expert mode privileges technical credibility, adjacent to efficiency logic"),
  C4=(n, "Does not document community concerns shaping outcomes"),
  C5=(p, "Implies misalignment via omission of community consultation"),
  C6=(p, "Evidence within the AV domain only; no explicit broader claim"),
  C7=(n, "No relational/provisioning framing"))
t(ENG, "London, A.J. & Danks, D.", 2018,
  C1=(d, "Proposes infrastructure-scale regulatory regime for AV deployment"),
  C2=(p, "Never discusses who decides an AV should be deployed in a community"),
  C3=(d, "Entirely an engineering-certification safety framing"),
  C4=(n, "No community concerns discussed"),
  C5=(p, "Drug-approval analogy ignores non-consenting neighbors, an implied misalignment"),
  C6=(n, "AV-specific proposal, no generalization claim"),
  C7=(n, "No relational framing"))
t(ENG, "Robles, P. & Mallinson, D.J.", 2024,
  C1=(d, "AV policy diffusion across state regulatory infrastructure"),
  C2=(p, "Regulation shown as insider conversation among governments and industry"),
  C3=(p, "Diffusion driven by interstate learning and industry consultation, efficiency-adjacent"),
  C4=(n, "No community concerns examined"),
  C5=(n, "Does not compare against community concerns"),
  C6=(n, "AV-specific"),
  C7=(n, "No relational framing"))
t(ENG, "Alkurdi, D. & Alsaid, A.", 2025,
  C1=(p, "AV-specific but vehicle-level, not infrastructure framing"),
  C2=(n, "Not about community input"),
  C3=(d, "Trust treated as individually measured psychological variable"),
  C4=(n, "No community concerns"), C5=(n, "N/A"), C6=(n, "AV-specific"), C7=(n, "No relational framing"))
t(ENG, "Lee, J.D. & Kolodge, K.", 2020,
  C1=(n, "Consumer-level trust study, no infrastructure framing"),
  C2=(n, "Not about community input"),
  C3=(d, "Field measures trust as an individual attitude to be managed for brand acceptance"),
  C4=(p, "Surfaces relational/societal trust bases, but routes them to manufacturer strategy"),
  C5=(p, "Demonstrates relational trust being redirected away from community authority"),
  C6=(n, "AV-specific"), C7=(n, "No relational framing"))
t(ENG, "Kraus, J., Scholz, D., Stiegemeier, D., & Baumann, M.", 2020,
  C1=(n, "Simulator study of individual driver trust"), C2=(n, "N/A"),
  C3=(d, "Trust operationalized as a repeatedly measured scalar, an engineering control variable"),
  C4=(n, "N/A"), C5=(n, "N/A"), C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Zhang, B., de Winter, J., Varotto, S., Happee, R., & Martens, M.", 2019,
  C1=(p, "AV handover behavior, vehicle-level not infrastructure"), C2=(n, "N/A"),
  C3=(d, "Field vocabulary built entirely around efficiency and safety-margin optimization"),
  C4=(n, "N/A"), C5=(n, "N/A"), C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Peng, Q., Wu, Y., Qie, N., & Iwaki, S.", 2022,
  C1=(n, "Cognitive testing study, no infrastructure framing"), C2=(n, "N/A"),
  C3=(d, "Frames older adults through an engineering-safety lens rather than service or relational one"),
  C4=(p, "Older adults appear only as a population to be screened, not as agents shaping design"),
  C5=(p, "Illustrates the safety-metric framing eclipsing a service framing for an underserved group"),
  C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Pedroff, J.", 2025,
  C1=(p, "Street-crossing signaling touches shared road space"), C2=(n, "N/A"),
  C3=(d, "Framed as a communication-design problem, not community access or consent"),
  C4=(n, "N/A"), C5=(p, "Implied by explicit contrast with access/consent framing"), C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Lee, M.B., Lee, C.T., Abas, M.A., & Chong, W.W.F.", 2025,
  C1=(p, "Field-wide bibliometric view of AV-pedestrian safety research"), C2=(n, "N/A"),
  C3=(d, "Dominated by engineering and statistical approaches; policy named as underdeveloped"),
  C4=(n, "N/A"), C5=(n, "N/A"),
  C6=(p, "Field-wide pattern, though only within the AV research domain"), C7=(n, "N/A"))
t(ENG, "Kooijman, L., Happee, R., & de Winter, J.C.F.", 2019,
  C1=(p, "Crossing behavior study touches street space design"), C2=(n, "N/A"),
  C3=(d, "Pedestrian encounter framed as signal-legibility optimization, closing with surveillance framing"),
  C4=(n, "N/A"), C5=(p, "Explicit contrast with who has standing to shape the street"), C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Pimenta, A.R., Kamruzzaman, M., & Currie, G.", 2023,
  C1=(d, "Literally about AVs reshaping the built environment"),
  C2=(d, "Review shows built environment framed as engineered and forecast from above, never community-shaped"),
  C3=(p, "Ownership-model framing (SAV/PAV) is market-driven rather than explicitly efficiency-labeled"),
  C4=(n, "Communities appear only as aggregate statistics"),
  C5=(p, "No reviewed study considered redirecting freed parking to community-defined uses"),
  C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Park, J., Jang, S., & Ko, J.", 2024,
  C1=(d, "Exclusive AV lanes on urban expressways, road infrastructure"),
  C2=(n, "No community input discussed"),
  C3=(d, "Entire study organized around network efficiency at a given AV market share"),
  C4=(n, "N/A"), C5=(n, "N/A"), C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Lu, Q., Tettamanti, T., Hörcher, D., & Varga, I.", 2020,
  C1=(d, "Urban traffic network capacity is core infrastructure question"),
  C2=(n, "No community input discussed"),
  C3=(d, "Explicitly prizes recovered road capacity without asking whom it serves"),
  C4=(n, "N/A"), C5=(n, "N/A"), C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Palatinus, Z., Volosin, M., Csabi, E., Hallgato, E., Hajnal, E., Lukovics, M., Pronay, S., Ujhazi, T., Osztobanyi, L., Szabo, B., Kralik, T., & Majo-Petri, Z.", 2022,
  C1=(p, "Real vehicle ride, service-level not infrastructure-level"), C2=(n, "N/A"),
  C3=(p, "Frames acceptance as an individual measurable affective/physiological state"),
  C4=(n, "N/A"), C5=(n, "N/A"), C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Zoellick, J.C., Kuhlmey, A., Schenk, L., Schindel, D., & Bluher, S.", 2019,
  C1=(p, "Real shuttle service, not framed as infrastructure"), C2=(n, "N/A"),
  C3=(p, "Refines standard technology-acceptance measurement instruments"),
  C4=(p, "Human safety operator's talkativeness shaped riders' perceptions, a rare relational finding"),
  C5=(p, "That relational finding is treated as a confound to control for, not to design around"),
  C6=(n, "AV-specific"), C7=(n, "N/A"))
t(ENG, "Nordhoff, S., Stapel, J., van Arem, B., & Happee, R.", 2020,
  C1=(p, "Real shuttle service, not explicitly infrastructure-framed"), C2=(n, "N/A"),
  C3=(d, "Whole encounter framed as perceived safety to optimize; non-compliant road users flagged to police"),
  C4=(p, "Relational cues, sharing the ride, trusting the operator, briefly surface"),
  C5=(d, "Explicitly shows the field approaching a relational framing, then turning back to safety/efficiency"),
  C6=(n, "AV-specific"), C7=(n, "N/A"))

# ---------------- Equity ----------------
t(EQ, "Levine", 2024,
  C1=(n,"Not about AVs"), C2=(d,"ADA-compliant infrastructure built without disabled riders' participation reproduces exclusion"),
  C3=(p,"ADA compliance metrics are technical/compliance-driven"), C4=(d,"Own text: supports both halves; access unevenly distributed by disability, gender, race"),
  C5=(d,"Compliance metrics ignore first/last-mile and diverse disability needs"), C6=(d,"Direct non-AV evidence of the broader pattern"),
  C7=(p,"Participants excluded from decisions; touches relational trust but not full provisioning framing"))
t(EQ, "Zhang et al.", 2024,
  C1=(n,"Not about AVs"), C2=(p,"Own text: thinner fit, does not address community participation"),
  C3=(d,"Top down, metric driven inclusion framework"), C4=(d,"Supports unevenly distributed half directly"),
  C5=(d,"Metric-driven framework vs elderly travelers' own participation in defining inclusion"), C6=(d,"Non-AV evidence across three decades of research"),
  C7=(n,"Framework is accessibility/cost metric based, not relational provisioning"))
t(EQ, "Pinski et al.", 2024,
  C1=(n,"Not about AVs"), C2=(d,"Community needs assessments reproduce representation gaps"),
  C3=(p,"Formal participatory processes still fail, a process critique more than efficiency-values one"),
  C4=(d,"Documents disadvantaged and hard-to-reach populations' access needs"),
  C5=(d,"Funded inclusive processes still fail to serve those needs"), C6=(d,"Traces pattern back to 1950s-60s highway displacement"),
  C7=(p,"Tokenism critique touches ongoing relational engagement"))
t(EQ, "Agrawaal et al.", 2024,
  C1=(n,"Not about AVs"), C2=(d,"Own text: directly supports reproduces exclusion half"),
  C3=(p,"Jargon-heavy technical planning tools are technocratic/efficiency-adjacent"),
  C4=(d,"Planners' focus on traffic counts over lived experience shows what should govern instead"),
  C5=(d,"Jargon tools and traffic-count focus vs lived experience"), C6=(d,"Kinetic elite/mobility poor divide is a historical, broader pattern"),
  C7=(p,"Path dependence framing is systemic but not fully relational-provisioning"))
t(EQ, "Gomes et al.", 2026,
  C1=(n,"Not about AVs"), C2=(d,"Own text: directly supports reproduces exclusion half"),
  C3=(p,"Top-down fixed templates critiqued vs co-created ones"),
  C4=(d,"Citizen-defined priorities (transit reliability, safe pedestrian access) govern the outcome"),
  C5=(d,"Fixed templates missed what residents needed, resolved via co-creation"), C6=(d,"15-Minute City/TOD/MaaS as broader non-AV paradigms"),
  C7=(d,"Co-creation across institutional, technical, citizen actors is close to ongoing relational provisioning"))
t(EQ, "Bailey et al.", 2010,
  C1=(n,"Not about AVs"), C2=(d,"Arnstein Gap is a persistent, structural shortfall"),
  C3=(p,"Geovisual decision support tools are procedural/technical, not explicitly efficiency-labeled"),
  C4=(d,"Cultural values elicited via SPI are meant to govern outcomes"), C5=(d,"Professional conceit vs the public's own reported experience"),
  C6=(d,"Framed as structural to U.S. transportation planning generally"), C7=(n,"Procedural justice framing, not explicitly ongoing relational provisioning"))
t(EQ, "Soliz et al.", 2026,
  C1=(n,"Not about AVs"), C2=(d,"Planning built without disabled people's input structurally forecloses access"),
  C3=(p,"Official policy definitions are rigid categorical/bureaucratic logic"), C4=(d,"Disabled people's leadership should center infrastructure design"),
  C5=(d,"Formal definitions exclude actual mobility practices"), C6=(d,"Disability justice as a broader, non-AV framework"),
  C7=(p,"Crip time reframing is a relational, flexible-provisioning concept"))
t(EQ, "McCullough et al.", 2024,
  C1=(n,"Not about AVs"), C2=(d,"Own text: supports both halves"), C3=(p,"Performative work is surface-level process without power redistribution"),
  C4=(d,"Documents power/voice unevenly distributed among professionals of color"), C5=(d,"Performative vs authentic equity is an explicit misalignment concept"),
  C6=(d,"Applies across the transportation field broadly, non-AV"), C7=(d,"Authentic equity as sustained relational redistribution of power closely matches Mobility as Social Service"))
t(EQ, "Chen et al.", 2025,
  C1=(n,"Not about AVs"), C2=(p,"Own text: thinner fit, authors flag need for community engagement"), C3=(d,"Quantitative, top-down allocation formula"),
  C4=(d,"Supports unevenly distributed half directly"), C5=(d,"Own text: model lacks community engagement to capture residents' actual perspectives"),
  C6=(d,"Non-AV evidence across 394 municipalities and a decade"), C7=(n,"No relational framing"))
t(EQ, "Golub et al.", 2013,
  C1=(n,"Not about AVs"), C2=(d,"Own text: directly supports both halves"), C3=(p,"Facially neutral technical funding formula produces racialized exclusion"),
  C4=(d,"Documents historically uneven mobility access"), C5=(d,"Technical criteria producing racialized exclusion, 'racism without racists'"),
  C6=(d,"Pre-dates AVs entirely; strong historical broader-pattern evidence"), C7=(n,"No relational provisioning framing"))
t(EQ, "McCullogh et al.", 2026,
  C1=(n,"Not about AVs"), C2=(d,"Participation necessary for equitable implementation; groups deterred or excluded"),
  C3=(p,"Frameworks built by default for able-bodied road users"), C4=(d,"Community engagement and partnerships are central facilitators/barriers"),
  C5=(d,"Nominal engagement and marginalized-group exclusion documented"), C6=(d,"Cross-context, non-AV review evidence"), C7=(n,"No relational provisioning framing"))
t(EQ, "Twardzik et al.", 2025,
  C1=(n,"Not about AVs"), C2=(d,"Red Line cancelled without input from Baltimore residents, a concrete example"),
  C3=(p,"'Ideal rider' assumption is a default optimization logic"), C4=(d,"Black and disabled riders' needs should govern, intersectional framework"),
  C5=(d,"Ideal-rider design vs actual riders is an explicit misalignment"), C6=(d,"Traces to slavery, redlining, highway construction, deep historical pattern"),
  C7=(p,"Crip Mobility Justice includes interdependence, a relational concept"))
t(EQ, "Johnson et al.", 2025,
  C1=(n,"Not about AVs"), C2=(p,"Own text: gestures at participation half only in closing recommendation"),
  C3=(d,"Accessibility indices and affordability metrics are the primary tools reviewed"),
  C4=(p,"Own text: a thinner fit than most sources in this section"), C5=(p,"Implied by the review's own framing, not strongly demonstrated"),
  C6=(p,"Broad review, general pattern but described as a thinner fit"), C7=(n,"No relational provisioning framing"))
t(EQ, "Johnson et al.", 2024,
  C1=(n,"Not about AVs"), C2=(n,"Own text: relevance is indirect, not an infrastructure planning process"),
  C3=(n,"Not applicable, recreational social movement study"), C4=(p,"Touches equity/access/inclusion in cycling advocacy indirectly"),
  C5=(n,"Not tested empirically per own text"), C6=(n,"Own text: connection not empirically tested here"), C7=(n,"No relational provisioning framing"))
t(EQ, "Karner et al.", 2017,
  C1=(n,"Not about AVs"), C2=(d,"Own text: directly supports reproduces exclusion half"), C3=(p,"Quantitative equity analyses and distant forecasts critiqued as technical"),
  C4=(d,"Community-led identification of needs is central to the proposed model"), C5=(d,"Standard MPO involvement rarely translates input into funded action"),
  C6=(d,"Civil rights/EJ mandate history, broad non-AV pattern"), C7=(d,"Three-step ongoing model: identify needs, fund, track closely matches relational provisioning"))
t(EQ, "Mottee et al.", 2020,
  C1=(n,"Not about AVs"), C2=(d,"Own text: directly supports, consultation occurring too late in project lifecycle"),
  C3=(d,"'Predict and provide' technical, model-driven planning explicitly critiqued"), C4=(d,"Affected communities' needs should shape assessment early"),
  C5=(d,"Technical planning treats social impacts as secondary"), C6=(d,"Two rail megaprojects, broader non-AV pattern"), C7=(n,"No relational provisioning framing"))
t(EQ, "Klaever et al.", 2025,
  C1=(n,"Not about AVs"), C2=(d,"Own text: directly supports, invited spaces actively discouraged residents"),
  C3=(p,"Official participatory venues framed by planners on their own terms"), C4=(d,"Lived expertise vs technical planning expertise, strong community-concerns framing"),
  C5=(d,"Repeated negative experiences including public humiliation demonstrate misalignment"), C6=(d,"Direct evidence though the authors note limited generalizability"),
  C7=(p,"Transdisciplinary research format better reflecting lived expertise is relational, though not policy provisioning itself"))
t(EQ, "Pineo et al.", 2026,
  C1=(n,"Not about AVs"), C2=(p,"Own text: moderate fit, transportation is one of several domains"),
  C3=(p,"City processes and regulations 'stacked against transformative solutions'"), C4=(d,"Youth-led tactical urbanism is community-led action defining need"),
  C5=(d,"Own text: infrastructure change possible only after community-led action pushed a reluctant agency"), C6=(d,"Cross-domain (housing, parks, transportation), non-AV"),
  C7=(p,"Bottom-up transformation as ongoing organizing, relational but advocacy-framed"))
t(EQ, "Di Ruocco", 2025,
  C1=(n,"Not about AVs"), C2=(p,"Own text: touches participation half more lightly"), C3=(d,"ICT/MaaS solutions designed by default around urban digitally literate users"),
  C4=(d,"Own text: supports unevenly distributed half directly"), C5=(d,"Own text: digitizes the same exclusion by assuming urban, digitally literate users"),
  C6=(d,"Global review evidence, non-AV specific tech-mediated mobility"), C7=(n,"No relational provisioning framing"))
t(EQ, "Jensen", 2026,
  C1=(n,"Not about AVs"), C2=(d,"Design choices encode exclusion with no participation in design"), C3=(p,"Design choices reflect a default material/engineering logic"),
  C4=(d,"Unhoused, disabled, and aging people should be centered in design"), C5=(d,"City built for an able-bodied middle-class default"),
  C6=(d,"Broad framework beyond any single project, deeply historical"), C7=(n,"No relational provisioning framing"))
t(EQ, "van Holstein et al.", 2020,
  C1=(n,"Not about AVs"), C2=(d,"Existing participatory mechanisms systematically underrepresent people with intellectual disability"),
  C3=(p,"Splintered, privatized transport governance is market/efficiency-driven fragmentation"), C4=(d,"People with intellectual disability's needs should govern network design"),
  C5=(d,"Access committees exclude intellectual disability; advocate expertise goes unpaid"), C6=(d,"Broader non-AV pattern of committee tokenism"),
  C7=(p,"Performative research method aimed at prompting collaboration is a relational engagement attempt"))
t(EQ, "Jeghers et al.", 2024,
  C1=(n,"Not about AVs"), C2=(p,"Own text: thinner on participation half, centers professionals not community"),
  C3=(p,"SWOT and funding-priority framing is institutional/technical"), C4=(p,"Own text: moderate fit for unevenly distributed half"),
  C5=(p,"Funding/priority misalignment documented via professional perceptions, not community voice directly"), C6=(p,"Smart Cities pilot context has some generalizability"),
  C7=(n,"No relational provisioning framing"))
t(EQ, "Yin et al.", 2026,
  C1=(n,"Not about AVs"), C2=(n,"Own text: thinner fit, no infrastructure-without-participation case examined"),
  C3=(p,"Quantitative modeling of unmet demand is a technical framing"), C4=(p,"Social participation as the strongest predictor touches community concerns loosely"),
  C5=(n,"Not demonstrated"), C6=(n,"Own text: included only as background evidence"), C7=(n,"No relational provisioning framing"))
t(EQ, "Contreras et al.", 2026,
  C1=(n,"Not about AVs"), C2=(d,"Distinct mechanism: funding cuts remove the community-knowledge pipeline from decisions"),
  C3=(p,"Techno-rational planning explicitly contrasted with community knowledge"), C4=(d,"Community-reported dangers like poor lighting should govern route-safety decisions"),
  C5=(d,"Quantitative metrics can certify a route safe while missing community-reported dangers"), C6=(d,"Broader structural/funding pattern, non-AV"),
  C7=(p,"Epistemic justice treats community knowledge as legitimate ongoing input"))
t(EQ, "Bailey et al.", 2012,
  C1=(n,"Not about AVs"), C2=(d,"VDOT committee shrank from nearly 70 to about 30 representatives, held up as a model process"),
  C3=(p,"Four process metrics are a procedural/technical measurement framework"), C4=(d,"Low-income and minority stakeholders' full participation is the stated EJ goal"),
  C5=(d,"Small-group advisory committees compromise the inclusiveness EJ mandates require"), C6=(d,"Procedural justice under-theorized broadly in transportation EJ work, historical, non-AV"),
  C7=(n,"No relational provisioning framing"))
t(EQ, "Chapman et al.", 2024,
  C1=(n,"Not about AVs"), C2=(d,"Own text: standards developed without embedding diverse disabled people's needs"),
  C3=(d,"Compliance-based accessibility standards are a rule/metric-driven default"), C4=(d,"Dignity depends on infrastructure, staff, and information across the whole journey"),
  C5=(d,"Standards met on paper while still excluding people whose needs fall outside them"), C6=(d,"Broader compliance-standards critique, non-AV, applies to ADA/DSAPT generally"),
  C7=(p,"Dignity across a whole journey is relational and ongoing, close to C7 but not explicitly provisioning"))
t(EQ, "Bahman et al.", 2026,
  C1=(d,"Explicitly about AV deployment as an infrastructure/policy matter"), C2=(p,"Names community engagement as a required component, conceptually not evidenced"),
  C3=(p,"Siloed AV research treating equity/sustainability separately is an institutional/technical silo logic"), C4=(p,"Equitable access is a stated principle, not empirically demonstrated"),
  C5=(p,"Warns AVs could burden marginalized communities unless equity is designed in"), C6=(n,"Specific to AVs, does not generalize beyond"),
  C7=(p,"Adaptive governance hints at ongoing process but remains conceptual"))
t(EQ, "Nakshi et al.", 2025,
  C1=(n,"Not about AVs"), C2=(p,"Names undelivered infrastructure promises as a pattern of underinvestment"), C3=(p,"Delayed infrastructure investment reflects institutional/bureaucratic logic"),
  C4=(d,"Racism and harassment shaping travel attitudes puts relational trust explicitly at the center"), C5=(d,"Chronic underinvestment and distrust vs residents' needs"),
  C6=(d,"Broader urban transit disinvestment pattern, non-AV"), C7=(p,"Relational trust as a central foreclosed value, an ongoing distrust dynamic"))
t(EQ, "Linovski et al.", 2026,
  C1=(n,"Not about AVs"), C2=(d,"Locates the disconnect at the level of who holds decision-making power"),
  C3=(p,"Technical-rational model treats politicians as external to decision-making, an adjacent institutional logic"),
  C4=(d,"Decision-makers demographically and experientially unlike the communities decisions most affect"), C5=(d,"Officials distant from the barriers under discussion"),
  C6=(d,"Broader pattern about who makes decisions generally, non-AV"), C7=(n,"No relational provisioning framing"))
t(EQ, "Zhang et al.", 2025,
  C1=(n,"Not about AVs"), C2=(p,"Proactive outreach argued for, implying current lack of participation"), C3=(p,"Logit demand model is a quantitative, demand-responsive framing"),
  C4=(d,"Hispanic PWD trusting neighbors over formal services shows relational trust as a governing factor"), C5=(d,"Standard demand-responsive planning misses needs trust barriers keep people from voicing"),
  C6=(d,"Intersectional pattern, broader non-AV evidence"), C7=(p,"Community trust over formal services is a relational-provisioning concept"))
t(EQ, "Wander et al.", 2026,
  C1=(n,"Not about AVs"), C2=(p,"Connects to participation half via centering affected voices, conceptually"), C3=(p,"Past supply-side, one-size-fits-all policy is a uniform-efficiency default"),
  C4=(d,"Mobility justice requires centering voices of those experiencing disparities"), C5=(d,"One-size-fits-all approaches fail dispersed low-income communities"),
  C6=(d,"Traces historical car-access disparities, broader non-AV pattern"), C7=(d,"Mobility as capability, targeted universalism, ongoing subsidy-plus-service pairing closely matches Mobility as Social Service"))
t(EQ, "Mouratidis", 2026,
  C1=(n,"Not about AVs"), C2=(p,"Own text: briefly names participatory planning as needed but underused"), C3=(p,"Transit-led gentrification is a market-driven displacement mechanism"),
  C4=(p,"Mobility-related exclusion for non-drivers is documented"), C5=(p,"Accessibility benefits lost to displacement is a form of misalignment, though economic not efficiency-values based"),
  C6=(p,"Broad wellbeing review, a thinner fit per own text"), C7=(n,"No relational provisioning framing"))
t(EQ, "Situ", 2025,
  C1=(n,"Not about AVs"), C2=(n,"Own text does not address participation, purely quantitative constraint modeling"), C3=(p,"Car-dependent planning assumes a baseline driving ability as default"),
  C4=(d,"Intersectional account of who bears constraints centers community needs"), C5=(p,"Car-dependent assumption compounding disadvantage is an implied, not process-based, misalignment"),
  C6=(d,"Broader structural pattern, non-AV"), C7=(n,"No relational provisioning framing"))
t(EQ, "Karner et al.", 2020,
  C1=(n,"Not about AVs"), C2=(d,"Own text: directly and centrally supports"), C3=(d,"Quantitative equity analyses and pro forma involvement explicitly named as insufficient technical process"),
  C4=(d,"Residents' active participation is essential per central claim"), C5=(d,"Incremental technical reforms leave underlying power positions unchanged"),
  C6=(d,"Broad historical framework spanning state and society-centered strategies, non-AV"), C7=(d,"Transportation justice as structural, ongoing redistribution of power and resources"))
t(EQ, "Cha et al.", 2020,
  C1=(n,"Not about AVs"), C2=(d,"Own text: does not address community participation, illustrating top-down technically-defined equity"),
  C3=(d,"Purely technical GIS optimization, explicit"), C4=(n,"No described role for residents at all"), C5=(d,"Equity solved by planners selecting weights with no resident role"),
  C6=(d,"Exemplifies broader top-down technical pattern, non-AV"), C7=(n,"No relational provisioning framing"))
t(EQ, "Pan et al.", 2024,
  C1=(n,"Not about AVs"), C2=(d,"Pro forma public meetings; equity absent from tech-focused scenarios"), C3=(d,"Agencies use pro forma meetings; tech/economy-focused scenarios lack equity"),
  C4=(d,"Community participation as justice-building is explicitly proposed"), C5=(d,"Own text: input 'collected and set aside' rather than shaping plans"),
  C6=(d,"Broad review across scenario planning practice, non-AV though touches emerging tech like EVs"), C7=(p,"Training communities in the planning process is ongoing capacity-building, close to relational provisioning"))
t(EQ, "Vanderschuren et al.", 2021,
  C1=(n,"Not about AVs"), C2=(p,"Own text: recommends including community leaders/NGOs but did not investigate their actual role"),
  C3=(p,"Universal design vs superficial policy address is a default design logic"), C4=(d,"Disability-specific needs should shape policy"),
  C5=(d,"Superficial policy address is a misalignment; reduced trip-making evidences the real-world cost"), C6=(d,"29-country pattern, broad non-AV, historical policy neglect"),
  C7=(n,"No relational provisioning framing"))
t(EQ, "Sutcliffe et al.", 2021,
  C1=(n,"Not about AVs"), C2=(d,"Windsor mayor's unilateral shutdown without consulting transit groups or users"), C3=(p,"Emergency top-down authority bypassing consultation is a speed/efficiency logic under crisis"),
  C4=(d,"Low-income and marginalized riders disproportionately harmed by cuts"), C5=(d,"Own text: officials aware of equity concerns had little practical ability to consult"),
  C6=(d,"Broader emergency-decision-making pattern, non-AV"), C7=(n,"No relational provisioning framing"))
t(EQ, "Grasso et al.", 2020,
  C1=(n,"Not about AVs"), C2=(p,"Touches participation half through a policy recommendation for community-based design input, not evidenced directly"),
  C3=(p,"Uniform system design is a one-size-fits-all default"), C4=(d,"Documents who is left out and why: safety and cargo-carrying needs"),
  C5=(d,"Uniform design does not accommodate documented needs"), C6=(d,"Broader pattern of uniform-design mobility systems failing subgroups, non-AV"),
  C7=(n,"No relational provisioning framing"))

# ---------------- Participatory Method ----------------
t(PM, "Baumann, K., Caldwell, B., Bar, F., & Stokes, B.", 2018,
  C1=(p,"Self-driving cars are one of several speculative techs discussed, not the primary infrastructure focus"),
  C2=(p,"Co-design proposed explicitly as an alternative to having a future imposed on a community"),
  C3=(n,"Not about efficiency-driven values specifically"), C4=(d,"Residents author their own scenarios, values governing the process"),
  C5=(n,"Method paper; does not document a specific misalignment case"), C6=(p,"Infrastructures of the imagination is a general capacity-building concept, not AV-specific"),
  C7=(p,"Long-term capacity building is an ongoing relational practice"))
t(PM, "Van Wynsberghe, A., & Guimarães Pereira, Â.", 2022,
  C1=(d,"About AVs' political and imaginary framing directly"), C2=(d,"Citizens redefine mobility on their own terms rather than the industry's"),
  C3=(d,"Own text: efficiency-driven industry visions of AVs don't match what communities actually value"),
  C4=(d,"Citizens redefining mobility on their own terms centers community concerns"), C5=(d,"Explicit mismatch between industry visions and community values"),
  C6=(n,"Specific to AVs"), C7=(p,"Material deliberation with embodied knowledge is a relational method"))
t(PM, "Severs, R., Wu, J., Diels, C., Harrow, D., Singleton, J., & Winsor, R.", 2022,
  C1=(p,"AV interiors are vehicle-level, not full infrastructure framing"), C2=(d,"Transport-excluded groups' needs missed by mainstream AV design"),
  C3=(p,"Mainstream AV design as the unexamined default implies an efficiency/mainstream-optimized logic"), C4=(d,"Transport-excluded groups hold specific, identifiable design needs"),
  C5=(d,"Mainstream AV design misses those needs"), C6=(n,"AV-specific"), C7=(p,"Journey mapping is a relational method surfacing ongoing mobility practice"))
t(PM, "Tan, Y., Soh, K.X., Zhang, R., Lee, J., Meng, H., Sen, B., & Lee, Y.-C.", 2025,
  C1=(n,"Not about AVs or infrastructure; AI casework tool"), C2=(p,"Co-design workshops proposed as an antidote to imposed technology, same underlying pattern"),
  C3=(n,"Not about efficiency-engineering values; about professional identity and skill loss"), C4=(d,"Frontline workers' relational-trust concerns surfaced via workshops"),
  C5=(p,"Implied risk of overreliance and lost skills if not co-designed"), C6=(p,"Parallel domain (social service) demonstrates the general pattern outside mobility"),
  C7=(d,"Own text explicitly names relational-trust and human-connection concerns, a strong direct match"))
t(PM, "Aranda-Muñoz, Á., Bozic Yams, N., & Carlgren, L.", 2025,
  C1=(n,"Healthcare-worker training domain, not AVs"), C2=(p,"Own text: proves the method works outside its original context"),
  C3=(n,"Not applicable"), C4=(p,"Participants' agency over their own future is strengthened"), C5=(n,"Not applicable"),
  C6=(p,"Own text: explicit generalizability evidence across domains, non-AV"), C7=(p,"Experiential futures are an ongoing relational engagement"))
t(PM, "Liao, Q.V., & Muller, M.", 2019,
  C1=(n,"AI systems generally, not infrastructure"), C2=(p,"Method exists because neither current-practice study nor speculation alone surfaces values for a non-existent technology"),
  C3=(n,"Not applicable"), C4=(d,"Stakeholder values are central to the method's purpose"), C5=(n,"Methodological paper, not a documented misalignment case"),
  C6=(p,"Value Sensitive Design is an established approach beyond just AVs"), C7=(n,"No relational provisioning framing"))
t(PM, "Barendregt, L., Bendor, R., & van Eekelen, B.F.", 2024,
  C1=(n,"Not about AVs"), C2=(d,"Own text: mostly includes only experts and professionals rather than affected publics"),
  C3=(n,"Not applicable"), C4=(p,"Arnstein's ladder critique implies communities should hold real power"), C5=(d,"Process often not designed to genuinely empower, even when publics are included"),
  C6=(d,"Field-level review across participatory futuring broadly, non-AV, strong broader-pattern evidence"), C7=(n,"No relational provisioning framing"))
t(PM, "Forlano, L., & Mathew, A.", 2014,
  C1=(n,"General urban technology, not AV/infrastructure specific"), C2=(p,"Friction from resistance and reframing is a symptom of imposed technology meeting resistance"),
  C3=(n,"Not applicable"), C4=(d,"Embedded values become visible and contestable through friction"), C5=(p,"Friction as the site where misalignment surfaces, meta-level not case-specific"),
  C6=(p,"Mixed policy actor stakeholders, broader than just AVs"), C7=(p,"Design friction as ongoing negotiation is a relational process"))
t(PM, "Omori, M., & Lim, Y.", 2025,
  C1=(n,"Not applicable"), C2=(n,"Method-focused single case, not documented exclusion"), C3=(n,"Not applicable"),
  C4=(p,"Provokes people to reflect on their own values"), C5=(n,"Not applicable"), C6=(n,"Single design case, no generalization claim"), C7=(n,"No relational provisioning framing"))
t(PM, "Sörries, P., Leimstädtner, D., & Müller-Birn, C.", 2024,
  C1=(n,"Healthcare/legal data-donation domain, not AVs"), C2=(p,"Method for converting stakeholder values into design requirements avoids imposed design"),
  C3=(n,"Not applicable"), C4=(d,"Vulnerable stakeholders' values are converted into concrete design requirements"), C5=(n,"Positive/successful case, not documenting a misalignment"),
  C6=(p,"Single healthcare/legal context; own text notes transferability to mobility is untested"),
  C7=(d,"Own text: closes the workshop-to-values-to-design pipeline, directly analogous to ongoing equitable provisioning"))
t(PM, "Wong, R.Y., Mulligan, D.K., Van Wyk, E., Pierce, J., & Chuang, J.", 2017,
  C1=(n,"Privacy technology domain, not AVs"), C2=(p,"Design workbook is a deliberate values-surfacing alternative to imposed design"),
  C3=(n,"Not applicable"), C4=(d,"Values levers foreground values as central to design"), C5=(n,"Methodological demonstration, not a misalignment case"),
  C6=(p,"Privacy by Design is an established broader design paradigm"), C7=(n,"No relational provisioning framing"))

with open("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/_step3_all.json", "w") as f:
    json.dump({f"{k[0]}|{k[1]}|{k[2]}": v for k, v in TAGS.items()}, f, indent=2, ensure_ascii=False)
print(f"Total rows tagged: {len(TAGS)}")

# ---- Build thesis_clause_matrix.csv (one row per paper, one column per clause) ----
unified = pd.read_csv("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/unified_lit_review.csv")
matrix_rows = []
missing = []
for _, row in unified.iterrows():
    key = (row["Thread"], row["Author(s)"], int(str(row["Year"])[:4]))
    tags = TAGS.get(key)
    if tags is None:
        missing.append(key)
        continue
    out = {"Thread": row["Thread"], "Reviewers": row["Reviewers"], "Author(s)": row["Author(s)"],
           "Year": key[2], "Paper Title": row["Paper Title"]}
    for code in CLAUSES:
        short = code.split("_")[0]  # e.g. "C1"
        out[code] = tags[short][0]
        out[code + "_reason"] = tags[short][1]
    matrix_rows.append(out)

if missing:
    print("MISSING KEYS (need fix):", missing)

matrix_df = pd.DataFrame(matrix_rows)
matrix_df.to_csv("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/thesis_clause_matrix.csv", index=False)
print(f"Saved thesis_clause_matrix.csv: {len(matrix_df)} rows")

# ---- Build thesis_clause_summary.csv (direct/partial counts per clause per thread) ----
summary_rows = []
for thread in matrix_df["Thread"].unique():
    sub = matrix_df[matrix_df["Thread"] == thread]
    n_papers = len(sub)
    for code, clause_text in CLAUSES.items():
        counts = sub[code].value_counts()
        summary_rows.append({
            "Thread": thread, "Clause": code, "Clause_text": clause_text,
            "n_papers": n_papers,
            "n_direct": int(counts.get("direct", 0)),
            "n_partial": int(counts.get("partial", 0)),
            "n_none": int(counts.get("none", 0)),
            "pct_direct": round(100 * counts.get("direct", 0) / n_papers, 1),
            "pct_direct_or_partial": round(100 * (counts.get("direct", 0) + counts.get("partial", 0)) / n_papers, 1),
        })
summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv("/Users/adityanaik/Documents/Work/UDMA-/crosscomp/thesis_clause_summary.csv", index=False)
print(f"Saved thesis_clause_summary.csv: {len(summary_df)} rows")
print(summary_df.pivot(index="Clause", columns="Thread", values="pct_direct"))
