# Templates

Every template has four layers: **the artifact structure** → **the source's field definition**
(quoted, with attribution) → **the checklist criteria** used to judge a filled note → **a
collapsible worked example**. The example is a fictional product ("Lantern", a clinic shift
scheduling tool) used consistently across all templates so the traceability chain is visible.

Delete the `[!example]` block before using a template for real work.

| Template | Use for | Framework | Source |
|---|---|---|---|
| [[Product-Vision-Board]] | `00-Product/Product.md` | Pichler | [Vision Board](https://romanpichler.com/tools/product-vision-board/) |
| [[Strategy]] | `00-Product/Strategy.md` | Pichler | [Strategy model](https://romanpichler.com/blog/my-product-strategy-model/) |
| [[Goals]] | `00-Product/Goals.md` | Pichler + OKR + Impact Mapping | [Goal-setting](https://romanpichler.com/blog/leading-through-shared-goals/) · [Impact Mapping](https://www.impactmapping.org/) |
| [[Metrics]] | `00-Product/Metrics.md` | Pichler + North Star | [KPI selection](https://romanpichler.com/blog/how-to-choose-the-right-kpis-for-your-product/) · [North Star](https://amplitude.com/books/north-star/about-north-star-framework) |
| [[GO-Roadmap]] | `06-Roadmap/` | Pichler | [GO Product Roadmap](https://romanpichler.com/tools/the-go-product-roadmap/) |
| [[Persona]] | `01-Users/Personas/` | Pichler | [Persona Template](https://www.romanpichler.com/the-persona-template/) |
| [[Discovery-Map]] | `03-Opportunities/Discovery Map.md` | Torres | [Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/) |
| [[Opportunity]] | `03-Opportunities/` | SVPG | [Opportunity assessment](https://www.svpg.com/assessing-product-opportunities/) |
| [[Experiment]] | `07-Delivery/Experiments/` | SVPG | [Four big risks](https://www.svpg.com/four-big-risks/) |
| [[PRD]] | `07-Delivery/PRDs/` | Pichler canvas + SVPG | [Product Canvas](https://www.romanpichler.com/tools/the-product-canvas/) |
| [[Problem]] | `02-Problems/` | — | supported by both, formalised by neither |
| [[Research]] | `04-Research/` | — | evidence layer for both |
| [[Feedback]] | `01-Users/Feedback/` | — | raw signal, verbatim quotes and account frequency |
| [[Release]] | `07-Delivery/Releases/` | Pichler | GO goal and measured result after delivery |
| [[Decision]] | `05-Decisions/` | — | decision records are outside both frameworks |
| [[Review]] | `08-Reviews/` | Pichler + SVPG | goal vs outcome, risk retired vs not |
| [[JTBD]] | `01-Users/JTBD/` | — | supporting lens for Problem and Persona |

## Frontmatter contract

Every Dataview table in this vault reads **frontmatter keys**, not headings. `TABLE a, b` renders
columns from the `a:` and `b:` keys of each note; `WHERE type = "x"` filters on the `type:` key;
`SORT date DESC` uses the frontmatter `date:`, not the file's modification time.

Which is why every template's frontmatter **is** the instance schema — a note created from it is
queryable immediately. Copy the frontmatter verbatim; never retype it.

| Key | Feeds |
|---|---|
| `type` | every `WHERE type = "…"` filter — if this is wrong, the note is invisible |
| `id` | note identity (`PROB-003`), wikilink targets |
| `status` | most tables; drives "not closed" filters |
| `confidence` | sorted ascending everywhere — weakest evidence surfaces first |
| `date` / `updated` / `review_after` / `review_date` | sorting and staleness queries |
| `category` (research) | `04-Research` per-category tables |
| `reliability` (research) | evidence-ladder filtering |
| `risk_type`, `risk_owner` (opportunity, experiment) | risk coverage |
| `recommendation` (opportunity) | go / no-go / defer surfacing |
| `primary_metric` (prd) | gate on "no baseline, no brief" |
| `template: true` | **not used** — see below |

**Templates carry their real `type`, not `type: template`.** That is deliberate: the schema stays
correct when you copy the file, and these files sit in `99-Hermes/`, outside every folder-scoped
query, so they never appear in a table. Do not move a template into `02-Problems/` or similar.

## Folder mode

This vault is a folder inside a larger Obsidian vault, so every query names its path
(`FROM "PM vault/05-Decisions"`). If you ever open `PM vault` as its own vault, strip the
`PM vault/` prefix from all 27 `FROM` clauses or the tables will match nothing.

## Attribution

Pichler field definitions and checklists are quoted from the official tools, **CC BY-SA 4.0**
(© Roman Pichler / Pichler Consulting Limited). The Pichler sections of every template that quotes
them are therefore share-alike. SVPG material is quoted from Marty Cagan's published articles
(© Silicon Valley Product Group), quoted for reference rather than reproduced in bulk.

## Added discovery and measurement layers

- **Torres / Opportunity Solution Trees** provide a linked view from desired outcomes through
  problems and opportunities to alternative solutions and assumption tests. The map never replaces
  the canonical notes it links.
- **Impact Mapping** (Gojko Adzic, CC BY 4.0 materials) connects Why → Who → How → What inside Goals.
- **North Star Framework** (Amplitude) adds one customer-value metric, its inputs and guardrails.
- **OKRs** give each horizon one qualitative Objective with measurable Key Results; they do not
  weaken Pichler's single-goal roadmap rule.

## Why both frameworks

Pichler answers *what are we building, and how do we plan and communicate it?* — durable strategy,
outcome-based roadmap, personas, canvas. Cagan answers *should we build it at all, and what will
kill it?* — ten-question opportunity assessment, four big risks, prototype over PRD.

Used alone, each leaves a hole the other fills: Pichler assumes the opportunity is sound, Cagan
refuses to plan. The vault uses Pichler for artifacts that survive quarters and SVPG for the gate
that stops you building the wrong thing.
