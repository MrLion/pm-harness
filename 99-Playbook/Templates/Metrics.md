---
type: metrics
artifact: metrics
framework: "Pichler + North Star"
status: draft
confidence: low
north_star: Share of eligible outpatient imaging requests that receive a pre-booking estimate
north_star_definition: Eligible requests are all outpatient imaging requests captured at intake, including those that later end without a booking or are cancelled. Eligibility is fixed at intake; cancellations are reported separately. Pre-booking means shown before confirmation or abandonment.
north_star_source: request + booking system
updated: 2026-11-09
source: "https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/ + https://amplitude.com/books/north-star/about-north-star-framework"
example: true
---

# Metrics — estimate coverage and reconciliation

## North Star Metric

Share of eligible outpatient imaging requests that receive a pre-booking estimate.

| Requirement | Answer |
|---|---|
| Represents value customers actually receive | Patients get cost information before deciding |
| Precise definition, including exclusions and window | Eligible requests are fixed at intake, including non-bookers and later cancellations; self-pay excluded; measured weekly. Cancellations are reported separately. |
| Source of truth | request + booking system |
| Current value | unknown |
| Why it is a leading indicator of sustainable results | Coverage is necessary for any patient decision effect |

## North Star inputs

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
| Lagging (outcome) | Booking decisions after estimate | Share of patients who book, switch, or defer after seeing estimate | unknown | booking + survey | PM |
| Leading (behaviour) | Estimate views | Share of eligible requests with an estimate opened | unknown | product analytics | Eng |
| Health (guardrail) | Complaint rate | Surprise-bill complaints per 1,000 bookings | unknown | support | PM |
| Diagnostic | Cancellation after estimate | Share of estimated requests cancelled after viewing the estimate | unknown | booking system | PM |

## Instrumentation gaps

| Metric we need | Why we can't measure it yet | Fix |
|---|---|---|
| Non-booker estimate coverage | Request system may not capture abandonment | Add event tracking |
| Cancellation after estimate | Request system may not distinguish cancellation from abandonment | Tag cancellation reason and timestamp |
| Final patient responsibility | Needs billing reconciliation | Partner data review |

## Related

- [[PM vault/99-Playbook/Templates/Goals|Goals]] · [[PM vault/99-Playbook/Templates/Strategy|Strategy]]