# Manuscript Draft (S001)

## Working Title
Durability of Natural Arousal-Enhancing Protocols in Low-Arousal Adults: A Systematic Review Focused on Habituation and Sustained Vigilance

## Research Question (Locked)
In low-baseline-arousal adults, which natural intervention protocols sustain elevated daytime tonic arousal and cognitive performance over repeated daily use, and which show habituation?

## Methods (Draft; PRISMA-Oriented)

### Protocol and Reporting Framework

We followed a PRISMA-oriented protocol for evidence identification, retrieval, screening, and extraction. The locked question and PICOS eligibility criteria are specified in `protocol/01_prisma_protocol.md`.

### Information Sources and Search Strategy

Search and chaining (manuscript-ready text):

We conducted a PRISMA-oriented evidence retrieval using OpenAlex (https://api.openalex.org) on February 14, 2026 (UTC). The search used 20 predefined seed queries spanning the intersection of (1) natural intervention terms (e.g., bright light, caffeine/coffee, exercise, sleep/circadian strategies, cold exposure, breathing, HRV biofeedback), (2) cognitive-vigilance outcomes (e.g., vigilance, sustained attention, reaction time, psychomotor vigilance), and (3) baseline/duration qualifiers (e.g., trait, baseline, repeated use, habituation, tolerance). Search calls were executed at `per-page=200` with one page per seed query, with full API trace logging.

Records were deduplicated by OpenAlex work ID and machine-screened using pre-registered title/abstract rules. Core inclusion required intervention-hit + cognitive/vigilance outcome-hit + baseline or repeated-use relevance; support inclusion required intervention-hit + cognitive/vigilance outcome-hit + trial/review signal. Forward and backward citation chaining was then applied with two-hop expansion: hop-1 from the top 10 seed-included parent works (12 backward + 12 forward cap per parent), followed by hop-2 from the top 6 hop-1 included parents (6 backward + 6 forward cap per parent). This design balanced recall with tractable, reproducible expansion.

The exact seed queries and keyword dictionaries used are logged in `protocol/02_exact_search_strategy_log.md` and the full API trace is logged in `logs/openalex_api_log.csv`.

### Eligibility Criteria

Eligibility criteria were defined a priori using a PICOS structure (adults, natural/non-pharmacologic interventions, repeated-use relevance, and vigilance/tonic arousal outcomes). Operational definitions for 'low baseline arousal' and 'repeated-use durability' were applied during full-text screening (see `protocol/06_fulltext_screening_codebook.md`).

### Full-Text Retrieval and Corpus Construction

Full-text retrieval was attempted for all records included at the title/abstract stage. Automated retrieval used OpenAlex locations and a series of resolver retry passes; the final retrieval status is reported in `protocol/04_corpus_status_and_reproducibility.md` with audit logs in `logs/`.

Post-retrieval QA included mismatch detection; mismatched PDFs were moved to `_trash/mismatched_pdfs/` and logged in `logs/pdf_download_log.csv`. In rare cases, a mismatched file was replaced with a relevant artifact (e.g., a supplement); these were flagged and treated as context-only evidence when the main article remained paywalled.

### Study Selection and Tiering for Synthesis

Full-text screening and evidence extraction were tracked in a single manifest (`data/fulltext_processing_manifest.csv`). Records were tiered for synthesis into `T1_core` (directly answers the locked question) and `T2_context` (mechanism/gap-map support). To prevent scope creep, `T2_context` extraction used a pre-specified cutoff and stopping rule (see `workflow/extraction/10_T2_context_cutoff_and_stopping_rule.md`).

### Data Extraction and Risk of Bias

Structured extraction was performed into an outcome-level evidence table (`data/evidence_table.csv`) with a corresponding per-work risk-of-bias log (`data/risk_of_bias.csv`). The extraction schema and minimum required fields are specified in `protocol/07_evidence_extraction_schema.md`.

### Synthesis Approach

Given heterogeneous designs and endpoints, we performed a narrative synthesis oriented around repeated-use durability and habituation/tolerance signals, supplemented by evidence mapping visualizations (see `output/synthesis/`). Core conclusions are based on `T1_core` evidence; `T2_context` is used to constrain interpretation and map gaps.

## Results (Draft)

### Study Identification and Retrieval (PRISMA Flow)

- Records identified from OpenAlex seed query retrieval: 3,685
- Records identified via citation chaining, hop 1: 216
- Records identified via citation chaining, hop 2: 12
- Total raw identified records: 3,913
- Unique records after deduplication: 3,116
- Records screened (title/abstract): 3,116
- Records excluded (title/abstract): 2,778
- Reports sought for full-text retrieval: 338
- Reports retrieved in initial pass: 142
- Additional reports retrieved in automated retry passes: 187
- Final reports retrieved (PDF downloaded successfully): 329
- Final reports not retrieved (blocked/non-PDF/unavailable): 16
- Studies included for evidence synthesis (title/abstract stage): 338

### Extracted Evidence Base

Across the extracted evidence set, we mapped 30 works and 101 outcome rows (see `output/synthesis/S001_evidence_map_worklevel.csv` and `output/synthesis/S001_vigilance_outcomes.csv`).

### Study Characteristics (Extracted Set)

We extracted structured outcomes for 30 works ({'T2_context': 22, 'T1_core': 8}). The core evidence set (`T1_core`) comprises 8 works and primarily tests circadian/light and sleep-timing interventions in low-arousal proxy populations (shift work disorder, rotating shift workers, chronic short sleepers, and post-injury fatigue).
Across `T1_core`, repeated-use duration ranged from 3 to 60 days (max per work).

Core works by primary intervention category:
- `light`: 4 works
- `sleep_timing`: 2 works
- `multi`: 1 works
- `melatonin`: 1 works

### Core Findings by Intervention Class (T1_core)

#### Light Manipulation

- `W1981621779` Tanaka 2011 (J Occup Health) (duration max=30.0d; RoB=some_concerns): Registered nurses (all female) working rapidly rotating shifts including night shifts..
- Vigilance `PVT mean RT (msec; 5-min)` (Day-shift afternoon break (~14:00-15:00), repeated measures; subset n=11): `improves`; Estimated mean RT: 264 ms (non-BL) vs 235.8 ms (BL); diff -28.2 ms (95% CI -46.2, -10.2), F(1,17.0)=11.0, p<0.01 (Table 4).
- Vigilance `PVT lapses (>500 ms)` (Day-shift afternoon break; subset n=11): `improves`; Estimated lapses: 2.03 (non-BL) vs 0.84 (BL); diff -1.19 (95% CI -1.98, -0.40), F(1,17.4)=10.0, p<0.01 (Table 4).

- `W2094064988` Boudreau 2013 (PLoS ONE) (duration max=7.0d; RoB=some_concerns): Same cohort..
- Vigilance `PVT median reaction speed (1/RT) (10-min), by time awake` (Post-night-shift lab visit (daytime sleep schedule), across wake period): `improves`; Median reaction speed: no main effect of adaptation group (p=0.88); main effect of visit (p=0.012); main effect of time awake (p=0.036); 3-way interaction (group×visit×time-awake) p=0.046. During visit 2, adapted group faster than non-adapted after 8–14h awake (p≤0.045).

- `W3180479501` Connolly 2021 (BMC Neurology) (duration max=60.0d; RoB=unclear): Community-dwelling adults with mild-severe TBI or stroke >=3 months prior, reporting significant fatigue..
- Vigilance `PVT mean RT (10-min)` (end of each 2-month condition (mixed model treatment effect estimate)): `improves`; Treatment effect estimate -28.36 ms (95% CI -47.48, -9.23), t=-2.91, d=-1.75, p=.004; n=18 for PVT.
- Vigilance `PVT fastest 10% RT (10-min)` (end of each 2-month condition (mixed model treatment effect estimate)): `improves`; Treatment effect estimate -15.10 ms (95% CI -25.03, -5.16), t=-2.98, d=-2.98, p=.003; n=18 for PVT.

- `W3200473843` Connolly 2021 (Frontiers Neurology; case studies) (duration max=60.0d; RoB=high): Same as above..
- Vigilance `PVT mean RT (ms)` (Case 2 only: baseline, mid/end treatment, mid/end control): `unclear`; Case 2 PVT mean RT (ms): 310.44 (baseline) -> 300.03 (mid T) -> 314.75 (end T) -> 288.65 (mid C) -> 268.51 (end C) (Table 2).

Across these core light studies, objective vigilance outcomes tended to improve at the endpoint of repeated-use protocols (weeks to months), but causal strength is limited by small sample sizes, partial blinding feasibility, and outcome subsets in some designs.

#### Sleep Timing / Sleep Extension

- `W2128384646` Kubo 2011 (Scand J Work Environ Health) (duration max=3.0d; RoB=some_concerns; habituation_signal=yes): Daytime manufacturing employees with habitual short weekday sleep (mean weekday sleep ≤6h); neither extreme morning nor evening chronotype; no prescription meds; N=26 completers..
- Vigilance `PVT reaction time / reaction speed (10-min; PVT-192)` (Monday afternoon after the weekend (post-intervention vs post-control weekend)): `improves`; Significantly shorter reaction times on Mondays after the intervention vs habitual weekend sleep (p<0.05); overall condition×day interaction F(3,175)=6.01, p=0.001 (Figure 3; Table 1).
- Vigilance `PVT lapses (>500 ms) (10-min)` (Monday afternoon after the weekend): `improves`; Fewer PVT lapses on Mondays after intervention vs habitual weekend sleep (p<0.05); overall condition×day interaction F(3,175)=4.53, p=0.004 (Figure 3; Table 1).
- Vigilance `PVT reaction time / reaction speed (10-min)` (Thursday afternoon after the weekend): `worsens`; Significantly longer reaction times on Thursdays after intervention vs habitual weekend sleep (p<0.05), despite Monday improvement; condition×day interaction F(3,175)=6.01, p=0.001 (Figure 3; Table 1).
- Vigilance `PVT lapses (>500 ms) (10-min)` (Thursday afternoon after the weekend): `worsens`; Significantly more lapses on Thursdays after intervention vs habitual weekend sleep (p<0.05); condition×day interaction F(3,175)=4.53, p=0.004 (Figure 3; Table 1).

- `W4211135645` Cheng 2022 (Sleep) (duration max=7.0d; RoB=some_concerns; habituation_signal=yes): Night shift workers (>=20y) with ICSD-3 shift work disorder confirmed by interview + 2-week sleep log; pure 8h night shifts during study..
- Vigilance `Smartphone PVT reaction time (5-min) after night shift` (First night shift of each schedule (Table 2)): `improves`; First shift PVT RT: 0.67 s (morning sleep) vs 0.55 s (evening sleep), p=0.001; adjusted p=0.015 (Table 2). Lapses: 18.5 vs 15.4, p=0.009; adjusted p=0.115.
- Sleepiness `Karolinska Sleepiness Scale (KSS)` (After night shift (within 1h), by shift number (Table 2)): `improves`; KSS First shift: 4.9 (morning) vs 4.1 (evening), p=0.002; adjusted p=0.012. Second shift: 4.3 vs 4.0, adjusted p=0.097. Third shift: 5.1 vs 3.8, adjusted p=0.019. Fourth shift: ns (Table 2).

Across core sleep-timing/sleep-extension studies, benefits were often time-dependent (e.g., strongest on early shifts or early week) and could attenuate or reverse later, consistent with limited durability when the underlying schedule constraint persists.

#### Melatonin (Natural Hormone)

- `W2165853793` Bjorvatn 2007 (Scand J Work Environ Health) (duration max=4.0d; RoB=some_concerns): Same cohort..
- Vigilance `Objective 5-min serial reaction-time test (Palm) at 3 timepoints during shifts` (Nights 1,3,6 and days 1,3,6): `unclear`; No significant differences in reaction times when averaged across night shift or day shift. Day shift showed condition×day interaction F(4,44)=4.1, p=0.025 (Table 1), driven by increased reaction times on day 1 after melatonin and bright light (narrative; Figure 4).
- Sleepiness `ATS: Fighting sleep (%) during day shift week` (Day-shift week (second week), averaged across week): `improves`; Day shift fighting sleep: placebo 3.4±3.5 vs melatonin 1.8±2.8; effect size vs placebo d=0.50; melatonin significantly lower than placebo (p=0.021) and bright light (p=0.022) (Table 3).
- Sleepiness `Quality of day rating (1 very good to 9 very bad) during day shift week` (Day-shift week (second week), averaged across week): `improves`; Quality of day (day shift): placebo 4.1±1.1 vs melatonin 3.4±0.6; effect size vs placebo d=0.79; melatonin significantly better than placebo (p=0.041) (Table 3).

In the extracted core melatonin evidence, subjective sleepiness and sleep outcomes improved modestly, while objective reaction-time measures showed limited consistent benefit in field conditions.

#### Multicomponent Countermeasure Packages

- `W2158979070` Smith-Coggins 1997 (Acad Emerg Med) (duration max=30.0d; RoB=some_concerns): Attending emergency physicians working rotating shifts with night rotations..
- Vigilance `PVT (10-min): median RT and lapses` (multiple times during shifts; compared across conditions and across shift hours): `null`; PVT performance comparable regardless of intervention; neither experimental nor active placebo altered PVT (Fig 6). Median RT increased across the night shift when averaged across interventions (p=0.007).

In the extracted multicomponent core evidence, objective vigilance changes were limited, despite some subjective improvements reported in the underlying papers.

### Context Evidence for Habituation/Tolerance Framing (T2_context)

Context studies were extracted under a pre-specified cutoff emphasizing repeated-use duration and/or explicit habituation testing. These studies inform interpretation of durability mechanisms (e.g., stimulant tolerance/withdrawal; time-of-day and circadian interactions in light).

See `output/synthesis/S001_vigilance_outcomes.csv` for the vigilance-only endpoint ledger used for this synthesis.

## Discussion (Draft)

### Summary of What the Extracted Evidence Suggests

Across the core evidence base, repeated-use protocols that act via circadian and sleep regulation (light manipulation and sleep timing) show the most consistent objective vigilance improvements in low-arousal proxy populations. However, the evidence is heterogeneous and often limited by feasibility constraints (blinding, adherence, small samples) typical of real-world sleep/circadian interventions.

A critical interpretive distinction for this manuscript is whether an intervention plausibly shifts a 'tonic arousal set-point' versus reducing sleep pressure or circadian misalignment. In practice, most natural protocols likely improve daytime vigilance by changing upstream sleep/circadian state, not by directly elevating tonic arousal in a stimulant-like fashion.

### Habituation and Durability: How to Interpret Signals

Habituation signals in the extracted set most often appear as time-dependent effects across repeated exposures (e.g., strongest on early shifts, attenuation later) or reversal when the underlying constraint returns (e.g., weekend extension followed by recurrent weekday restriction). These patterns are consistent with state regulation rather than classical pharmacologic tolerance. By contrast, the caffeine context literature more directly illustrates tolerance/withdrawal dynamics that can compress net benefits over time.

### Practical Implications (Research, Not Clinical Guidance)

For repeated-use performance optimization in low-arousal proxies (shift workers, chronic short sleepers, fatigue populations), the most defensible evidence-driven framing is: (i) manipulate light and sleep timing to reduce misalignment and sleepiness, (ii) expect time-of-day and schedule interactions, and (iii) explicitly measure durability (day-by-day) rather than endpoint-only effects.

### Research Agenda Enabled by Secondary Research

This corpus supports a publishable durability-first taxonomy and a harmonized habituation coding framework. The highest-leverage next steps that do not require new experiments are: (1) protocol dose harmonization (timing, intensity, adherence), (2) explicit mapping of durability windows (day 1 vs day 7 vs day 30), and (3) separating proxy low-arousal populations from trait low-arousal claims.

### Limitations of This Evidence Base

- Proxy populations dominate; trait low baseline arousal is rarely defined explicitly.
- Few studies jointly measure physiology + performance strongly enough to claim a tonic baseline shift.
- Abstract-only extraction exists for at least one context item due to paywalled full text; these items are treated as context with reduced confidence.

## Figures and Tables (Current Draft Set)

- Fig 1: `output/synthesis/S001_fig1_study_counts_by_intervention.png`
- Fig 2: `output/synthesis/S001_fig2_vigilance_durability_map.png`
- Fig 3: `output/synthesis/S001_fig3_risk_of_bias_distribution.png`
- Table (work-level evidence map): `output/synthesis/S001_evidence_map_worklevel.csv`
- Table (vigilance endpoints): `output/synthesis/S001_vigilance_outcomes.csv`

## Supplementary Material (Audit Trail)

- Exact search protocol log: `protocol/02_exact_search_strategy_log.md`
- PRISMA flow text: `protocol/03_prisma_flow_and_reporting_text.md`
- Corpus status and reproducibility: `protocol/04_corpus_status_and_reproducibility.md`
- Full-text screening codebook: `protocol/06_fulltext_screening_codebook.md`
- Evidence extraction schema: `protocol/07_evidence_extraction_schema.md`
