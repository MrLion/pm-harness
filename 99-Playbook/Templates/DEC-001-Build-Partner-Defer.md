---
type: decision
artifact: decision
id: DEC-001
status: proposed
date: 2026-11-08
review_date: 2026-12-08
reversibility: high
expected_outcome: "By 2026-12-08, 4 of 5 patients can explain the estimate and estimate data is accessible."
actual_outcome: Pending
framework: none
updated: 2026-11-09
example: true
---

# Decision — build, partner, or defer?

## Question

Should we build, partner, or defer on a transparent outpatient cost estimate?

## Context

The patient uncertainty is credible, but data ownership, the buyer, and estimate reconciliation are unresolved. The current evidence is market-level and does not establish behavioural impact.

## Decision criteria

| Criterion | Why it matters | Weight | Evidence available |
|---|---|---|---|
| Speed to validated learning | The central uncertainty is whether patients act on an estimate. | 30% | No behavioural evidence yet |
| Data-access confidence | A build or partner option is unusable if estimate data cannot be accessed and reconciled. | 25% | Unresolved |
| Patient impact if correct | The upside is a better-informed booking decision. | 20% | Problem evidence only; outcome unproven |
| Build and operating cost | The team should not fund a full build before feasibility is proven. | 10% | Rough order only |
| Partner dependency | A partner may accelerate data access but creates terms and roadmap dependency. | 10% | Not assessed |
| Reversibility | A reversible option can be corrected cheaply if the evidence changes. | 5% | Known qualitatively |

> Weights are provisional. Do not convert them into a numerical score until the evidence behind each criterion is rated.

## Options

| Option | Description | Hard constraint it must satisfy |
|---|---|---|
| A — build | Build a scoped estimator for one imaging type | Estimate data can be accessed and reconciled |
| B — partner | Integrate an existing payer/provider estimator | Partner terms permit a patient-readable estimate |
| C — defer | Run comprehension and data-access tests first | The tests can produce a decision within one review cycle |

## Tradeoffs

| Criterion | A — Build | B — Partner | C — Defer |
|---|---|---|---|
| Speed to validated learning | slow — builds before behavioural proof | medium — integration still needs validation | fast — tests comprehension and data access first |
| Data-access confidence | low — must secure data and reconciliation | medium — depends on partner terms | unknown — designed to find out |
| Patient impact if correct | high — full control of the estimate experience | high — can reuse an existing estimator | none yet — learning only |
| Build and operating cost | high — new build and reconciliation | medium — integration and partner management | low — interviews and data review |
| Partner dependency | none | high — terms, roadmap, and data access | none |
| Reversibility | medium — code and data commitments | medium — contract and integration | high — no build started |
| Evidence confidence | low | low | high for learning; no patient outcome |

> Ratings are relative judgments based on the sources in **Research basis**; they are not quantified estimates.

## Tradeoff detail

- **Speed to validated learning** — A national patient-specific estimate pipe cannot be assumed: the Advanced Explanation of Benefits requirement for insured patients is not operational, and standards work is still in progress [S5]. Defer can test comprehension and data access inside one review cycle; build and partner wait on data access, terms, and reconciliation.
- **Data-access confidence** — CMS says payer machine-readable files are large, lack context, and often contain limited or no out-of-network allowed-amount data [S1]. Hospital price-transparency files exist, but compliance and format consistency are uneven [S2][S3]. A commercial consumer-pricing API exists, but personalized estimate coverage is limited to specific plans [S4].
- **Patient impact if correct** — The survey signal is stated intent, not observed behaviour: 43% said they would likely postpone care without an accurate estimate [S6]. Build and partner could improve the booking decision; defer creates no patient impact now.
- **Build and operating cost** — Price-transparency tooling requires significant personnel and financial investment; machine-readable files can be too large for existing hospital websites and need frequent refresh [S2]. Build carries the highest cost; partner trades build cost for integration and partner management; defer is cheapest.
- **Partner dependency** — A partner API can supply patient-specific pricing, but personalized estimates cover a limited set of plans, other plans are pre-benefit pricing only, and real patient data requires a signed BAA [S4]. That creates terms, coverage, and vendor dependency.
- **Reversibility** — This is a judgment, not an external research finding: defer is highly reversible because no build or contract has started; build and partner create sunk effort, contracts, or integration work.
- **Evidence confidence** — Build and partner rest on unvalidated data-access, coverage, and cost assumptions [S1][S4]. Defer has high confidence for learning, but no patient-outcome evidence [S6].

## Research basis

| Ref | Source | What it establishes |
|---|---|---|
| S1 | [CMS, Transparency in Coverage Final Rules](https://www.cms.gov/newsroom/fact-sheets/transparency-coverage-final-rules-cms-9882-f) | Payer price files are required, but CMS identifies large file size, missing context, misalignment with hospital data, and limited out-of-network allowed amounts as barriers. |
| S2 | [AHA, Hospital Price Transparency: Current Landscape](https://www.aha.org/fact-sheets/2026-06-05-fact-sheet-hospital-price-transparency-current-landscape-and-better-path-forward) | Hospitals must publish machine-readable files and consumer tools; tooling requires significant investment, and AEOB is not yet implemented. |
| S3 | [TechTarget, CMS price transparency challenges](https://www.techtarget.com/revcyclemanagement/feature/How-the-CMS-price-transparency-rule-challenges-hospitals) | Hospital machine-readable file posting is widespread, but compliant format adoption remains incomplete. |
| S4 | [Turquoise Health, Consumer Pricing API](https://turquoise.health/api/docs) | A commercial API can return patient-specific estimates, but personalized coverage is limited by plan, other plans use pre-benefit pricing, and real patient data requires a BAA. |
| S5 | [CMS, Progress Toward AEOB Rulemaking](https://www.cms.gov/files/document/progress-aeob-rulemaking-implementation.pdf) | The insured-patient AEOB requirement is not operational; data-exchange standards and rulemaking are still being developed. |
| S6 | [William Blair, Consumer-Centric Healthcare 2026](https://www.williamblair.com/-/media/downloads/eqr/2026/williamblair_consumer-centric-healthcare-2026-update.pdf), citing [Experian Health](https://www.experian.com/content/dam/noindex/na/us/healthcare/state-of-patient-access-2025.pdf) | 41% received an estimate; 71% said it was accurate to $400; 43% said they would likely postpone without an accurate estimate — stated intent, not observed behaviour. |

## What each option gives up

| Option | What it buys | What it gives up | Reversal trigger |
|---|---|---|---|
| A — build | Control over the estimate experience | Speed to learning, cost, and reversibility | Fewer than 4 of 5 patients understand the estimate, or data access fails |
| B — partner | Faster access to existing estimate data | Control, independence, and freedom from partner terms | Partner cannot reconcile estimates or terms block a patient-readable estimate |
| C — defer | Learning first, low cost, high reversibility | Immediate patient impact | Comprehension passes and data access is proven |

## Decision

Proposed: defer build until comprehension and data access are proven. Evaluate partner options in parallel.

## Rationale

Against the criteria, defer scores best on speed to validated learning, reversibility, and cost. It scores lowest on immediate patient impact. That is the tradeoff being accepted: we give up near-term patient impact to avoid committing build effort before comprehension and data access are proven.

## Regulatory and compliance risk

| Risk | Applies? | Evidence | Owner |
|---|---|---|---|
| HIPAA covered entity / business associate | Not assessed in example | [[COMP-001-Compliance-Scope\|COMP-001]] | Compliance owner |
| PHI / ePHI handling | None in example | [[DATA-001-Data-Inventory\|DATA-001]] | Compliance owner |
| Vendor BAA | Not applicable — no vendor selected | [[VEND-001-Vendor-BAA-Register\|VEND-001]] | Compliance owner |
| Medical-device QMS | Not applicable — not a device or SaMD | Not a device or SaMD | Compliance owner |

## Residual risk and dissent

- **Residual risk:** deferring may let a competitor establish the estimate first.
- **Dissent:** a build could produce learning faster if a data partner is already available.
- **Reversal trigger:** comprehension passes and data access is proven.

## Assumptions

- If patients cannot explain the estimate, a build is premature.
- If an existing estimator is good enough, partnership is preferable.
- If data access is unavailable, the idea is not feasible.

## Reversibility

High — no build has started.

## Expected outcome

By 2026-12-08, we know whether 4 of 5 patients can explain the estimate and whether estimate data is accessible.

## Review date

2026-12-08

## Actual outcome

Pending