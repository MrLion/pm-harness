# Hermes PM

Turn customer signal and feature requests into evidence-backed problems, opportunities, decisions,
experiments and delivery briefs. **Obsidian is the workspace; `/pm` is the reasoning layer; git is
the audit trail.**

The harness will not invent evidence, silently rewrite strategy, or produce a solution brief before
validation. Empty fields and `Evidence unavailable.` are preferable to plausible fiction.

## Start in five minutes

1. Open the iCloud **`Documents`** vault in Obsidian. `PM vault` remains a folder inside it.
2. Enable **Dataview** in that parent vault: Settings → Community plugins.
3. Open **`PM vault/Dashboard.md`**. Empty tables are normal before any artifacts exist.
4. Follow **[[START-HERE]]** for your first problem-to-experiment workflow.

No paid Obsidian features or GitHub repository are required.

## Choose your starting point

| You have… | Start here |
|---|---|
| A feature idea | Convert it to a problem with `/pm discover <area>` |
| A user complaint or support signal | Create a Feedback note, then a Problem |
| Interview or market material | Add a Research note and link the claims it supports |
| Several possible opportunities | `/pm analyze OPP-001` |
| An opportunity you feel optimistic about | `/pm challenge OPP-001` |
| A defined product with goals and metrics | Fill Product, Goals and Metrics, then `/pm status` |
| No defined product yet | Start with research and problems; skip strategy and PRDs |
| Existing PRDs, roadmaps or decision documents | Add them as source material, then `/pm review` |

Replace `OPP-001` with the actual ID of your note.

## The operating loop

```text
Problem → Evidence → Opportunity → Challenge
                              ├── uncertain → Experiment → revise Opportunity
                              └── sufficient evidence
                                            ↓
                             Decision → Solution brief → Delivery → Release → Review
```

Two linked views keep the reasoning visible:

- **[[Discovery Map]]** — outcome → problems → opportunities → alternative solutions → experiments
- **[[Goals]]** — Objective and Key Results plus goal → actor → behaviour change → deliverable

## Commands

| Command | Use when | Produces |
|---|---|---|
| `/pm status` | You want current health and one next action | Read-only summary |
| `/pm discover <area>` | You need candidate problems | Research/problem notes and OST links |
| `/pm analyze OPP-001` | You need evidence, impact, alternatives and risks | Opportunity analysis |
| `/pm challenge OPP-001` | You want adversarial review | Objections, no-go/defer options, cheapest test |
| `/pm prd OPP-001` | Validation has passed | Solution brief—or a refusal explaining the gate |
| `/pm decide <question>` | A significant choice must be recorded | Proposed decision record |
| `/pm review` | You want vault-quality findings | Stale, orphaned, unsupported and map-integrity findings |

## Where does this information go?

| Information | Destination |
|---|---|
| Verbatim customer complaint | `01-Users/Feedback` |
| Interview synthesis | `04-Research/Users` |
| Market sizing or regulatory change | `04-Research/Market` |
| Competitor or workaround analysis | `04-Research/Competitors` |
| Metric, query or baseline | `04-Research/Data` |
| Evidence-backed user pain | `02-Problems` |
| Proposed opportunity and risk assessment | `03-Opportunities` |
| Outcome-to-experiment relationships | `03-Opportunities/Discovery Map.md` |
| Objective, Key Results and Impact Map | `00-Product/Goals.md` |
| North Star, inputs and guardrails | `00-Product/Metrics.md` |
| Feature idea without a problem | Do not file it yet; convert it first |
| Significant choice between options | `05-Decisions` |
| Riskiest assumption test | `07-Delivery/Experiments` |
| Validated solution brief | `07-Delivery/PRDs` |
| Shipped outcome | `07-Delivery/Releases` |
| Monthly learning and mistakes | `08-Reviews` |

Templates live in `99-Hermes/Templates/`; the index is [[_Templates]].

## Creating notes correctly

- Copy the template's **frontmatter verbatim**, then fill the values.
- Never change `type:`; Dataview uses it to route notes into tables.
- Allocate the next ID from the highest existing ID in that folder.
- Link canonical artifacts with Obsidian internal links; do not duplicate their contents.
- Delete the collapsible fictional example before using a template for real work.
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

## A useful operating cadence

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

- **[[START-HERE]]** — first guided workflow
- **[[Frameworks]]** — how Pichler, SVPG, Torres, Impact Mapping, OKRs and North Star fit together
- **[[Architecture]]** — folder mode, frontmatter, query paths, git and agent write boundaries
