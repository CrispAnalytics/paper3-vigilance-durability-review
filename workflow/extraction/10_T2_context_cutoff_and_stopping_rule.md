# T2_context Extraction Cutoff + Stopping Rule (Authoritative)

Purpose: keep evidence extraction focused enough for a top-journal paper while still using `T2_context` to support mechanism and tolerance/habituation framing.

## Definitions
- `T1_core`: studies that directly answer the locked question (low-arousal adults + repeated-use natural interventions + vigilance/tonic arousal outcomes). These are the primary evidence base.
- `T2_context`: studies that are relevant but not primary (e.g., induced low arousal, general adults, acute-only exposures, mechanism-heavy trials).

The authoritative state machine is the manifest:
- `<REPO_ROOT>/data/fulltext_processing_manifest.csv`

## Cutoff Rule (What Gets Extracted From T2_context)
Only extract structured evidence for a `T2_context` record if all are true:
- `pdf_status = downloaded`
- `fulltext_screen_status = include`
- `extracted_evidence_status = todo`

AND at least one is true:
1. `habituation_class` in `{H1_tested_no_habituation, H2_tested_habituation}`
2. `repeated_use_class` in `{D2_repeated_weekplus, D3_repeated_monthplus}`
3. `low_baseline_arousal_class` in `{A1_explicit_low_arousal, A2_structural_proxy_low_arousal}`

Rationale:
- (1) captures papers that explicitly test waning/maintenance.
- (2) captures real durability timescales that can reframe same-day effects.
- (3) captures closer-to-core populations (even when exposures are acute).

## Priority Order (Within The Cutoff Set)
Sort descending by:
1. `habituation_class` (H2 > H1 > H3 > H0)
2. `repeated_use_class` (D3 > D2 > D1 > D0)
3. `low_baseline_arousal_class` (A1/A2 > A3 > A4 > AX)
4. `type` (article > preprint > dissertation/review)
5. `publication_year`, then `cited_by_count`

Queue file (prioritized remaining work):
- `<REPO_ROOT>/workflow/extraction/T2_context_extraction_queue.csv`

## Stopping Rule (Thematic Saturation)
Stop extracting `T2_context` when the most recent batch of ~5 extracted papers adds no new:
- intervention category,
- repeated-use timescale, AND
- habituation/tolerance pattern.

Operationally, when this happens twice in a row, treat the `T2_context` extraction set as complete for this manuscript.

## Batch Hygiene
- Each batch produces `E00X_queue.csv`, `E00X_evidence_rows.csv`, `E00X_extraction.md`, `E00X_QA.md`.
- The manifest is updated to `extracted_evidence_status=qa_passed` with notes containing `extract:E00X; qa:E00X_pass; evidence_rows=<n>`.

