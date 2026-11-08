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

## Tradeoff detail

### Speed to validated learning

Defer is the fastest path to learning: five comprehension interviews plus a data-access review can run inside one review cycle. Partner is slower because integration, terms, and data validation have to be resolved before the first patient sees an estimate. Build is slowest because it requires data access, estimate logic, reconciliation, interface work, and support before the team can test whether the estimate changes a decision.

This criterion carries the most weight because the central uncertainty is behavioural. We do not need a finished product to learn whether patients understand an estimate; we need the cheapest test that can falsify the assumption.

What would change this: a signed data-access agreement or an existing partner integration that already produces reconciled estimates. That would shorten the learning loop for build or partner and reduce the advantage of defer.

### Data-access confidence

Build has the lowest confidence: it assumes a data owner will provide usable estimate inputs and that the final patient responsibility can be reconciled. Partner has medium confidence because the partner may already hold the data, but API access, terms, and reconciliation quality are unproven. Defer does not solve data access; it is designed to establish whether access is possible before either build or partner is funded.

This is a hard feasibility gate. If estimate data cannot be accessed and reconciled, the other criteria are irrelevant.

What would change this: a signed data-access agreement, a validated partner API, or a sample reconciliation showing estimates within the agreed tolerance.

### Patient impact if correct

Build gives the most control over the patient experience: the team can decide what the estimate shows, how inclusions and exclusions are explained, and how the patient moves from estimate to booking. Partner can reuse an existing estimator, but the patient experience is constrained by the partner’s data and interface. Defer creates no patient impact now; it only buys learning.

The upside is real but unproven. The evidence supports the problem, not the claim that an estimate changes a booking decision.

What would change this: evidence that patients act differently after seeing an estimate — not just that they understand it.

### Build and operating cost

Build is the most expensive option: engineering, data integration, reconciliation, support, and ongoing maintenance. Partner is cheaper to build but carries integration work, contract management, partner management, and possibly revenue share. Defer is the cheapest because it uses interviews and data review rather than production software.

Cost matters because the team should not fund a full build before feasibility is proven. It does not outweigh learning speed, but it reinforces the case for a staged commitment.

What would change this: a reusable internal estimate service or an existing data pipeline that lowers the build cost enough to justify earlier investment.

### Partner dependency

Build has no partner dependency, though it still depends on data access. Partner creates dependency on the partner’s terms, roadmap, API stability, pricing, and willingness to support a patient-readable estimate. Defer creates no partner dependency.

This is the main strategic downside of option B. A partner can accelerate access, but it can also constrain the product and make the estimate experience someone else’s decision.

What would change this: partner terms with clear data rights, service levels, exit clauses, and control over the patient-facing explanation.

### Reversibility

Build is medium-reversible: code and data commitments can be stopped, but sunk effort and integration work are lost. Partner is medium-reversible: contracts and integrations create exit costs. Defer is highly reversible because no build or contract has started.

Reversibility receives a lower weight because all three options are still reversible at this stage. It becomes more important if a long-term contract, data migration, or public commitment is added.

What would change this: a multi-year partner contract or a build that creates switching costs for patients or providers.

### Evidence confidence

Build and partner both have low evidence confidence: the data-access, cost, and dependency assumptions are not validated. Defer has high confidence for learning because the proposed tests are cheap and executable, but it has no evidence of patient outcome.

This criterion keeps the table honest. A high-impact option with low evidence confidence should not outrank a cheap learning step just because its upside sounds larger.

What would change this: completed interviews, a data-access review, or a partner term sheet that converts an assumption into evidence.

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