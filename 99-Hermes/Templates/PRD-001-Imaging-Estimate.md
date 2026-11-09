---
type: prd
artifact: solution-brief
id: PRD-001
status: draft
opportunity: "[[OPP-001-Outpatient-Imaging-Cost|OPP-001]]"
candidate_id: CAND-003
decision: "[[DEC-001-Build-Partner-Defer|DEC-001]]"
primary_metric: coverage
created: 2026-11-08
updated: 2026-11-08
framework: "Pichler (Product Canvas) + SVPG (prototype-as-spec)"
example: true
---

# Solution Brief — patient-readable imaging estimate

## Canvas

| Element                  | Content                                                                                   |               |
| ------------------------ | ----------------------------------------------------------------------------------------- | ------------- |
| Problem | [[PROB-001-Imaging-Cost-Problem\|PROB-001]] |
| Opportunity | [[OPP-001-Outpatient-Imaging-Cost\|OPP-001]] |
| Target user | [[PERSONA-001-HDHP-Imaging-Patient\|PERSONA-001]] |
| Outcome (one sentence)   | More eligible imaging requests receive a pre-booking estimate the patient can understand. |               |
| Prototype                | Paper prototype of one imaging estimate with inclusions, exclusions, and validity         |               |
| Epics (big capabilities) | Estimate request · patient-readable explanation · reconciliation check                    |               |

## Non-goals

- Provider matching
- Appointment scheduling
- Claims adjudication
- Multi-service estimates in the first pilot

## User stories

- As an HDHP patient, I want to see what an imaging estimate includes and excludes, so that I can decide whether to book.

## Acceptance criteria

- [ ] Estimate shows inclusions, exclusions, and validity period.
- [ ] Patient can explain all three in a comprehension test.
- [ ] Estimate can be reconciled against final patient responsibility.

## Metrics

**Primary metric:** Share of eligible imaging requests that receive a pre-booking estimate.

**Accuracy companion:** Share of reconciled estimates within $400 of final patient responsibility.

**Guardrail:** Underestimation over $400 must not exceed 10% of reconciled estimates (provisional).

**Threshold note:** $400 and 10% are provisional; validate against patient expectations.

## Risks

| Risk | Mitigation |
|---|---|
| Data access | Partner or provider data review before build |
| Patient comprehension | Paper-prototype test before build |
| Wrong estimate | Reconciliation report and underestimation guardrail |