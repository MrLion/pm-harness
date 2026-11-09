---
type: walkthrough
artifact: walkthrough
status: active
updated: 2026-11-09
---

# Agent Walkthrough

> [!NOTE] For humans and agents
> This is the guided lab, not the reference manual. It takes you from a cold vault to one complete discovery-to-decision chain, with checkpoints where the agent must stop instead of inventing.

## How to use this walkthrough

- Work in order. Each lesson depends on the previous checkpoint.
- Run the prompt, inspect the result, then decide whether the checkpoint passed.
- The imaging scenario is a **lab**, not evidence. If you use it without a real signal, mark the output `example: true`.
- Do not let the agent fill Product, Strategy, or accepted decisions on your behalf.
- The canonical chain and gates live in [Discovery to Delivery](Discovery-to-Delivery.md).
- The prompts use `OPP-001` as shorthand. Use the live ID the agent actually assigns; templates are not live artifacts.

## Before you start

- [ ] Obsidian is open on the parent `Documents` vault.
- [ ] Dataview is enabled.
- [ ] The agent layer is installed and `/pm status` works.
- [ ] Git is clean, or you know what is uncommitted.
- [ ] You accept that an empty vault is a valid starting state.

If `/pm` is unknown, stop and fix the bundle in [Agent Manual](Agent-Manual.md).

## Permission ladder

| Level | Agent can do | Human must do |
|---|---|---|
| 1. Read-only | `/pm status`, `/pm review`, analysis | Nothing |
| 2. Draft | Write research, problems, opportunities | Check evidence |
| 3. Gated draft | Draft PRD, decision, release | Approve the gate |
| 4. Human-only | Product, Strategy, accepted decisions, Rules | Write and approve |

Do not skip levels. The lab deliberately starts at level 1.

## Lesson 1 — Read-only

**Goal:** prove the agent can report without writing.

**Prompt:**

```text
/pm status
```

**Agent should:**

- report product health, gaps, stale artifacts, and one next action
- say what is missing rather than invent a product
- avoid creating or editing files

**You should see:** a status report, not a new note.

**Checkpoint:** no file changed.

**Common failure:** the agent produces a confident product summary from empty notes. Stop and correct it.

## Lesson 2 — Product spine

**Goal:** learn how the empty product blocks strategy and PRDs.

**Do this manually:**

1. Open [Product](../00-Product/Product.md).
2. If you do not have a real product definition, leave it `confidence: none`.
3. Open [Strategy](../00-Product/Strategy.md), [Goals](../00-Product/Goals.md), and [Metrics](../00-Product/Metrics.md).
4. Do not fill them with the imaging example unless you mark the work as a lab.

**Prompt:**

```text
/pm prd OPP-001
```

**Agent should:** refuse, or stop at the missing product spine. If the live opportunity does not exist yet, a “not found” response is also acceptable for this lesson. It should not write a PRD.

**Checkpoint:** the refusal names the missing artifact or the missing live opportunity.

**Common failure:** the agent writes a PRD from the template example. That is fabricated evidence.

## Lesson 3 — Discovery

**Goal:** turn one observation into a problem and an opportunity candidate.

**Prompt:**

```text
/pm discover "Patients on high-deductible plans cannot estimate outpatient imaging cost before booking"
```

**Agent should:**

- create or update a problem note
- create an opportunity candidate
- link evidence and name missing evidence
- keep the problem separate from a feature request

**You should see:** a problem artifact and an opportunity artifact, or a clear reason why one was not created.

**Checkpoint:** every claim has a source, a date, or `Evidence unavailable.`

**Common failure:** the agent writes “patients want a cost estimator” as the problem. That is a solution.

## Lesson 4 — Challenge

**Goal:** prove the agent can kill or defer an opportunity.

**Prompt:**

```text
/pm challenge OPP-001
```

**Agent should:**

- attack the evidence
- name the weakest assumption
- allow `go`, `no-go`, `defer`, or `Pending`
- not turn the challenge into a summary

**You should see:** a verdict with reasons in the opportunity note.

**Checkpoint:** the verdict is explicit.

**Common failure:** the challenge validates everything. That is not a challenge.

## Lesson 5 — Test and decide

**Goal:** learn the gate between “interesting” and “authorized.”

**Prompt:**

```text
/pm prd OPP-001
```

**Agent should:** refuse if the opportunity has no experiment or decision.

Then run:

```text
/pm analyze OPP-001
```

**Agent should:** list evidence gaps and the next test.

Then create the missing artifact:

- use [Experiment template](Templates/EXP-001-Comprehension-Test.md) for a test
- use [Decision template](Templates/DEC-001-Build-Partner-Defer.md) for a choice

**Prompt:**

```text
/pm decide "Build, partner, or defer the imaging estimate pilot"
```

**Agent should:** propose options, tradeoffs, residual risk, reversibility, and a review date.

**Checkpoint:** a decision record exists and a human accepts it.

**Common failure:** the agent treats `/pm decide` as permission to build. It is not. The human accepts.

## Lesson 6 — Compliance gate

**Goal:** prove health data stops delivery when the scope is unresolved.

**Prompt:**

```text
/pm prd OPP-001
```

Use a real or lab case that touches PII, PHI, ePHI, vendors, or health data.

**Agent should:** stop at the live [compliance scope](../11-Compliance/COMP-003-Compliance-Scope.md) if the status is `draft` or the owner is `Unassigned`.

**Checkpoint:** no health-data PRD is produced while the gate is open.

**Common failure:** the agent treats `COMP-001` as the live scope. `COMP-001` is the template.

## Lesson 7 — Delivery

**Goal:** produce the build contract only after the gate passes.

**Prompt:**

```text
/pm prd OPP-001
```

**Agent should produce:** a PRD with canvas, non-goals, user stories, acceptance criteria, metrics, risks, and compliance impact.

Then create the release and review records from:

- [Release template](Templates/REL-001-Imaging-Estimate-Pilot.md)
- [Review template](Templates/REVIEW-2027-02-Imaging-Estimate-Pilot.md)

**Checkpoint:** the PRD has non-goals and acceptance criteria; the release has a metric movement section; the review has a next decision.

**Common failure:** the PRD is a feature list with no non-goals and no metric.

## Lesson 8 — Recovery drill

**Goal:** learn what to do when the agent goes wrong.

Pick one failure:

| Drill | How to break it | Expected behavior |
|---|---|---|
| Empty product | Clear `00-Product/Product.md` | `/pm prd` refuses |
| Draft compliance | Set `COMP-003` to `draft` | health-data delivery stops |
| Missing source | Remove a source URL from a research note | `/pm review` flags the gap |
| Solution-shaped problem | Write “patients want an estimator” as the problem | agent rewrites it as a problem, or refuses |

**Checkpoint:** the agent names the constraint and does not produce a plausible fiction.

If the agent invents evidence, delete the output, record the violation, and rerun with the missing artifact supplied.

## Multi-agent track

Use this only after the single-agent walkthrough passes.

| Agent | Owns | Hands back |
|---|---|---|
| PM agent | Problem, opportunity, experiment, review | Decision-ready recommendation |
| Research agent | `04-Research` | Source, date, confidence |
| Compliance agent | `11-Compliance` drafts | Scope, risk, control gaps |
| Delivery agent | Experiment and release evidence | What shipped and what moved |

Handoff format:

```text
Artifact:
Question:
Sources:
Confidence:
What changed:
What is still unknown:
```

Rules:

- one writer per folder
- the PM agent integrates research; it does not let another agent rewrite Product or Strategy
- two agents never write the same artifact
- handoffs include a source and a date or they are not evidence

## What not to do

- Do not start with `/pm prd`.
- Do not ask the agent to “fill in” Product from imagination.
- Do not treat the imaging lab as market evidence.
- Do not let `/pm decide` authorize build without a human acceptance.
- Do not run two agents against the same artifact folder.
- Do not call a challenge successful because it approved everything.

## Verification

The walkthrough is complete when:

- [ ] `/pm status` runs read-only
- [ ] `/pm prd` refuses before the product or evidence gate
- [ ] `/pm discover` produces a problem, not a feature request
- [ ] `/pm challenge` can say no-go or defer
- [ ] `/pm decide` records options and residual risk
- [ ] `/pm prd` produces a PRD only after the gate passes
- [ ] health data stops at `COMP-003`
- [ ] `/pm review` catches a missing source or stale artifact
- [ ] one human accepts the decision

## Related

- [Discovery to Delivery](Discovery-to-Delivery.md) — canonical chain
- [Agent Manual](Agent-Manual.md) — setup and command reference
- [Rules](Rules.md) — operating law
- [Architecture](Architecture.md) — technical contract
- [Templates](Templates/_Templates.md) — artifact shapes
