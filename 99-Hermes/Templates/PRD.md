---
type: template
artifact: solution-brief
framework: Pichler (Product Canvas) + SVPG (prototype-as-spec)
source: https://www.romanpichler.com/tools/the-product-canvas/ + https://www.svpg.com/four-big-risks/
---

# Solution Brief (replaces "PRD")

Cagan's position: a lightweight high-fidelity prototype is a better basis for a spec than a
heavy-weight PRD, because it answers the questions a document only describes. So this note is a
**canvas + acceptance criteria that links to a prototype** — not a requirements document.

> [!warning] Validation gate
> Do not fill this in unless the opportunity has: an evidence table with at least one source,
> a challenge review, named risks with owners, and a baseline for the primary metric.
> An ungated brief is a draft for discussion, not a delivery document.

## Canvas
| Element | Content |
|---|---|
| Problem | [[PROB-000]] |
| Opportunity | [[OPP-000]] |
| Target user | [[PERSONA-000]] |
| Outcome (one sentence) | [FILL] |
| Prototype | <link to prototype / Figma / clickable> |
| Epics (big capabilities) | [FILL] |

## Non-goals
- <Be generous here — this is what prevents scope creep.>

## User stories
- As a **<segment>**, I want **<capability>**, so that **<outcome>**.

## Acceptance criteria
- [ ] <Testable statement.>
- [ ] 

## Metrics
**Primary:** <one metric, baseline → target>
**Secondary:** 
**Guardrails:** <what must not get worse>

## Risks carried forward
| Risk (value/usability/feasibility/viability) | Mitigation |
|---|---|
| | |

## Open questions
| Question | Owner | Needed by |
|---|---|---|
| | | |

## Launch plan
- Rollout · Comms · Support readiness · Rollback

## Related
- [[DEC-000]] · [[EXP-000]]

---

> [!example]- Worked example — fictional
> **Outcome:** a manager fills a same-day gap in under 15 minutes without phoning anyone.
> **Prototype:** clickable two-tap accept flow, tested with 4 staff.
> **Epics:** gap detection · eligibility ranking · offer + accept · manager fallback.
> **Non-goals:** payroll export, multi-site rota templates, shift swapping.
> **Primary metric:** gaps filled without a manager call — 22% → 60% within 30 days of launch.
> **Guardrail:** illegal assignments must not increase (baseline 0).
> **Risks carried:** value (staff may ignore offers — mitigate with reminder cadence), usability
> (accept must work one-handed — mitigate with prototype test).
