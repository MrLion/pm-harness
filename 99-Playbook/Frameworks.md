# Frameworks

The harness uses one operating model. Frameworks are assigned to the layer where they answer a
distinct question; they are not competing document formats.

| Layer | Methods | Question answered | Canonical artifacts |
|---|---|---|---|
| Direction and planning | Pichler | What are we building, and why? | Product Vision Board, Strategy, GO Roadmap, Persona |
| Discovery and validation | SVPG + Torres | Should we build it, and what could kill it? | Problem, Opportunity, Discovery Map, Experiment |
| Alignment and causality | OKRs + Impact Mapping | What outcome aligns the work, and whose behaviour must change? | Goals |
| Measurement and learning | North Star + Pichler KPI selection | What customer value and outcomes resulted? | Metrics, Release, Review |
| Operating model | Transformation thesis + Team Topologies + Flow Framework | How should product work be funded, staffed, and governed? | Transformation Thesis, Product Taxonomy, Funding Model, Team Topology, Flow Metrics, Transition Roadmap |

## Operating chain

| Stage | Question | Artifact |
|---|---|---|
| Vision | What future are we trying to create? | [[PM vault/99-Playbook/Templates/Product-Vision-Board\|Product Vision Board]] |
| Objective / North Star | What outcome aligns the work, and what customer value proves it? | [[PM vault/99-Playbook/Templates/Goals\|Goals]] · [[PM vault/99-Playbook/Templates/Metrics\|Metrics]] |
| Impact Map | Whose behaviour must change, and what deliverable could cause it? | [[PM vault/99-Playbook/Templates/Goals\|Impact Map]] |
| Discovery Map | Which problems, opportunities, and assumptions matter most? | [[PM vault/99-Playbook/Templates/Discovery-Map\|Discovery Map]] |
| Evidence and risk gate | Do we know enough to commit? | [[PM vault/99-Playbook/Templates/OPP-001-Outpatient-Imaging-Cost\|Opportunity]] · [[PM vault/99-Playbook/Templates/EXP-001-Comprehension-Test\|Experiment]] |
| Decision | Which option do we choose, and why? | [[PM vault/99-Playbook/Templates/DEC-001-Build-Partner-Defer\|Decision]] |
| Solution brief | What is the smallest coherent solution? | [[PM vault/99-Playbook/Templates/PRD-001-Imaging-Estimate\|PRD]] |
| Release | What shipped, and what moved? | [[PM vault/99-Playbook/Templates/REL-001-Imaging-Estimate-Pilot\|Release]] |
| Review | What did we learn, and what risk remains? | [[PM vault/99-Playbook/Templates/REVIEW-2027-02-Imaging-Estimate-Pilot\|Review]] |

## Layer rules

### Pichler

Provides the Product Vision Board, strategy elements, outcome-based GO Roadmap, personas and
solution canvas. Each roadmap row carries one goal; features serve that goal rather than replacing it.

### SVPG

Provides the ten-question Product Opportunity Assessment and four risks: value, usability,
feasibility and business viability. Risks need owners and tests. **No-go is a successful answer**
when it prevents a weak build. Prototypes are preferred over heavyweight requirement documents.

### Opportunity Solution Trees

Teresa Torres's tree links a desired outcome to opportunities, alternative solutions and assumption
tests. Here it is a view over existing artifacts. Torres's “opportunity” maps to this vault's
problem plus its assessment; do not create a third opportunity category.

### Impact Mapping

Gojko Adzic's Why → Who → How → What chain lives in Goals. A deliverable belongs only when it could
plausibly cause the required behaviour change. Find the shortest path to the goal rather than
implementing the whole map.

### OKRs

Each horizon has one qualitative Objective and measurable Key Results. Key Results need baselines
and targets; unknown baselines remain `unknown`. OKRs do not create multiple competing roadmap goals.

### North Star

One metric represents the value customers receive, with a precise definition, source, inputs and
guardrails. Supporting KPIs remain few and decision-relevant. A North Star is not a roadmap,
prioritization score, or substitute for instrumentation.

## Operating-model chain

| Stage | Question | Artifact |
|---|---|---|
| Transformation Thesis | What digital outcome is the organization trying to create? | [[PM vault/99-Playbook/Templates/Operating-Models/Transformation/TRANS-001-Transformation-Thesis\|TRANS-001]] |
| Capability Map | Which capabilities must change? | [[PM vault/99-Playbook/Templates/Operating-Models/Transformation/CAP-001-Capability-Map\|CAP-001]] |
| Value-Stream Map | Where does work wait today? | [[PM vault/99-Playbook/Templates/Operating-Models/Transformation/VS-001-Value-Stream-Map\|VS-001]] |
| Product Taxonomy | What durable products, platforms, and services should exist? | [[PM vault/99-Playbook/Templates/Operating-Models/Shared/TAX-001-Product-Taxonomy\|TAX-001]] |
| Funding Model | How is work funded across horizons? | [[PM vault/99-Playbook/Templates/Operating-Models/Shared/FUND-001-Funding-Model\|FUND-001]] |
| Team Topology | Which teams own which product outcomes? | [[PM vault/99-Playbook/Templates/Operating-Models/Project-to-Product/TEAM-001-Team-Topology\|TEAM-001]] |
| Flow Metrics Baseline | Where is work waiting, and how efficiently does it flow? | [[PM vault/99-Playbook/Templates/Operating-Models/Project-to-Product/FLOW-001-Flow-Metrics-Baseline\|FLOW-001]] |
| Dependency Map | What blocks flow between teams or products? | [[PM vault/99-Playbook/Templates/Operating-Models/Project-to-Product/DEP-001-Dependency-Map\|DEP-001]] |
| Transition Roadmap | What changes first, and what proves the transition is working? | [[PM vault/99-Playbook/Templates/Operating-Models/Project-to-Product/TRANS-002-Transition-Roadmap\|TRANS-002]] |
| Adoption Scorecard | Are the new capabilities actually used? | [[PM vault/99-Playbook/Templates/Operating-Models/Transformation/ADOPT-001-Adoption-Scorecard\|ADOPT-001]] |
| Portfolio Roadmap | What sequence of product bets delivers the transformation? | [[PM vault/99-Playbook/Templates/Operating-Models/Transformation/PORT-001-Portfolio-Roadmap\|PORT-001]] |
| Review | What changed in the operating model, and what is still blocked? | [[PM vault/99-Playbook/Templates/Operating-Models/Shared/REVIEW-OM-001-Operating-Model-Review\|REVIEW-OM-001]] |

## Sources

- [Roman Pichler's tools](https://www.romanpichler.com/tools)
- [SVPG opportunity assessment](https://www.svpg.com/assessing-product-opportunities/) and
  [four big risks](https://www.svpg.com/four-big-risks/)
- [Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/)
- [Impact Mapping](https://www.impactmapping.org/)
- [North Star Playbook](https://amplitude.com/books/north-star/about-north-star-framework)
- [Team Topologies](https://teamtopologies.com/)
- [Flow Framework](https://flowframework.org/)
- [Project to Product](https://projecttoproduct.org/)

Pichler material quoted in templates is CC BY-SA 4.0. Impact Mapping reference materials are CC BY
4.0. Other frameworks are linked and summarized rather than reproduced in bulk.
