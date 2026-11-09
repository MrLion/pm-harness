---
type: playbook
artifact: playbook
status: active
updated: 2026-11-09
---

# Discovery to Delivery

> [!NOTE] For humans and agents
> This is the canonical product chain: discovery through delivery, launch, operations, and review. It owns the product transition gates. Operating-model transitions are separate and route to `Project-to-Product` or `Digital-Transformation`.

## Purpose

Use this page to answer one question:

> What must be true before we move from discovery to delivery, from delivery to operations, and from operations to the next decision?

It is a map and a gate document. It does not replace the artifacts. Each stage links to the live artifact or the template that defines its shape.

## Scope

This page covers the product path:

`Signal → Problem → Opportunity → Challenge → Experiment → Decision → PRD → Build → Release → Operate → Review`

If the team proceeds without an experiment, the decision record must state which risk is being accepted and why.

It does not cover:

- operating-model transition from project funding to durable product teams
- portfolio or enterprise capability transformation
- legal advice or compliance approval

Those are separate rails. See [Operating-model escalation](#operating-model-escalation).

## The canonical chain

| Stage | Question | Required artifact | Gate to the next stage | Owner |
|---|---|---|---|---|
| Signal | What did we observe, from whom, and when? | [Feedback](../01-Users/Feedback/_Feedback.md) or [Research](../04-Research/_Research.md) | Source, date, and evidence label exist | PM / research |
| Problem | Who experiences what problem, when, and at what cost? | [Problem template](Templates/PROB-001-Imaging-Cost-Problem.md) | Problem is evidenced, not a feature request | PM |
| Opportunity | Is this worth pursuing, and what are the four risks? | [Opportunity template](Templates/OPP-001-Outpatient-Imaging-Cost.md) | Value, usability, feasibility, and viability risks are named | PM |
| Challenge | What would make this a no-go or defer? | [Opportunity challenge](Templates/OPP-001-Outpatient-Imaging-Cost.md#adversarial-challenge) | Verdict is `go`, `no-go`, `defer`, or `Pending` with reasons | PM |
| Test | What is the cheapest evidence that retires the primary risk? | [Experiment template](Templates/EXP-001-Comprehension-Test.md) | Pre-registered criteria and result exist | PM / design |
| Decision | What are we choosing, and why? | [Decision template](Templates/DEC-001-Build-Partner-Defer.md) | Options, tradeoffs, residual risk, and review date are recorded | PM + accountable owner |
| Solution | What is the smallest coherent solution? | [PRD template](Templates/PRD-001-Imaging-Estimate.md) | Non-goals, user stories, acceptance criteria, metrics, risks, compliance impact | PM / design / eng |
| Build | Does the implementation meet the acceptance criteria? | PRD plus implementation evidence | Acceptance criteria and controls are met | Engineering |
| Release | What shipped, and what moved? | [Release template](Templates/REL-001-Imaging-Estimate-Pilot.md) | Scope, metric movement, compliance sign-off, surprises, and follow-up | PM / eng |
| Operate | Who owns it, and how do we know it is healthy? | [Metrics template](Templates/Metrics.md) plus release record | Metric is instrumented, owner named, incident path known | Operations / PM |
| Review | What did we learn, and what happens next? | [Review template](Templates/REVIEW-2027-02-Imaging-Estimate-Pilot.md) | Actual outcome vs expected; continue, pivot, or stop recorded | PM |

## Transition gates

### Discovery → Delivery

Delivery starts only when all of these are true:

- a decision record records build, partner, or defer; only build or partner proceeds
- the PRD has non-goals, user stories, acceptance criteria, metrics, risks, and compliance impact
- the primary metric has a baseline or an explicit “baseline unavailable” note
- the riskiest assumption has an experiment result or a decision to accept the risk
- the live compliance scope is approved when PII, PHI, ePHI, vendors, or health data are involved

If the decision is `defer` or `no-go`, delivery does not start. That is a successful gate, not a failure.

### Delivery → Operations

Operations accepts the product only when:

- the release record is complete
- the North Star and guardrail metrics are instrumented
- a named owner exists for operations and support
- the incident path is known
- vendor, BAA, and data-handling obligations are resolved
- known limitations and follow-ups are recorded

### Operations → Next cycle

The next cycle starts only when the review records:

- actual outcome against the expected outcome
- metric movement and guardrails
- what surprised the team
- the next decision: continue, pivot, stop, or escalate

## Minimum delivery set

The smallest set that can support a real delivery decision:

| Artifact | Why it is required |
|---|---|
| Decision record | Authorizes the investment |
| PRD | Defines what is being built and what “done” means |
| Roadmap | Shows sequence and what is deliberately not being built |
| Metrics | Defines success and guardrails |
| Release record | Records what shipped and what moved |
| Review | Converts delivery into learning |
| Live compliance scope | Blocks health-data delivery until resolved |

## Artifact map

| Artifact | Live folder |
|---|---|
| Feedback | `01-Users/Feedback/` |
| Research | `04-Research/` |
| Problem | `02-Problems/` |
| Opportunity and challenge | `03-Opportunities/` |
| Experiment | `07-Delivery/Experiments/` |
| Decision | `05-Decisions/` |
| PRD | `07-Delivery/PRDs/` |
| Release | `07-Delivery/Releases/` |
| Review | `08-Reviews/` |
| Compliance | `11-Compliance/` |

Templates live in `99-Playbook/Templates/`. A template is a shape, not evidence. Copy it into the live folder and allocate the next ID.

## Compliance rail

If the work touches PII, PHI, ePHI, vendors, or health data, the [live compliance scope](../11-Compliance/COMP-003-Compliance-Scope.md) gates delivery.

- `status: draft` or `owner: Unassigned` is a stop condition
- complete the [data inventory](Templates/Compliance/DATA-001-Data-Inventory.md), [risk assessment](Templates/Compliance/RISK-001-Privacy-Security-Risk.md), [control matrix](Templates/Compliance/CTRL-001-Control-Matrix.md), [vendor/BAA register](Templates/Compliance/VEND-001-Vendor-BAA-Register.md), and [incident plan](Templates/Compliance/INC-001-Incident-Breach-Response.md)
- record the compliance review in [COMP-002](Templates/Compliance/COMP-002-Compliance-Review.md)

## Operating-model escalation

Delivery can be blocked by the operating model. When that happens, do not force the product chain. Route to the right playbook.

| Blocker | Route |
|---|---|
| Funding is project-based and stops durable product work | [Project-to-Product](Playbooks/Project-to-Product.md) |
| Team topology or dependencies prevent ownership | [Project-to-Product](Playbooks/Project-to-Product.md) |
| Portfolio or capability change is the actual problem | [Digital-Transformation](Playbooks/Digital-Transformation.md) |
| Governance or funding model must change first | [Project-to-Product](Playbooks/Project-to-Product.md) |

## Failure modes

| Failure | What it looks like | Correction |
|---|---|---|
| PRD before evidence | Solution brief appears before problem, opportunity, or challenge | Return to discovery |
| Decision without options | Only one option is considered | Record alternatives and tradeoffs |
| Release without metrics | Launch is declared, but no metric moved | Instrument before release |
| Review without a decision | Learning is recorded, but no continue/pivot/stop choice | Record the next decision |
| Compliance as a formality | Scope is `draft` or owner is unassigned | Stop delivery |
| Operating-model problem treated as product delivery | Product team cannot own funding, teams, or dependencies | Escalate to the operating-model playbook |

## Related

- [Rules](Rules.md) — operating law
- [Architecture](Architecture.md) — technical contract
- [Agent Manual](Agent-Manual.md) — setup and command use
- [Playbooks](Playbooks/_Playbooks.md) — playbook router
- [Templates](Templates/_Templates.md) — artifact shapes
