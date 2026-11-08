---
type: decision
artifact: decision
id: DEC-001
status: proposed
date: 2026-11-08
review_date: 2026-12-08
reversibility: high
expected_outcome: TBD
actual_outcome: Pending
framework: none
updated: 2026-11-08
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