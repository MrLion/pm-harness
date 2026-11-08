---
type: metrics
artifact: metrics
framework: "Pichler + North Star"
status: draft
confidence: none
north_star: TBD
north_star_definition: TBD
north_star_source: TBD
updated: YYYY-MM-DD
source: "https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/ + https://amplitude.com/books/north-star/about-north-star-framework"
---

# Metrics

## Example — transparent outpatient imaging

> [!example]- Example — HDHP outpatient imaging
> **North Star:** Patients who get an accurate pre-care cost estimate.
> **Definition:** Number of accurate estimates delivered before care.
> **Guardrail:** Accuracy must not decline.
>
> Sourced example, not product evidence.

## North Star Metric

[FILL]

| Requirement | Answer |
|---|---|
| Represents value customers actually receive | [FILL] |
| Precise definition, including exclusions and window | [FILL] |
| Source of truth | [FILL] |
| Current value | unknown |
| Why it is a leading indicator of sustainable results | [FILL] |

> One North Star per product. If the team can move it directly without creating customer value,
> it is probably the wrong metric.

## North Star inputs

| Input metric | Definition | Current | Owner |
|---|---|---|---|
| [FILL] | [FILL] | unknown | [FILL] |

## Guardrails

| Metric | Definition | Threshold |
|---|---|---|
| [FILL] | [FILL] | [FILL] |

## Supporting KPIs

| Layer | Metric | Definition | Current | Source of truth | Owner |
|---|---|---|---|---|---|
| Lagging (outcome) | [FILL] | | unknown | | |
| Leading (behaviour) | [FILL] | | unknown | | |
| Health (guardrail) | [FILL] | | unknown | | |

## Instrumentation gaps

| Metric we need | Why we can't measure it yet | Fix |
|---|---|---|
| [FILL] | | |

## Related

- [[PM vault/00-Product/Goals|Goals]] · [[PM vault/00-Product/Strategy|Strategy]]

---

> [!example]- Worked example — fictional
> **North Star:** shifts successfully filled per active clinic per week.
> **Definition:** a shift counts once when an eligible staff member accepts and the assignment is
> not subsequently cancelled; cancelled shifts and test accounts are excluded; measured weekly.
> **Why:** it represents the operational value clinics buy, and repeated weekly value should precede
> retention and revenue. Source: assignment event log. Current value: unknown until instrumented.
>
> **Inputs:** offer acceptance rate · median time-to-fill · active clinics with at least one gap.
> **Guardrail:** illegal assignments must remain 0; cancellation rate must not exceed baseline.
>
> **Instrumentation gap:** the metric does not exist historically. Record `unknown`; do not infer it
> from registered clinics or total offers sent.