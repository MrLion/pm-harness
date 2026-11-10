# Templates

Product-lifecycle templates have four layers: **the artifact structure** → **the source's field
definition** (quoted, with attribution) → **the checklist criteria** used to judge a filled note →
**a worked example**. The example is the fictional HDHP outpatient-imaging scenario used consistently
across all templates so the traceability chain is visible.

Operating-model templates are structure-only: they use `[FILL]` prompts because portfolio,
capability, funding, and team facts must come from real evidence.

Replace the example values with your own product facts before using a product template for real work.
The case spine is [Scenario](../../00-Product/Scenario.md), `case_id: CASE-001`. Every product template
carries that `case_id` so the worked example stays traceable.

Compliance links in the case point to `COMP-001` as a structure template. A live case must use the
live `11-Compliance/COMP-003-Compliance-Scope.md`; a template is not approval.

| Template | Use for | Framework | Source |
|---|---|---|---|
| [Product-Vision-Board](Product-Vision-Board.md) | `00-Product/Product.md` | Pichler | [Vision Board](https://romanpichler.com/tools/product-vision-board/) |
| [Strategy template](Strategy.md) | `00-Product/Strategy.md` | Pichler | [Strategy model](https://romanpichler.com/blog/my-product-strategy-model/) |
| [Goals template](Goals.md) | `00-Product/Goals.md` | Pichler + OKR + Impact Mapping | [Goal-setting](https://romanpichler.com/blog/leading-through-shared-goals/) · [Impact Mapping](https://www.impactmapping.org/) |
| [Metrics template](Metrics.md) | `00-Product/Metrics.md` | Pichler + North Star | [KPI selection](https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/) · [North Star](https://amplitude.com/books/north-star/about-north-star-framework) |
| [GO-Roadmap](GO-Roadmap.md) | `06-Roadmap/` | Pichler | [GO Product Roadmap](https://romanpichler.com/tools/the-go-product-roadmap/) |
| [Dashboard-Example](Dashboard-Example.md) | `Dashboard.md` | Dataview | working dashboard over the pre-filled templates |
| [PERSONA-001-HDHP-Imaging-Patient](PERSONA-001-HDHP-Imaging-Patient.md) | `01-Users/Personas/` | Pichler | [Persona Template](https://www.romanpichler.com/the-persona-template/) |
| [PERSONA-002-Buyer-Payer](PERSONA-002-Buyer-Payer.md) | `01-Users/Personas/` | Pichler | buyer hypothesis for an unresolved buyer |
| [JOURNEY-001-Imaging-Path](JOURNEY-001-Imaging-Path.md) | `01-Users/Journey-Maps/` | Journey mapping | discovery view over the case |
| [Discovery-Map](Discovery-Map.md) | `03-Opportunities/Discovery Map.md` | Torres | [Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/) |
| [OPP-001-Outpatient-Imaging-Cost](OPP-001-Outpatient-Imaging-Cost.md) | `03-Opportunities/` | SVPG | [Opportunity assessment](https://www.svpg.com/assessing-product-opportunities/) |
| [EXP-001-Comprehension-Test](EXP-001-Comprehension-Test.md) | `07-Delivery/Experiments/` | SVPG | [Four big risks](https://www.svpg.com/four-big-risks/) |
| [PRD-001-Imaging-Estimate](PRD-001-Imaging-Estimate.md) | `07-Delivery/PRDs/` | Pichler canvas + SVPG | [Product Canvas](https://www.romanpichler.com/tools/the-product-canvas/) |
| [PROB-001-Imaging-Cost-Problem](PROB-001-Imaging-Cost-Problem.md) | `02-Problems/` | — | shared evidence-backed problem layer |
| [RESEARCH-001-Imaging-Cost-Transparency](RESEARCH-001-Imaging-Cost-Transparency.md) | `04-Research/` | — | evidence layer for the whole model |
| [RESEARCH-003-Mock-Booking-Journeys](RESEARCH-003-Mock-Booking-Journeys.md) | `99-Playbook/Templates/` | — | synthetic rehearsal of the eight-journey capture |
| [FB-001-Imaging-Cost-Feedback](FB-001-Imaging-Cost-Feedback.md) | `01-Users/Feedback/` | — | raw signal, verbatim quotes and account frequency |
| [REL-001-Imaging-Estimate-Pilot](REL-001-Imaging-Estimate-Pilot.md) | `07-Delivery/Releases/` | Pichler | GO goal and measured result after delivery |
| [DEC-001-Build-Partner-Defer](DEC-001-Build-Partner-Defer.md) | `05-Decisions/` | — | framework-neutral decision record |
| [REVIEW-2027-02-Imaging-Estimate-Pilot](REVIEW-2027-02-Imaging-Estimate-Pilot.md) | `08-Reviews/` | Pichler + SVPG | goal vs outcome, risk retired vs not |
| [JTBD-001-Know-Cost-Before-Booking](JTBD-001-Know-Cost-Before-Booking.md) | `01-Users/JTBD/` | — | supporting lens for Problem and Persona |

## Opportunity examples

These extra example notes make the dashboard’s recommendation states visible:

- [OPP-002 — defer](OPP-002-Provider-Comparison.md)
- [OPP-003 — no-go](OPP-003-Prior-Authorization.md)

## Operating-model templates

The digital-transformation and project-to-product playbooks use a separate structure-only template
set: [_Operating-Models](Operating-Models/_Operating-Models.md).

It covers product taxonomy, funding, transformation thesis, capability maps, value streams,
adoption, portfolio roadmap, team topology, flow metrics, dependencies, and transition roadmap.

## Compliance templates

Tier 1 health-data compliance uses a separate structure-only template set:
[_Compliance-Templates](Compliance/_Compliance-Templates.md).

It covers compliance scope, data inventory, privacy/security risk, controls, vendor BAAs, incident
response, and compliance review. Tier 2 medical-device QMS is not included.

## Frontmatter contract

Every Dataview table in this vault reads **frontmatter keys**, not headings. `TABLE a, b` renders
columns from the `a:` and `b:` keys of each note; `WHERE type = "x"` filters on the `type:` key;
`SORT date DESC` uses the frontmatter `date:`, not the file's modification time.

Which is why every template's frontmatter **is** the instance schema — a note created from it is
queryable immediately. Copy the template frontmatter, then update `project`, `id`, `status`, links, and `updated:`; never retype the schema from memory. Live notes use `project: pm-harness`; the worked example uses `project: pm-harness-example`.

| Key | Allowed values → how it is used |
|---|---|
| `type` | one artifact type per note; every `WHERE type = "…"` filter depends on it |
| `id` | `PROB-003` style; note identity and wikilink target |
| `scope` (operating model) | `portfolio` · `product` · `value-stream` · `team` |
| `owner` / `sponsor` | accountable role; never a private individual's personal data |
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
| `opportunity` / `decision` (PRD) | quoted Obsidian links, e.g. `"[OPP-001](OPP-001-Outpatient-Imaging-Cost.md)"`, so traceability resolves |
| `primary_metric` (prd) | gate on "no baseline, no brief" |

**Templates carry their real `type`, not `type: template`.** That is deliberate: the schema stays
correct when you copy the file, and these files sit in `99-Playbook/`, outside every folder-scoped
query, so they never appear in a table. Do not move a template into `02-Problems/` or similar.

## Vault layout

The standard Dashboard uses `FROM ""` plus type filters and works in nested or root layouts. A
custom folder-scoped query uses a prefix (`FROM "PM vault/05-Decisions"` nested, `FROM
"05-Decisions"` root); do not mix them.

## Attribution

Pichler field definitions and checklists are quoted from the official tools, **CC BY-SA 4.0**
(© Roman Pichler / Pichler Consulting Limited). The Pichler sections of every template that quotes
them are therefore share-alike. SVPG material is quoted from Marty Cagan's published articles
(© Silicon Valley Product Group), quoted for reference rather than reproduced in bulk.

## How the frameworks fit together

| Layer | Methods | Canonical artifacts |
|---|---|---|
| **Direction and planning** | Pichler | Product Vision Board, Strategy, GO Roadmap, Persona, solution canvas |
| **Discovery and validation** | SVPG + Torres | Journey Map, Problem, Opportunity assessment, Discovery Map, Experiment |
| **Alignment and causality** | OKRs + Impact Mapping | Goals: one Objective, measurable KRs, Why → Who → How → What |
| **Measurement and learning** | North Star + Pichler KPI selection | Metrics, Release, Review |

Pichler supplies durable direction. SVPG supplies the evidence and risk gate. Torres's Opportunity
Solution Tree links desired outcomes to problems, alternative solutions and assumption tests without
duplicating their canonical notes. OKRs and Impact Mapping align each horizon around one Objective
and explicit behaviour change. North Star adds one customer-value metric with inputs and guardrails.

The canonical chain is in [Discovery to Delivery](../Discovery-to-Delivery.md). This page maps methods
to artifacts; it does not restate the chain.

Impact Mapping reference materials are CC BY 4.0 (Gojko Adzic). Torres and Amplitude material is
linked and summarized rather than reproduced in bulk.