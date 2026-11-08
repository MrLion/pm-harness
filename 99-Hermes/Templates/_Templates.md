# Templates

Every template has four layers: **the artifact structure** → **the source's field definition**
(quoted, with attribution) → **the checklist criteria** used to judge a filled note → **a
collapsible worked example**. The example is a fictional product ("Lantern", a clinic shift
scheduling tool) used consistently across all templates so the traceability chain is visible.

Delete the `[!example]` block before using a template for real work.

| Template | Use for | Framework | Source |
|---|---|---|---|
| [[99-Hermes/Templates/Product-Vision-Board|Product-Vision-Board]] | `00-Product/Product.md` | Pichler | [Vision Board](https://romanpichler.com/tools/product-vision-board/) |
| [[99-Hermes/Templates/Strategy|Strategy template]] | `00-Product/Strategy.md` | Pichler | [Strategy model](https://romanpichler.com/blog/my-product-strategy-model/) |
| [[99-Hermes/Templates/Goals|Goals template]] | `00-Product/Goals.md` | Pichler + OKR + Impact Mapping | [Goal-setting](https://romanpichler.com/blog/leading-through-shared-goals/) · [Impact Mapping](https://www.impactmapping.org/) |
| [[99-Hermes/Templates/Metrics|Metrics template]] | `00-Product/Metrics.md` | Pichler + North Star | [KPI selection](https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/) · [North Star](https://amplitude.com/books/north-star/about-north-star-framework) |
| [[GO-Roadmap]] | `06-Roadmap/` | Pichler | [GO Product Roadmap](https://romanpichler.com/tools/the-go-product-roadmap/) |
| [[Persona]] | `01-Users/Personas/` | Pichler | [Persona Template](https://www.romanpichler.com/the-persona-template/) |
| [[Discovery-Map]] | `03-Opportunities/Discovery Map.md` | Torres | [Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/) |
| [[Opportunity]] | `03-Opportunities/` | SVPG | [Opportunity assessment](https://www.svpg.com/assessing-product-opportunities/) |
| [[Experiment]] | `07-Delivery/Experiments/` | SVPG | [Four big risks](https://www.svpg.com/four-big-risks/) |
| [[PRD]] | `07-Delivery/PRDs/` | Pichler canvas + SVPG | [Product Canvas](https://www.romanpichler.com/tools/the-product-canvas/) |
| [[Problem]] | `02-Problems/` | — | shared evidence-backed problem layer |
| [[Research]] | `04-Research/` | — | evidence layer for the whole model |
| [[Feedback]] | `01-Users/Feedback/` | — | raw signal, verbatim quotes and account frequency |
| [[Release]] | `07-Delivery/Releases/` | Pichler | GO goal and measured result after delivery |
| [[Decision]] | `05-Decisions/` | — | framework-neutral decision record |
| [[Review]] | `08-Reviews/` | Pichler + SVPG | goal vs outcome, risk retired vs not |
| [[JTBD]] | `01-Users/JTBD/` | — | supporting lens for Problem and Persona |

## Frontmatter contract

Every Dataview table in this vault reads **frontmatter keys**, not headings. `TABLE a, b` renders
columns from the `a:` and `b:` keys of each note; `WHERE type = "x"` filters on the `type:` key;
`SORT date DESC` uses the frontmatter `date:`, not the file's modification time.

Which is why every template's frontmatter **is** the instance schema — a note created from it is
queryable immediately. Copy the frontmatter verbatim; never retype it.

| Key | Allowed values → how it is used |
|---|---|
| `type` | one artifact type per note; every `WHERE type = "…"` filter depends on it |
| `id` | `PROB-003` style; note identity and wikilink target |
| `status` | artifact-specific: proposed/accepted/reversed; draft/complete; planned/completed; released |
| `confidence` | `none` → `low` → `medium` → `high`; dashboards sort by that rank, not alphabetically |
| `date` / `updated` / `review_after` / `review_date` | date fields used for sorting and overdue reporting |
| `category` (research) | `market` · `competitor` · `user` · `data` |
| `reliability` (research) | `weak` → `medium` → `strong`; used by weak-evidence reporting |
| `severity` / `priority` (problem) | `low` · `medium` · `high` and `unknown`/`unprioritized`; sorted by rank |
| `recommendation` (opportunity) | `go` · `no-go` · `defer` · `Pending` |
| `risk_type` (primary risk) | `value` · `usability` · `feasibility` · `viability` |
| `risk_owner` | `PM` · `Design` · `Eng` · named role |
| `candidate_id` (prd) | stable Opportunity candidate row ID, e.g. `CAND-001`; the Discovery Map links the same row |
| `opportunity` / `decision` (PRD) | quoted Obsidian links, e.g. `"[[OPP-000]]"`, so traceability resolves |
| `primary_metric` (prd) | gate on "no baseline, no brief" |

**Templates carry their real `type`, not `type: template`.** That is deliberate: the schema stays
correct when you copy the file, and these files sit in `99-Hermes/`, outside every folder-scoped
query, so they never appear in a table. Do not move a template into `02-Problems/` or similar.

## Folder mode

This vault is a folder inside a larger Obsidian vault, so every query names its path
(`FROM "PM vault/05-Decisions"`). If you ever open `PM vault` as its own vault, strip the
`PM vault/` prefix from all 33 `FROM` clauses or the tables will match nothing.

## Attribution

Pichler field definitions and checklists are quoted from the official tools, **CC BY-SA 4.0**
(© Roman Pichler / Pichler Consulting Limited). The Pichler sections of every template that quotes
them are therefore share-alike. SVPG material is quoted from Marty Cagan's published articles
(© Silicon Valley Product Group), quoted for reference rather than reproduced in bulk.

## How the frameworks fit together

| Layer | Methods | Canonical artifacts |
|---|---|---|
| **Direction and planning** | Pichler | Product Vision Board, Strategy, GO Roadmap, Persona, solution canvas |
| **Discovery and validation** | SVPG + Torres | Problem, Opportunity assessment, Discovery Map, Experiment |
| **Alignment and causality** | OKRs + Impact Mapping | Goals: one Objective, measurable KRs, Why → Who → How → What |
| **Measurement and learning** | North Star + Pichler KPI selection | Metrics, Release, Review |

Pichler supplies durable direction. SVPG supplies the evidence and risk gate. Torres's Opportunity
Solution Tree links desired outcomes to problems, alternative solutions and assumption tests without
duplicating their canonical notes. OKRs and Impact Mapping align each horizon around one Objective
and explicit behaviour change. North Star adds one customer-value metric with inputs and guardrails.

The operating chain is therefore:

`Vision → Objective / North Star → Impact Map → Discovery Map → Evidence and risk gate →
Decision → Solution brief → Release → Review`.

Impact Mapping reference materials are CC BY 4.0 (Gojko Adzic). Torres and Amplitude material is
linked and summarized rather than reproduced in bulk.
