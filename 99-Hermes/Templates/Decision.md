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

## Options

| Option | Description | Effort | Risk |
|---|---|---|---|
| A — build | Build a scoped estimator for one imaging type | high | high data and reconciliation risk |
| B — partner | Integrate an existing payer/provider estimator | medium | dependence on partner data and terms |
| C — defer | Run comprehension and data-access tests first | low | slow progress |

## Tradeoffs

| Dimension | A | B | C |
|---|---|---|---|
| User impact | potentially high | potentially high | none yet |
| Business impact | unknown | unknown | preserves optionality |
| Effort | high | medium | low |
| Risk | high | medium | low |
| Strategic fit | unknown | unknown | learning first |
| Reversibility | medium | medium | high |

## Decision

Proposed: defer build until comprehension and data access are proven. Evaluate partner options in parallel.

## Rationale

The evidence supports the problem, not the build. We do not yet know whether a patient-readable estimate changes a decision, or whether existing estimator data can be accessed and reconciled.

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
