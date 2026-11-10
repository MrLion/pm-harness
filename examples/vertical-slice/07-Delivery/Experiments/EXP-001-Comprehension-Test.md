---
type: experiment
project: pm-harness-example
artifact: experiment
id: EXP-001
status: planned
risk_type: usability
risk_owner: Design
opportunity: "[OPP-001](../../03-Opportunities/OPP-001-Outpatient-Imaging-Cost.md)"
start: 2026-11-10
end: 2026-11-21
sample_size: 5 interviews
budget: unknown
effort: 5 interviews plus analysis
updated: 2026-11-09
framework: SVPG
example: true
synthetic: true
case_id: CASE-001
---

# Experiment — can patients understand an imaging estimate?

## Risk being retired

Patients can explain what an estimate includes, excludes, and how long it is valid.

## Hypothesis

At least 4 of 5 participants explain all three correctly in a comprehension task.

## Design

5 moderated interviews with a paper prototype.

After the three-part explanation, ask: “Name one charge that might still be missing from this estimate.”

## Pre-registered criteria

| Success | Failure | Kill |
|---|---|---|
| ≥4 of 5 explain all three | ≤3 of 5 explain all three | ≤2 of 5 explain all three |

The missing-charge probe is recorded separately. It does not change the pass/fail rule in this round.

## Scope note

This tests comprehension, not prediction of final responsibility and not reduced postponement.

## Links

- [PRD-001](../PRDs/PRD-001-Imaging-Estimate.md)
- [Decision](../../05-Decisions/DEC-001-Build-Partner-Defer.md)
