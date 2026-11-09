# Operating-Model Templates

Structure-only templates for the two operating-model playbooks. They use portfolio, value-stream, team, and operating-model units of analysis — not a single product.

## Shared

| Template | Use for |
|---|---|
| [TAX-001](Shared/TAX-001-Product-Taxonomy.md) | Durable products, platforms, and services |
| [FUND-001](Shared/FUND-001-Funding-Model.md) | Portfolio or product funding and decision rights |
| [REVIEW-OM-001](Shared/REVIEW-OM-001-Operating-Model-Review.md) | Transformation or transition review |

## Digital transformation

| Template | Use for |
|---|---|
| [TRANS-001](Transformation/TRANS-001-Transformation-Thesis.md) | Transformation thesis and why now |
| [CAP-001](Transformation/CAP-001-Capability-Map.md) | Capability gaps and maturity |
| [VS-001](Transformation/VS-001-Value-Stream-Map.md) | Current value-stream flow and delays |
| [ADOPT-001](Transformation/ADOPT-001-Adoption-Scorecard.md) | Adoption and changed work |
| [PORT-001](Transformation/PORT-001-Portfolio-Roadmap.md) | Sequenced portfolio bets |

## Project-to-product

| Template | Use for |
|---|---|
| [TEAM-001](Project-to-Product/TEAM-001-Team-Topology.md) | Durable teams and ownership |
| [FLOW-001](Project-to-Product/FLOW-001-Flow-Metrics-Baseline.md) | Flow time, load, efficiency, distribution |
| [DEP-001](Project-to-Product/DEP-001-Dependency-Map.md) | Cross-team and cross-product dependencies |
| [TRANS-002](Project-to-Product/TRANS-002-Transition-Roadmap.md) | Sequenced operating-model change |

## Flow

```text
Transformation Thesis
└── Capability Map
    └── Value-Stream Map
        ├── Product Taxonomy
        │   ├── Funding Model
        │   └── Team Topology
        │       └── Flow Metrics Baseline
        │           └── Dependency Map
        └── Adoption Scorecard
            └── Portfolio Roadmap
                └── Transition Roadmap
```

`Product Taxonomy` is the shared bridge. Do not duplicate it per playbook.
