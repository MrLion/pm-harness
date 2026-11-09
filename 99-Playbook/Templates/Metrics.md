---
type: metrics
artifact: metrics
framework: "Pichler + North Star"
status: draft
confidence: low
north_star: Share of eligible outpatient imaging requests that receive a pre-booking estimate
north_star_definition: Eligible requests are all outpatient imaging requests captured at intake, including those that later end without a booking or are cancelled. Eligibility is fixed at intake; cancellations are reported separately. Pre-booking means shown before confirmation or abandonment.
north_star_source: request + booking system
outcome_metric: Share of patients who can predict final responsibility within $400 before booking
outcome_source: comprehension study + billing reconciliation
updated: 2026-11-09
case_id: CASE-001
source: "https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/ + https://amplitude.com/books/north-star/about-north-star-framework"
example: true
---

# Metrics — estimate coverage and reconciliation

## Primary coverage metric

Share of eligible outpatient imaging requests that receive a pre-booking estimate.

| Requirement | Answer |
|---|---|
| Represents value customers actually receive | No — coverage is a leading indicator; the outcome is prediction accuracy |
| Precise definition, including exclusions and window | Eligible requests are fixed at intake, including non-bookers and later cancellations; self-pay excluded; measured weekly. Cancellations are reported separately. |
| Source of truth | request + booking system |
| Current value | unknown |
| Why it is a leading indicator of sustainable results | Coverage is necessary for any patient decision effect |

## Outcome metric

| Field | Answer |
|---|---|
| Metric | Share of patients who can predict final responsibility within $400 before booking |
| Denominator | Patients with a reconciled bill who received an estimate; non-bookers are covered separately by decision follow-up |
| Capture point | Before booking, after the estimate is shown, and before any bill or EOB is visible. Record the patient's expected dollar amount. |
| Comparison point | Final patient responsibility after claim adjudication. |
| Timing rule | Do not ask retrospectively after the bill; a retrospective answer measures recall, not prediction. |
| Source of truth | Pilot follow-up plus billing reconciliation. The comprehension study does not test prediction. |
| Current value | unknown |
| Why it matters | Coverage can rise while patients remain unable to predict what they will owe |

## Coverage inputs

| Input metric | Definition | Current | Owner |
|---|---|---|---|
| Eligible imaging requests | Requests for covered outpatient imaging | unknown | PM |
| Estimate delivery rate | Share of eligible requests shown an estimate | unknown | Eng |
| Cancelled after estimate | Requests cancelled after seeing an estimate, reported separately | unknown | PM |

## Guardrails

| Metric | Definition | Threshold |
|---|---|---|
| Reconciled accuracy | Share of reconciled estimates within $400 of final responsibility | ≥70% (provisional) |
| Underestimation | Share of reconciled estimates underestimated by more than $400 | ≤10% (provisional) |

## Supporting KPIs

| Layer | Metric | Definition | Current | Source of truth | Owner |
|---|---|---|---|---|---|
| Lagging (outcome) | Decision follow-up | Among all patients who received an estimate, including non-bookers: action taken; whether the estimate informed the choice; driver: uncertainty, affordability, network, or urgency | unknown | booking + short follow-up | PM |
| Leading (behaviour) | Estimate views | Share of eligible requests with an estimate opened | unknown | product analytics | Eng |
| Health (guardrail) | Complaint rate | Surprise-bill complaints per 1,000 bookings | unknown | support | PM |
| Diagnostic | Cancellation after estimate | Share of estimated requests cancelled after viewing the estimate | unknown | booking system | PM |

## Instrumentation gaps

| Metric we need | Why we can't measure it yet | Fix |
|---|---|---|
| Non-booker estimate coverage | Request system may not capture abandonment | Add event tracking |
| Cancellation after estimate | Request system may not distinguish cancellation from abandonment | Tag cancellation reason and timestamp |
| Final patient responsibility | Needs billing reconciliation | Partner data review |
| Decision follow-up for non-bookers | Request and booking systems may not identify people who never booked | Add a short follow-up at estimate delivery, with consent |
| Reason for the choice | Current systems record the action, not the driver | Ask one open question: what drove the choice? |

## Related

- [Goals](Goals.md) · [Strategy](Strategy.md)
- [JOURNEY-001](JOURNEY-001-Imaging-Path.md) — where coverage and prediction diverge