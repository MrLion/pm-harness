---
type: roadmap
artifact: go-roadmap
horizon: now
status: draft
updated: YYYY-MM-DD
framework: Pichler
source: https://romanpichler.com/tools/the-go-product-roadmap/
license: "CC BY-SA 4.0 — Roman Pichler, GO Product Roadmap v01/2023"
---

# GO Product Roadmap

Replaces `06-Roadmap/Now.md`, `Next.md`, `Later.md`. Rows are **goals**, not features. A feature
list with dates is the thing this template exists to prevent.

> [!quote] The five fields
> **NAME** — the name of the new release.
> **GOAL** — the outcome or benefit you want to achieve.
> **METRICS** — the measures to determine if the goal has been met.
> **DATE** — the date or time frame when a goal should be met.
> **FEATURES** — the high-level features required to meet the goal.

> [!todo] Checklist
> **Goal** — outcome-based · specific · measurable · prioritised · **single**
> **Date** — appropriately detailed (coarse for external, precise for internal) · realistic
> **Metrics** — precise · time-bound
> **Features** — goal-directed · coarse-grained (no user stories) · max 3–5 per goal
> **Name** — communicates the essence of the work

## Roadmap

| NAME | GOAL (outcome) | METRICS | DATE | FEATURES (max 3–5) |
|---|---|---|---|---|
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

## Sequencing rationale

[FILL: Why this order — dependencies, cost of delay, risk being retired first.]

## Related

- [[PM vault/00-Product/Goals|Goals]] · [[Now]] · [[Later]]

---

> [!example]- Worked example — fictional
> | NAME | GOAL | METRICS | DATE | FEATURES |
> |---|---|---|---|---|
> | Lantern 1.4 — Safe Instant Gap | Fill an open shift without the manager phoning anyone, without breaching rest rules | Gaps filled without a manager call: 22% → 60%; median time-to-fill under 15 min; illegal assignments: 0 | Q1 | Rest-period guardrail · Gap auto-offer · Rank-order eligibility · Two-tap mobile accept |
> | Lantern 1.5 — Compliance Operations | Reduce manual compliance effort while keeping the first-release guardrail | Support tickets about rest periods: −50%; audit-report preparation time: −30% | Q2 | Assignment audit log · Compliance report |
>
> **Sequencing:** the rest-period guardrail is a **non-negotiable constraint**, so it ships in 1.4
> rather than waiting for value discovery. 1.5 then reduces the operating cost of compliance with
> audit logging and reporting. Value discovery still gates the richer offering features; it does not
> gate a legal constraint.

> **Live scenario:** see [[Live-Scenario-Examples]] — a source-backed example pack, not product evidence.
