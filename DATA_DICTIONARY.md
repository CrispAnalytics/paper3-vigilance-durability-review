# Data Dictionary

## `data/prisma_counts.json`
Counts from the OpenAlex seed + citation chaining search run (identification and title/abstract screening).

## `logs/openalex_api_log.csv`
Machine-auditable trace of OpenAlex API calls used in the search and citation chaining workflow.

## `data/fulltext_processing_manifest.csv`
Report-level manifest for the retrieval + full-text screening workflow.
- Public bundle version removes the local `pdf_path` field.

Key fields:
- `short_id`: OpenAlex work short identifier
- `pdf_status`: `downloaded` or `unresolved`
- `fulltext_screen_status`: `include` or `exclude`
- `eligibility_tier`: `T1_core` or `T2_context` for included reports
- `low_baseline_arousal_class`, `repeated_use_class`, `habituation_class`: operational classification codes

## `data/evidence_table.csv`
Outcome-level evidence extraction table.
- Public bundle version removes the local `pdf_path` field.

Key fields:
- `intervention_protocol`: dose/timing/frequency as extracted
- `exposure_duration_days`: repeated-use duration per condition
- `outcome_measure`, `effect_direction`, `effect_size_reported`
- `anchors`: location in source PDF (page/table/figure/section) for audit

## `data/risk_of_bias.csv`
Work-level risk-of-bias log with pragmatic notes aligned to extraction.

## `output/synthesis/S001_*`
Derived synthesis outputs (evidence maps, statistics) used for figures and narrative synthesis.

## `figures/Figure1.png` ... `figures/Figure4.png`
Figure files referenced in the manuscript submission package.

