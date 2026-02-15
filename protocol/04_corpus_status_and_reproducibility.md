# Corpus Status and Reproducibility (Current)

- Last updated (UTC): `2026-02-14T21:53:25+00:00`

## Current Authoritative Counts
Source: `logs/pdf_retrieval_final_summary.json`

- Initial downloaded full texts: 142
- Additional recovered via automated retries: 187
- Final downloaded full texts: 329
- Final unresolved full texts: 16

## Post-Retrieval QA Adjustments (Full-Text Triage)
During full-text triage, some downloaded PDFs were found to be mismatched (non-scholarly documents saved under a study ID).
These files were moved to `_trash/mismatched_pdfs/` and logged in `logs/pdf_download_log.csv` with status `mismatched_moved_to_trash`.
When no valid replacement full text was available, corresponding rows in `data/fulltext_processing_manifest.csv` were set to `pdf_status=unresolved` and excluded as `full_text_unavailable`.
In rare cases, a mismatched file was replaced with a relevant artifact (e.g., supplemental material) and the record was explicitly flagged in the manifest notes (and treated as non-full-text evidence where appropriate).

- Mismatched PDFs moved to trash: 15
- Effective full texts available for screening (manifest `pdf_status=downloaded`): 308
- Effective unresolved full texts (manifest `pdf_status=unresolved`): 30

Note (E006 extraction QA): `W3132047372` initially had a mismatched non-article file; this was moved to `_trash/mismatched_pdfs/` and replaced with a Figshare-hosted supplement PDF. The publisher full text remains paywalled, so evidence extraction for this record is marked as abstract-only context in `data/evidence_table.csv` and `data/risk_of_bias.csv`.

## Authoritative Tables and Logs
- Screening master table: `data/all_candidates_screened.csv`
- Included records table: `data/included_studies.csv`
- Excluded records table: `data/excluded_studies.csv`
- PRISMA counts: `data/prisma_counts.json`
- Citation chaining edges: `data/citation_network_edges.csv`
- Full-text processing manifest (work queue + progress tracker): `data/fulltext_processing_manifest.csv`
- OpenAlex API trace: `logs/openalex_api_log.csv`
- Initial PDF retrieval log: `logs/pdf_download_log.csv`
- Manual full-text additions log: `logs/manual_pdf_additions_2026-02-14.csv`
- Final merged PDF status table: `logs/pdf_retrieval_merged_status.csv`
- Final retrieval summary: `logs/pdf_retrieval_final_summary.json`
- Consolidated retry-pass ledger: `logs/pdf_retry_passes_summary.json`

## Reproducibility Scripts
- Seed + chaining + screening + initial PDF retrieval:
  - `protocol/run_openalex_pipeline.py`
- Manual import (organize and validate already-downloaded PDFs into canonical corpus naming):
  - `protocol/import_manual_pdfs_2026_02_14.py`
- Full-text phase manifest builder (preserves screening/extraction annotations):
  - `protocol/build_fulltext_processing_manifest.py`
- Full-text triage batching helpers (manifest-first workflow):
  - `protocol/queue_next_fulltext_batch.py`
  - `protocol/triage_fulltext_batch.py`
  - `protocol/export_fulltext_batch_snapshot.py`
- Automated retry pipelines:
  - `protocol/retry_failed_pdfs_pass3_oa_resolvers.py`
  - `protocol/retry_failed_pdfs_pass4_crossref_s2.py`
  - `protocol/retry_failed_pdfs_pass5b_openaire_filtered.py`
  - `protocol/retry_failed_pdfs_pass6_search_harvest.py`
  - `protocol/retry_failed_pdfs_pass7_title_openaire.py`
  - `protocol/retry_failed_pdfs_pass8_openalex_locations.py`
  - `protocol/retry_failed_pdfs_pass9_deep_resolver.py`
  - `protocol/retry_failed_pdfs_pass10_pmc_opus_playwright.py`
  - `protocol/retry_failed_pdfs_pass11_pmc_playwright_abortsafe.py`
  - `protocol/retry_failed_pdfs_pass12_creative_targeted.py`
  - `protocol/retry_failed_pdfs_pass13_tail_recovery.py`
  - `protocol/retry_failed_pdfs_pass14_tail_recovery_fixes.py`
  - `protocol/retry_failed_pdfs_pass15_lboro_doaj_fix.py`
  - `protocol/retry_failed_pdfs_pass16_doaj_wayback_pdf.py`
  - `protocol/retry_failed_pdfs_pass17_wayback_core_dspace_waf.py`
  - `protocol/retry_failed_pdfs_pass18_validated_targeted.py`

## Note for Manuscript Methods
Use the final merged status table and final summary JSON for full-text retrieval reporting, not the initial pass-only PDF log.
