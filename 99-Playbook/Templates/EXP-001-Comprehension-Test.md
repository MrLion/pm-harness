---
type: experiment
project: pm-harness
artifact: experiment
id: EXP-001
status: planned
risk_type: usability
risk_owner: Design
opportunity: "[OPP-001](OPP-001-Outpatient-Imaging-Cost.md)"
start: 2026-11-10
end: 2026-11-21
sample_size: 5 interviews
budget: unknown
effort: 5 interviews + analysis
created: 2026-11-08
framework: SVPG
source: https://www.svpg.com/four-big-risks/
updated: 2026-11-09
example: true
case_id: CASE-001
---

# Experiment — can patients understand an imaging estimate?

## Journey

[JOURNEY-001](JOURNEY-001-Imaging-Path.md) — the stage where the comprehension test applies.

## Risk being retired

| Field | Content |
|---|---|
| Risk type | usability (comprehension) |
| Assumption | Patients can explain what an estimate includes, excludes, and how long it is valid |
| Opportunity | [OPP-001](OPP-001-Outpatient-Imaging-Cost.md) |

## Hypothesis

> We believe a patient-readable estimate with inclusions, exclusions, and validity will cause at least 4 of 5 interviewed patients to explain all three correctly, measured by a comprehension task.

> [!NOTE] What this does not test
> This test measures comprehension only. It does not test whether the patient can predict final responsibility. Prediction requires reconciled bills and belongs in the pilot, not this prototype.

## Data handling

| Field | Answer |
|---|---|
| Real PHI used? | No |
| De-identified or synthetic data? | Synthetic paper prototype only |
| BAA in place? | Not applicable |
| Where data is stored | Local design file; no patient data |
| Retention and destruction | Delete after study |
| Compliance scope | Synthetic prototype: [COMP-001](Compliance/COMP-001-Compliance-Scope.md) is the structure template. Any pilot with real patient data uses the live [COMP-003](../../11-Compliance/COMP-003-Compliance-Scope.md). |

## Design

5 moderated interviews using a paper prototype of an outpatient imaging estimate.

After the participant explains inclusions, exclusions, and validity, ask: **“Name one charge that might still be missing from this estimate.”** Record the answer verbatim. The probe tests whether the participant can identify a gap, not whether they know the exact billing structure.

| Field | Content |
|---|---|
| Population | Adults on employer-sponsored HDHPs who have recently sought outpatient imaging |
| Duration | 45 minutes per interview |
| Cost | Budget unknown; effort is 5 interviews plus analysis |
| Accessibility | Plain language, large-print option, screen-reader-compatible prototype |

## Pre-registered criteria

| Success | Failure | Kill |
|---|---|---|
| ≥4 of 5 explain all three correctly | ≤3 of 5 explain all three | ≤2 of 5 explain all three; prototype unusable |

The missing-charge probe is recorded separately. It does not change the pass/fail rule in this round.

## Result

Pending

## Secondary observations

- Record where patients look first, what they ask, and which terms confuse them.
- Missing-charge probe: record whether the participant names a plausible charge (radiologist, facility, contrast, anesthesia, interpretation) or says none.
- Do not treat these as evidence of behavioural impact.

## What we learned

Pending

## Decision

Pending — link the resulting [DEC-001](DEC-001-Build-Partner-Defer.md) or updated [OPP-001](OPP-001-Outpatient-Imaging-Cost.md).

## Scope note

This tests comprehension, not prediction of final responsibility and not reduced postponement. Prediction requires reconciled bills; behavioural impact requires a separate pilot.