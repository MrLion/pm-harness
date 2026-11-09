# PM / Product Owner Role Boundaries

Use this reference when a request asks who owns a decision, how to split PM and Product Owner duties, or how to encode the roles in the harness.

## Principle

Delineate by **decision rights**, not title. Titles vary by organization; accountability should not.

| Decision | Product Manager | Product Owner |
|---|---|---|
| Product vision, strategy, target outcome | **Accountable** | Consulted |
| Which problem or opportunity to pursue | **Accountable** | Consulted |
| Build / partner / defer | **Accountable**, with executive sign-off | Input on delivery cost and reversibility |
| Roadmap priority and sequencing | **Accountable** | Consulted on capacity and dependencies |
| Backlog order and refinement | Consulted on outcome | **Accountable** |
| User stories and acceptance criteria | Consulted on user value | **Accountable** |
| Sprint goal and scope | Informed | **Accountable** |
| Release readiness | Shared — outcome and stakeholder impact | **Accountable** for delivery readiness |
| Post-release review | **Accountable** | Contributes delivery learning |
| Stakeholder, commercial, and compliance alignment | **Accountable** | Consulted |

The one-line version: **the PM owns the problem, the bet, and the outcome; the PO owns the backlog, the sprint contract, and delivery acceptance.**

The Product Owner is a Scrum accountability, not a synonym for Product Manager. In product-led organizations the PM often absorbs PO duties; in scaled or project-based organizations they are separate roles.

## Harness mapping

| Artifact | PM owns | PO owns |
|---|---|---|
| `Product-Vision-Board`, `Strategy`, `Goals` | Direction and outcomes | Feasibility input |
| `PROB-001`, `OPP-001` | Problem and opportunity | Technical and delivery constraints |
| `DEC-001` | Decision and tradeoffs | Delivery cost and reversibility input |
| `PRD-001` | Problem, outcome, scope, non-goals, success metrics | User stories, acceptance criteria, backlog readiness |
| `REL-001` | Outcome, stakeholder impact, compliance | Release readiness and acceptance |
| `REVIEW-2027-02` | Learning and next decision | Delivery variance and process learning |

When the split matters, put explicit `product_manager:` and `product_owner:` fields in `DEC-001` and `PRD-001`. A role split that exists only in conversation is not enforceable.

## Anti-patterns

- **PO as order-taker** — the PO only writes tickets and never influences value.
- **PM throws the PRD over the wall** — the PO inherits acceptance criteria they did not shape.
- **Two backlog owners** — PM and PO both reorder work.
- **PO sets product strategy alone** — delivery authority becomes product authority.
- **PM micromanages the sprint** — outcome accountability becomes task control.
- **One person holds both hats silently** — allowed in small teams, but the active hat must be stated in the decision record and PRD.

## Write-boundary consequence

`05-Decisions` is human-approved only under `Rules.md` Rule 21. An agent may prepare decision options, tradeoffs, and a recommendation, but it must not write or accept the decision record on the human's behalf. Any simplified permission ladder must preserve that boundary.
