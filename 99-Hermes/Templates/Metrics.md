---
type: template
artifact: metrics
framework: Pichler
source: https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/
---

# Metrics / KPI Selection

| Layer | Metric | Definition | Current | Source of truth | Owner |
|---|---|---|---|---|---|
| Lagging (outcome) | [FILL] | | unknown | | |
| Leading (behaviour) | [FILL] | | unknown | | |
| Health (guardrail) | [FILL] | | unknown | | |

> [!quote] KPI selection principle
> Few, not many. Each KPI needs a precise definition, a data source, and a decision it informs.

## Instrumentation gaps
| Metric we need | Why we can't measure it yet | Fix |
|---|---|---|
| [FILL] | | |

## Related
- [[Goals]]

---

> [!example]- Worked example — fictional
> | Layer | Metric | Definition | Current | Source |
> |---|---|---|---|---|
> | Lagging | Clinics retained at 6 months | Active = ≥1 shift filled that month | unknown | billing + event log |
> | Leading | Gaps filled without manager call | (gaps auto-filled) / (all gaps) | 22% | event log |
> | Health | Illegal-assignment attempts blocked | Count per 100 assignments | 0 | guardrail log |
>
> **Gap:** retention has no historical baseline — product launched 6 weeks ago. Fix: wait for the
> first cohort rather than invent a number.
