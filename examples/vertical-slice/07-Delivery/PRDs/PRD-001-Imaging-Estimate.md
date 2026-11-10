---
type: prd
project: pm-harness-example
artifact: solution-brief
id: PRD-001
status: draft
opportunity: "[OPP-001](../../03-Opportunities/OPP-001-Outpatient-Imaging-Cost.md)"
decision: "[DEC-001](../../05-Decisions/DEC-001-Build-Partner-Defer.md)"
primary_metric: coverage
outcome_metric: prediction_accuracy
product_manager: Unassigned
product_owner: Unassigned
compliance_owner: Unassigned
buyer: Unresolved
updated: 2026-11-09
framework: "Pichler (Product Canvas)"
example: true
synthetic: true
case_id: CASE-001
---

# Solution brief — patient-readable imaging estimate

## Problem

[PROB-001](../../02-Problems/PROB-001-Imaging-Cost-Problem.md)

## Opportunity

[OPP-001](../../03-Opportunities/OPP-001-Outpatient-Imaging-Cost.md)

## Outcome

Patients can predict their final responsibility before booking, supported by a pre-booking estimate.

## Scope

One imaging type. One estimate pathway. Synthetic prototype first.

## Non-goals

Provider matching, scheduling, claims adjudication, and multi-service estimates.

## Acceptance criteria

- [ ] The estimate shows inclusions, exclusions, and validity.
- [ ] The patient can explain those three items.
- [ ] The patient can name one charge that might still be missing.
- [ ] Deductible-met and deductible-not-met cases differ.
- [ ] Out-of-network status is visible.
- [ ] A changed order invalidates or recalculates the estimate.

## Compliance

Synthetic prototype only. Any pilot with real patient data uses the live `11-Compliance/COMP-003-Compliance-Scope.md`.

## Links

- [Experiment](../Experiments/EXP-001-Comprehension-Test.md)
- [Release](../Releases/REL-001-Imaging-Estimate-Pilot.md)
