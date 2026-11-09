# Start Here

Use this guide to produce your first useful artifact in about 30 minutes. The goal is **one honest
problem-to-experiment chain**, not a complete vault.

## Before you begin

Open the parent iCloud `Documents` vault and ensure Dataview is enabled. Open
`PM vault/Dashboard.md`; empty tables are expected. The technical setup is in [[Architecture]].

## 1. Capture a problem — 5 minutes

Start with something observed, not a solution:

- Weak: “Add automated shift offers.”
- Better: “Managers lose time phoning staff to cover unexpected gaps.”

Copy `99-Hermes/Templates/Problem.md` into `02-Problems/`, using the next available `PROB-NNN` ID.
Keep the frontmatter. State who experiences the problem, when, how often, and what it costs.

If you only have a feature request, run:

```text
/pm discover <the user or situation behind the request>
```

## 2. Attach evidence — 5 minutes

Use the right source artifact:

- Verbatim complaint → `01-Users/Feedback`, from [[FB-001-Imaging-Cost-Feedback]]
- Interview synthesis → `04-Research/Users`, from [[RESEARCH-001-Imaging-Cost-Transparency]]
- Metric or baseline → `04-Research/Data`

Link the source from the Problem's evidence table. If there is no evidence, leave the table empty,
set `confidence: low`, and write `Evidence unavailable.` Do not make the note look stronger than it is.

## 3. Assess the opportunity — 7 minutes

Copy [[OPP-001-Outpatient-Imaging-Cost]] into `03-Opportunities/` with the next `OPP-NNN` ID.

Answer the ten questions conservatively, then name the four risks: **value, usability, feasibility,
business viability**. Each material risk needs an owner and a test. `unknown` is a valid rating;
`no-go` is a valid recommendation.

For a structured analysis, run:

```text
/pm analyze OPP-001
```

Replace the ID with yours.

## 4. Challenge it — 5 minutes

```text
/pm challenge OPP-001
```

Expect objections: unsupported assumptions, contradictory evidence, alternative explanations, and
the cheapest way to discover you are wrong. A challenge that validates everything has not done its job.

## 5. Design the smallest experiment — 5 minutes

If a material uncertainty remains, copy [[EXP-001-Comprehension-Test]] into `07-Delivery/Experiments/`.

Name **one** risk being retired. Pre-register success, failure and kill criteria before seeing data.
Choose the cheapest test that could change the decision: interviews, a prototype, concierge run,
fake door, or a short pilot.

Do not write a PRD merely because you have a promising idea.

## 6. Link the reasoning — 3 minutes

Open [[Discovery Map]] and link the existing notes:

```text
Desired outcome
└── PROB-001
    └── OPP-001
        ├── CAND-001 → EXP-001
        └── CAND-002
```

The map is a view, not another source of truth. If a solution exists only in the map, create its
canonical artifact or remove it.

## 7. Decide only when evidence supports it

A significant choice becomes a [[DEC-001-Build-Partner-Defer]] record with options, tradeoffs, reversibility, an
expected outcome and a review date. The agent proposes; the human accepts.

Only then consider a solution brief through `/pm prd OPP-001`. If the validation gate is not met,
the refusal is the harness working correctly.

## What “good” looks like

- [ ] Problem contains no embedded solution
- [ ] Claims are linked to evidence or explicitly marked unknown
- [ ] Opportunity has all four risks and a possible no-go
- [ ] Experiment retires one primary named risk, with secondary observations kept separate
- [ ] Discovery Map links canonical notes
- [ ] Decision and solution brief wait until justified

## If you already have a defined product

You do not need to manufacture a discovery exercise. Fill [[Product]], [[PM vault/00-Product/Goals|Goals]] and [[PM vault/00-Product/Metrics|Metrics]]
with real information, then run `/pm status`. Use this guide only for the next uncertain opportunity.
