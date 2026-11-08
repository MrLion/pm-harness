---
type: release
artifact: release
id: REL-000
date: YYYY-MM-DD
status: released
goal: TBD
metric_result: TBD
roadmap: TBD
created: YYYY-MM-DD
framework: Pichler
updated: YYYY-MM-DD
---

# Release

A delivery record tied to the GO Roadmap goal it was meant to move. Without a goal and a measured
result, this is a deployment log rather than a learning artifact.

## Example — US healthcare consumer

> [!example]- Example — outpatient cost estimator pilot
> **Release:** Cost estimator MVP.
> **Goal:** Reduce postponed care due to unknown out-of-pocket cost.
> **Metric before/after:** Baseline unknown.
> **Follow-up:** Add provider matching if pilot succeeds.

> [!todo] Ambiguous fields — how to fill
> | Field | Meaning | If unsure |
> |---|---|---|
> | date | real release date | no fictional dates |
> | contents | what shipped | concise |
> | goal | outcome it should move | link artifact |
> | metric movement | measured learning | not an estimate |
> | surprises | what actually surprised us | can be negative |
> | unexpected cost | support/ops burden | not just dollars |

## Release

| Field | Content |
|---|---|
| Date | [FILL] |
| Contents | [FILL] |
| GOAL it was meant to move | [FILL] |
| Roadmap row | [[Now]] |
| Related opportunity / brief | [[OPP-000]] · [[PRD-000]] |

## Metric movement

| Metric | Before | After | Window | Source |
|---|---|---|---|---|
| [FILL] | unknown | unknown | [FILL] | [FILL] |

## What surprised us

- [FILL]

## Unexpected cost

- Support load / incidents / debt / rollback: [FILL]

## Follow-up

- [FILL]

---

> [!example]- Worked example — fictional
> **Lantern 1.4 — Instant Gap**, released 2026-03-12: gap auto-offer, rank-order eligibility,
> two-tap mobile accept. **Goal:** fill an open shift without the manager phoning anyone.
> **Metric:** gaps filled without a manager call moved from 22% to 47% in the 30 days after release,
> against a 60% target. Source: event log.
> **Surprise:** offers sent during a shift were ignored; reminders at shift start performed better.
> **Unexpected cost:** ranking explanations generated 11 support tickets in week one.
> **Follow-up:** EXP-002 tests notification timing before changing the ranking model.
