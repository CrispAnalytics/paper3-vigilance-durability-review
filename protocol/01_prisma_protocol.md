# PRISMA-Oriented Protocol (Paper 3)

## Locked Research Question
In low-baseline-arousal adults, which natural intervention protocols sustain elevated daytime tonic arousal and cognitive performance over repeated daily use, and which show habituation?

## Review Objective
To synthesize evidence on natural interventions that increase baseline tonic arousal and cognitive-vigilance outcomes in low-arousal individuals, with emphasis on repeated-use durability and habituation/tolerance dynamics.

## Eligibility Criteria (PICOS)
- Population: Adults (>=18 years) with low baseline arousal proxies (daytime sleepiness, trait fatigue, low alertness, unfavorable chronotype alignment, low resting arousal markers).
- Intervention: Natural/non-pharmacologic protocols (e.g., bright light exposure, sleep/circadian alignment strategies, exercise/physical activity, breathing interventions, cold exposure, HRV biofeedback, caffeine/coffee used as behavioral nutritional intervention).
- Comparator: Within-subject baseline, passive control, active control, alternative protocol, or no intervention.
- Outcomes: Tonic/baseline arousal proxies (physiologic or psychometric) and cognitive performance (vigilance, sustained attention, reaction time, PVT, attentional lapses).
- Study designs: RCTs, controlled trials, crossover studies, longitudinal interventions, and high-value systematic reviews/meta-analyses.

## Information Sources
- Primary source: OpenAlex API.
- Retrieval date (UTC): 2026-02-14T00:16:33.552104+00:00
- Seed query count: 20

## Search Strategy Summary
- Multi-query seed retrieval (high-recall, intervention x outcome x baseline/duration terms).
- Forward and backward citation chaining.
- Hop depth: 2 hops with predefined caps to control combinatorial explosion.
- Full API trace logged in logs/openalex_api_log.csv.

## Screening and Selection Logic
Records were machine-screened using title/abstract rules:
- Include core: Intervention term + cognitive/vigilance outcome + baseline or repeated-use/duration relevance.
- Include support: Intervention + cognitive/vigilance + RCT/review/meta-analysis signal.
- Exclude: Insufficient fit to objective.

## Citation Chaining Design
- Hop 1 parents: top 10 seed includes by relevance and evidence centrality.
- Hop 1 backward cap: 12 references per parent.
- Hop 1 forward cap: 12 citing works per parent.
- Hop 2 parents: top 6 hop-1 includes.
- Hop 2 backward cap: 6 references per parent.
- Hop 2 forward cap: 6 citing works per parent.

## PRISMA Flow Inputs (Current Run)
- Records identified (seed raw): 3685
- Records identified (hop-1 raw): 216
- Records identified (hop-2 raw): 12
- Unique records after deduplication: 3116
- Records screened (title/abstract): 3116
- Records excluded (title/abstract): 2778
- Reports sought for retrieval: 338
- Included studies (title/abstract stage): 338

## Full-Text Retrieval Status
- Initial pass PDFs downloaded: 142
- Additional PDFs recovered via automated retry passes: 187
- Final PDFs downloaded (current corpus): 329
- Final unresolved full-text records: 16

## Full-Text Phase Operationalization (For Screening + Synthesis)
The title/abstract stage intentionally used broad, high-recall heuristics. The full-text phase applies the locked question with higher precision using:
- Full-text processing manifest (single work queue + progress tracker): `data/fulltext_processing_manifest.csv`
- Full-text screening codebook (operational definitions and decision codes): `protocol/06_fulltext_screening_codebook.md`
- Evidence extraction schema (structured evidence table fields): `protocol/07_evidence_extraction_schema.md`

Operational constructs tracked during full-text screening:
- Low baseline arousal classification: `A1/A2/A3/A0`
- Repeated-use durability classification: `D0/D1/D2/D3`
- Habituation/tolerance evidence classification: `H0/H1/H2/H3`
- Tiering for synthesis: `T1_core` (answers locked question) vs `T2_context` (mechanism/gap-map support)

## Evidence Extraction Scope Control (T2_context Cutoff)
The primary synthesis that answers the locked research question is based on `T1_core` studies only.

`T2_context` is used to support mechanism, tolerance/habituation framing, and intervention-category gap coverage without expanding this paper into a mega-review.

Detailed, auditable cutoff + stopping rule doc (authoritative implementation spec):
- `<REPO_ROOT>/workflow/extraction/10_T2_context_cutoff_and_stopping_rule.md`

### Pre-specified `T2_context` extraction inclusion filter (manifest-driven)
From the set of `T2_context` records with `pdf_status=downloaded`, `fulltext_screen_status=include`, and `extracted_evidence_status=todo`, extract evidence only if **any** of the following are true:
1. `habituation_class` is `H1_tested_no_habituation` or `H2_tested_habituation` (explicit waning/maintenance tested).
2. `repeated_use_class` is `D2_repeated_weekplus` or `D3_repeated_monthplus` (durability timescales).
3. `low_baseline_arousal_class` is `A1_explicit_low_arousal` or `A2_structural_proxy_low_arousal` (closer to core population, even if outcomes are acute).

### Stopping rule (thematic saturation)
Stop `T2_context` extraction when the most recent batch of ~5 extracted papers adds no new:
- intervention category,
- repeated-use timescale, and
- habituation/tolerance pattern (i.e., it only repeats already-covered conclusions with minor variants).

Implementation artifacts:
- Prioritized `T2_context` queue: `workflow/extraction/T2_context_extraction_queue.csv`
- Batch snapshot queues: `workflow/extraction/E00X_queue.csv`

## Risk and Limitations for Manuscript Methods Section
- Screening here is algorithm-assisted and should be followed by manual full-text confirmation and dual-review adjudication for final publication.
- OpenAlex relevance ranking can include domain noise; mitigation includes multi-query design + explicit keyword-based fit criteria + citation chaining.
- Some records are inaccessible in full text due publisher restrictions.

## Automated Retrieval Audit Trail (Full-Text Stage)
- Primary retrieval run: `protocol/run_openalex_pipeline.py`
- Retry pass 3 (DOI OA resolvers): `protocol/retry_failed_pdfs_pass3_oa_resolvers.py`
- Retry pass 4 (Semantic Scholar + Crossref + DOI landing parsing): `protocol/retry_failed_pdfs_pass4_crossref_s2.py`
- Retry pass 5b (OpenAIRE filtered full-text harvesting, concurrent): `protocol/retry_failed_pdfs_pass5b_openaire_filtered.py`
- Retry pass 6 (search-index harvest, legal domains only): `protocol/retry_failed_pdfs_pass6_search_harvest.py`
- Retry pass 7 (title-based OpenAIRE fallback for no-DOI tail): `protocol/retry_failed_pdfs_pass7_title_openaire.py`
- Retry pass 8 (OpenAlex locations + PubMed->PMC resolver): `protocol/retry_failed_pdfs_pass8_openalex_locations.py`
- Retry pass 9 (deep resolver: OpenAIRE/title/meta extraction): `protocol/retry_failed_pdfs_pass9_deep_resolver.py`
- Retry pass 10 (PMC PoW + OPUS repository recovery): `protocol/retry_failed_pdfs_pass10_pmc_opus_playwright.py`
- Retry pass 11 (PMC PoW abort-safe): `protocol/retry_failed_pdfs_pass11_pmc_playwright_abortsafe.py`
- Retry pass 12 (targeted OA recovery: WAF-cookie + mdpi-res + NCBI Bookshelf + DNS): `protocol/retry_failed_pdfs_pass12_creative_targeted.py`
- Retry pass 13 (tail recovery: mdpi-res + WAF-cookie + DOAJ/Wayback + figshare): `protocol/retry_failed_pdfs_pass13_tail_recovery.py`
- Retry pass 14 (tail fixes: DOAJ/Wayback + figshare regex fixes): `protocol/retry_failed_pdfs_pass14_tail_recovery_fixes.py`
- Retry pass 15 (Lboro + DOAJ recovery pass): `protocol/retry_failed_pdfs_pass15_lboro_doaj_fix.py`
- Retry pass 16 (DOAJ Wayback PDF download w/ PDF-preferring Accept): `protocol/retry_failed_pdfs_pass16_doaj_wayback_pdf.py`
- Retry pass 17 (Wayback/CDX + CORE + DSpace7 + WAF-cookie recovery): `protocol/retry_failed_pdfs_pass17_wayback_core_dspace_waf.py`
- Retry pass 18 (validated OA recovery: iOSPress Wayback + UWO DSpace + CORE validation): `protocol/retry_failed_pdfs_pass18_validated_targeted.py`
- Final reconciled full-text status table: `logs/pdf_retrieval_merged_status.csv`
- Final retrieval summary (authoritative): `logs/pdf_retrieval_final_summary.json`
