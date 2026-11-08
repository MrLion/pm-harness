---
type: metrics
artifact: metrics
framework: "Pichler + North Star"
status: draft
confidence: low
north_star: Share of eligible outpatient imaging requests that receive a pre-booking estimate
north_star_definition: Eligible requests include those that do not end in a booking. Pre-booking means shown before confirmation or abandonment.
north_star_source: request + booking system
updated: 2026-11-08
source: "https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/ + https://amplitude.com/books/north-star/about-north-star-framework"
example: true
---

# Metrics — estimate coverage and reconciliation

## North Star Metric

Share of eligible outpatient imaging requests that receive a pre-booking estimate.

| Requirement | Answer |
|---|---|
| Represents value customers actually receive | Patients get cost information before deciding |
| Precise definition, including exclusions and window | Eligible requests include non-bookers; excludes cancelled visits and self-pay; measured weekly |
| Source of truth | request + booking system |
| Current value | unknown |
| Why it is a leading indicator of sustainable results | Coverage is necessary for any patient decision effect |

## North Star inputs

| Input metric | Definition | Current | Owner |
|---|---|---|---|
| Eligible imaging requests | Requests for covered outpatient imaging | unknown | PM |
| Estimate delivery rate | Share of eligible requests shown an estimate | unknown | Eng |

## Guardrails

| Metric | Definition | Threshold |
|---|---|---|
| Reconciled accuracy | Share of reconciled estimates within $400 of final responsibility | ≥70% (provisional) |
| Underestimation | Share of reconciled estimates under $400 | ≤10% (provisional) |

## Supporting KPIs

| Layer | Metric | Definition | Current | Source of truth | Owner |
|---|---|---|---|---|---|
| Lagging (outcome) | Booking decisions after estimate | Share of patients who book, switch, or defer after seeing estimate | unknown | booking + survey | PM |
| Leading (behaviour) | Estimate views | Share of eligible requests with an estimate opened | unknown | product analytics | Eng |
| Health (guardrail) | Complaint rate | Surprise-bill complaints per 1,000 bookings | unknown | support | PM |

## Instrumentation gaps

| Metric we need | Why we can't measure it yet | Fix |
|---|---|---|
| Non-booker estimate coverage | Request system may not capture abandonment | Add event tracking |
| Final patient responsibility | Needs billing reconciliation | Partner data review |

## Related

- [[PM vault/00-Product/Goals|Goals]] · [[PM vault/00-Product/Strategy|Strategy]]