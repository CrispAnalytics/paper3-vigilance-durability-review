# PRISMA Flow + Reporting Text

## PRISMA 2020 Flow Inputs (from this run)
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

## Manuscript-Ready Methods Text (Search)
We conducted a PRISMA-oriented evidence retrieval using OpenAlex (https://api.openalex.org) on February 14, 2026 (UTC). The search used 20 predefined seed queries spanning the intersection of (1) natural intervention terms (e.g., bright light, caffeine/coffee, exercise, sleep/circadian strategies, cold exposure, breathing, HRV biofeedback), (2) cognitive-vigilance outcomes (e.g., vigilance, sustained attention, reaction time, psychomotor vigilance), and (3) baseline/duration qualifiers (e.g., trait, baseline, repeated use, habituation, tolerance). Search calls were executed at `per-page=200` with one page per seed query, with full API trace logging.

## Manuscript-Ready Methods Text (Screening + Chaining)
Records were deduplicated by OpenAlex work ID and machine-screened using pre-registered title/abstract rules. Core inclusion required intervention-hit + cognitive/vigilance outcome-hit + baseline or repeated-use relevance; support inclusion required intervention-hit + cognitive/vigilance outcome-hit + trial/review signal. Forward and backward citation chaining was then applied with two-hop expansion: hop-1 from the top 10 seed-included parent works (12 backward + 12 forward cap per parent), followed by hop-2 from the top 6 hop-1 included parents (6 backward + 6 forward cap per parent). This design balanced recall with tractable, reproducible expansion.

## Manuscript-Ready Results Text (Flow)
The search identified 3,913 raw records (3,685 seed; 216 hop-1; 12 hop-2). After deduplication, 3,116 unique records were screened by title/abstract; 2,778 were excluded and 338 were retained for synthesis-stage inclusion. Full-text retrieval was attempted for all 338 included records. The initial retrieval pass downloaded 142 PDFs; automated resolver retries recovered an additional 187 full texts, yielding a final corpus of 329 downloadable PDFs and 16 reports not retrieved due to access restrictions, missing/invalid full-text links, or unresolved host-level failures.

## Full-Text Phase Tracking (Operational)
Full-text screening and evidence extraction are tracked using a single manifest (work queue + progress state):
- `data/fulltext_processing_manifest.csv`

Full-text screening operational definitions for the locked constructs "low baseline arousal" and "repeated-use durability" are specified in:
- `protocol/06_fulltext_screening_codebook.md`
