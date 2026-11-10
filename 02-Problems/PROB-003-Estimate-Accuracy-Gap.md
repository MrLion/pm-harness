---
type: problem
project: pm-harness
artifact: problem
id: PROB-003
status: discovery
priority: medium
confidence: low
frequency: unknown
severity: unknown
created: 2026-11-10
updated: 2026-11-10
framework: none
---

# Problem — an estimate, when provided, is not reliable enough to support a booking decision

## Problem Statement

Patients who receive a pre-service estimate cannot rely on it to match their final responsibility. The best available survey reports that 41% of consumers received an estimate in 2025, but 29% of those estimates were not accurate within `$400`. The survey is broader than employer-sponsored HDHP members choosing imaging, and it measures perceived accuracy rather than reconciliation against an adjudicated claim.

## User / Segment

The live target group is unresolved: [Product](../00-Product/Product.md) is `confidence: none` and its TARGET GROUP is `[FILL]`.

The working segment is the illustrative HDHP imaging case in [Scenario](../00-Product/Scenario.md). It is illustrative, not product evidence.

## JTBD

No live JTBD note exists. Hypothesis: when I am shown an estimate before booking, I want it to include the relevant facility and professional charges, apply my plan correctly, and remain valid long enough to act on, so I can avoid a surprise bill.

## Evidence

| Type | Source | Date | Says what | Strength |
|---|---|---|---|---|
| survey | [William Blair, *Consumer-Centric Healthcare 2026*](https://www.williamblair.com/-/media/downloads/eqr/2026/williamblair_consumer-centric-healthcare-2026-update.pdf), citing [Experian Health *2025 State of Patient Access*](https://www.experian.com/content/dam/noindex/na/us/healthcare/state-of-patient-access-2025.pdf) | Jan 2026 | 41% received an estimate in 2025, up from 29% in 2022; 71% said it was accurate to `$400`, down from 78% in 2022 | weak for this segment; medium for the survey population |
| study | [Grant et al., JACR](https://www.jacr.org/article/S1546-1440(24)00831-7/fulltext) | 2024-10-15 | Only 15.4% of 532 patients had pre-imaging out-of-pocket cost knowledge; the paper notes cost information is not always accurate or reliable | medium for this system |
| synthesis | [RESEARCH-004](../04-Research/RESEARCH-004-Imaging-Cost-Transparency-Evidence-2024-2025.md) | 2026-11-10 | Combines estimate-accuracy and price-variation evidence | medium |

> **Not established:** no source found that reconciles imaging estimates to final patient responsibility after adjudication. The 71% figure is perceived accuracy within `$400`, not a reconciled error rate. `Evidence unavailable.`

## Next evidence

Collect 20 de-identified imaging estimates and their final adjudicated patient-responsibility amounts. For each, record:

- the services included and excluded;
- the plan assumptions and validity window;
- whether the site or service changed after the estimate;
- the final responsibility and the variance;
- whether the patient saw the estimate before or after booking.

This requires a data-access agreement and a compliance scope before collection. [COMP-003](../11-Compliance/COMP-003-Compliance-Scope.md) is still `draft` with `owner: Unassigned`, so do not collect PHI yet.

## Journey

No live journey map exists. The illustrative path is [JOURNEY-001](../99-Playbook/Templates/JOURNEY-001-Imaging-Path.md), which is a template, not evidence.

## Frequency

Unknown. The 29% inaccurate-within-`$400` figure is a survey population estimate, not a frequency for this segment or service.

## Severity

Unknown. Underestimation can produce a surprise bill; overestimation can cause a patient to delay or choose a different site. Neither effect is measured here.

## Current workaround

Patients call the insurer or provider, use a portal estimator, ask for a cash price, or compare a prior explanation of benefits. None of these guarantees the final responsibility.

## Business impact

Evidence unavailable. Candidate effects to measure: surprise-bill complaints, rebilling and call volume, write-offs, patient trust, and site switching.

## Assumptions / Unknowns

- An estimate can be made accurate enough to be useful without creating false precision.
- The patient sees the estimate before booking; the JACR study shows most do not know their cost at all.
- Differences between estimated and final responsibility are material enough to change a decision.
- A `$400` accuracy band is meaningful to patients; the survey does not establish a patient-defined tolerance.

## Related Opportunities

[Discovery Map](../03-Opportunities/Discovery%20Map.md) — no opportunity assessment exists yet.

## Buyer

Unresolved. The buyer could be an employer benefits lead, a payer product lead, or a provider finance/access lead.
