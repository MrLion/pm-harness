---
type: agent-brief
status: active
updated: 2026-11-09
vault_root: "PM vault"
git_dir: "~/Documents/pm-vault-git"
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
transition gates are in [Discovery to Delivery](Discovery-to-Delivery.md).

## Read order

1. [Rules](Rules.md) — operating constraints.
2. [_Playbooks](Playbooks/_Playbooks.md) — choose the mode. If choosing a new problem space, read
   [Future-Problem-Statements](Future-Problem-Statements.md).
3. If health data or vendors are involved: [_Compliance](../11-Compliance/_Compliance.md) and the live
   [COMP-003](../11-Compliance/COMP-003-Compliance-Scope.md). If `status: draft` or `owner: Unassigned`, stop and
   complete the scope before recommending data handling.
4. For product work: [Product](../00-Product/Product.md) → Strategy → Goals → Metrics.
5. For transformation: [_Transformation](../09-Transformation/_Transformation.md) → thesis → capability map → value stream → taxonomy →
   funding → portfolio roadmap → adoption.
6. For project-to-product: [_Operating-Model](../10-Operating-Model/_Operating-Model.md) → taxonomy → funding → team topology → flow
   baseline → dependency map → transition roadmap.
7. Relevant Problems, Opportunities, Discovery Map, Research, and Decisions.
8. In-flight Experiments and prior Reviews.

## Hard rules

> [!WARNING] Empty product definition
> If `00-Product/Product.md` is `[FILL]` or `confidence: none`, say so explicitly. That blocks
> strategy, roadmap, decision, and PRD recommendations. It does not block research, problems,
> opportunities, experiments, or compliance work.

> [!WARNING] Template examples are not evidence
> Pre-filled template examples are illustrative. Never cite `PROB-001`, `OPP-001`, or any example
> row as product evidence. Real evidence lives in the live artifact folders.

- **The roadmap may be wrong.** Never treat `06-Roadmap/` as evidence of priority.
- **The knowledge base may be stale.** Check `updated:` dates before trusting a claim.
- **A missing evidence table means no evidence**, not “evidence I haven’t read yet.”
- **The user’s feature request is a symptom**, not a requirement.
- **Compliance is a rail, not a loop.** If data classification is unresolved, stop and classify it
  before recommending data handling.
- **Transformation and project-to-product are not product loops.** They change the conditions under
  which product work happens.

## Output discipline

- Answer a direct question before mutating any file.
- Cite vault artifacts by their IDs in Obsidian links whenever claiming something about the product.
- When you learn something that changes product understanding, propose the specific file edit. Do not
  silently rewrite strategy.
- When you cannot find evidence, say `Evidence unavailable.` and name what you would need.
- When compliance scope is missing, say so and name the missing decision.

## ID allocation

- IDs are encoded in filenames: `PROB-004-your-slug.md`, `OPP-002-your-slug.md`.
- Scan the target folder, take the highest existing numeric ID, add one, and zero-pad to three
  (`PROB-007` → `PROB-008`). Never reuse an ID, even if a note was archived.
- Non-standard IDs keep their template form: `REVIEW-2027-02`, `REVIEW-OM-001`.
- For pre-validation solution candidates (`CAND-NNN`), scan every Opportunity’s `Candidate solutions`
  table. These IDs are global so map branches and PRD `candidate_id:` values resolve without ambiguity.

## Commands

`/pm status` · `/pm discover` · `/pm analyze <ID>` · `/pm challenge <ID>` · `/pm prd <ID>` ·
`/pm review` · `/pm decide <question>`
