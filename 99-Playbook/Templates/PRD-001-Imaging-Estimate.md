---
type: prd
artifact: solution-brief
id: PRD-001
status: draft
opportunity: "[OPP-001](OPP-001-Outpatient-Imaging-Cost.md)"
candidate_id: CAND-003
decision: "[DEC-001](DEC-001-Build-Partner-Defer.md)"
primary_metric: coverage
outcome_metric: prediction_accuracy
product_manager: Unassigned
product_owner: Unassigned
compliance_owner: Unassigned
buyer: Unresolved
created: 2026-11-08
updated: 2026-11-09
framework: "Pichler (Product Canvas) + SVPG (prototype-as-spec)"
example: true
case_id: CASE-001
---

# Solution Brief — patient-readable imaging estimate

## Canvas

| Element                  | Content                                                                                   |               |
| ------------------------ | ----------------------------------------------------------------------------------------- | ------------- |
| Problem | [PROB-001](PROB-001-Imaging-Cost-Problem.md) |
| Opportunity | [OPP-001](OPP-001-Outpatient-Imaging-Cost.md) |
| Target user | [PERSONA-001](PERSONA-001-HDHP-Imaging-Patient.md) |
| Outcome (one sentence)   | Patients can predict their final responsibility before booking, supported by a pre-booking estimate. |               |
| Prototype                | Paper prototype of one imaging estimate with inclusions, exclusions, and validity         |               |
| Epics (big capabilities) | Estimate request · patient-readable explanation · reconciliation check                    |               |

## Non-goals

- Provider matching
- Appointment scheduling
- Claims adjudication
- Multi-service estimates in the first pilot

## User stories

- As an HDHP patient, I want to see what an imaging estimate includes and excludes, so that I can decide whether to book.
- As an HDHP patient whose deductible is not met, I want the estimate to show the full expected responsibility, not only the plan-paid portion.
- As an HDHP patient choosing an out-of-network provider, I want the estimate to flag the network assumption and the financial exposure.
- As a scheduler, I want a changed order or additional procedure to invalidate the estimate rather than silently reuse it.

## Acceptance criteria

- [ ] Estimate shows inclusions, exclusions, and validity period.
- [ ] Patient can explain all three in a comprehension test.
- [ ] Estimate can be reconciled against final patient responsibility.
- [ ] Deductible-met and deductible-not-met cases show different patient responsibility.
- [ ] Out-of-network status is visible and does not default to in-network pricing.
- [ ] A changed order or added procedure invalidates or recalculates the estimate.
- [ ] Self-pay and multiple-procedure cases are either supported or explicitly out of scope.
- [ ] The estimate states the data source and the date it was generated.

## Metrics

**Primary coverage metric:** Share of eligible imaging requests that receive a pre-booking estimate. Eligibility is fixed at intake; cancellations after the estimate are reported separately.

**Outcome metric:** Share of patients who can predict final responsibility within $400 before booking. Record the expected dollar amount before booking and before any bill is visible; compare it with reconciled final responsibility. The paper prototype tests comprehension only.

**Accuracy companion:** Share of reconciled estimates within $400 of final patient responsibility.

**Guardrail:** Underestimation over $400 must not exceed 10% of reconciled estimates (provisional).

**Threshold note:** $400 and 10% are provisional; validate against patient expectations.

## Compliance impact

| Question | Answer |
|---|---|
| Data used | Synthetic prototype data only |
| PII / PHI / ePHI | None in the synthetic prototype; reassess before pilot |
| BAA required | Not applicable until a vendor is selected |
| Risk assessment | [RISK-001](Compliance/RISK-001-Privacy-Security-Risk.md) |
| Controls | [CTRL-001](Compliance/CTRL-001-Control-Matrix.md) |
| Compliance approval | Live [COMP-003](../../11-Compliance/COMP-003-Compliance-Scope.md) approved and a named owner before pilot; [COMP-001](Compliance/COMP-001-Compliance-Scope.md) is the structure template |

## Journey

[JOURNEY-001](JOURNEY-001-Imaging-Path.md) — the experience this brief changes.

## Risks

| Risk | Mitigation |
|---|---|
| Data access | Partner or provider data review before build |
| Patient comprehension | Paper-prototype test before build |
| Wrong estimate | Reconciliation report and underestimation guardrail |