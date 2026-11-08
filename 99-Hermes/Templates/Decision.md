---
type: decision
artifact: decision
id: DEC-000
status: proposed
date: YYYY-MM-DD
review_date: YYYY-MM-DD
reversibility: medium
expected_outcome: TBD
actual_outcome: Pending
framework: none
updated: YYYY-MM-DD
---

# Decision

## Example — build vs partner for cost estimator

> [!example]- Example — HDHP outpatient imaging
> **Question:** Should we build, partner, or defer on a transparent outpatient cost estimate?
> **Context:** The patient decision friction is real, but data ownership, buyer, and estimate reconciliation are unresolved.
> **Options:** Build · partner with an existing estimator · defer until feasibility and data access are proven
> **Decision gate:** No build until the data owner, buyer, and achievable estimate scope are known.
> **Why not build yet:** data access, estimate accuracy, and the buyer are unproven; a partner may get there faster.
> **Reversibility:** high
> **Review:** after feasibility check
>
> Sourced example, not product evidence.

## Question

[FILL: One sentence. If it contains "and", split it into two decisions.]

## Context

[FILL: What is true now that forces this.]

## Options

| Option | Description | Effort | Risk |
|---|---|---|---|
| A — [FILL: name] | [FILL] | [FILL] | [FILL] |
| B — [FILL: name] | [FILL] | [FILL] | [FILL] |
| C — do nothing / defer | [FILL] | [FILL] | [FILL] |

## Tradeoffs

| Dimension | A | B | C |
|---|---|---|---|
| User impact | | | |
| Business impact | | | |
| Effort | | | |
| Risk | | | |
| Strategic fit | | | |
| Reversibility | | | |

## Decision

[FILL: Chosen option.]

## Rationale

[FILL: Why — including what we are knowingly giving up.]

## Assumptions

- [FILL: If wrong, revisit.]

## Reversibility

High / Medium / Low, and the actual cost of reversal.

## Expected outcome

[FILL: Measurable. "X moves from A to B by DATE."]

## Review date

YYYY-MM-DD

## Actual outcome

Pending

---

> [!example]- Worked example — fictional
> **Question:** do we ship gap-filling first, or the full rota builder?
> **Context:** pilots ask for gap-filling; the rota builder is 3× the build.
> **Options:** A gap-filling only · B full rota builder · C do nothing, keep the spreadsheet.
> **Decision:** A. **Rationale:** retires value risk for the whole thesis in 4 weeks instead of 14;
> knowingly gives up switching cost — clinics still keep the spreadsheet for planning.
> **Reversibility:** high — the rota builder can follow without re-architecting.
> **Expected:** gaps filled without a manager call 22% → 60% by 31 Mar. **Review:** 2026-03-31.
