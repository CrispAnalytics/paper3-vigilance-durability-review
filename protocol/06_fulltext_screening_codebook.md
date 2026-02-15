# Full-Text Screening Codebook (v2)

Purpose: keep full-text screening decisions consistent, auditable, and batchable across many PDFs.

## Decision Codes
- `include`: full text matches the locked research question and meets PICOS.
- `exclude`: full text does not meet PICOS or is otherwise out-of-scope.
- `uncertain`: cannot decide quickly; requires deeper read or missing key info.
- `todo`: not yet screened.

## Core Operational Definitions (Locked Question)
Locked question focus (from `protocol/01_prisma_protocol.md`):
- Low-baseline-arousal adults
- Natural intervention protocols
- Sustained elevation of daytime tonic arousal and cognitive performance over repeated daily use
- Habituation/tolerance signals (when available)

This codebook operationalizes two ambiguous constructs so full-text screening is consistent:
1. "Low baseline arousal"
2. "Repeated-use durability"

### 1) Low Baseline Arousal (Classify One)
Log one class code in the manifest column `low_baseline_arousal_class`:
- `A1_explicit_low_arousal` (Core)
  - Adults selected/stratified by an a priori low-arousal proxy at baseline, for example:
    - Excessive daytime sleepiness (e.g., ESS >= 10; or author-defined clinical cutoff)
    - High sleepiness ratings at baseline (e.g., KSS consistently high; or author-defined cutoff)
    - Trait fatigue scales at baseline with explicit threshold (FSS, CFQ, etc.)
    - Clinical diagnosis tightly linked to persistent low alertness in the sample context (e.g., shift work disorder; hypersomnia syndromes if included in your scope)
    - Objective baseline impairment threshold used for enrollment/stratification (e.g., PVT lapses above cutoff; MSLT mean sleep latency below cutoff)
- `A2_structural_proxy_low_arousal` (Core)
  - Adults not explicitly selected by a cutoff, but the population context is a strong structural proxy for low baseline alertness in real life, and baseline measures are taken in that context, for example:
    - Real-life night shift workers (especially with SWD symptoms, chronic misalignment, or documented daytime sleepiness)
    - Habitual short sleepers / chronic sleep restriction in field settings (not a one-night lab manipulation)
    - Chronic circadian misalignment cohorts where baseline sleepiness/alertness impairment is documented in the paper
- `A3_experimentally_induced_low_arousal` (Context)
  - Lab-induced sleep deprivation/sleep restriction/misalignment where the low-arousal state is created by protocol (acute or short-term).
  - Include only as context for mechanism/intervention response unless you explicitly decide the primary scope includes induced states.
- `A4_general_adults_unscreened` (Context)
  - Adult samples not selected/stratified for low arousal and not a structural proxy cohort.
  - Keep as context when it informs intervention durability/habituation, but do not treat as primary evidence for low-arousal adults.
- `AX_review_or_mixed_population` (Context)
  - Systematic reviews/meta-analyses or mixed-population papers where a single low-arousal class cannot be assigned without double-counting.

Default rule for the main synthesis that answers the locked question:
- Tier A core = `A1` or `A2`
- Tier B context = `A3`, `A4`, `AX` (as needed)

### 2) Repeated-Use Durability (Classify One)
Log one class code in the manifest column `repeated_use_class`:
- `D0_acute_only`
  - Single exposure session (even if multiple tasks within a day), no repeated-day protocol.
- `D1_repeated_short` (Core)
  - Same intervention repeated on >= 2 separate days, with outcomes measured at baseline and at least one post-baseline timepoint while still using the intervention.
  - Typical: 2-6 days.
- `D2_repeated_weekplus` (Core)
  - Repeated use for >= 7 days.
- `D3_repeated_monthplus` (Core)
  - Repeated use for >= 28 days.

Minimum requirement to claim "durability" rather than "acute":
- Intervention is applied on >= 2 days AND outcomes are measured beyond day 1.

### 3) Habituation/Tolerance Signal (Classify One)
Log one class code in the manifest column `habituation_class`:
- `H0_not_tested`
- `H1_tested_no_habituation` (authors test for waning and find none, or effect maintained across repeated days)
- `H2_tested_habituation` (effect size declines across repeated days or statistically significant time x condition consistent with tolerance)
- `H3_unclear_or_mixed`

Minimum evidence to mark "tested":
- At least 2 post-baseline measurements across different days (or sufficient repeated-measures across days) enabling a trend/interaction test.

## Tiering (Recommended For Best Paper)
Log one tier in the manifest column `eligibility_tier`:
- `T1_core`:
  - `A1` or `A2`
  - AND `D1`/`D2`/`D3`
  - AND outcome includes vigilance/sustained attention OR tonic/baseline arousal proxy (physiology or psychometric) relevant to daytime performance.
- `T2_context`:
  - Otherwise still relevant (e.g., `A3` induced low arousal; or `A4` general adults; or `D0` acute-only), useful for mechanism/gap-mapping but not the primary answer.

## Required Logged Fields (Minimum Viable)
For each `short_id`:
- `fulltext_screen_status`: one of `todo|include|exclude|uncertain`
- `fulltext_exclusion_reason`: required if `exclude`
- `notes`: optional

## Standard Exclusion Reasons (Pick One Primary)
- `population_not_adult`
- `population_not_low_arousal_proxy` (adult population but not low-arousal-relevant for this review's scope)
- `intervention_not_natural` (primary effect driven by prescription drug or surgical/clinical procedure)
- `no_intervention_evaluated` (observational/cross-sectional only; no intervention protocol tested)
- `no_repeated_use_or_durability` (classified as `D0_acute_only` and excluded from core if the main scope requires repeated-use)
- `outcome_not_tonic_arousal_or_vigilance` (no baseline arousal proxy, no sustained attention/vigilance/performance measure)
- `wrong_domain` (not cognitive performance/arousal optimization)
- `not_primary_study_or_high_value_review` (e.g., editorial, commentary, protocol-only, conference abstract-only if excluded)
- `full_text_unavailable`
- `duplicate_or_overlapping_report`

## Notes
- If you change whether `A3_experimentally_induced_low_arousal` is part of the primary scope, bump this codebook version and log the change rationale in `protocol/01_prisma_protocol.md`.
