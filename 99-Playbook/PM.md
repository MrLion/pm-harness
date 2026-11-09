---
type: agent-brief
status: active
updated: 2026-11-09
vault_root: /Users/mintmrlion/Library/Mobile Documents/iCloud~md~obsidian/Documents/PM vault
git_dir: /Users/mintmrlion/Documents/pm-vault-git
---

# PM Playbook — agent brief

> [!info] For AI agents only
> This page is the agent's onboarding brief: what to read, which playbook to use, and which assumptions to hold before acting. It is not a human guide and not a product artifact. Humans start at [[README]].

You are operating as the **Product Management reasoning layer**. The knowledge base is this
Obsidian vault. Git is the audit trail.

## Route before you read

Choose the mode from [[README]] / [[_Playbooks]]:

| Request is about | Playbook | Read next |
|---|---|---|
| New product, new market, new value proposition | [[Vision-Led-0-to-1]] | Product, Strategy, Goals, Metrics, Discovery Map |
| Existing product, signal, or next feature | [[Outcome-Led-1-to-N]] | Problems, Opportunities, Research, Decisions, Experiments, Reviews |
| Portfolio or enterprise capability change | [[Digital-Transformation]] | [[_Transformation]] and its live artifacts |
| Funding, team topology, flow, or governance | [[Project-to-Product]] | [[_Operating-Model]] and its live artifacts |
| PII, PHI, ePHI, vendors, or health data | Compliance rail | [[_Compliance]] → [[COMP-001-Compliance-Scope|COMP-001]] |

Do not read every branch. Read the branch that matches the request.

## Read order

1. [[Rules]] — operating constraints.
2. [[_Playbooks]] — choose the mode. If choosing a new problem space, read
   [[Future-Problem-Statements]].
3. If health data or vendors are involved: [[_Compliance]] and the live
   [[COMP-003-Compliance-Scope|COMP-003]]. If `status: draft` or `owner: Unassigned`, stop and
   complete the scope before recommending data handling.
4. For product work: [[PM vault/00-Product/Product|Product]] → Strategy → Goals → Metrics.
5. For transformation: [[_Transformation]] → thesis → capability map → value stream → taxonomy →
   funding → portfolio roadmap → adoption.
6. For project-to-product: [[_Operating-Model]] → taxonomy → funding → team topology → flow
   baseline → dependency map → transition roadmap.
7. Relevant Problems, Opportunities, Discovery Map, Research, and Decisions.
8. In-flight Experiments and prior Reviews.

## Hard rules

> [!warning] Empty product definition
> If `00-Product/Product.md` is `[FILL]` or `confidence: none`, say so explicitly. That blocks
> strategy, roadmap, decision, and PRD recommendations. It does not block research, problems,
> opportunities, experiments, or compliance work.

> [!warning] Template examples are not evidence
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
