---
type: value-note
status: active
confidence: low
updated: 2026-11-09
---

# Harness Value

> [!NOTE] For humans and agents
> This is an estimate of the harness's time value, not a measured benchmark. The numbers are planning assumptions. Replace them with the user's own baseline after four weeks.

## What this page answers

> What time reduction should a senior product manager expect from this harness?

The answer depends on evidence density, team count, compliance load, and how much of the PM's week is spent writing versus aligning people.

## Baseline assumption

These estimates assume:

- one senior PM on a 40-hour week
- one or two product teams
- existing product evidence, or a willingness to create it
- the agent layer is installed and `/pm` works
- the PM uses the vault as the working system, not a separate archive
- a 2–4 week adoption ramp

They do not assume the harness replaces interviews, stakeholder alignment, legal review, or engineering delivery.

## 40-hour roll-up

This roll-up applies each reduction to its share of a 40-hour week. The per-task numbers are not
summed directly; they are weighted by time share.

| Activity | Share | Time | Reduction used | Saved |
|---|---:|---:|---:|---:|
| Docs, status, reporting | 18% | 7.2 hrs | 40% | 2.9 hrs |
| Discovery synthesis | 18% | 7.2 hrs | 30% | 2.2 hrs |
| PRD, decision, review | 18% | 7.2 hrs | 25% | 1.8 hrs |
| Meetings and alignment | 31% | 12.4 hrs | 5% | 0.6 hrs |
| Delivery and operations | 16% | 6.4 hrs | 0% | 0 hrs |
| **Total** | | **40 hrs** | | **7.5 hrs — 18.7%** |

After a 25% overlap and adoption haircut: **5.6 hours — 14%**.

## Aggregate estimate

| Measure | Estimate |
|---|---|
| Documentation and admin time | **30–45% reduction** |
| Decision-to-PRD cycle | **20–30% reduction** |
| End-to-end product delivery cycle | **5–15% reduction** |
| Senior PM weekly saving | **4–7 hours** after ramp on a 40-hour week |
| Time to first useful result | **1–2 hours** |
| Time to reliable use | **2–4 weeks** |

The first two weeks are usually net negative because setup and artifact cleanup cost time.

## Where the gain comes from

The gain is not faster typing. It comes from:

- faster context reload through `/pm status`
- fewer “where is that decision?” conversations
- fewer PRDs written before evidence exists
- fewer status meetings
- less rework from missing non-goals, metrics, or compliance
- faster onboarding of another agent or stakeholder
- traceability that survives a handoff

## Where it does not help

- customer interviews
- stakeholder negotiation
- legal and compliance approval
- engineering estimation and build
- organizational politics
- decisions that require a meeting, not a document

## Senior-PM caveat

A senior PM already writes quickly and carries context. The harness helps less with drafting and more with **consistency, recall, and preventing unsupported work**.

The larger value is quality:

- fewer decisions made on missing evidence
- fewer artifacts that cannot be traced
- less time reconstructing why a choice was made
- fewer repeated debates about scope or priority

## What changes the estimate

| Condition | Effect |
|---|---|
| Evidence already exists in the vault | Higher reduction |
| Vault is empty or full of `[FILL]` | Lower reduction; setup cost dominates |
| Health data or regulated delivery | Lower reduction; approval time dominates |
| Multiple teams and dependencies | Higher coordination value, lower drafting value |
| PM already uses a disciplined artifact system | Lower reduction, higher consistency value |
| Agent is used as a writing shortcut without gates | Higher output, higher rework risk |

## How to validate

Baseline these three numbers for four weeks before and after adoption:

| Measure | Definition |
|---|---|
| Time to PRD | Hours from opportunity decision to reviewable PRD |
| Time to status | Minutes to prepare the weekly product status |
| Rework rate | Share of artifacts returned for missing evidence, metrics, or compliance |

A fourth measure is useful if delivery is the concern:

| Measure | Definition |
|---|---|
| Decision-to-release cycle | Days from accepted decision to release record |

Do not use this page as a sales claim. It is a set of hypotheses.

## Related

- [Discovery to Delivery](Discovery-to-Delivery.md) — canonical chain
- [Agent Manual](Agent-Manual.md) — setup and reference
- [Agent Walkthrough](Agent-Walkthrough.md) — guided lab
- [Rules](Rules.md) — operating law
- [Architecture](Architecture.md) — technical contract
