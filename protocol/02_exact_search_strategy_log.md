# Exact Search Protocol Log (Paper 3)

## Run Metadata
- UTC run timestamp: 2026-02-14T00:16:33.552104+00:00
- API: https://api.openalex.org
- User-Agent: Paper3-OpenAlex-Protocol/1.0
- Per-page: 200
- Max pages per seed query: 1
- Citation forward pages max: 1

## Locked Question
In low-baseline-arousal adults, which natural intervention protocols sustain elevated daytime tonic arousal and cognitive performance over repeated daily use, and which show habituation?

## Seed Queries (Exact)
1. low arousal cognitive performance intervention
2. trait sleepiness vigilance intervention
3. daytime sleepiness psychomotor vigilance intervention
4. caffeine vigilance repeated daily use tolerance
5. coffee alertness tolerance psychomotor vigilance
6. bright light alertness sustained attention trial
7. morning bright light chronotype alertness performance
8. sleep extension psychomotor vigilance performance
9. sleep regularity daytime alertness cognitive performance
10. circadian alignment alertness intervention
11. acute exercise sustained attention vigilance adults
12. exercise training cognitive performance attention adults
13. heart rate variability biofeedback attention performance trial
14. slow breathing intervention attention vigilance
15. breathwork alertness cognitive performance
16. cold water immersion alertness cognitive performance
17. natural intervention tonic arousal baseline pupil vigilance
18. habituation alertness intervention repeated use
19. tolerance alertness intervention longitudinal
20. reaction time vigilance natural intervention low baseline

## Classification Rules (Exact)
- Core include: intervention-hit AND outcome-hit AND (baseline-hit OR duration-hit)
- Support include: intervention-hit AND outcome-hit AND (trial-hit OR review/meta signal)
- Exclude otherwise.

Keyword dictionaries used:
- Intervention terms: caffeine, coffee, bright light, light therapy, light exposure, exercise, physical activity, training, sleep extension, sleep regularity, circadian, chronotype, cold exposure, cold water, cold immersion, breathwork, slow breathing, biofeedback, hrv
- Outcome terms: vigilance, alertness, sustained attention, attention, cognitive performance, reaction time, psychomotor vigilance, pvt, fatigue, sleepiness
- Baseline terms: baseline, trait, low arousal, daytime sleepiness, chronotype, resting, tonic
- Duration terms: daily, repeated, longitudinal, chronic, weeks, months, habituation, tolerance, sustained
- Trial/RCT terms: randomized, randomised, trial, controlled, crossover, cross-over

## Citation Chaining Parameters
- Hop 1 parent selection: top 10 seed includes by decision, score, review flag, cited_by_count.
- Hop 1 backward references cap: 12.
- Hop 1 forward citing works cap: 12.
- Hop 2 parent selection: top 6 hop-1 includes.
- Hop 2 backward references cap: 6.
- Hop 2 forward citing works cap: 6.

## Output Artifacts
- All screened records: data/all_candidates_screened.csv
- Included set: data/included_studies.csv
- Excluded set with reasons: data/excluded_studies.csv
- PRISMA count inputs: data/prisma_counts.json
- Citation edges: data/citation_network_edges.csv
- API trace log: logs/openalex_api_log.csv
- PDF retrieval log: logs/pdf_download_log.csv
- Downloaded PDFs: pdfs/

## Notes for Manuscript Transparency
- This run is fully reproducible from protocol/run_openalex_pipeline.py.
- All API calls are logged with timestamp, endpoint, params, status, and result count.
- Any future rerun should preserve this script and archive a new timestamped output folder.
