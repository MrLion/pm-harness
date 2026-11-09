# Operating-Model Playbooks

Use when the vault needs to describe more than one way of working, or when a playbook lists templates that do not exist yet.

## Two axes, not four stages

- **Product lifecycle:** vision-led `0→1` vs outcome-led `1→N`.
- **Operating model:** digital transformation vs project-to-product.

Digital transformation and project-to-product change funding, team topology, governance, and metrics. They are not product-lifecycle stages, and they are not substitutes for discovery.

## Router

Ask two questions:

1. **What are you changing?** Product, portfolio, or operating model.
2. **How is work governed?** Project funding or durable product teams.

| Change | Product-model governance | Project-model governance |
|---|---|---|
| New product or market | Vision-led 0→1 | Project-to-product first, then vision-led |
| Existing product | Outcome-led 1→N | Project-to-product first, then outcome-led |
| Portfolio or enterprise capability | Digital transformation | Project-to-product + digital transformation |

## Playbooks

| Playbook | Use when | Entry artifact |
|---|---|---|
| Vision-led 0→1 | New product, new market, new value proposition | Product Vision Board |
| Outcome-led 1→N | Existing product; improve an outcome from signal | Feedback or Problem |
| Digital transformation | Portfolio or enterprise capability change | Transformation thesis + capability map |
| Project-to-product | Project funding or team topology blocks durable product work | Product taxonomy + flow baseline |

## Operating-model template set

`99-Playbook/Templates/Operating-Models/`

| ID | Template | Type | Scope |
|---|---|---|---|
| `TAX-001` | Product Taxonomy | `product-taxonomy` | portfolio |
| `FUND-001` | Funding Model | `funding-model` | portfolio or product |
| `TRANS-001` | Transformation Thesis | `transformation-thesis` | portfolio |
| `CAP-001` | Capability Map | `capability-map` | portfolio |
| `VS-001` | Value-Stream Map | `value-stream-map` | value-stream |
| `ADOPT-001` | Adoption Scorecard | `adoption-scorecard` | portfolio |
| `PORT-001` | Portfolio Roadmap | `portfolio-roadmap` | portfolio |
| `TEAM-001` | Team Topology | `team-topology` | team |
| `FLOW-001` | Flow Metrics Baseline | `flow-metrics-baseline` | value-stream |
| `DEP-001` | Dependency Map | `dependency-map` | portfolio |
| `TRANS-002` | Transition Roadmap | `transition-roadmap` | portfolio |
| `REVIEW-OM-001` | Operating-Model Review | `operating-model-review` | portfolio |

Product Taxonomy is shared across both operating-model playbooks. Funding Model uses `scope: portfolio` or `scope: product`; do not duplicate it. Operating-Model Review serves both transformation and transition reviews, with `scope` and `period` set per review.

## Flow-table contract

Every playbook flow table uses three columns: `Stage | Question | Artifact`. The Artifact cell is not a prose label; it is the playbook's navigation layer.

- Every Artifact cell must contain a wikilink. A bare `Transformation thesis` or `Product governance model` is an incomplete row even if the template exists elsewhere.
- Link to a template ID, not a generic noun. Use `[[TRANS-001-Transformation-Thesis|Transformation thesis]]`, not plain text.
- When the artifact is a section of a larger template, use a heading anchor: `TAX-001#Current inventory`, `TAX-001#Taxonomy`, `FUND-001#Decision rights`, `OPP-001#The four big risks`.
- If a flow row names an artifact with no template, create the template or explicitly map the row to the closest template section. Do not leave it as an open-ended label.
- Audit after editing: every flow-table row's third cell must contain `[[`; then run the link/anchor audit and `obsidian unresolved vault=Documents`.
- **Framework chains are tables too.** The operating chain and operating-model chain in `Frameworks.md` use the same `Stage | Question | Artifact` table contract. Do not leave them as fenced `text` arrow chains when the rest of the playbook is table-based.
- **A review artifact needs its own template.** Do not point transformation or transition review at a product release review; use `REVIEW-OM-001-Operating-Model-Review` with `scope` and `period` set per review.

## Destinations

- `09-Transformation/` — thesis, capability, value stream, adoption, portfolio roadmap
- `10-Operating-Model/` — product taxonomy, funding, team topology, flow baseline, dependencies, transition roadmap

Both are draft-only: create or propose, do not overwrite accepted operating-model decisions.

## Rules

- Operating-model templates are **structure-only**; `[FILL]` prompts are intentional. The zero-`[FILL]` check applies only to prefilled product-lifecycle templates.
- Do not reuse Problem, Opportunity, Experiment, or PRD as operating-model artifacts. They are product-level and make transformation work look like a backlog.
- A playbook's "Templates this playbook still needs" section is debt. Once the templates exist, replace that section with links to the actual template IDs.
- A README must show both product loops and route all four modes in the body. A router plus a link to the vision path, while the body still shows only the outcome loop, is a partial patch.
- When renaming a folder or template, update wikilinks, frontmatter links, Dataview `FROM` clauses, plain code paths, index notes, README/Rules/Architecture references, then grep for the old token.
- Bulk wikilink rewrites must preserve the alias exactly. Naive target replacement can append the alias twice (`PROB-001PROB-001`); after every bulk pass, scan for duplicated aliases and collapse them before committing.
- Verify the flow-table link map separately from file resolution: a row can resolve to a template and still be wrong if the Artifact cell is plain text or points to the wrong artifact.
