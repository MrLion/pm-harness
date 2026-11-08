---
type: problem
artifact: problem
id: PROB-000
status: discovery
priority: unprioritized
confidence: low
frequency: unknown
severity: unknown
created: YYYY-MM-DD
updated: YYYY-MM-DD
framework: none
---

# Problem

> [!warning] Problem ≠ feature request
> "We need X" is not a problem. Convert it before writing anything else. If the statement contains
> a solution noun, rewrite it.

> [!example]- Example — US healthcare consumer (from William Blair report)
> **Scenario:** An insured consumer with a high-deductible plan is choosing between outpatient imaging providers.
> **Problem they hit:** They don't know the full out-of-pocket cost before booking. In the report, 70% want the
> price before the procedure, but estimates are received by only 41% and accuracy is dropping.
> **Fill example:**
> - **Who:** Adults on employer-sponsored HDHP plans
> - **What:** Can’t estimate the real out-of-pocket cost before imaging
> - **Evidence:** William Blair *Consumer-Centric Healthcare 2026*; Experian Health 2025
> - **Impact:** 43% postpone care without an accurate estimate; 66% of people with debt are in collections
>
> This is **not** real product evidence; it is a sourced example to show how to fill the template.

> [!todo] Ambiguous fields — how to fill
> | Field | Meaning | If unsure |
> |---|---|---|
> | status | `discovery`, `validated`, or `resolved` | keep `discovery` until evidence confirms it |
> | priority | `unprioritized / low / medium / high` | leave `unprioritized` until scoring is discussed |
> | confidence | `none / low / medium / high` | reflect the evidence, not optimism |
> | severity | cost in time / money / risk / abandonment | use `unknown` until measured |
> | frequency | how often it occurs | use a range if exact number unavailable |
> | evidence | source, date, and what it says | no source = unsupported claim |
> | current workaround | what users do today | “nothing” is valid |
> | business impact | what it costs the org | if unknown, say `Evidence unavailable.` |


## Problem Statement

[FILL: Who experiences what problem, under what circumstances, and why it matters. No solution language.]

## User / Segment

[[PERSONA-000]]

## JTBD

[[JTBD-000]]

## Evidence

| Type | Source | Date | Says what | Strength |
|---|---|---|---|---|
| interview / metric / ticket / review / support | [[RESEARCH-000]] | | | weak |

> Empty evidence table → this is a hypothesis. Set `confidence: low` and say so out loud.

## Frequency

[FILL: How often, per user per period.]

## Severity

[FILL: What it costs when it happens: time, money, risk, abandonment.]

## Current workaround

[FILL: What users do today instead. "Nothing" is a signal.]

## Business impact

[FILL: What it costs us. Evidence, not vibes.]

## Assumptions / Unknowns

- 

## Related Opportunities

- [[OPP-000]]

---

> [!example]- Worked example — fictional
> **Statement:** Practice managers in 5–20-staff clinics lose 3–6 hours a week phoning staff to
> cover unexpected shift gaps, and still open short-staffed about one morning a month.
> **Frequency:** 2–4 gaps per clinic per week. **Severity:** ~6 calls per gap, 45-min median; a
> missed open costs half a day of appointments.
> **Workaround:** a personal WhatsApp list of reliable staff, ordered from memory.
> **Evidence:** 11 interviews (9 describe the phone tree), 3 weeks of support tickets.
> Confidence: medium.
