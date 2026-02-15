# Evidence Extraction Schema (Draft v1)

Goal: a structured evidence table that supports synthesis, gap-mapping, and reproducible claims.

## Table 1: `data/evidence_table.csv` (One Row Per Study Outcome)
Required columns (current v1; keep stable once extraction scales):
- `short_id`
- `citation` (author-year or source string)
- `publication_year`
- `study_design` (free text; include RCT/crossover/blinding notes)
- `population_description`
- `low_arousal_proxy_definition` (e.g., shift-work disorder, high ESS, trait fatigue)
- `n_total`
- `setting` (lab|field|workplace|clinical|other)
- `intervention_category` (light|melatonin|sleep_timing|exercise|caffeine|cold|breathing|biofeedback|multi|other)
- `intervention_protocol` (dose, timing, duration, frequency; free text)
- `comparator` (baseline|control|active_control|other; free text)
- `exposure_duration_days` (per condition / per protocol segment)
- `outcome_domain` (vigilance|sleepiness|fatigue|sleep_quality|physiology|other)
- `outcome_measure` (PVT lapses/RT, KSS, ESS, HRV, pupil, etc.)
- `outcome_timepoint` (e.g., end of condition, first shift, follow-up)
- `effect_direction` (improves|worsens|null|mixed|unclear)
- `effect_size_reported` (as reported; free text; include CI/p-values when available)
- `habituation_or_tolerance_signal` (yes|no|unclear)
- `adherence_or_compliance` (as reported)
- `notes`
- `anchors` (where in the PDF: page/table/figure/section)
- `pdf_path`
- `pdf_sha256_16` (prefix for file integrity / mismatch detection)

## Table 2: `data/risk_of_bias.csv` (One Row Per Study)
Required columns (draft):
- `short_id`
- `rob_tool` (RoB2|ROBINS-I|AMSTAR2|other)
- `rob_overall` (low|some_concerns|high|unclear)
- `rob_notes`

## Implementation Notes
- Keep extraction batchable: aim for 10-20 studies per batch.
- If systematic reviews/meta-analyses are included, extract both:
  - their headline findings (for context)
  - and avoid double-counting primary studies if you later meta-analyze.
