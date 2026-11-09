---
type: rules
status: active
version: 4
updated: 2026-11-09
---

# PM Rules

> [!NOTE] For AI agents only
> This page is the `/pm` layer’s operating law. Humans author and approve it; the agent enforces it. Humans start at [README](../README.md).

Operating law for the `/pm` layer. These are constraints, not suggestions.

## Operating modes

- **Vision-led 0→1** — starts from a product thesis and target future.
- **Outcome-led 1→N** — starts from customer signal about an existing product.
- **Digital transformation** — changes portfolio capabilities, value streams, and funding.
- **Project-to-product** — changes funding, team topology, flow, and governance.
- **Compliance rail** — cross-cutting; applies whenever PII, PHI, ePHI, vendors, or health data are involved.

## 1. Route before recommending
Choose the mode from [_Playbooks](Playbooks/_Playbooks.md) before applying any rule. A product rule must not be forced onto
transformation or operating-model work.

## 2. Problem before solution — outcome-led only
For an existing product, convert “we need X” into “what problem would X solve?” and refuse to advance
until that is answered.

For a new product, the entry point is a **thesis**, not a problem backlog. Do not force vision-led work
into a problem-first sequence.

## 3. Evidence before confidence
Label every claim: **Fact** / **Observation** / **Hypothesis** / **Assumption** / **Opinion**.
Never present a hypothesis as a fact. `confidence:` frontmatter must reflect the weakest load-bearing
claim, not the strongest.

## 4. Empty product definition blocks strategy
If `00-Product/Product.md` is `[FILL]` or `confidence: none`, say so explicitly. That blocks strategy,
roadmap, decision, and PRD recommendations. It does not block research, problems, opportunities,
experiments, or compliance work.

## 5. Compliance scope before health data
Before handling PII, PHI, ePHI, vendor data, or health data, determine:

- covered-entity or business-associate status
- PII / PHI / ePHI / de-identified / limited-data-set status
- BAA requirement
- medical-device or SaMD classification
- applicable jurisdictions

If unresolved, write `Compliance scope unresolved` and stop. Do not guess regulatory applicability.

## 6. Discovery is separate from delivery
The product gates are in [Discovery to Delivery](Discovery-to-Delivery.md). Do not bypass them.
Transformation and operating-model work use their own gates, not a product PRD gate.

## 7. Challenge every significant recommendation
Each one carries: assumptions, contradicting evidence, alternatives considered, risks, and unknowns.
A recommendation missing any of the five is incomplete, not concise.

## 8. Cheapest safe experiment first
When uncertainty is high, recommend the cheapest test that could materially reduce it before
recommending a build. The test must also satisfy the data-handling and compliance constraints.

## 9. Decisions are explicit and recorded
A Decision Record is required when a decision:

- costs more than a week of work
- is hard to reverse
- changes regulatory posture or data handling
- changes a vendor or BAA obligation
- changes funding, team topology, or governance

Verbal decisions do not exist.

## 10. Traceability is mandatory
Traceability chains are defined in [Architecture](Architecture.md#identity-and-traceability). The product chain is canonical in [Discovery to Delivery](Discovery-to-Delivery.md).

Every artifact reference is a relative Markdown link that resolves in both Obsidian and GitHub. An orphaned artifact is a defect reported in
`/pm review`.

## 11. Never fabricate evidence
If information is unavailable, write `Evidence unavailable.` Do not invent customer quotes, metrics,
market sizes, competitor behaviour, regulatory applicability, or dates.

Pre-filled template examples are illustrative. Never cite an example row, ID, quote, or metric as
product evidence.

## 12. Scores support judgement, not replace it
A score is a conversation starter. Never let a number close a discussion that evidence has not closed.

## 13. Keep the knowledge base current
When new information materially changes understanding, update the artifact — frontmatter `updated:`
included — rather than leaving the stale claim in place.

## 14. Staleness is a finding
Flag artifacts past `review_after` / `review_cadence_days`, artifacts with missing `updated:`,
opportunities with no `review_after`, accepted decisions with no `review_date`, decisions with no
recorded expected outcome, metrics with no baseline, compliance reviews that are overdue, and
transformation or operating-model reviews that have not run.

## 15. Declare the framework
Every artifact’s frontmatter names its framework: `Pichler`, `SVPG`, `Torres`, `North Star`,
`Impact Mapping`, `OKR`, `Team Topologies`, `Flow Framework`, `Transformation thesis`,
`HIPAA/compliance`, `none`, or a declared combination. Do not invent a hybrid structure silently.

## 16. No-go is an answer
A Product Opportunity Assessment may recommend **no-go**, and that is a successful outcome — it saved
the build. A `/pm challenge` run that never produces a no-go, a defer, or a kill is broken, not thorough.

## 17. Risks need owners
For product opportunities, name the four SVPG risks — value, usability, feasibility, business
viability — and state which is load-bearing.

For transformation and operating-model work, name adoption, funding, team/flow, and dependency risks.
For compliance work, name privacy, security, and regulatory risks.

Compliance risk is not forced into the four SVPG risks. A risk with no owner and no test is decoration.

## 18. One goal at a time
Per Pichler: a roadmap row carries a single goal. Two concurrent goals in one row means the row is
really two rows, or the goal is not yet understood.

## 19. Maps are views, not duplicate knowledge
The Opportunity Solution Tree links canonical Goals, Problems, Opportunities, solution briefs, and
Experiments. Pre-validation solution candidates live as `CAND-NNN` rows in the Opportunity’s
`Candidate solutions` section; every map branch names that exact ID and links its parent Opportunity
section. A validated `CAND-` row links the PRD created from it via `candidate_id:`.

Never create a candidate, solution, or opportunity that exists only in the map.

## 20. Goals and metrics remain falsifiable
An OKR has one Objective per horizon and measurable Key Results. A North Star Metric represents
customer value, has a precise definition and source, and is supported by inputs and guardrails.
Unknown baselines stay `unknown`; never invent them.

## 21. Respect the write boundary
**Free to write:** `04-Research`, `02-Problems`, `03-Opportunities`, `07-Delivery/Experiments`,
`08-Reviews`, `99-Playbook/Templates`, `99-Playbook/Playbooks`, `99-Playbook/Future-Problem-Statements.md`.

**Draft only — propose, do not overwrite:** `07-Delivery/PRDs`, `06-Roadmap`,
`09-Transformation`, `10-Operating-Model`, `11-Compliance`.

**Human-approved only:** `00-Product`, `05-Decisions`, `README.md`, `99-Playbook/Rules.md`,
`99-Playbook/PM.md`, `99-Playbook/Visual-Standards.md`.

## 22. Answer before writing
Answer a direct question about an artifact or output before mutating anything. “Why…”, “what’s the
difference…”, and “did I say…” are questions, not write requests.

## 23. IDs live in filenames
Follow [Architecture](Architecture.md#identity-and-traceability). Never invent or reuse an ID.
