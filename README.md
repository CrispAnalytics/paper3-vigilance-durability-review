# Durability-First Vigilance Review (Public Reproducibility Bundle)

This repository contains the **protocol**, **search/audit logs**, **screening manifest metadata**, **extracted evidence tables**, and **analysis outputs** used to produce the accompanying review manuscript.

## What This Repo Includes
- PRISMA-oriented search and screening metadata (OpenAlex-based)
- Full-text screening manifest (metadata only)
- Structured evidence extraction table (outcome-level)
- Risk of bias log (work-level)
- Synthesis outputs (evidence maps, summary stats)
- Figure PNGs used in the manuscript
- A LaTeX manuscript source used for drafting

## What This Repo Does Not Include
- Full-text PDFs are **not redistributed** here due to copyright and licensing constraints.
- The manifest and evidence table provide OpenAlex IDs / DOIs and extraction anchors to support independent retrieval and audit.

## Reproducing Key Outputs
- The included outputs under `output/synthesis/` are the authoritative synthesis artifacts used for writing.
- To regenerate figures/statistics from the included tables, run:

```bash
python3 scripts/synthesize_evidence.py
```

This regenerates `output/synthesis/S001_*` artifacts in-place.

## Notes
- Full-text PDFs are not included; the tables provide identifiers and extraction anchors for audit.

## Minimal Software Requirements
- Python 3.10+ recommended
- Python packages: `matplotlib` (the synthesis script avoids pandas)
