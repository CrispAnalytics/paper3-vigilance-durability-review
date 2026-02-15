# Zenodo Archiving (Publisher-Friendly DOI)

Most journals expect a stable, citable archive (DOI) for data/materials. The recommended path is to use the Zenodo GitHub integration, which automatically archives GitHub Releases and mints a DOI.

## One-time setup
1. Create (or sign into) a Zenodo account.
2. In Zenodo, go to **Account** -> **GitHub** (or the GitHub integration page).
3. Authorize Zenodo to access your GitHub account/org.
4. Enable the repository: `CrispAnalytics/paper3-vigilance-durability-review`.

## Create an archived Zenodo record (DOI)
Zenodo mints DOIs for **GitHub Releases** (not just tags).

1. Create a GitHub Release for tag `v1.0.0` (already tagged in git).
2. Zenodo will detect the Release and create a deposition (this can take a few minutes).
3. In Zenodo, open the new record and verify metadata (title, description, authors).
4. Publish the record. Zenodo will mint:
   - a version DOI (for `v1.0.0`)
   - a concept DOI (points to the latest version)

## Metadata
- `.zenodo.json` provides default metadata for the Zenodo record (title, description, license, keywords).
- `CITATION.cff` provides citation metadata for GitHub and downstream tools.

## After the DOI exists
Update the manuscript Data Availability section to reference the Zenodo DOI (preferred) and optionally include the GitHub URL as a convenience mirror.

