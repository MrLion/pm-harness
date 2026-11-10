---
type: problem
project: pm-harness
artifact: problem
id: PROB-004
status: discovery
priority: medium
confidence: low
frequency: unknown
severity: unknown
created: 2026-11-10
updated: 2026-11-10
framework: none
---

# Problem — patients cannot see how site of care changes their responsibility

## Problem Statement

The same imaging study can carry very different negotiated prices depending on where it is performed, but a patient deciding where to book usually sees neither the site-level price difference nor a usable estimate of their own responsibility. Commercial facility fees for common imaging vary 3–6× more than professional fees, and hospital outpatient departments are paid substantially more than ambulatory surgical centers for the same procedures. Whether patients would use that difference, and whether it survives plan cost-sharing, is unproven.

## User / Segment

The live target group is unresolved: [Product](../00-Product/Product.md) is `confidence: none` and its TARGET GROUP is `[FILL]`.

The working segment is the illustrative HDHP imaging case in [Scenario](../00-Product/Scenario.md). It is illustrative, not product evidence.

## JTBD

No live JTBD note exists. Hypothesis: when my clinician orders a shoppable imaging study, I want to compare what the same study would cost me at the available sites, so I can choose a site that is both clinically appropriate and financially tolerable.

## Evidence

| Type | Source | Date | Says what | Strength |
|---|---|---|---|---|
| price analysis | [Philips and Whaley, *Commercial price variation for common imaging studies*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12097484) | 2025-04-30 | Facility-fee variation was 3–6× higher than professional-fee variation across 30 imaging studies; brain MRI with and without contrast had a facility-fee mean of `$1,210`, median `$792`, IQR `$515–$1,487` | medium |
| price analysis | [Maughan et al., *Commercial Insurers Paid More For Procedures At Hospital Outpatient Departments Than At Ambulatory Surgical Centers*](https://www.healthaffairs.org/doi/abs/10.1377/hlthaff.2025.00297) | 2025-10-06 | 2024 commercial prices were `$1,489` (78%) higher in hospital outpatient departments than ambulatory surgical centers across 13 procedures; the differential ranged from `$327` at Cigna to `$1,673` at UnitedHealthcare | medium |
| study | [Grant et al., JACR](https://www.jacr.org/article/S1546-1440(24)00831-7/fulltext) | 2024-10-15 | Only 15.4% of 532 patients knew their pre-imaging out-of-pocket cost; awareness is the precondition for site comparison | medium for this system |
| synthesis | [RESEARCH-004](../04-Research/RESEARCH-004-Imaging-Cost-Transparency-Evidence-2024-2025.md) | 2026-11-10 | Combines price-variation and cost-knowledge evidence | medium |

> **Unit mismatch:** the price studies report negotiated allowed amounts, not patient responsibility. A lower allowed amount does not automatically mean a lower out-of-pocket cost for a given patient. Do not present the `$1,489` differential as a patient saving.

## Next evidence

Test a two-site comparison with 8–10 patients before they book. Show the same study at an ambulatory site and a hospital outpatient site, with a plan-specific estimate, and capture:

- whether the patient notices the difference;
- whether they can explain what the difference means for their own cost;
- whether it changes where they book;
- what they do when the cheaper site has a longer wait or is farther away.

The test must not expose patients to misleading prices. The live compliance scope is still `draft`; resolve [COMP-003](../11-Compliance/COMP-003-Compliance-Scope.md) before any patient data collection.

## Journey

No live journey map exists. The illustrative path is [JOURNEY-001](../99-Playbook/Templates/JOURNEY-001-Imaging-Path.md), which is a template, not evidence.

## Frequency

Unknown. The price studies establish variation, not how often a patient faces a meaningful site choice.

## Severity

Unknown. A wrong site can produce a higher bill, but the effect on patient responsibility, delayed care, or site switching is not measured.

## Current workaround

Patients ask the provider for a cash price, call the insurer, use a hospital estimator, compare online, or accept the first available appointment.

## Business impact

Evidence unavailable. Candidate effects to measure: site steering, network leakage, patient complaints, and employer cost.

## Assumptions / Unknowns

- The patient has a real choice between sites with equivalent clinical suitability.
- The plan's cost-sharing design preserves a meaningful difference after deductible and coinsurance.
- A patient can interpret a plan-specific estimate without clinical guidance.
- A lower patient responsibility is worth a longer wait or greater travel distance.
- The buyer values site steering; the buyer is unresolved.

## Related Opportunities

[Discovery Map](../03-Opportunities/Discovery%20Map.md) — no opportunity assessment exists yet.

## Buyer

Unresolved. Candidates: employer benefits lead, payer product lead, or provider finance/access lead.
