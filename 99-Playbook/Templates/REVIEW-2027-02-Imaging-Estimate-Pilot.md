---
type: review
project: pm-harness
artifact: review
id: REVIEW-2027-02
period: 2027-02
date: 2027-02-15
status: simulated
framework: "Pichler (goal vs outcome) + SVPG (risk retired vs not)"
updated: 2026-11-09
example: true
case_id: CASE-001
gate: REL-001 conditional; pilot not run
---

# Review — imaging estimate pilot

> [!WARNING] Simulated future review
> The pilot has not run. Every result here is pending; this page shows the review shape, not evidence.

## Goals vs outcomes

| Goal | Target | Actual | Measurement status | Met? |
|---|---|---|---|---|
| Pre-booking estimate coverage | 60% of eligible requests | Pending | not measured | unknown |
| Patient prediction accuracy | ≥70% within $400 (pilot) | Pending | pilot metric; expected amount captured before booking; not tested by EXP-001 | unknown |
| Decision follow-up | Estimated patients can say whether the estimate informed their choice and why | Pending | pilot metric; not measured | unknown |
| Reconciled accuracy | 70% within $400 | Pending | not measured | unknown |

## Risks retired

| Risk | Was it tested? | Result | Now |
|---|---|---|---|
| usability — comprehension | planned — EXP-001, not run | not measured | still open |
| value — changes booking decision | no | not tested | still open |
| feasibility — data access | no | not tested | still open |
| viability — buyer willingness | no | not tested | still open |

## What we learned

- Pending pilot data.

## What we got wrong

- Pending.

## Decisions still unresolved

- [DEC-001](DEC-001-Build-Partner-Defer.md) — proposed defer; human acceptance still required.

## Metric movement

| Metric | Start | End | Δ | Commentary |
|---|---|---|---|---|
| Estimate coverage | unknown | Pending | — | report after pilot |
| Patient prediction accuracy | unknown | Pending | — | pilot only; requires reconciled bills |
| Decision follow-up | unknown | Pending | — | report separately for bookers, switchers, deferrers, and non-bookers |
| Reconciled accuracy | unknown | Pending | — | report after pilot |

## Compliance review

| Check | Result |
|---|---|
| Incidents | Pending — pilot not run |
| Audit findings | Pending — pilot not run |
| Access review | Pending — pilot not run |
| Vendor / BAA | Pending — pilot not run |
| Corrective actions | Pending — pilot not run |

## Next period

1. Run the behavioural pilot if comprehension and data access pass.