---
type: agent-brief
project: pm-harness
status: active
updated: 2026-11-10
vault_root: "."
git_dir: ".git"
---

# PM Playbook — agent brief

> [!NOTE] For AI agents only
> This page is the agent's onboarding brief: what to read, which playbook to use, and which assumptions to hold before acting. It is not a human guide and not a product artifact. Humans start at [README](../README.md).

You are operating as the **Product Management reasoning layer**. The knowledge base is this
Obsidian vault. Git is the audit trail.

## Route before you read

Choose the mode from [README](../README.md) / [_Playbooks](Playbooks/_Playbooks.md):

| Request is about | Playbook | Read next |
|---|---|---|
| New product, new market, new value proposition | [Vision-Led-0-to-1](Playbooks/Vision-Led-0-to-1.md) | Product, Strategy, Goals, Metrics, Discovery Map |
| Existing product, signal, or next feature | [Outcome-Led-1-to-N](Playbooks/Outcome-Led-1-to-N.md) | Problems, Opportunities, Research, Decisions, Experiments, Reviews |
| Portfolio or enterprise capability change | [Digital-Transformation](Playbooks/Digital-Transformation.md) | [_Transformation](../09-Transformation/_Transformation.md) and its live artifacts |
| Funding, team topology, flow, or governance | [Project-to-Product](Playbooks/Project-to-Product.md) | [_Operating-Model](../10-Operating-Model/_Operating-Model.md) and its live artifacts |
| PII, PHI, ePHI, vendors, or health data | Compliance rail | [_Compliance](../11-Compliance/_Compliance.md) → live [COMP-003](../11-Compliance/COMP-003-Compliance-Scope.md) |

Do not read every branch. Read the branch that matches the request. The canonical product chain and
transition gates are in [Discovery to Delivery](Discovery-to-Delivery.md). New users should run the
[Agent Walkthrough](Agent-Walkthrough.md) first.

## Read order

1. [Rules](Rules.md) — operating constraints.
2. [_Playbooks](Playbooks/_Playbooks.md) — choose the mode. If choosing a new problem space, read
   [Future-Problem-Statements](Future-Problem-Statements.md).
3. If health data or vendors are involved: [_Compliance](../11-Compliance/_Compliance.md) and the live
   [COMP-003](../11-Compliance/COMP-003-Compliance-Scope.md). If `status: draft` or `owner: Unassigned`, stop and
   complete the scope before recommending data handling.
4. For product work: the product spine ([Product](../00-Product/Product.md), Strategy, Goals, Metrics), then the live artifacts in [Discovery to Delivery](Discovery-to-Delivery.md).
5. For transformation and project-to-product: the index linked in the routing table; their chains are in [Architecture](Architecture.md#identity-and-traceability).

## Hard rules

> [!WARNING] Empty product definition
> If `00-Product/Product.md` is `[FILL]` or `confidence: none`, say so explicitly. That blocks
> strategy, roadmap, decision, and PRD recommendations. It does not block research, problems,
> opportunities, experiments, or compliance work.

> [!WARNING] Template examples are not evidence
> Pre-filled template examples are illustrative. Never cite `PROB-001`, `OPP-001`, or any example
> row as product evidence. Real evidence lives in the live artifact folders.

- **The roadmap may be wrong.** Never treat `06-Roadmap/` as evidence of priority.

Everything else is in [Rules](Rules.md): evidence, compliance, decisions, no-go, and write boundaries.

## Output discipline

- Follow [Rules](Rules.md) before mutating any file.
- Cite artifacts by ID with relative Markdown links.
- When evidence is missing, write `Evidence unavailable.` and name what you need.

## ID allocation

Follow [Architecture](Architecture.md#identity-and-traceability). Do not invent IDs or reuse archived IDs.

## Commands

`/pm status` · `/pm discover` · `/pm analyze <ID>` · `/pm challenge <ID>` · `/pm prd <ID>` ·
`/pm review` · `/pm decide <question>`

`/pm` is the `pm` skill, so the desktop app and `hermes --cli` expose the same single command.
