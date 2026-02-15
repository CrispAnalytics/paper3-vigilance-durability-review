#!/usr/bin/env python3
"""
Paper 3 - Synthesis Builder (S001)

Reads:
- data/evidence_table.csv
- data/risk_of_bias.csv
- data/fulltext_processing_manifest.csv

Writes (under output/synthesis/):
- S001_evidence_map_worklevel.csv
- S001_stats.json
- S001_fig1_study_counts_by_intervention.png
- S001_fig2_vigilance_durability_map.png
- S001_fig3_risk_of_bias_distribution.png
- S001_synthesis_report.md
- S001_gap_map.md
- S001_manuscript_outline.md

Design goals:
- No pandas dependency (CSV module only)
- Auditable, manifest-linked, work-level + outcome-level views
- Figures suitable as internal working drafts (not final journal art)
"""

from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROTOCOL = ROOT / "protocol"
OUT = ROOT / "output" / "synthesis"

EVIDENCE_PATH = DATA / "evidence_table.csv"
ROB_PATH = DATA / "risk_of_bias.csv"
MANIFEST_PATH = DATA / "fulltext_processing_manifest.csv"
LOCKED_Q_PATH = PROTOCOL / "00_locked_question.md"


@dataclass(frozen=True)
class WorkRow:
    short_id: str
    eligibility_tier: str
    publication_year: str
    citation: str
    doi: str
    primary_intervention_category: str
    intervention_categories: str
    primary_setting: str
    settings: str
    n_total: str
    exposure_days_min: str
    exposure_days_max: str
    outcome_domains: str
    has_vigilance_outcome: str
    vigilance_effect_summary: str
    habituation_signal_any: str
    low_baseline_arousal_class: str
    repeated_use_class: str
    habituation_class: str
    rob_overall: str
    rob_tool: str
    abstract_only_flag: str
    notes: str


def _now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _read_csv_dicts(path: Path) -> List[Dict[str, str]]:
    with open(path, newline="") as f:
        r = csv.DictReader(f)
        return list(r)


def _read_locked_question() -> str:
    try:
        txt = LOCKED_Q_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""
    # Keep just the actual question line(s).
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    # Usually last line holds the question.
    return lines[-1] if lines else ""


def _safe_float(x: str) -> Optional[float]:
    try:
        return float(x)
    except Exception:
        return None


def _mode_str(values: Iterable[str]) -> str:
    c = Counter([v for v in values if (v or "").strip()])
    if not c:
        return ""
    # Deterministic tie-breaker: alphabetical.
    top_n = max(c.values())
    tops = sorted([k for k, v in c.items() if v == top_n])
    return tops[0]


def _join_unique(values: Iterable[str]) -> str:
    uniq = sorted({(v or "").strip() for v in values if (v or "").strip()})
    return "; ".join(uniq)


def _vigilance_summary(rows: List[Dict[str, str]]) -> str:
    v_rows = [r for r in rows if (r.get("outcome_domain") or "").strip() == "vigilance"]
    if not v_rows:
        return "no_vigilance"
    dirs = {(r.get("effect_direction") or "").strip() for r in v_rows}
    if "improves" in dirs and "worsens" in dirs:
        return "mixed"
    if "mixed" in dirs:
        return "mixed"
    if "improves" in dirs:
        return "improves"
    if "worsens" in dirs:
        return "worsens"
    if "null" in dirs:
        return "null"
    if "unclear" in dirs:
        return "unclear"
    return "unclear"


def build_work_level_map(
    evidence_rows: List[Dict[str, str]],
    rob_rows: List[Dict[str, str]],
    manifest_rows: List[Dict[str, str]],
) -> Tuple[List[WorkRow], Dict[str, Any]]:
    evidence_by_sid: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for r in evidence_rows:
        sid = (r.get("short_id") or "").strip()
        if not sid:
            continue
        evidence_by_sid[sid].append(r)

    rob_by_sid: Dict[str, Dict[str, str]] = {}
    for r in rob_rows:
        sid = (r.get("short_id") or "").strip()
        if sid:
            rob_by_sid[sid] = r

    manifest_by_sid: Dict[str, Dict[str, str]] = {}
    for r in manifest_rows:
        sid = (r.get("short_id") or "").strip()
        if sid:
            manifest_by_sid[sid] = r

    works: List[WorkRow] = []
    stats: Dict[str, Any] = {}

    for sid in sorted(evidence_by_sid.keys()):
        rows = evidence_by_sid[sid]
        m = manifest_by_sid.get(sid, {})
        rob = rob_by_sid.get(sid, {})

        eligibility_tier = (m.get("eligibility_tier") or "").strip()
        low_cls = (m.get("low_baseline_arousal_class") or "").strip()
        rep_cls = (m.get("repeated_use_class") or "").strip()
        hab_cls = (m.get("habituation_class") or "").strip()
        doi = (m.get("doi") or "").strip()
        notes_m = (m.get("notes") or "").strip()

        year = _mode_str([r.get("publication_year", "") for r in rows]) or (m.get("publication_year") or "").strip()
        citation = _mode_str([r.get("citation", "") for r in rows])
        n_total = _mode_str([r.get("n_total", "") for r in rows])

        settings = _join_unique([r.get("setting", "") for r in rows])
        primary_setting = _mode_str([r.get("setting", "") for r in rows])

        cats = [r.get("intervention_category", "") for r in rows]
        primary_cat = _mode_str(cats)
        cats_join = _join_unique(cats)

        durs = [_safe_float(r.get("exposure_duration_days", "")) for r in rows]
        durs = [d for d in durs if d is not None]
        d_min = str(min(durs)) if durs else ""
        d_max = str(max(durs)) if durs else ""

        domains = _join_unique([r.get("outcome_domain", "") for r in rows])
        has_vigilance = "yes" if any((r.get("outcome_domain") or "").strip() == "vigilance" for r in rows) else "no"
        vig_sum = _vigilance_summary(rows)

        hab_any = "yes" if any((r.get("habituation_or_tolerance_signal") or "").strip().lower() == "yes" for r in rows) else "no"

        rob_overall = (rob.get("rob_overall") or "").strip()
        rob_tool = (rob.get("rob_tool") or "").strip()

        abstract_only = "yes" if ("abstract-only" in (citation.lower() if citation else "") or "abstract-only" in notes_m.lower()) else "no"

        works.append(
            WorkRow(
                short_id=sid,
                eligibility_tier=eligibility_tier,
                publication_year=year,
                citation=citation,
                doi=doi,
                primary_intervention_category=primary_cat,
                intervention_categories=cats_join,
                primary_setting=primary_setting,
                settings=settings,
                n_total=n_total,
                exposure_days_min=d_min,
                exposure_days_max=d_max,
                outcome_domains=domains,
                has_vigilance_outcome=has_vigilance,
                vigilance_effect_summary=vig_sum,
                habituation_signal_any=hab_any,
                low_baseline_arousal_class=low_cls,
                repeated_use_class=rep_cls,
                habituation_class=hab_cls,
                rob_overall=rob_overall,
                rob_tool=rob_tool,
                abstract_only_flag=abstract_only,
                notes=notes_m,
            )
        )

    # Aggregate stats
    tier_counts = Counter(w.eligibility_tier or "(missing)" for w in works)
    cat_counts = Counter(w.primary_intervention_category or "(missing)" for w in works)
    vig_counts = Counter(w.vigilance_effect_summary for w in works if w.has_vigilance_outcome == "yes")
    hab_counts = Counter(w.habituation_signal_any for w in works)
    rob_counts = Counter(w.rob_overall or "(missing)" for w in works)

    stats.update(
        {
            "generated_utc": _now_utc_iso(),
            "locked_question": _read_locked_question(),
            "n_unique_works": len(works),
            "n_outcome_rows": len(evidence_rows),
            "works_by_tier": dict(tier_counts),
            "works_by_primary_intervention_category": dict(cat_counts),
            "works_with_vigilance_outcomes": sum(1 for w in works if w.has_vigilance_outcome == "yes"),
            "vigilance_effect_summary_counts": dict(vig_counts),
            "habituation_signal_any_counts": dict(hab_counts),
            "risk_of_bias_overall_counts": dict(rob_counts),
        }
    )

    return works, stats


def write_work_map_csv(path: Path, works: List[WorkRow]) -> None:
    fieldnames = [f.name for f in WorkRow.__dataclass_fields__.values()]  # type: ignore[attr-defined]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in works:
            w.writerow(row.__dict__)


def write_vigilance_outcomes_csv(path: Path, works: List[WorkRow], evidence_rows: List[Dict[str, str]]) -> None:
    works_by_sid = {w.short_id: w for w in works}

    fieldnames = [
        "short_id",
        "eligibility_tier",
        "citation",
        "publication_year",
        "primary_intervention_category",
        "exposure_duration_days",
        "outcome_measure",
        "outcome_timepoint",
        "effect_direction",
        "effect_size_reported",
        "habituation_or_tolerance_signal",
        "rob_overall",
        "abstract_only_flag",
    ]

    rows_out: List[Dict[str, str]] = []
    for r in evidence_rows:
        if (r.get("outcome_domain") or "").strip() != "vigilance":
            continue
        sid = (r.get("short_id") or "").strip()
        w = works_by_sid.get(sid)
        if not w:
            continue
        rows_out.append(
            {
                "short_id": sid,
                "eligibility_tier": w.eligibility_tier,
                "citation": w.citation,
                "publication_year": w.publication_year,
                "primary_intervention_category": w.primary_intervention_category,
                "exposure_duration_days": (r.get("exposure_duration_days") or "").strip(),
                "outcome_measure": (r.get("outcome_measure") or "").strip(),
                "outcome_timepoint": (r.get("outcome_timepoint") or "").strip(),
                "effect_direction": (r.get("effect_direction") or "").strip(),
                "effect_size_reported": (r.get("effect_size_reported") or "").strip(),
                "habituation_or_tolerance_signal": (r.get("habituation_or_tolerance_signal") or "").strip(),
                "rob_overall": w.rob_overall,
                "abstract_only_flag": w.abstract_only_flag,
            }
        )

    # Stable ordering: core first, then context; then year desc; then short_id.
    def _key(row: Dict[str, str]) -> Tuple[int, int, str]:
        tier = row.get("eligibility_tier") or ""
        tier_rank = 0 if tier == "T1_core" else 1
        try:
            year = int(row.get("publication_year") or "0")
        except Exception:
            year = 0
        return (tier_rank, -year, row.get("short_id") or "")

    rows_out.sort(key=_key)

    with open(path, "w", newline="") as f:
        wtr = csv.DictWriter(f, fieldnames=fieldnames)
        wtr.writeheader()
        for row in rows_out:
            wtr.writerow(row)


def write_json(path: Path, obj: Dict[str, Any]) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")


def build_figures(works: List[WorkRow], evidence_rows: List[Dict[str, str]]) -> None:
    # Local import so the script still runs in environments without mpl.
    import matplotlib.pyplot as plt

    OUT.mkdir(parents=True, exist_ok=True)

    # Fig 1: Unique works by primary intervention category, stacked by tier.
    tiers = ["T1_core", "T2_context"]
    # Collect categories in descending total order.
    cat_totals: Counter[str] = Counter()
    counts: Dict[Tuple[str, str], int] = defaultdict(int)
    for w in works:
        cat = w.primary_intervention_category or "(missing)"
        tier = w.eligibility_tier or "(missing)"
        cat_totals[cat] += 1
        counts[(tier, cat)] += 1
    cats_sorted = [c for c, _ in cat_totals.most_common()]

    fig, ax = plt.subplots(figsize=(10, max(4, 0.35 * len(cats_sorted))))
    left = [0] * len(cats_sorted)
    colors = {"T1_core": "#1f77b4", "T2_context": "#ff7f0e", "(missing)": "#7f7f7f"}
    for tier in tiers + ["(missing)"]:
        vals = [counts.get((tier, cat), 0) for cat in cats_sorted]
        if sum(vals) == 0:
            continue
        ax.barh(cats_sorted, vals, left=left, color=colors.get(tier, "#7f7f7f"), label=tier)
        left = [l + v for l, v in zip(left, vals)]

    ax.set_title("S001: Extracted Works by Primary Intervention Category (Unique Works)")
    ax.set_xlabel("Number of works")
    ax.invert_yaxis()
    ax.legend(loc="lower right", frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "S001_fig1_study_counts_by_intervention.png", dpi=200)
    plt.close(fig)

    # Fig 2: Durability map for vigilance outcomes (work-level).
    # x = max exposure days; y = categorical effect summary.
    y_order = ["worsens", "null", "unclear", "mixed", "improves"]
    y_pos = {k: i for i, k in enumerate(y_order)}

    # Assign a stable color per primary intervention category (top 8 categories).
    cat_palette = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ]
    top_cats = [c for c, _ in cat_totals.most_common(8)]
    cat_color = {c: cat_palette[i] for i, c in enumerate(top_cats)}

    fig, ax = plt.subplots(figsize=(11, 5.8))
    # Collision-aware label offsets for core works (keeps labels readable when points share x/y).
    # Offsets include both left and right placements to avoid stacking when multiple core works
    # share (or nearly share) the same x/y (common near short durations on log-scale).
    label_offsets = [
        (12, 14),
        (12, -14),
        (-12, 14),
        (-12, -14),
        (24, 24),
        (24, -24),
        (-24, 24),
        (-24, -24),
        (36, 0),
        (-36, 0),
        (12, 30),
        (12, -30),
        (-12, 30),
        (-12, -30),
    ]
    label_cluster_counts: Dict[Tuple[int, int], int] = defaultdict(int)
    for w in works:
        if w.has_vigilance_outcome != "yes":
            continue
        x = _safe_float(w.exposure_days_max) or 0.0
        if x <= 0:
            continue
        y = y_pos.get(w.vigilance_effect_summary, y_pos["unclear"])
        cat = w.primary_intervention_category or "(missing)"
        tier = w.eligibility_tier or "(missing)"
        marker = "o" if tier == "T1_core" else "^" if tier == "T2_context" else "s"
        color = cat_color.get(cat, "#444444")
        ax.scatter([x], [y], s=85 if tier == "T1_core" else 65, marker=marker, color=color, alpha=0.85, edgecolors="white", linewidths=0.7)

        if tier == "T1_core":
            # Label core works for quick reading (offset in display coords to reduce overlap).
            key = (int(round(x)), int(round(y)))
            idx = label_cluster_counts[key]
            label_cluster_counts[key] += 1
            dx, dy = label_offsets[idx % len(label_offsets)]
            ha = "left" if dx >= 0 else "right"
            ax.annotate(
                w.short_id,
                xy=(x, y),
                xycoords="data",
                xytext=(dx, dy),
                textcoords="offset points",
                fontsize=6.5,
                ha=ha,
                va="center",
                bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.9),
                arrowprops=dict(arrowstyle="-", color="0.55", lw=0.6, alpha=0.7),
                annotation_clip=False,
            )

    ax.set_xscale("log")
    ax.set_yticks([y_pos[k] for k in y_order])
    ax.set_yticklabels(y_order)
    ax.set_xlabel("Repeated-use duration (days; max per work; log scale)")
    ax.set_title("S001: Vigilance Durability Map (Work-Level Summary)")
    ax.grid(True, axis="x", which="both", linestyle=":", alpha=0.4)

    # Legend: tiers + categories (top cats only)
    handles = []
    labels = []
    for tier, marker in [("T1_core", "o"), ("T2_context", "^")]:
        handles.append(ax.scatter([], [], s=70, marker=marker, color="#999999", edgecolors="white", linewidths=0.7))
        labels.append(tier)
    for cat in top_cats:
        handles.append(ax.scatter([], [], s=70, marker="o", color=cat_color[cat], edgecolors="white", linewidths=0.7))
        labels.append(cat)
    ax.legend(handles, labels, loc="lower right", frameon=False, fontsize=8, ncol=2)

    fig.tight_layout()
    fig.savefig(OUT / "S001_fig2_vigilance_durability_map.png", dpi=200)
    plt.close(fig)

    # Fig 3: Risk of bias distribution by tier (work-level).
    rob_order = ["low", "some_concerns", "high", "unclear", "(missing)"]
    tier_order = ["T1_core", "T2_context", "(missing)"]
    counts_rob: Dict[Tuple[str, str], int] = defaultdict(int)
    for w in works:
        tier = w.eligibility_tier or "(missing)"
        rob = w.rob_overall or "(missing)"
        if rob not in rob_order:
            rob = "(missing)"
        counts_rob[(tier, rob)] += 1

    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    x = list(range(len(rob_order)))
    width = 0.25
    for i, tier in enumerate(tier_order):
        vals = [counts_rob.get((tier, rob), 0) for rob in rob_order]
        ax.bar([xi + (i - 1) * width for xi in x], vals, width=width, label=tier, color=colors.get(tier, "#7f7f7f"), alpha=0.9)

    ax.set_xticks(x)
    ax.set_xticklabels(rob_order)
    ax.set_ylabel("Number of works")
    ax.set_title("S001: Risk of Bias (Overall) Distribution by Tier")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "S001_fig3_risk_of_bias_distribution.png", dpi=200)
    plt.close(fig)


def write_report_md(
    works: List[WorkRow],
    stats: Dict[str, Any],
    evidence_rows: List[Dict[str, str]],
    manifest_rows: List[Dict[str, str]],
) -> None:
    out_path = OUT / "S001_synthesis_report.md"

    # Build quick access lookups
    manifest_by_sid = {r["short_id"]: r for r in manifest_rows if r.get("short_id")}
    works_by_sid = {w.short_id: w for w in works}
    evidence_by_sid: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for r in evidence_rows:
        sid = (r.get("short_id") or "").strip()
        if sid:
            evidence_by_sid[sid].append(r)

    def pick(rows: List[Dict[str, str]], field: str) -> str:
        return _mode_str([(r.get(field) or "").strip() for r in rows])

    # Core list in stable order
    core_ids = sorted([w.short_id for w in works if w.eligibility_tier == "T1_core"])

    # Core vigilance takeaways
    core_vig = []
    for sid in core_ids:
        w = works_by_sid[sid]
        core_vig.append((sid, w.citation, w.primary_intervention_category, w.exposure_days_max, w.vigilance_effect_summary, w.habituation_signal_any))

    # Habituation / tolerance signals
    hab_ids = sorted([w.short_id for w in works if w.habituation_signal_any == "yes"])

    # Primary intervention distribution at work-level
    cat_counts = Counter(w.primary_intervention_category or "(missing)" for w in works)
    cat_top = cat_counts.most_common()

    lines: List[str] = []
    lines.append("# S001 Synthesis Report (Draft Working Notes)")
    lines.append("")
    lines.append(f"- Generated (UTC): `{stats.get('generated_utc','')}`")
    lines.append(f"- Locked question: {stats.get('locked_question','').strip()}")
    lines.append("")

    lines.append("## Evidence Base Snapshot")
    lines.append("")
    lines.append(f"- Unique works in extracted evidence table: **{stats.get('n_unique_works')}**")
    lines.append(f"- Outcome rows (one row per study-outcome): **{stats.get('n_outcome_rows')}**")
    lines.append(f"- Works by tier: `{stats.get('works_by_tier')}`")
    lines.append("")
    lines.append("Primary intervention categories (work-level, by primary category):")
    for cat, n in cat_top:
        lines.append(f"- `{cat}`: {n} works")
    lines.append("")

    lines.append("## Core Evidence (T1_core)")
    lines.append("")
    lines.append("The `T1_core` set is the closest available evidence to the locked question (low-baseline-arousal proxy + repeated-use natural interventions + vigilance/tonic arousal outcomes).")
    lines.append("")
    lines.append("Work-level core summary (vigilance-focused):")
    lines.append("")
    lines.append("| short_id | citation | primary intervention | duration max (days) | vigilance summary | habituation signal |")
    lines.append("|---|---|---:|---:|---|---|")
    for sid, cit, cat, dmax, vsum, hab in core_vig:
        lines.append(f"| `{sid}` | {cit} | `{cat}` | {dmax or ''} | `{vsum}` | `{hab}` |")
    lines.append("")

    lines.append("### What Looks Most Durable (From Core Evidence)")
    lines.append("")
    lines.append("- **Light-based protocols** dominate the core evidence for sustaining objective vigilance improvements over weeks to months (field and home-based designs), but the evidence is constrained by small samples, partial blinding, and subset analyses in some studies.")
    lines.append("- **Sleep timing/sleep extension** protocols show time-dependent benefits (often strongest early in a sequence) and can attenuate or reverse when underlying sleep restriction or circadian stressors persist.")
    lines.append("- **Multi-component shiftwork countermeasure packages** may improve subjective ratings yet show limited objective vigilance gains in small crossover field trials.")
    lines.append("")

    lines.append("### Core Protocol-Level Notes (T1_core)")
    lines.append("")
    lines.append("Goal of this subsection: anchor durability/habituation claims in concrete protocol parameters and objective vigilance endpoints.")
    lines.append("")
    for sid in core_ids:
        w = works_by_sid[sid]
        rows = evidence_by_sid.get(sid, [])
        if not rows:
            continue

        design = pick(rows, "study_design")
        pop = pick(rows, "population_description")
        low_proxy = pick(rows, "low_arousal_proxy_definition")
        protocol = pick(rows, "intervention_protocol")
        comparator = pick(rows, "comparator")
        setting = pick(rows, "setting")
        n_total = pick(rows, "n_total")
        dmax = w.exposure_days_max

        lines.append(f"#### `{sid}` - {w.citation}")
        lines.append(f"- Tier: `{w.eligibility_tier}`")
        lines.append(f"- Population: {pop}")
        lines.append(f"- Low-arousal operationalization/proxy: {low_proxy}")
        lines.append(f"- Design: {design}")
        lines.append(f"- Setting: {setting}")
        lines.append(f"- Sample size (as extracted): {n_total}")
        lines.append(f"- Protocol (as extracted): {protocol}")
        lines.append(f"- Comparator (as extracted): {comparator}")
        lines.append(f"- Repeated-use duration (max per work): {dmax} days")
        lines.append(f"- Work-level vigilance summary: `{w.vigilance_effect_summary}`")
        lines.append(f"- Habituation/tolerance signal present: `{w.habituation_signal_any}`")
        lines.append(f"- Risk of bias (overall): `{w.rob_overall}` ({w.rob_tool})")
        lines.append("")
        # Objective vigilance endpoints
        v_rows = [r for r in rows if (r.get("outcome_domain") or "").strip() == "vigilance"]
        if v_rows:
            lines.append("Vigilance endpoints (as extracted):")
            for r in v_rows:
                meas = (r.get("outcome_measure") or "").strip()
                tp = (r.get("outcome_timepoint") or "").strip()
                direction = (r.get("effect_direction") or "").strip()
                eff = (r.get("effect_size_reported") or "").strip()
                hab = (r.get("habituation_or_tolerance_signal") or "").strip()
                lines.append(f"- `{meas}` ({tp}): `{direction}`; {eff} (habituation_flag={hab})")
            lines.append("")
        else:
            lines.append("- Vigilance endpoints: none extracted.")
            lines.append("")

        # Optional: include sleepiness/fatigue where it materially changes interpretation.
        sf_rows = [r for r in rows if (r.get("outcome_domain") or "").strip() in {"sleepiness", "fatigue"}]
        if sf_rows:
            lines.append("Sleepiness/fatigue endpoints (selected; as extracted):")
            for r in sf_rows:
                dom = (r.get("outcome_domain") or "").strip()
                meas = (r.get("outcome_measure") or "").strip()
                tp = (r.get("outcome_timepoint") or "").strip()
                direction = (r.get("effect_direction") or "").strip()
                eff = (r.get("effect_size_reported") or "").strip()
                lines.append(f"- `{dom}` `{meas}` ({tp}): `{direction}`; {eff}")
            lines.append("")

    lines.append("## Habituation / Tolerance Patterns (Across Core + Context)")
    lines.append("")
    lines.append(f"- Works with explicit `habituation_or_tolerance_signal=yes` in the extracted evidence rows: **{len(hab_ids)}**")
    if hab_ids:
        lines.append("- IDs: " + ", ".join(f"`{sid}`" for sid in hab_ids))
    lines.append("")
    lines.append("Interpretation note: a 'habituation signal' here includes any within-study evidence of attenuation across days/weeks, reversal after repeated use, or explicit tolerance framing; it does not guarantee a formal tolerance test.")
    lines.append("")

    lines.append("## Context Evidence That Constrains Durability Claims (T2_context)")
    lines.append("")
    lines.append("This manuscript uses `T2_context` to support interpretation (mechanism and habituation framing), not to replace `T1_core` for the locked question.")
    lines.append("")

    # Caffeine tolerance/withdrawal cluster
    caffeine_ids = [w.short_id for w in works if w.eligibility_tier == "T2_context" and w.primary_intervention_category == "caffeine"]
    if caffeine_ids:
        lines.append("### Caffeine: Tolerance/Withdrawal and the Durability Problem")
        lines.append("")
        for sid in sorted(caffeine_ids):
            w = works_by_sid[sid]
            rows = evidence_by_sid.get(sid, [])
            design = pick(rows, "study_design")
            pop = pick(rows, "population_description")
            dmax = w.exposure_days_max
            lines.append(f"- `{sid}` {w.citation} (duration max={dmax}d; RoB={w.rob_overall}; {('ABSTRACT-ONLY' if w.abstract_only_flag=='yes' else 'full-text')}): {design}. Population: {pop}.")
            v_rows = [r for r in rows if (r.get('outcome_domain') or '').strip() == 'vigilance']
            for r in v_rows:
                meas = (r.get('outcome_measure') or '').strip()
                tp = (r.get('outcome_timepoint') or '').strip()
                direction = (r.get('effect_direction') or '').strip()
                eff = (r.get('effect_size_reported') or '').strip()
                hab = (r.get('habituation_or_tolerance_signal') or '').strip()
                lines.append(f"- `{meas}` ({tp}): `{direction}`; {eff} (habituation_flag={hab})")
            lines.append("")

        lines.append("Interpretive synthesis (caffeine): repeated-use durability is often limited by tolerance and/or withdrawal dynamics; acute performance benefits can persist, but the net day-to-day state depends on baseline caffeine exposure and abstinence/withdrawal context.")
        lines.append("")

    # Light + shiftwork adaptation cluster (include abstract-only explicitly)
    light_ctx_ids = [w.short_id for w in works if w.eligibility_tier == "T2_context" and w.primary_intervention_category == "light"]
    if light_ctx_ids:
        lines.append("### Light: Time-Dependent Effects and Shiftwork Adaptation")
        lines.append("")
        # Prioritize items with abstract-only or habituation flags for discussion
        def _prio(sid: str) -> Tuple[int, int, str]:
            w = works_by_sid[sid]
            a = 0 if w.abstract_only_flag == "yes" else 1
            h = 0 if w.habituation_signal_any == "yes" else 1
            try:
                y = -int(w.publication_year or "0")
            except Exception:
                y = 0
            return (a, h, y, sid)

        for sid in sorted(light_ctx_ids, key=_prio):
            w = works_by_sid[sid]
            rows = evidence_by_sid.get(sid, [])
            if not rows:
                continue
            # Keep to the most relevant endpoints for the locked question framing.
            v_rows = [r for r in rows if (r.get("outcome_domain") or "").strip() == "vigilance"]
            s_rows = [r for r in rows if (r.get("outcome_domain") or "").strip() == "sleepiness"]
            dmax = w.exposure_days_max
            lines.append(f"- `{sid}` {w.citation} (duration max={dmax}d; abstract_only={w.abstract_only_flag}; RoB={w.rob_overall})")
            if w.abstract_only_flag == "yes":
                lines.append("- Note: extracted from abstract only due to paywalled full text; treat as context with reduced confidence.")
            for r in v_rows[:3]:
                lines.append(f"- Vigilance `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            for r in s_rows[:2]:
                lines.append(f"- Sleepiness `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            lines.append("")

        lines.append("Interpretive synthesis (light): effects are often time-locked (circadian phase, time awake, and exposure timing), so durability should be operationalized as stability across repeated shifts/days rather than endpoint-only comparisons.")
        lines.append("")

    lines.append("## Risk of Bias (Work-Level)")
    lines.append("")
    lines.append("The evidence base includes many field studies and uncontrolled designs, which are valuable for ecological validity but limit causal inference about tonic arousal 'set-point' engineering.")
    lines.append("")
    lines.append("Key constraints observed in the extracted set:")
    lines.append("- Small samples in many crossover studies, with risk of period/carryover effects and multiple outcomes.")
    lines.append("- Limited blinding feasibility for light and sleep scheduling interventions.")
    lines.append("- Frequent reliance on subjective measures for sleepiness/fatigue, with fewer objective tonic arousal markers (e.g., pupil baseline, continuous autonomics).")
    lines.append("- A substantial fraction of evidence is outside the core target population and is used for context/mechanism rather than direct answer to the locked question.")
    lines.append("")

    lines.append("## Immediate Implications for the Manuscript (Elite-Journal Positioning)")
    lines.append("")
    lines.append("The strongest publishable contribution from this corpus is likely a structured synthesis that:")
    lines.append("- Treats **light manipulation** and **sleep timing** as the two dominant natural lever classes with repeated-use evidence relevant to low-arousal proxies (shift workers, fatigue populations, chronic short sleepers).")
    lines.append("- Makes durability/habituation the organizing axis (not simply 'does it work acutely?').")
    lines.append("- Explicitly separates **core evidence** (T1_core) from **context evidence** (T2_context) and avoids overstating generalizability to trait low-arousal individuals.")
    lines.append("")

    lines.append("## Files Generated (S001)")
    lines.append("")
    lines.append("- Work-level evidence map: `output/synthesis/S001_evidence_map_worklevel.csv`")
    lines.append("- Vigilance-only outcomes table: `output/synthesis/S001_vigilance_outcomes.csv`")
    lines.append("- Figures:")
    lines.append("  - `output/synthesis/S001_fig1_study_counts_by_intervention.png`")
    lines.append("  - `output/synthesis/S001_fig2_vigilance_durability_map.png`")
    lines.append("  - `output/synthesis/S001_fig3_risk_of_bias_distribution.png`")
    lines.append("- Gap map (draft): `output/synthesis/S001_gap_map.md`")
    lines.append("- Manuscript outline (draft): `output/synthesis/S001_manuscript_outline.md`")
    lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_gap_map_md(works: List[WorkRow], stats: Dict[str, Any]) -> None:
    out_path = OUT / "S001_gap_map.md"
    lines: List[str] = []
    lines.append("# S001 Gap Map (Draft)")
    lines.append("")
    lines.append(f"- Generated (UTC): `{stats.get('generated_utc','')}`")
    lines.append(f"- Locked question: {stats.get('locked_question','').strip()}")
    lines.append("")
    lines.append("## Core Gaps (What Prevents Strong Claims About Sustained Tonic Arousal Engineering)")
    lines.append("")
    lines.append("Population gaps:")
    lines.append("- Trait-defined 'low baseline arousal' is rarely operationalized directly; most core-relevant work uses **structural or symptomatic proxies** (shift work disorder, chronic short sleep, post-injury fatigue).")
    lines.append("- Limited stratified analyses testing whether low-arousal subgroups benefit more (or show different habituation) than higher-arousal subgroups.")
    lines.append("")
    lines.append("Measurement gaps:")
    lines.append("- Objective 'tonic arousal' markers (baseline pupil size/variability, continuous autonomic tone, EEG vigilance indices) are uncommon in field protocols; PVT is common but still a downstream proxy.")
    lines.append("- Few studies align physiology + performance to support a mechanistic claim that baseline arousal is shifted (vs reduced sleep pressure, reduced circadian misalignment, or acute stimulation).")
    lines.append("")
    lines.append("Durability/habituation gaps:")
    lines.append("- Many repeated-use protocols report endpoints but do not test **within-protocol attenuation** (day 1 vs day 7 vs day 30) with enough resolution to call habituation vs stabilization.")
    lines.append("- Where attenuation appears, it is often confounded with adaptation to the schedule or re-emergence of sleep restriction rather than a clean tolerance model.")
    lines.append("")
    lines.append("Intervention gaps (natural, scalable, repeated-use):")
    lines.append("- Underrepresented in the extracted evidence base: structured **breathing**, **cold exposure**, and **exercise** protocols explicitly designed to shift daytime arousal over repeated use in low-arousal adults with objective vigilance measures.")
    lines.append("- Few studies test combined protocols as an optimization problem (e.g., light + sleep timing + caffeine timing) with factorial designs.")
    lines.append("")
    lines.append("Design gaps:")
    lines.append("- Blinding is often infeasible; strong designs therefore need robust counterbalancing, objective endpoints, and careful control of expectancy and carryover.")
    lines.append("- Many studies are underpowered or have subset analyses for PVT; publication-quality conclusions require larger samples and preregistered primary outcomes.")
    lines.append("")
    lines.append("## Highest-Leverage Next-Step Analyses (Secondary Research Only)")
    lines.append("")
    lines.append("1. Build a durability-first taxonomy: classify each protocol by expected mechanism (sleep pressure reduction, circadian phase management, sensory stimulation, autonomic modulation) and map which mechanisms show evidence of attenuation.")
    lines.append("2. Extract and compare protocol 'dose' parameters (light intensity/target, timing, adherence) and tie them to effect direction and durability windows.")
    lines.append("3. Formalize a 'habituation' coding scheme usable across heterogeneous designs, then re-label the evidence in a transparent audit trail (can be done without new experiments).")
    lines.append("")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manuscript_outline_md(stats: Dict[str, Any]) -> None:
    out_path = OUT / "S001_manuscript_outline.md"
    q = (stats.get("locked_question") or "").strip()
    lines: List[str] = []
    lines.append("# S001 Manuscript Outline (Draft)")
    lines.append("")
    lines.append(f"- Generated (UTC): `{stats.get('generated_utc','')}`")
    lines.append("")
    lines.append("## Working Title Candidates")
    lines.append("- Durability of Natural Arousal-Enhancing Protocols in Low-Arousal Adults: A Systematic Review Focused on Habituation and Sustained Vigilance")
    lines.append("- Engineering Daytime Tonic Arousal Without Drugs: What Repeated-Use Evidence Supports and Where It Breaks")
    lines.append("- Repeated-Use Natural Interventions for Low Arousal: Evidence Map and Habituation-Aware Synthesis")
    lines.append("")
    lines.append("## Research Question (Locked)")
    lines.append(f"- {q}")
    lines.append("")
    lines.append("## Abstract (Structured)")
    lines.append("- Background: Why tonic arousal and sustained vigilance matter; why durability is understudied.")
    lines.append("- Objective: Evaluate repeated-use natural intervention protocols in low-arousal adults, emphasizing sustained effects and habituation.")
    lines.append("- Methods: PRISMA; OpenAlex-driven discovery + chaining; full-text retrieval constraints; manifest-driven screening; evidence extraction schema; RoB approach.")
    lines.append("- Results: Number of core vs context studies; dominant intervention classes; durability patterns; habituation signals; RoB summary.")
    lines.append("- Conclusions: What appears durable vs transient; key gaps; recommendations for next trials.")
    lines.append("")
    lines.append("## Introduction (Key Moves)")
    lines.append("- Define tonic arousal vs phasic arousal; why vigilance is a practical endpoint (PVT).")
    lines.append("- Argue that 'does it work today' is not the relevant question; 'does it keep working with repeated use' is.")
    lines.append("- Motivate why non-pharmacological approaches matter (safety, scalability, occupational relevance).")
    lines.append("")
    lines.append("## Methods")
    lines.append("- Protocol + PRISMA: `protocol/01_prisma_protocol.md`")
    lines.append("- Search strategy log: `protocol/02_exact_search_strategy_log.md`")
    lines.append("- Retrieval status + corpus reproducibility: `protocol/04_corpus_status_and_reproducibility.md`")
    lines.append("- Full-text screening codebook: `protocol/06_fulltext_screening_codebook.md`")
    lines.append("- Evidence schema: `protocol/07_evidence_extraction_schema.md`")
    lines.append("- Cutoff/stopping rule for context extraction: `workflow/extraction/10_T2_context_cutoff_and_stopping_rule.md`")
    lines.append("")
    lines.append("## Results (Suggested Structure)")
    lines.append("- Study characteristics (core vs context; populations; settings; durations).")
    lines.append("- Intervention classes:")
    lines.append("  - Light manipulation (timing, spectral composition, intensity; workplace vs home).")
    lines.append("  - Sleep timing / sleep extension (shift-work schedules; weekend extension).")
    lines.append("  - Melatonin (as natural hormone; limited repeated-use data with objective vigilance).")
    lines.append("  - Multicomponent packages (education + countermeasures).")
    lines.append("  - Context-only: caffeine tolerance/withdrawal framing; confined environment; mechanistic physiology.")
    lines.append("- Durability/habituation mapping (primary contribution): which protocols maintain vs attenuate and on what timescale.")
    lines.append("- Risk of bias summary.")
    lines.append("")
    lines.append("## Discussion (Suggested Structure)")
    lines.append("- Summary of durable vs transient effects, interpreted mechanistically (sleep pressure vs circadian alignment vs sensory stimulation).")
    lines.append("- Why habituation signals appear: adaptation, ceiling effects, diminishing marginal returns, adherence decay.")
    lines.append("- Practical implications (occupational health framing) without prescribing clinical guidance.")
    lines.append("- Limitations (proxy populations; heterogeneity; unblinded designs; abstract-only context item).")
    lines.append("- Research agenda: a next-generation repeated-use trial architecture (counterbalanced, objective endpoints, physiology + performance, preregistered).")
    lines.append("")
    lines.append("## Figures/Tables (From S001)")
    lines.append("- Fig 1: `output/synthesis/S001_fig1_study_counts_by_intervention.png`")
    lines.append("- Fig 2: `output/synthesis/S001_fig2_vigilance_durability_map.png`")
    lines.append("- Fig 3: `output/synthesis/S001_fig3_risk_of_bias_distribution.png`")
    lines.append("- Table: `output/synthesis/S001_evidence_map_worklevel.csv` (convert to manuscript Table 1).")
    lines.append("")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_figure_captions_md(stats: Dict[str, Any]) -> None:
    out_path = OUT / "S001_figure_captions.md"
    lines: List[str] = []
    lines.append("# S001 Figure Captions (Draft)")
    lines.append("")
    lines.append(f"- Generated (UTC): `{stats.get('generated_utc','')}`")
    lines.append("")
    lines.append("## Fig 1")
    lines.append("Extracted works by primary intervention category, stratified by evidence tier (`T1_core` vs `T2_context`). Counts are unique works (not outcome rows).")
    lines.append("")
    lines.append("## Fig 2")
    lines.append("Vigilance durability map (work-level): x-axis is maximum repeated-use duration (days; log scale). y-axis is the work-level direction summary for vigilance endpoints. Points are colored by primary intervention category and shaped by tier; `T1_core` works are labeled by short_id. This plot is intended as an evidence map, not a meta-analysis.")
    lines.append("")
    lines.append("## Fig 3")
    lines.append("Risk of bias (overall) distribution by tier, using the per-work RoB summary recorded in `data/risk_of_bias.csv`. Missing/unclear ratings reflect incomplete reporting and/or abstract-only extraction for paywalled full texts.")
    lines.append("")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_results_and_discussion_drafts(
    works: List[WorkRow],
    stats: Dict[str, Any],
    evidence_rows: List[Dict[str, str]],
) -> None:
    works_by_sid = {w.short_id: w for w in works}
    evidence_by_sid: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for r in evidence_rows:
        sid = (r.get("short_id") or "").strip()
        if sid:
            evidence_by_sid[sid].append(r)

    core_ids = sorted([w.short_id for w in works if w.eligibility_tier == "T1_core"])
    ctx_ids = sorted([w.short_id for w in works if w.eligibility_tier == "T2_context"])

    # Work-level counts for quick statements
    core_cats = Counter(works_by_sid[sid].primary_intervention_category for sid in core_ids)
    core_durs = [_safe_float(works_by_sid[sid].exposure_days_max) for sid in core_ids]
    core_durs = [d for d in core_durs if d is not None]
    core_dur_min = min(core_durs) if core_durs else None
    core_dur_max = max(core_durs) if core_durs else None

    # RESULTS DRAFT
    r_path = OUT / "S001_results_draft.md"
    r_lines: List[str] = []
    r_lines.append("# S001 Results Draft (Working Text)")
    r_lines.append("")
    r_lines.append(f"- Generated (UTC): `{stats.get('generated_utc','')}`")
    r_lines.append("")
    r_lines.append("## Study Characteristics (Extracted Set)")
    r_lines.append("")
    r_lines.append(f"We extracted structured outcomes for {stats.get('n_unique_works')} works ({stats.get('works_by_tier',{})}). The core evidence set (`T1_core`) comprises {len(core_ids)} works and primarily tests circadian/light and sleep-timing interventions in low-arousal proxy populations (shift work disorder, rotating shift workers, chronic short sleepers, and post-injury fatigue).")
    if core_dur_min is not None and core_dur_max is not None:
        r_lines.append(f"Across `T1_core`, repeated-use duration ranged from {int(core_dur_min)} to {int(core_dur_max)} days (max per work).")
    r_lines.append("")
    r_lines.append("Core works by primary intervention category:")
    for cat, n in core_cats.most_common():
        r_lines.append(f"- `{cat}`: {n} works")
    r_lines.append("")

    r_lines.append("## Core Findings by Intervention Class (T1_core)")
    r_lines.append("")

    # Light (core)
    light_core = [sid for sid in core_ids if works_by_sid[sid].primary_intervention_category == "light"]
    if light_core:
        r_lines.append("### Light Manipulation")
        r_lines.append("")
        for sid in light_core:
            w = works_by_sid[sid]
            rows = evidence_by_sid.get(sid, [])
            pop = _mode_str([(r.get("population_description") or "").strip() for r in rows])
            dmax = w.exposure_days_max
            r_lines.append(f"- `{sid}` {w.citation} (duration max={dmax}d; RoB={w.rob_overall}): {pop}.")
            for r in [rr for rr in rows if (rr.get("outcome_domain") or "").strip() == "vigilance"]:
                r_lines.append(f"- Vigilance `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            r_lines.append("")
        r_lines.append("Across these core light studies, objective vigilance outcomes tended to improve at the endpoint of repeated-use protocols (weeks to months), but causal strength is limited by small sample sizes, partial blinding feasibility, and outcome subsets in some designs.")
        r_lines.append("")

    # Sleep timing (core)
    sleep_core = [sid for sid in core_ids if works_by_sid[sid].primary_intervention_category == "sleep_timing"]
    if sleep_core:
        r_lines.append("### Sleep Timing / Sleep Extension")
        r_lines.append("")
        for sid in sleep_core:
            w = works_by_sid[sid]
            rows = evidence_by_sid.get(sid, [])
            pop = _mode_str([(r.get("population_description") or "").strip() for r in rows])
            dmax = w.exposure_days_max
            r_lines.append(f"- `{sid}` {w.citation} (duration max={dmax}d; RoB={w.rob_overall}; habituation_signal={w.habituation_signal_any}): {pop}.")
            for r in [rr for rr in rows if (rr.get("outcome_domain") or "").strip() == "vigilance"]:
                r_lines.append(f"- Vigilance `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            for r in [rr for rr in rows if (rr.get("outcome_domain") or "").strip() == "sleepiness"]:
                r_lines.append(f"- Sleepiness `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            r_lines.append("")
        r_lines.append("Across core sleep-timing/sleep-extension studies, benefits were often time-dependent (e.g., strongest on early shifts or early week) and could attenuate or reverse later, consistent with limited durability when the underlying schedule constraint persists.")
        r_lines.append("")

    # Melatonin (core)
    mel_core = [sid for sid in core_ids if works_by_sid[sid].primary_intervention_category == "melatonin"]
    if mel_core:
        r_lines.append("### Melatonin (Natural Hormone)")
        r_lines.append("")
        for sid in mel_core:
            w = works_by_sid[sid]
            rows = evidence_by_sid.get(sid, [])
            pop = _mode_str([(r.get("population_description") or "").strip() for r in rows])
            dmax = w.exposure_days_max
            r_lines.append(f"- `{sid}` {w.citation} (duration max={dmax}d; RoB={w.rob_overall}): {pop}.")
            for r in [rr for rr in rows if (rr.get("outcome_domain") or "").strip() == "vigilance"]:
                r_lines.append(f"- Vigilance `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            for r in [rr for rr in rows if (rr.get("outcome_domain") or "").strip() == "sleepiness"]:
                r_lines.append(f"- Sleepiness `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            r_lines.append("")
        r_lines.append("In the extracted core melatonin evidence, subjective sleepiness and sleep outcomes improved modestly, while objective reaction-time measures showed limited consistent benefit in field conditions.")
        r_lines.append("")

    # Multicomponent (core)
    multi_core = [sid for sid in core_ids if works_by_sid[sid].primary_intervention_category == "multi"]
    if multi_core:
        r_lines.append("### Multicomponent Countermeasure Packages")
        r_lines.append("")
        for sid in multi_core:
            w = works_by_sid[sid]
            rows = evidence_by_sid.get(sid, [])
            pop = _mode_str([(r.get("population_description") or "").strip() for r in rows])
            dmax = w.exposure_days_max
            r_lines.append(f"- `{sid}` {w.citation} (duration max={dmax}d; RoB={w.rob_overall}): {pop}.")
            for r in [rr for rr in rows if (rr.get("outcome_domain") or "").strip() == "vigilance"]:
                r_lines.append(f"- Vigilance `{r.get('outcome_measure','').strip()}` ({r.get('outcome_timepoint','').strip()}): `{r.get('effect_direction','').strip()}`; {r.get('effect_size_reported','').strip()}")
            r_lines.append("")
        r_lines.append("In the extracted multicomponent core evidence, objective vigilance changes were limited, despite some subjective improvements reported in the underlying papers.")
        r_lines.append("")

    r_lines.append("## Context Evidence for Habituation/Tolerance Framing (T2_context)")
    r_lines.append("")
    r_lines.append("Context studies were extracted under a pre-specified cutoff emphasizing repeated-use duration and/or explicit habituation testing. These studies inform interpretation of durability mechanisms (e.g., stimulant tolerance/withdrawal; time-of-day and circadian interactions in light).")
    r_lines.append("")
    r_lines.append("See `output/synthesis/S001_vigilance_outcomes.csv` for the vigilance-only endpoint ledger used for this synthesis.")
    r_lines.append("")

    r_path.write_text("\n".join(r_lines) + "\n", encoding="utf-8")

    # DISCUSSION DRAFT
    d_path = OUT / "S001_discussion_draft.md"
    d_lines: List[str] = []
    d_lines.append("# S001 Discussion Draft (Working Text)")
    d_lines.append("")
    d_lines.append(f"- Generated (UTC): `{stats.get('generated_utc','')}`")
    d_lines.append("")
    d_lines.append("## Summary of What the Extracted Evidence Suggests")
    d_lines.append("")
    d_lines.append("Across the core evidence base, repeated-use protocols that act via circadian and sleep regulation (light manipulation and sleep timing) show the most consistent objective vigilance improvements in low-arousal proxy populations. However, the evidence is heterogeneous and often limited by feasibility constraints (blinding, adherence, small samples) typical of real-world sleep/circadian interventions.")
    d_lines.append("")
    d_lines.append("A critical interpretive distinction for this manuscript is whether an intervention plausibly shifts a 'tonic arousal set-point' versus reducing sleep pressure or circadian misalignment. In practice, most natural protocols likely improve daytime vigilance by changing upstream sleep/circadian state, not by directly elevating tonic arousal in a stimulant-like fashion.")
    d_lines.append("")
    d_lines.append("## Habituation and Durability: How to Interpret Signals")
    d_lines.append("")
    d_lines.append("Habituation signals in the extracted set most often appear as time-dependent effects across repeated exposures (e.g., strongest on early shifts, attenuation later) or reversal when the underlying constraint returns (e.g., weekend extension followed by recurrent weekday restriction). These patterns are consistent with state regulation rather than classical pharmacologic tolerance. By contrast, the caffeine context literature more directly illustrates tolerance/withdrawal dynamics that can compress net benefits over time.")
    d_lines.append("")
    d_lines.append("## Practical Implications (Research, Not Clinical Guidance)")
    d_lines.append("")
    d_lines.append("For repeated-use performance optimization in low-arousal proxies (shift workers, chronic short sleepers, fatigue populations), the most defensible evidence-driven framing is: (i) manipulate light and sleep timing to reduce misalignment and sleepiness, (ii) expect time-of-day and schedule interactions, and (iii) explicitly measure durability (day-by-day) rather than endpoint-only effects.")
    d_lines.append("")
    d_lines.append("## Research Agenda Enabled by Secondary Research")
    d_lines.append("")
    d_lines.append("This corpus supports a publishable durability-first taxonomy and a harmonized habituation coding framework. The highest-leverage next steps that do not require new experiments are: (1) protocol dose harmonization (timing, intensity, adherence), (2) explicit mapping of durability windows (day 1 vs day 7 vs day 30), and (3) separating proxy low-arousal populations from trait low-arousal claims.")
    d_lines.append("")
    d_lines.append("## Limitations of This Evidence Base")
    d_lines.append("")
    d_lines.append("- Proxy populations dominate; trait low baseline arousal is rarely defined explicitly.")
    d_lines.append("- Few studies jointly measure physiology + performance strongly enough to claim a tonic baseline shift.")
    d_lines.append("- Abstract-only extraction exists for at least one context item due to paywalled full text; these items are treated as context with reduced confidence.")
    d_lines.append("")

    d_path.write_text("\n".join(d_lines) + "\n", encoding="utf-8")


def write_manuscript_draft_md(stats: Dict[str, Any]) -> None:
    """
    Assemble a single manuscript draft that pulls Methods text from protocol/PRISMA docs
    and embeds the current Results + Discussion drafts (with heading levels adjusted).
    """
    out_path = OUT / "S001_manuscript_draft.md"

    def read_text(path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def md_body_demote(path: Path, demote_by: int = 1) -> str:
        lines = read_text(path).splitlines()
        # Drop the top metadata block; keep from first "##" heading onward.
        start = 0
        for i, ln in enumerate(lines):
            if ln.startswith("## "):
                start = i
                break
        body = lines[start:]
        out_lines: List[str] = []
        for ln in body:
            if ln.startswith("#"):
                n = len(ln) - len(ln.lstrip("#"))
                n2 = min(6, n + demote_by)
                out_lines.append("#" * n2 + ln[n:])
            else:
                out_lines.append(ln)
        return "\n".join(out_lines).strip() + "\n"

    # Inputs
    protocol_prisma = ROOT / "protocol" / "01_prisma_protocol.md"
    protocol_search_log = ROOT / "protocol" / "02_exact_search_strategy_log.md"
    protocol_prisma_flow = ROOT / "protocol" / "03_prisma_flow_and_reporting_text.md"
    protocol_corpus = ROOT / "protocol" / "04_corpus_status_and_reproducibility.md"
    codebook = ROOT / "protocol" / "06_fulltext_screening_codebook.md"
    extraction_schema = ROOT / "protocol" / "07_evidence_extraction_schema.md"
    t2_cutoff = ROOT / "workflow" / "extraction" / "10_T2_context_cutoff_and_stopping_rule.md"

    results_draft = OUT / "S001_results_draft.md"
    discussion_draft = OUT / "S001_discussion_draft.md"

    # Pull the manuscript-ready methods/search text block from the PRISMA flow doc.
    # We keep it concise and point to the full search log as supplement.
    prisma_flow_txt = read_text(protocol_prisma_flow)

    lines: List[str] = []
    lines.append("# Manuscript Draft (S001)")
    lines.append("")
    lines.append("## Working Title")
    lines.append("Durability of Natural Arousal-Enhancing Protocols in Low-Arousal Adults: A Systematic Review Focused on Habituation and Sustained Vigilance")
    lines.append("")
    lines.append("## Research Question (Locked)")
    lines.append(stats.get("locked_question", "").strip())
    lines.append("")

    lines.append("## Methods (Draft; PRISMA-Oriented)")
    lines.append("")
    lines.append("### Protocol and Reporting Framework")
    lines.append("")
    lines.append("We followed a PRISMA-oriented protocol for evidence identification, retrieval, screening, and extraction. The locked question and PICOS eligibility criteria are specified in `protocol/01_prisma_protocol.md`.")
    lines.append("")
    lines.append("### Information Sources and Search Strategy")
    lines.append("")
    # Use the explicit manuscript-ready text block already present.
    # Keep verbatim to minimize drift from the logged protocol, but avoid duplicating entire logs.
    lines.append("Search and chaining (manuscript-ready text):")
    lines.append("")
    # Extract the two paragraphs from the PRISMA flow doc by simple markers.
    def extract_between(text: str, start: str, end: str) -> str:
        si = text.find(start)
        if si < 0:
            return ""
        si2 = si + len(start)
        ei = text.find(end, si2)
        if ei < 0:
            ei = len(text)
        return text[si2:ei].strip()

    meth_search = extract_between(
        prisma_flow_txt,
        "## Manuscript-Ready Methods Text (Search)",
        "## Manuscript-Ready Methods Text (Screening + Chaining)",
    )
    meth_chain = extract_between(
        prisma_flow_txt,
        "## Manuscript-Ready Methods Text (Screening + Chaining)",
        "## Manuscript-Ready Results Text (Flow)",
    )
    if meth_search:
        lines.append(meth_search)
        lines.append("")
    if meth_chain:
        lines.append(meth_chain)
        lines.append("")

    lines.append("The exact seed queries and keyword dictionaries used are logged in `protocol/02_exact_search_strategy_log.md` and the full API trace is logged in `logs/openalex_api_log.csv`.")
    lines.append("")

    lines.append("### Eligibility Criteria")
    lines.append("")
    lines.append("Eligibility criteria were defined a priori using a PICOS structure (adults, natural/non-pharmacologic interventions, repeated-use relevance, and vigilance/tonic arousal outcomes). Operational definitions for 'low baseline arousal' and 'repeated-use durability' were applied during full-text screening (see `protocol/06_fulltext_screening_codebook.md`).")
    lines.append("")

    lines.append("### Full-Text Retrieval and Corpus Construction")
    lines.append("")
    lines.append("Full-text retrieval was attempted for all records included at the title/abstract stage. Automated retrieval used OpenAlex locations and a series of resolver retry passes; the final retrieval status is reported in `protocol/04_corpus_status_and_reproducibility.md` with audit logs in `logs/`.")
    lines.append("")
    lines.append("Post-retrieval QA included mismatch detection; mismatched PDFs were moved to `_trash/mismatched_pdfs/` and logged in `logs/pdf_download_log.csv`. In rare cases, a mismatched file was replaced with a relevant artifact (e.g., a supplement); these were flagged and treated as context-only evidence when the main article remained paywalled.")
    lines.append("")

    lines.append("### Study Selection and Tiering for Synthesis")
    lines.append("")
    lines.append("Full-text screening and evidence extraction were tracked in a single manifest (`data/fulltext_processing_manifest.csv`). Records were tiered for synthesis into `T1_core` (directly answers the locked question) and `T2_context` (mechanism/gap-map support). To prevent scope creep, `T2_context` extraction used a pre-specified cutoff and stopping rule (see `workflow/extraction/10_T2_context_cutoff_and_stopping_rule.md`).")
    lines.append("")

    lines.append("### Data Extraction and Risk of Bias")
    lines.append("")
    lines.append("Structured extraction was performed into an outcome-level evidence table (`data/evidence_table.csv`) with a corresponding per-work risk-of-bias log (`data/risk_of_bias.csv`). The extraction schema and minimum required fields are specified in `protocol/07_evidence_extraction_schema.md`.")
    lines.append("")

    lines.append("### Synthesis Approach")
    lines.append("")
    lines.append("Given heterogeneous designs and endpoints, we performed a narrative synthesis oriented around repeated-use durability and habituation/tolerance signals, supplemented by evidence mapping visualizations (see `output/synthesis/`). Core conclusions are based on `T1_core` evidence; `T2_context` is used to constrain interpretation and map gaps.")
    lines.append("")

    lines.append("## Results (Draft)")
    lines.append("")
    # Add PRISMA flow text for completeness
    lines.append("### Study Identification and Retrieval (PRISMA Flow)")
    lines.append("")
    flow_results = extract_between(
        prisma_flow_txt,
        "## PRISMA 2020 Flow Inputs (from this run)",
        "## Manuscript-Ready Methods Text (Search)",
    )
    # Keep the bullet block as-is (it is already manuscript-ready).
    if flow_results:
        lines.append(flow_results)
        lines.append("")

    lines.append("### Extracted Evidence Base")
    lines.append("")
    lines.append(f"Across the extracted evidence set, we mapped {stats.get('n_unique_works')} works and {stats.get('n_outcome_rows')} outcome rows (see `output/synthesis/S001_evidence_map_worklevel.csv` and `output/synthesis/S001_vigilance_outcomes.csv`).")
    lines.append("")

    # Embed the results draft content, demoted by one level.
    lines.append(md_body_demote(results_draft, demote_by=1))

    lines.append("## Discussion (Draft)")
    lines.append("")
    lines.append(md_body_demote(discussion_draft, demote_by=1))

    lines.append("## Figures and Tables (Current Draft Set)")
    lines.append("")
    lines.append("- Fig 1: `output/synthesis/S001_fig1_study_counts_by_intervention.png`")
    lines.append("- Fig 2: `output/synthesis/S001_fig2_vigilance_durability_map.png`")
    lines.append("- Fig 3: `output/synthesis/S001_fig3_risk_of_bias_distribution.png`")
    lines.append("- Table (work-level evidence map): `output/synthesis/S001_evidence_map_worklevel.csv`")
    lines.append("- Table (vigilance endpoints): `output/synthesis/S001_vigilance_outcomes.csv`")
    lines.append("")

    lines.append("## Supplementary Material (Audit Trail)")
    lines.append("")
    lines.append("- Exact search protocol log: `protocol/02_exact_search_strategy_log.md`")
    lines.append("- PRISMA flow text: `protocol/03_prisma_flow_and_reporting_text.md`")
    lines.append("- Corpus status and reproducibility: `protocol/04_corpus_status_and_reproducibility.md`")
    lines.append("- Full-text screening codebook: `protocol/06_fulltext_screening_codebook.md`")
    lines.append("- Evidence extraction schema: `protocol/07_evidence_extraction_schema.md`")
    lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    evidence_rows = _read_csv_dicts(EVIDENCE_PATH)
    rob_rows = _read_csv_dicts(ROB_PATH)
    manifest_rows = _read_csv_dicts(MANIFEST_PATH)

    works, stats = build_work_level_map(evidence_rows, rob_rows, manifest_rows)

    write_work_map_csv(OUT / "S001_evidence_map_worklevel.csv", works)
    write_vigilance_outcomes_csv(OUT / "S001_vigilance_outcomes.csv", works, evidence_rows)
    write_json(OUT / "S001_stats.json", stats)

    build_figures(works, evidence_rows)
    write_gap_map_md(works, stats)
    write_manuscript_outline_md(stats)
    write_figure_captions_md(stats)
    write_results_and_discussion_drafts(works, stats, evidence_rows)
    write_manuscript_draft_md(stats)
    write_report_md(works, stats, evidence_rows, manifest_rows)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
