# S001 Synthesis Report (Draft Working Notes)

- Generated (UTC): `2026-02-15T14:54:09.182281Z`
- Locked question: In low-baseline-arousal adults, which natural intervention protocols sustain elevated daytime tonic arousal and cognitive performance over repeated daily use, and which show habituation?

## Evidence Base Snapshot

- Unique works in extracted evidence table: **30**
- Outcome rows (one row per study-outcome): **101**
- Works by tier: `{'T2_context': 22, 'T1_core': 8}`

Primary intervention categories (work-level, by primary category):
- `light`: 10 works
- `sleep_timing`: 8 works
- `other`: 4 works
- `caffeine`: 3 works
- `multi`: 2 works
- `exercise`: 1 works
- `melatonin`: 1 works
- `biofeedback`: 1 works

## Core Evidence (T1_core)

The `T1_core` set is the closest available evidence to the locked question (low-baseline-arousal proxy + repeated-use natural interventions + vigilance/tonic arousal outcomes).

Work-level core summary (vigilance-focused):

| short_id | citation | primary intervention | duration max (days) | vigilance summary | habituation signal |
|---|---|---:|---:|---|---|
| `W1981621779` | Tanaka 2011 (J Occup Health) | `light` | 30.0 | `improves` | `no` |
| `W2094064988` | Boudreau 2013 (PLoS ONE) | `light` | 7.0 | `improves` | `no` |
| `W2128384646` | Kubo 2011 (Scand J Work Environ Health) | `sleep_timing` | 3.0 | `mixed` | `yes` |
| `W2158979070` | Smith-Coggins 1997 (Acad Emerg Med) | `multi` | 30.0 | `null` | `no` |
| `W2165853793` | Bjorvatn 2007 (Scand J Work Environ Health) | `melatonin` | 4.0 | `unclear` | `no` |
| `W3180479501` | Connolly 2021 (BMC Neurology) | `light` | 60.0 | `improves` | `no` |
| `W3200473843` | Connolly 2021 (Frontiers Neurology; case studies) | `light` | 60.0 | `unclear` | `no` |
| `W4211135645` | Cheng 2022 (Sleep) | `sleep_timing` | 7.0 | `improves` | `yes` |

### What Looks Most Durable (From Core Evidence)

- **Light-based protocols** dominate the core evidence for sustaining objective vigilance improvements over weeks to months (field and home-based designs), but the evidence is constrained by small samples, partial blinding, and subset analyses in some studies.
- **Sleep timing/sleep extension** protocols show time-dependent benefits (often strongest early in a sequence) and can attenuate or reverse when underlying sleep restriction or circadian stressors persist.
- **Multi-component shiftwork countermeasure packages** may improve subjective ratings yet show limited objective vigilance gains in small crossover field trials.

### Core Protocol-Level Notes (T1_core)

Goal of this subsection: anchor durability/habituation claims in concrete protocol parameters and objective vigilance endpoints.

#### `W1981621779` - Tanaka 2011 (J Occup Health)
- Tier: `T1_core`
- Population: Registered nurses (all female) working rapidly rotating shifts including night shifts.
- Low-arousal operationalization/proxy: Rotating shift-work (structural proxy).
- Design: randomized crossover field study
- Setting: workplace/field
- Sample size (as extracted): 61
- Protocol (as extracted): As above.
- Comparator (as extracted): Non-BL period (usual routine; no morning BL exposure).
- Repeated-use duration (max per work): 30.0 days
- Work-level vigilance summary: `improves`
- Habituation/tolerance signal present: `no`
- Risk of bias (overall): `some_concerns` (RoB2 (crossover/cluster nuances) [planned])

Vigilance endpoints (as extracted):
- `PVT mean RT (msec; 5-min)` (Day-shift afternoon break (~14:00-15:00), repeated measures; subset n=11): `improves`; Estimated mean RT: 264 ms (non-BL) vs 235.8 ms (BL); diff -28.2 ms (95% CI -46.2, -10.2), F(1,17.0)=11.0, p<0.01 (Table 4). (habituation_flag=unclear)
- `PVT lapses (>500 ms)` (Day-shift afternoon break; subset n=11): `improves`; Estimated lapses: 2.03 (non-BL) vs 0.84 (BL); diff -1.19 (95% CI -1.98, -0.40), F(1,17.4)=10.0, p<0.01 (Table 4). (habituation_flag=unclear)

Sleepiness/fatigue endpoints (selected; as extracted):
- `sleepiness` `Karolinska Sleepiness Scale (KSS) at 10:00 (day shift)` (mean across day-shift days over each month): `improves`; Estimated mean difference -0.55 (95% CI -0.91, -0.20), F(1,55.6)=9.6, p<0.01 (Table 3).
- `fatigue` `Checklist Individual Strength (CIS) fatigue` (mean across day-shift days over each month): `improves`; Estimated means: 75.38 (non-BL) vs 73.24 (BL); diff -2.13 (95% CI -3.78, -0.48), F(1,49.6)=6.7, p=0.01 (Table 3).

#### `W2094064988` - Boudreau 2013 (PLoS ONE)
- Tier: `T1_core`
- Population: Same cohort.
- Low-arousal operationalization/proxy: Structural proxy (night shift) + adaptation status defined by melatonin acrophase timing.
- Design: As above (adapted vs non-adapted reanalysis).
- Setting: field + lab
- Sample size (as extracted): 15 (17 evaluations)
- Protocol (as extracted): As above.
- Comparator (as extracted): Adapted vs non-adapted.
- Repeated-use duration (max per work): 7.0 days
- Work-level vigilance summary: `improves`
- Habituation/tolerance signal present: `no`
- Risk of bias (overall): `some_concerns` (RoB2 (crossover/RCT dataset) [planned])

Vigilance endpoints (as extracted):
- `PVT median reaction speed (1/RT) (10-min), by time awake` (Post-night-shift lab visit (daytime sleep schedule), across wake period): `improves`; Median reaction speed: no main effect of adaptation group (p=0.88); main effect of visit (p=0.012); main effect of time awake (p=0.036); 3-way interaction (group×visit×time-awake) p=0.046. During visit 2, adapted group faster than non-adapted after 8–14h awake (p≤0.045). (habituation_flag=unclear)

#### `W2128384646` - Kubo 2011 (Scand J Work Environ Health)
- Tier: `T1_core`
- Population: Daytime manufacturing employees with habitual short weekday sleep (mean weekday sleep ≤6h); neither extreme morning nor evening chronotype; no prescription meds; N=26 completers.
- Low-arousal operationalization/proxy: Structural proxy: chronic weekday sleep restriction (mean weekday sleep ≤6h) in working adults.
- Design: Counterbalanced within-subject crossover over 3 successive weeks (weekend sleep extension vs habitual weekend sleep).
- Setting: field (real-life workers)
- Sample size (as extracted): 26
- Protocol (as extracted): Weekend sleep extension: instructed to remain in bed ≥8h between 22:00–09:00 on Fri/Sat/Sun; no daytime naps; minimal support (no reminders).
- Comparator (as extracted): Habitual weekend sleep pattern (control weekend), counterbalanced order.
- Repeated-use duration (max per work): 3.0 days
- Work-level vigilance summary: `mixed`
- Habituation/tolerance signal present: `yes`
- Risk of bias (overall): `some_concerns` (RoB2 (crossover) [planned])

Vigilance endpoints (as extracted):
- `PVT reaction time / reaction speed (10-min; PVT-192)` (Monday afternoon after the weekend (post-intervention vs post-control weekend)): `improves`; Significantly shorter reaction times on Mondays after the intervention vs habitual weekend sleep (p<0.05); overall condition×day interaction F(3,175)=6.01, p=0.001 (Figure 3; Table 1). (habituation_flag=yes)
- `PVT lapses (>500 ms) (10-min)` (Monday afternoon after the weekend): `improves`; Fewer PVT lapses on Mondays after intervention vs habitual weekend sleep (p<0.05); overall condition×day interaction F(3,175)=4.53, p=0.004 (Figure 3; Table 1). (habituation_flag=yes)
- `PVT reaction time / reaction speed (10-min)` (Thursday afternoon after the weekend): `worsens`; Significantly longer reaction times on Thursdays after intervention vs habitual weekend sleep (p<0.05), despite Monday improvement; condition×day interaction F(3,175)=6.01, p=0.001 (Figure 3; Table 1). (habituation_flag=yes)
- `PVT lapses (>500 ms) (10-min)` (Thursday afternoon after the weekend): `worsens`; Significantly more lapses on Thursdays after intervention vs habitual weekend sleep (p<0.05); condition×day interaction F(3,175)=4.53, p=0.004 (Figure 3; Table 1). (habituation_flag=yes)

#### `W2158979070` - Smith-Coggins 1997 (Acad Emerg Med)
- Tier: `T1_core`
- Population: Attending emergency physicians working rotating shifts with night rotations.
- Low-arousal operationalization/proxy: Structural proxy: night shiftwork / circadian disruption during night rotations.
- Design: prospective randomized double-blind active placebo-controlled crossover field study
- Setting: workplace/field (ED)
- Sample size (as extracted): 6
- Protocol (as extracted): Experimental package: education + chronobiologic schedule design + countermeasures (sleep hygiene, bright light, nap, caffeine timing, etc.; Table 1). Used for 1 month. Crossover after 1-month washout.
- Comparator (as extracted): Active placebo: jet lag diet + general sleep physiology/circadian education (1 month).
- Repeated-use duration (max per work): 30.0 days
- Work-level vigilance summary: `null`
- Habituation/tolerance signal present: `no`
- Risk of bias (overall): `some_concerns` (RoB2 (crossover) [planned])

Vigilance endpoints (as extracted):
- `PVT (10-min): median RT and lapses` (multiple times during shifts; compared across conditions and across shift hours): `null`; PVT performance comparable regardless of intervention; neither experimental nor active placebo altered PVT (Fig 6). Median RT increased across the night shift when averaged across interventions (p=0.007). (habituation_flag=unclear)

#### `W2165853793` - Bjorvatn 2007 (Scand J Work Environ Health)
- Tier: `T1_core`
- Population: Same cohort.
- Low-arousal operationalization/proxy: Swing-shift + adaptation problems.
- Design: Randomized placebo-controlled crossover field study.
- Setting: field
- Sample size (as extracted): 17
- Protocol (as extracted): Bright light: 30-min daily exposure using 10,000-lux light box (50 cm) during first 4 nights of night-shift week and first 4 days of day-shift week; timing individually scheduled and delayed by ~1h/day to phase delay; instructed to avoid bright light after exposure.
- Comparator (as extracted): Placebo (crossover).
- Repeated-use duration (max per work): 4.0 days
- Work-level vigilance summary: `unclear`
- Habituation/tolerance signal present: `no`
- Risk of bias (overall): `some_concerns` (RoB2 (crossover) [planned])

Vigilance endpoints (as extracted):
- `Objective 5-min serial reaction-time test (Palm) at 3 timepoints during shifts` (Nights 1,3,6 and days 1,3,6): `unclear`; No significant differences in reaction times when averaged across night shift or day shift. Day shift showed condition×day interaction F(4,44)=4.1, p=0.025 (Table 1), driven by increased reaction times on day 1 after melatonin and bright light (narrative; Figure 4). (habituation_flag=unclear)

Sleepiness/fatigue endpoints (selected; as extracted):
- `sleepiness` `ATS: Fighting sleep (%) during day shift week` (Day-shift week (second week), averaged across week): `improves`; Day shift fighting sleep: placebo 3.4±3.5 vs melatonin 1.8±2.8; effect size vs placebo d=0.50; melatonin significantly lower than placebo (p=0.021) and bright light (p=0.022) (Table 3).
- `sleepiness` `Quality of day rating (1 very good to 9 very bad) during day shift week` (Day-shift week (second week), averaged across week): `improves`; Quality of day (day shift): placebo 4.1±1.1 vs melatonin 3.4±0.6; effect size vs placebo d=0.79; melatonin significantly better than placebo (p=0.041) (Table 3).

#### `W3180479501` - Connolly 2021 (BMC Neurology)
- Tier: `T1_core`
- Population: Community-dwelling adults with mild-severe TBI or stroke >=3 months prior, reporting significant fatigue.
- Low-arousal operationalization/proxy: FSS >= 4 at screening.
- Design: pilot randomized controlled crossover trial (within-subject; assessor-blinded)
- Setting: home/field
- Sample size (as extracted): 24
- Protocol (as extracted): As above.
- Comparator (as extracted): control lighting condition (crossover)
- Repeated-use duration (max per work): 60.0 days
- Work-level vigilance summary: `improves`
- Habituation/tolerance signal present: `no`
- Risk of bias (overall): `unclear` (RoB2 (crossover variant) [planned])

Vigilance endpoints (as extracted):
- `PVT mean RT (10-min)` (end of each 2-month condition (mixed model treatment effect estimate)): `improves`; Treatment effect estimate -28.36 ms (95% CI -47.48, -9.23), t=-2.91, d=-1.75, p=.004; n=18 for PVT. (habituation_flag=no)
- `PVT fastest 10% RT (10-min)` (end of each 2-month condition (mixed model treatment effect estimate)): `improves`; Treatment effect estimate -15.10 ms (95% CI -25.03, -5.16), t=-2.98, d=-2.98, p=.003; n=18 for PVT. (habituation_flag=no)

Sleepiness/fatigue endpoints (selected; as extracted):
- `fatigue` `Brief Fatigue Inventory (BFI)` (end of each 2-month condition (mixed model treatment effect estimate)): `null`; Treatment effect estimate -0.39 (95% CI -1.16, 0.39), t=-0.97, d=-0.42, p=.33; n=24.
- `sleepiness` `Epworth Sleepiness Scale (ESS)` (end of each 2-month condition (mixed model treatment effect estimate)): `null`; Treatment effect estimate 0.59 (95% CI -0.83, 2.01), t=0.82, d=0.35, p=.41; n=24.

#### `W3200473843` - Connolly 2021 (Frontiers Neurology; case studies)
- Tier: `T1_core`
- Population: Same as above.
- Low-arousal operationalization/proxy: Eligibility required self-reported significant fatigue (FSS >= 4).
- Design: 2 case studies; cross-over (Treatment then Control); no washout
- Setting: home/field
- Sample size (as extracted): 2
- Protocol (as extracted): 5.5-month protocol: 2-week baseline, 2-month Treatment, 2-month Control, 1-month follow-up; ambient in-home lighting engineered for higher melanopic content daytime and lower melanopic content evenings; both cases allocated Treatment->Control (no washout).
- Comparator (as extracted): Control/sham lighting approximating baseline home lighting.
- Repeated-use duration (max per work): 60.0 days
- Work-level vigilance summary: `unclear`
- Habituation/tolerance signal present: `no`
- Risk of bias (overall): `high` (case_series (no standard tool applied yet))

Vigilance endpoints (as extracted):
- `PVT mean RT (ms)` (Case 2 only: baseline, mid/end treatment, mid/end control): `unclear`; Case 2 PVT mean RT (ms): 310.44 (baseline) -> 300.03 (mid T) -> 314.75 (end T) -> 288.65 (mid C) -> 268.51 (end C) (Table 2). (habituation_flag=unclear)

Sleepiness/fatigue endpoints (selected; as extracted):
- `fatigue` `Brief Fatigue Inventory (BFI)` (baseline, mid/end treatment, mid/end control, 1-month follow-up): `mixed`; Case 1 BFI: 5.67 (baseline) -> 1.56 (mid T) -> 1.00 (end T) -> 6.78 (mid C) -> 6.33 (end C) -> 7.00 (FU). Case 2 BFI: 4.33 -> 5.89 -> 2.33 -> 2.78 -> 3.89 -> 4.56 (Table 2). No inferential stats (case series).

#### `W4211135645` - Cheng 2022 (Sleep)
- Tier: `T1_core`
- Population: Night shift workers (>=20y) with ICSD-3 shift work disorder confirmed by interview + 2-week sleep log; pure 8h night shifts during study.
- Low-arousal operationalization/proxy: Shift Work Disorder diagnosis (ICSD-3) with excessive sleepiness/sleep disturbance >=3 months; sleep-time misalignment confirmed by specialist.
- Design: randomized order cross-over clinical trial (2 weeks total)
- Setting: field (real-life shift workers at home/work)
- Sample size (as extracted): 60
- Protocol (as extracted): Sleep timing schedules between night shifts: evening sleep 15:00-23:00 vs morning sleep 09:00-17:00; 1 week each; randomized order/counterbalanced; sleep at home; instructions to avoid bright light after work, avoid caffeine/nicotine, sleep dark/quiet, eat lightly.
- Comparator (as extracted): Alternative sleep schedule (within-subject crossover).
- Repeated-use duration (max per work): 7.0 days
- Work-level vigilance summary: `improves`
- Habituation/tolerance signal present: `yes`
- Risk of bias (overall): `some_concerns` (RoB2 (crossover) [planned])

Vigilance endpoints (as extracted):
- `Smartphone PVT reaction time (5-min) after night shift` (First night shift of each schedule (Table 2)): `improves`; First shift PVT RT: 0.67 s (morning sleep) vs 0.55 s (evening sleep), p=0.001; adjusted p=0.015 (Table 2). Lapses: 18.5 vs 15.4, p=0.009; adjusted p=0.115. (habituation_flag=yes)

Sleepiness/fatigue endpoints (selected; as extracted):
- `sleepiness` `Karolinska Sleepiness Scale (KSS)` (After night shift (within 1h), by shift number (Table 2)): `improves`; KSS First shift: 4.9 (morning) vs 4.1 (evening), p=0.002; adjusted p=0.012. Second shift: 4.3 vs 4.0, adjusted p=0.097. Third shift: 5.1 vs 3.8, adjusted p=0.019. Fourth shift: ns (Table 2).

## Habituation / Tolerance Patterns (Across Core + Context)

- Works with explicit `habituation_or_tolerance_signal=yes` in the extracted evidence rows: **7**
- IDs: `W1496048461`, `W2128384646`, `W2494879164`, `W2794678572`, `W2946071698`, `W3198610695`, `W4211135645`

Interpretation note: a 'habituation signal' here includes any within-study evidence of attenuation across days/weeks, reversal after repeated use, or explicit tolerance framing; it does not guarantee a formal tolerance test.

## Context Evidence That Constrains Durability Claims (T2_context)

This manuscript uses `T2_context` to support interpretation (mechanism and habituation framing), not to replace `T1_core` for the locked question.

### Caffeine: Tolerance/Withdrawal and the Durability Problem

- `W1496048461` Watson 2002 (Br J Clin Pharmacol) (duration max=7.0d; RoB=some_concerns; full-text): Randomized double-blind placebo-controlled crossover: 200 mg caffeine capsules vs placebo twice daily for 7 days; acute 200 mg caffeine challenge on test day with repeated measures over 120 min.. Population: Healthy volunteers (n=12 randomized; prior regular caffeine consumers per authors), fasting overnight; studied in metabolism research unit..
- `Four-choice reaction time (4CRT), 5-min portable test` (Post acute caffeine challenge (0-120 min summary)): `improves`; 4CRT improved by 0.02±0.01 s after caffeine in both caffeine-naive and caffeine-replete conditions; no between-condition difference reported (authors: cognitive performance not affected by prior exposure). (habituation_flag=no)

- `W2494879164` Pagar 2016 (IOSR-JDMS) (duration max=180.0d; RoB=high; full-text): Within-subject pre/post caffeine challenge at baseline, then re-tested after ~6 months daily coffee; no placebo; unblinded.. Population: Healthy adults (20-25y), 30 male + 30 female; baseline self-reported caffeine intake <200 mg/day; excluded major illness, smoking/alcohol, sensory deficits..
- `Visual reaction time (ms), red stimulus (VRT-R)` (Baseline (non-habitual; >=24h abstinent), 30 min post ~250 mg caffeine): `improves`; Males: 210.50±3.27 -> 202.80±3.02 ms (p<0.01). Females: 216.50±2.87 -> 208.30±2.06 ms (p<0.001). (habituation_flag=no)
- `Auditory reaction time (ms), high pitched stimulus (ART-H)` (Baseline (non-habitual; >=24h abstinent), 30 min post ~250 mg caffeine): `improves`; Males: 194.63±1.73 -> 184.43±1.97 ms (p<0.001). Females: 200.60±3.02 -> 191.50±3.00 ms (p<0.001). (habituation_flag=no)
- `Visual reaction time (ms), red stimulus (VRT-R)` (After ~6 months daily coffee (200-600 mg/day), 30 min post ~250 mg caffeine): `improves`; Males: 203.03±1.84 -> 197.16±2.10 ms (p<0.05). Females: 211.80±1.68 -> 205.96±2.10 ms (p<0.05). (habituation_flag=yes)
- `Auditory reaction time (ms), high pitched stimulus (ART-H)` (After ~6 months daily coffee (200-600 mg/day), 30 min post ~250 mg caffeine): `improves`; Males: 188.50±1.71 -> 182.66±1.86 ms (p<0.02). Females: 196.93±3.40 -> 190.80±3.45 ms (p<0.02). (habituation_flag=yes)

- `W2946071698` Weibel 2019 (bioRxiv preprint) (duration max=10.0d; RoB=some_concerns; full-text): Double-blind within-subject crossover with 3 conditions (caffeine vs placebo vs withdrawal), each 10 days; 43h controlled lab protocol starting day 9.. Population: Young healthy male habitual caffeine consumers (habitual intake 300-600 mg/day) screened for good sleep quality (PSQI<=5) and non-extreme chronotype; n=20 completed..
- `PVT (10-min): lapses (RT>500 ms), z-transformed` (Day+night during 43h lab protocol (mixed model)): `mixed`; More lapses during withdrawal vs placebo/caffeine: main effect condition F(2,51)=6.66, p=0.0027; mean±SD (z) placebo -0.18±0.77, caffeine -0.09±1.04, withdrawal 0.27±1.11; post-hoc withdrawal>both p<0.01. (habituation_flag=yes)

Interpretive synthesis (caffeine): repeated-use durability is often limited by tolerance and/or withdrawal dynamics; acute performance benefits can persist, but the net day-to-day state depends on baseline caffeine exposure and abstinence/withdrawal context.

### Light: Time-Dependent Effects and Shiftwork Adaptation

- `W3132047372` Martin 2021 (Chronobiology International) [abstract-only extraction] (duration max=4.0d; abstract_only=yes; RoB=unclear)
- Note: extracted from abstract only due to paywalled full text; treat as context with reduced confidence.
- Vigilance `PVT (10-min) at beginning and end of each night shift` (Across four consecutive night shifts per condition): `null`; Abstract reports no differences in alertness between conditions in summer or winter study (no effect sizes/p-values provided in abstract).
- Sleepiness `Karolinska Sleepiness Scale (KSS) every 2 h during shifts` (Across four consecutive night shifts per condition): `null`; Abstract reports no differences in sleepiness between conditions in either study (no effect sizes/p-values provided in abstract).

- `W4394879532` Wang 2024 (Buildings) (duration max=8.0d; abstract_only=no; RoB=high)
- Vigilance `PVT reaction time (5-min at 10:00)` (Daily across confinement (reported comparisons day 3/4 vs day 8)): `worsens`; Reaction time decreased on day 3 (practice effect; p=0.050) then increased day-by-day; day 8 reaction time significantly longer than day 3 (p=0.026) and day 4 (p=0.016). Error counts increased trend but not significant.
- Sleepiness `Karolinska Sleepiness Scale (KSS) (hourly; focus on wake-up 08:00)` (Across 8-day confinement): `worsens`; KSS at wake-up (08:00) increased day-by-day (Figure 4; between-day differences indicated with * p<0.05, ** p<0.01). KSS at 24:00 before sleep decreased day-by-day (mixed direction depending on time-of-day).

- `W4285731316` Kjorstad 2022 (BMC Nursing) (duration max=42.0d; abstract_only=no; RoB=high)
- Sleepiness `Subjective sleepiness (1-5) after each shift (work diary)` (Evening shifts during 14-day diary window (BDLE vs STLE; within-subject fixed-effects model)): `worsens`; Sleepiness higher in BDLE vs STLE during evening shifts: +17% (p=0.034; Cohen's d=0.49).

- `W4311622325` Cyr 2022 (PsyArXiv preprint) (duration max=20.0d; abstract_only=no; RoB=some_concerns)
- Sleepiness `Karolinska Sleepiness Scale (KSS; 1-9)` (Across baseline + intervention periods (mixed-effects; period effect)): `improves`; Sleepiness decreased over time in both groups: period effect B=-0.21 (beta=-0.10), 95% CI [-0.16,-0.04], t=-3.35, p<0.001. No clear differential by condition (period x condition p=0.934).

- `W3040483795` Domagalik 2020 (Frontiers in Neuroscience) (duration max=28.0d; abstract_only=no; RoB=some_concerns)
- Vigilance `PVT (5-min): mean reaction time (ms)` (Baseline + weeks 1-4; plus 1-week follow-up): `worsens`; Group×session interaction: mean RT F(4,144)=2.59, p<0.05, partial η²=0.07 (increase across weeks only in BLB). Follow-up (BLB only): baseline vs week4 vs follow-up F(2,36)=21.79, p<0.001, partial η²=0.55; baseline vs follow-up ns (reversible).
- Vigilance `PVT (5-min): omission errors (RT>=500 ms) (%)` (Baseline vs week4 vs follow-up (BLB only)): `worsens`; Baseline-weekly group×session for omissions not significant (p=0.25), but BLB baseline vs week4 vs follow-up differed: omission errors F(2,36)=5.15, p<0.05, partial η²=0.22 (post-hoc: baseline vs week4 and week4 vs follow-up significant; baseline vs follow-up ns).
- Sleepiness `Epworth Sleepiness Scale (ESS) and PSQI` (Weekly during intervention; PSQI baseline and last session): `null`; No group×session interaction: ESS F(4,144)=1.72, p=0.15; PSQI F(1,36)=0.12, p=0.73. Follow-up ESS effect ns (p=0.12).

- `W3068855346` Sunde 2020 (Frontiers in Psychology) (duration max=3.0d; abstract_only=no; RoB=some_concerns)
- Vigilance `PVT (10-min): fastest 10% reaction time (ms)` (Across shifts; light×time interaction): `mixed`; No light main effect overall (EMM 257.99 vs 259.24 ms; p=0.283), but light×time interaction significant: F(4,807)=2.91, p=0.021; post-hoc differences at later night timepoints (Figure 4; stars at ~04:00 and 05:30).
- Vigilance `PVT false starts (count per bout)` (Late night (05:30) during shifts): `improves`; Light×time effect: fewer false starts at 05:30 with 7000K vs 2500K: EMM 3.33 (SE 0.57) vs 4.83 (SE 0.93), p=0.040 (reported in results; Figure 3D).
- Sleepiness `Karolinska Sleepiness Scale (KSS; 1-9)` (Across 3 simulated night shifts (mixed models; Table 3)): `improves`; Lower sleepiness in 7000K vs 2500K: EMM 6.15 (SE 0.16) vs 6.32 (SE 0.16); light main effect F(1,834)=4.58, p=0.033; no significant interactions.

Interpretive synthesis (light): effects are often time-locked (circadian phase, time awake, and exposure timing), so durability should be operationalized as stability across repeated shifts/days rather than endpoint-only comparisons.

## Risk of Bias (Work-Level)

The evidence base includes many field studies and uncontrolled designs, which are valuable for ecological validity but limit causal inference about tonic arousal 'set-point' engineering.

Key constraints observed in the extracted set:
- Small samples in many crossover studies, with risk of period/carryover effects and multiple outcomes.
- Limited blinding feasibility for light and sleep scheduling interventions.
- Frequent reliance on subjective measures for sleepiness/fatigue, with fewer objective tonic arousal markers (e.g., pupil baseline, continuous autonomics).
- A substantial fraction of evidence is outside the core target population and is used for context/mechanism rather than direct answer to the locked question.

## Immediate Implications for the Manuscript (Elite-Journal Positioning)

The strongest publishable contribution from this corpus is likely a structured synthesis that:
- Treats **light manipulation** and **sleep timing** as the two dominant natural lever classes with repeated-use evidence relevant to low-arousal proxies (shift workers, fatigue populations, chronic short sleepers).
- Makes durability/habituation the organizing axis (not simply 'does it work acutely?').
- Explicitly separates **core evidence** (T1_core) from **context evidence** (T2_context) and avoids overstating generalizability to trait low-arousal individuals.

## Files Generated (S001)

- Work-level evidence map: `output/synthesis/S001_evidence_map_worklevel.csv`
- Vigilance-only outcomes table: `output/synthesis/S001_vigilance_outcomes.csv`
- Figures:
  - `output/synthesis/S001_fig1_study_counts_by_intervention.png`
  - `output/synthesis/S001_fig2_vigilance_durability_map.png`
  - `output/synthesis/S001_fig3_risk_of_bias_distribution.png`
- Gap map (draft): `output/synthesis/S001_gap_map.md`
- Manuscript outline (draft): `output/synthesis/S001_manuscript_outline.md`

