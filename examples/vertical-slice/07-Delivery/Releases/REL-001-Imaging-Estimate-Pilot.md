---
type: release
artifact: release
id: REL-001
status: conditional
gate: DEC-001 accepted; buyer selected; compliance scope approved
owner: Unassigned
support_owner: Unassigned
incident_contact: Unassigned
date: 2027-01-15
updated: 2026-11-09
framework: Pichler
example: true
synthetic: true
case_id: CASE-001
---

# Release — imaging estimate pilot

> [!WARNING] Conditional record
> This release cannot proceed until the decision is accepted, a buyer is named, and the live compliance scope is approved.

## Contents

Pre-booking estimate for one outpatient imaging type.

## Gate

- [DEC-001](../../05-Decisions/DEC-001-Build-Partner-Defer.md) accepted
- Buyer named
- Live `11-Compliance/COMP-003-Compliance-Scope.md` approved

## Metrics

| Metric | Before | After |
|---|---|---|
| Coverage: eligible requests with a pre-booking estimate | unknown | Pending |
| Prediction: patients within $400 before booking | unknown | Pending |
| Reconciliation: estimates within $400 of final responsibility | unknown | Pending |

## Links

- [PRD-001](../PRDs/PRD-001-Imaging-Estimate.md)
- [Experiment](../Experiments/EXP-001-Comprehension-Test.md)
- [Review](../../08-Reviews/REVIEW-2027-02-Imaging-Estimate-Pilot.md)
