# PM Playbook

**Obsidian is the workspace. `/pm` is the reasoning layer. Git is the audit trail.**

This playbook supports four ways of working, but they answer different questions:

- **Product lifecycle:** are we creating a new product, or improving an existing one?
- **Operating model:** are we changing a product, a portfolio, or how the organization funds and staffs product work?

The harness will not invent evidence, silently rewrite strategy, or produce a solution brief before
validation. Empty fields and `Evidence unavailable.` are preferable to plausible fiction.

## Start in five minutes

1. Open the iCloud **`Documents`** vault in Obsidian. `PM vault` remains a folder inside it.
2. Enable **Dataview** in that parent vault: Settings → Community plugins.
3. Open **`PM vault/Dashboard.md`**. Empty tables are normal before any artifacts exist.
4. Choose one playbook below and follow its flow.

No paid Obsidian features or GitHub repository are required.

## Choose your playbook

Ask two questions:

1. **What are you changing?** A product, a portfolio, or the operating model.
2. **How is work governed?** Project funding or durable product teams.

| What you are changing | Product-model governance | Project-model governance |
|---|---|---|
| New product or new market | [[Vision-Led-0-to-1]] | [[Project-to-Product]] first, then [[Vision-Led-0-to-1]] |
| Existing product | [[Outcome-Led-1-to-N]] | [[Project-to-Product]] first, then [[Outcome-Led-1-to-N]] |
| Portfolio or enterprise capability | [[Digital-Transformation]] | [[Project-to-Product]] + [[Digital-Transformation]] |

These are not four stages of one loop. **Vision-led** and **outcome-led** are product-lifecycle
paths. **Digital transformation** and **project-to-product** are operating-model transitions that
change funding, team topology, governance, and metrics before product discovery can run cleanly.

If you are unsure, start with the product-lifecycle question. Use project-to-product only when
funding or team structure blocks durable product work.

## The two product loops

### Vision-led 0→1

Use when the product or market does not exist yet, or when the team is entering a new segment with a
new value proposition.

```text
Vision → Target group & need → Why now / why us → Strategy
      → Goals & North Star → Opportunity map → What would have to be true
      → Concept tests → MVP → Launch → Review
```

**Entry artifact:** [[PM vault/99-Playbook/Templates/Product-Vision-Board|Product Vision Board]]

**Gate:** a PRD is produced only after the riskiest assumptions have concept-test evidence.

**Full playbook:** [[Vision-Led-0-to-1]]

### Outcome-led 1→N

Use when the product already exists and the work is to improve an outcome, respond to customer
signal, or decide what to build next.

```text
Signal → Problem → Evidence → Opportunity → Challenge
                              ├── uncertain → Experiment → revise Opportunity
                              └── sufficient evidence
                                            ↓
                             Decision → Solution brief → Delivery → Release → Review
```

**Entry artifact:** [[PM vault/99-Playbook/Templates/FB-001-Imaging-Cost-Feedback|Feedback]] or a
Problem note.

**Gate:** a solution brief is written only after the opportunity has evidence, a challenge, and a
defined metric baseline.

**Full playbook:** [[Outcome-Led-1-to-N]]

Both loops use the same artifacts. The difference is the entry point and the evidence gate.

## Operating-model transitions

These are not product lifecycle stages. They change the conditions under which product work happens.

| Transition | Use when | First artifact | Playbook |
|---|---|---|---|
| Digital transformation | The unit of change is a portfolio or enterprise capability | Transformation thesis and capability map | [[Digital-Transformation]] |
| Project-to-product | Project funding, team topology, or governance blocks durable product teams | Product taxonomy and flow baseline | [[Project-to-Product]] |

## Two linked views

Both loops keep the reasoning visible through the same two views:

- **[[Discovery Map]]** — outcome → problems → opportunities → alternative solutions → experiments
- **[[PM vault/00-Product/Goals|Goals]]** — Objective and Key Results plus goal → actor → behaviour change → deliverable

## Commands

| Command | Use when | Produces |
|---|---|---|
| `/pm status` | You want current health and one next action | Read-only summary |
| `/pm discover <area>` | You need candidate problems | Research/problem notes and OST links |
| `/pm analyze OPP-001` | You need evidence, impact, alternatives and risks | Opportunity analysis |
| `/pm challenge OPP-001` | You want adversarial review | Objections, no-go/defer options, cheapest test |
| `/pm prd OPP-001` | Validation has passed | Solution brief — or a refusal explaining the gate |
| `/pm decide <question>` | A significant choice must be recorded | Proposed decision record |
| `/pm review` | You want vault-quality findings | Stale, orphaned, unsupported and map-integrity findings |

Replace `OPP-001` with the actual ID of your note.

## Where information goes

| Information | Destination |
|---|---|
| Vision, target group and needs | `00-Product/Product.md` |
| Strategy, differentiation and why now / why us | `00-Product/Strategy.md` |
| Objective, Key Results and Impact Map | `00-Product/Goals.md` |
| North Star, inputs and guardrails | `00-Product/Metrics.md` |
| Verbatim customer complaint | `01-Users/Feedback` |
| Interview synthesis | `04-Research/Users` |
| Market sizing or regulatory change | `04-Research/Market` |
| Competitor or workaround analysis | `04-Research/Competitors` |
| Metric, query or baseline | `04-Research/Data` |
| Evidence-backed user pain | `02-Problems` |
| Proposed opportunity and risk assessment | `03-Opportunities` |
| Outcome-to-experiment relationships | `03-Opportunities/Discovery Map.md` |
| Feature idea without a problem | Park it; convert it to a problem before delivery |
| Significant choice between options | `05-Decisions` |
| Riskiest assumption test | `07-Delivery/Experiments` |
| Validated solution brief | `07-Delivery/PRDs` |
| Shipped outcome | `07-Delivery/Releases` |
| Monthly learning and mistakes | `08-Reviews` |

Templates live in `99-Playbook/Templates/`; the index is [[_Templates]].

## Creating notes correctly

- Copy the template's **frontmatter verbatim**, then fill the values.
- Never change `type:`; Dataview uses it to route notes into tables.
- Allocate the next ID from the highest existing ID in that folder.
- Link canonical artifacts with Obsidian internal links; do not duplicate their contents.
- Templates carry an illustrative example. Replace it with your own evidence before using the note for real work.
- Leave unknowns as `unknown`; do not invent baselines, quotes, dates or market figures.
- Update `updated:` whenever the note materially changes.

## Dashboard and troubleshooting

| Symptom | Meaning | Action |
|---|---|---|
| Grey query blocks | Dataview is not loading | Enable it in the parent `Documents` vault |
| Empty tables | Usually no artifacts yet | Add one correctly typed note |
| Note missing from a table | Wrong `type`, folder or query prefix | Check frontmatter and the `PM vault/` path |
| Blank column | Frontmatter key missing | Copy the template schema |
| New note not immediately visible | Obsidian index lag | Wait a few seconds |
| Stale item shown | Frontmatter `updated:` is old | Review and update the artifact |
| Git behaves unexpectedly | `.git` is a pointer file | Do not `git init` or clone here |

## Operating cadence

**Vision-led**

- **Monthly:** review the vision, target group, why now / why us, and the riskiest assumptions.
- **Before build:** require concept-test evidence and a decision record.
- **Quarterly:** compare the current bet with the original thesis.

**Outcome-led**

- **As signal arrives:** capture Feedback, Research and Problems.
- **Weekly:** `/pm status`; challenge the leading opportunity; review experiments.
- **Before committing:** opportunity assessment, alternative solutions, evidence and decision record.
- **After shipping:** Release note with metric movement and surprises.
- **Monthly:** `/pm review` plus a Review note covering goals, risks and mistakes.

## Permissions and privacy

Research, problems, opportunities, experiments and reviews are agent-writable. PRDs and roadmap
changes are drafts. Product strategy and accepted decisions require human approval; see [[Rules]].

Customer quotes and account names can be sensitive. Remove unnecessary personal information before
putting feedback into an iCloud-synced vault.

## Learn more

- **[[_Playbooks]]** — the four playbooks and when to use each
- **[[Vision-Led-0-to-1]]** — new product or new market
- **[[Outcome-Led-1-to-N]]** — existing product
- **[[Digital-Transformation]]** — portfolio or enterprise capability change
- **[[Project-to-Product]]** — funding, team topology, and governance transition
- **[[START-HERE]]** — first guided workflow for the outcome-led path
- **[[Frameworks]]** — how Pichler, SVPG, Torres, Impact Mapping, OKRs and North Star fit together
- **[[Architecture]]** — folder mode, frontmatter, query paths, git and agent write boundaries
