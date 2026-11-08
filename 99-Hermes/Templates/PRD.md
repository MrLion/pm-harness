---
type: prd
artifact: solution-brief
id: PRD-000
status: draft
opportunity: "[[OPP-000]]"
candidate_id: CAND-000
decision: "[[DEC-000]]"
primary_metric: TBD
created: YYYY-MM-DD
updated: YYYY-MM-DD
framework: "Pichler (Product Canvas) + SVPG (prototype-as-spec)"
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
| Prototype | [FILL: link to prototype / Figma / clickable] |
| Epics (big capabilities) | [FILL] |

## Non-goals

- [FILL: Be generous here — this is what prevents scope creep.]

## User stories

- As a **[FILL: segment]**, I want **[FILL: capability]**, so that **[FILL: outcome]**.

## Acceptance criteria

- [ ] [FILL: Testable statement.]
- [ ] 

## Metrics

**Primary:** [FILL: one metric, baseline → target]
**Secondary:** 
**Guardrails:** [FILL: what must not get worse]

> Non-negotiable constraints are not deferred by roadmap sequencing. They are enforced from the
> first release or the initiative is not ready.

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

- Candidate source: `CAND-000` in [[OPP-000#Candidate solutions]]
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
