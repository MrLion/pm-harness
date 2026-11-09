# Playbooks

Setup and operating manual: [Agent-Manual](../Agent-Manual.md). Canonical product chain:
[Discovery to Delivery](../Discovery-to-Delivery.md).

Choose by **what you are changing** and **how work is governed**.

Visual language: [Visual-Standards](../Visual-Standards.md).

Compliance rail: [_Compliance](../../11-Compliance/_Compliance.md) — complete the Tier 1 scope before handling PII, PHI, or ePHI.

| Playbook | Use when |
|---|---|
| [Vision-Led-0-to-1](Vision-Led-0-to-1.md) | New product, new market, or a new value proposition |
| [Outcome-Led-1-to-N](Outcome-Led-1-to-N.md) | Existing product; improve an outcome from signal |
| [Digital-Transformation](Digital-Transformation.md) | Portfolio or enterprise capability change |
| [Project-to-Product](Project-to-Product.md) | Project funding, team topology, or governance blocks durable product work |

Vision-led and outcome-led are product-lifecycle paths. Digital transformation and project-to-product
are operating-model transitions; they change funding, team topology, governance, and metrics before
product discovery can run cleanly.

## Methods and lineage

The playbooks use one operating model. Methods are assigned to the layer where they answer a distinct
question; they are not competing document formats.

| Layer | Methods | Question answered | Canonical artifacts |
|---|---|---|---|
| Direction and planning | Pichler | What are we building, and why? | Product Vision Board, Strategy, GO Roadmap, Persona |
| Discovery and validation | SVPG + Torres | Should we build it, and what could kill it? | Problem, Opportunity, Discovery Map, Experiment |
| Alignment and causality | OKRs + Impact Mapping | What outcome aligns the work, and whose behaviour must change? | Goals |
| Measurement and learning | North Star + Pichler KPI selection | What customer value and outcomes resulted? | Metrics, Release, Review |
| Operating model | Transformation thesis + Team Topologies + Flow Framework | How should product work be funded, staffed, and governed? | Transformation Thesis, Product Taxonomy, Funding Model, Team Topology, Flow Metrics, Transition Roadmap |

### Method boundaries

**Pichler** supplies the Product Vision Board, strategy elements, outcome-based GO Roadmap, personas,
and solution canvas. Each roadmap row carries one goal; features serve that goal rather than replace it.

**SVPG** supplies the ten-question Product Opportunity Assessment and four risks: value, usability,
feasibility, and business viability. Risks need owners and tests. No-go is a successful answer when it
prevents a weak build. Prototypes are preferred over heavyweight requirement documents.

**Torres** supplies the Opportunity Solution Tree: a desired outcome linked to opportunities,
alternative solutions, and assumption tests. Here it is a view over existing artifacts, not a third
source of truth.

**Impact Mapping** supplies the Why → Who → How → What chain used in Goals. A deliverable belongs
only when it could plausibly cause the required behaviour change.

**OKRs** keep one qualitative Objective per horizon with measurable Key Results. Unknown baselines
stay `unknown`; OKRs do not create competing roadmap goals.

**North Star** supplies one customer-value metric with a precise definition, source, inputs, and
guardrails. It is not a roadmap or a prioritization score.

**Team Topologies + Flow Framework** supply the operating-model lens: durable teams, explicit
interaction modes, and flow time/load/efficiency/distribution as system measures.

### Sources

- [Roman Pichler's tools](https://www.romanpichler.com/tools)
- [SVPG opportunity assessment](https://www.svpg.com/assessing-product-opportunities/) and [four big risks](https://www.svpg.com/four-big-risks/)
- [Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/)
- [Impact Mapping](https://www.impactmapping.org/)
- [North Star Playbook](https://amplitude.com/books/north-star/about-north-star-framework)
- [Team Topologies](https://teamtopologies.com/)
- [Flow Framework](https://flowframework.org/)
- [Project to Product](https://projecttoproduct.org/)

Pichler material quoted in templates is CC BY-SA 4.0. Impact Mapping reference materials are CC BY
4.0. Other frameworks are linked and summarized rather than reproduced in bulk.
