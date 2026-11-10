---
type: problem
project: pm-harness
artifact: problem
id: PROB-001
status: discovery
priority: high
confidence: low
frequency: unknown
severity: unknown
created: 2026-11-08
updated: 2026-11-09
framework: none
example: true
case_id: CASE-001
---

# Problem — out-of-pocket cost uncertainty before outpatient imaging

## Problem Statement

Adults on employer-sponsored high-deductible health plans cannot reliably predict their final patient responsibility before booking outpatient imaging. Some receive an estimate, but coverage and accuracy are uneven. How often that happens in this segment, and how close those estimates are to final responsibility, is unknown. They decide whether to book, where to book, and whether the expected cost is tolerable without a reliable number.

## User / Segment

[PERSONA-001](PERSONA-001-HDHP-Imaging-Patient.md)

## JTBD

[JTBD-001](JTBD-001-Know-Cost-Before-Booking.md)

## Evidence

| Type | Source | Date | Says what | Strength |
|---|---|---|---|---|
| survey | [William Blair, *Consumer-Centric Healthcare 2026*](https://www.williamblair.com/-/media/downloads/eqr/2026/williamblair_consumer-centric-healthcare-2026-update.pdf), citing [Experian Health *2025 State of Patient Access*](https://www.experian.com/content/dam/noindex/na/us/healthcare/state-of-patient-access-2025.pdf) | Jan 2026 | 41% received an estimate; 71% said it was accurate to $400 (29% not) | weak |
| survey | [Experian Health *2025 State of Patient Access*](https://www.experian.com/content/dam/noindex/na/us/healthcare/state-of-patient-access-2025.pdf) | 2025 | 43% said they would likely postpone care without an accurate estimate | weak |
| survey | Robert Wood Johnson Foundation data, [reported by William Blair](https://www.williamblair.com/-/media/downloads/eqr/2026/williamblair_consumer-centric-healthcare-2026-update.pdf) | Jan 2026 | Among patients carrying medical debt, 66.1% had a bill in collections | weak |

> Stated intent is not observed behavior. These sources do not establish that better estimates reduce postponement. The medical-debt row is population-level and not specific to imaging.
>
> **Segment transfer:** the survey population is broader than employer-sponsored HDHP members choosing imaging. The 41% and 71% figures are a reason to investigate this segment, not a segment estimate. Frequency and accuracy in this journey are unknown.
>
> Live research: [RESEARCH-002](../../04-Research/RESEARCH-002-William-Blair-Consumer-Healthcare-2026.md).

## Next evidence

Run 8–10 recent booking journeys, including at least 4 non-bookers. For each, record the information available at the decision point, the action taken, and the driver: uncertainty, affordability, network, urgency, or something else. Record whether the estimate changed the choice. This is the evidence that can change [DEC-001](DEC-001-Build-Partner-Defer.md).

| Journey ID | Segment | Information at decision | Action | Driver | Estimate changed choice? | Source |
|---|---|---|---|---|---|---|
| J-01 | Pending | Pending | Pending | Pending | Pending | Pending |

Use an ID, not a name. Do not record clinical details that are not needed for the decision.

Rehearsal data: [RESEARCH-003](RESEARCH-003-Mock-Booking-Journeys.md) — eight invented journeys. It tests the capture format, not the market.

## Journey

[JOURNEY-001](JOURNEY-001-Imaging-Path.md) — where the estimate appears, and where it goes stale.

## Frequency

Unknown for this segment. The source does not report frequency for employer-sponsored HDHP members choosing imaging.

## Severity

Unknown. Not measured: delayed booking, surprise bills, switching, or abandoned care.

## Current workaround

Patients call the provider or insurer, use a portal price tool, ask for a cash price, compare online, or delay the decision.

## Business impact

Evidence unavailable. Potential effects to measure: delayed bookings, call-centre volume, surprise-bill complaints, and trust.

## Assumptions / Unknowns

- The patient, not the provider or payer, is the buyer.
- The patient can access and understand an estimate before committing.
- Accuracy and coverage can be measured without exposing the patient to misleading prices.
- Employer-sponsored HDHP members are not the same population as the survey sample.

## Related Opportunities

- [OPP-001](OPP-001-Outpatient-Imaging-Cost.md)

## Buyer

Unresolved. See [PERSONA-002](PERSONA-002-Buyer-Payer.md).