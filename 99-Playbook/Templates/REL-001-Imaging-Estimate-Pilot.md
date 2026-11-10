---
type: release
project: pm-harness
artifact: release
id: REL-001
date: 2027-01-15
status: conditional
gate: DEC-001 accepted; buyer selected; COMP-003 approved
owner: Unassigned
support_owner: Unassigned
incident_contact: Unassigned
goal: Reduce out-of-pocket uncertainty before outpatient imaging
metric_result: Pending
roadmap: NOW (conditional)
created: 2026-11-08
framework: Pichler
updated: 2026-11-09
example: true
case_id: CASE-001
---

# Release — imaging estimate pilot

> [!WARNING] Conditional record
> This is a planned example, not a scheduled release. It cannot proceed until `DEC-001` is accepted, a buyer is named, and the live compliance scope is approved.

## Release

| Field | Content |
|---|---|
| Date | 2027-01-15 (planned) |
| Contents | Pre-booking estimate for one outpatient imaging type |
| GOAL it was meant to move | Reduce out-of-pocket uncertainty before imaging |
| Roadmap row | NOW (conditional) |
| Related opportunity / brief | [OPP-001](OPP-001-Outpatient-Imaging-Cost.md) · [PRD-001](PRD-001-Imaging-Estimate.md) |

## Metric movement

| Metric | Before | After | Window | Source |
|---|---|---|---|---|
| Share of eligible requests with a pre-booking estimate | unknown | TBD | 30 days | request + booking system |
| Share of patients who can predict final responsibility within $400 | unknown | TBD | 30 days | comprehension task |
| Share of reconciled estimates within $400 | unknown | TBD | 30 days | billing reconciliation |

## Compliance sign-off

| Check | Evidence |
|---|---|
| Vendor / BAA | No vendor selected; if one is selected, complete [VEND-001](Compliance/VEND-001-Vendor-BAA-Register.md) |
| Privacy-security risk | [RISK-001](Compliance/RISK-001-Privacy-Security-Risk.md) |
| Controls | [CTRL-001](Compliance/CTRL-001-Control-Matrix.md) |
| Incident plan | [INC-001](Compliance/INC-001-Incident-Breach-Response.md) |
| Approval | Live [COMP-003](../../11-Compliance/COMP-003-Compliance-Scope.md) approved and a named owner; currently `draft` / `Unassigned` |

## What surprised us

- To be recorded after the pilot.

## Unexpected cost

- Support load, reconciliation effort, data access cost: TBD.

## Follow-up

- Owner: Unassigned — assign before launch.
- Add provider matching only if the estimate pilot succeeds.
- Record the incident and support path in the release review.