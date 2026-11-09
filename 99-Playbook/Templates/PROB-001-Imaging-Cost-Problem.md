---
type: problem
artifact: problem
id: PROB-001
status: discovery
priority: high
confidence: low
frequency: unknown
severity: unknown
created: 2026-11-08
updated: 2026-11-08
framework: none
example: true
---

# Problem — out-of-pocket cost uncertainty before outpatient imaging

## Problem Statement

Adults on employer-sponsored high-deductible health plans cannot estimate their out-of-pocket cost before booking outpatient imaging. They decide whether to book, where to book, and whether the expected cost is tolerable without a reliable estimate.

## User / Segment

[[PERSONA-001-HDHP-Imaging-Patient|PERSONA-001]]

## JTBD

[[JTBD-001-Know-Cost-Before-Booking|JTBD-001]]

## Evidence

| Type | Source | Date | Says what | Strength |
|---|---|---|---|---|
| survey | [William Blair, *Consumer-Centric Healthcare 2026*](https://www.williamblair.com/-/media/downloads/eqr/2026/williamblair_consumer-centric-healthcare-2026-update.pdf), citing Experian Health *2025 State of Patient Access* | Jan 2026 | 41% received an estimate; 71% said it was accurate to $400 | weak |
| survey | Experian Health *2025 State of Patient Access* | 2025 | 43% said they would likely postpone care without an accurate estimate | weak |
| survey | Robert Wood Johnson Foundation data, [reported by William Blair](https://www.williamblair.com/-/media/downloads/eqr/2026/williamblair_consumer-centric-healthcare-2026-update.pdf) | Jan 2026 | Among patients carrying medical debt, 66.1% had a bill in collections | weak |

> Stated intent is not observed behavior. These sources do not establish that better estimates reduce postponement. The medical-debt row is population-level and not specific to imaging.

## Frequency

Unknown. The source does not report frequency for employer-sponsored HDHP members choosing imaging.

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

- [[OPP-001-Outpatient-Imaging-Cost|OPP-001]]