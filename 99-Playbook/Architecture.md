---
type: architecture
status: active
updated: 2026-11-09
---

# Architecture

> [!NOTE] For AI agents only
> This page is the technical contract for agents: vault mode, folder model, frontmatter, IDs, write boundaries, git, and verification. It is not a human guide. Humans start at [README](../README.md).

Technical reference for agents and advanced users. Setup and operation: [Agent-Manual](Agent-Manual.md). Start with
[README](../README.md) for routing. Use
[START-HERE](../START-HERE.md) only for the outcome-led 1→N path; use [Vision-Led-0-to-1](Playbooks/Vision-Led-0-to-1.md) for a new product.

## Vault mode

`PM vault` is a **folder inside the registered iCloud `Documents` Obsidian vault** in the maintainer's
deployment. A portable install may open the repository as the vault root.

- Dataview is enabled in the vault that contains the harness.
- A nested `PM vault/.obsidian/` is ignored by Obsidian and is not tracked in git.
- The standard Dashboard uses `FROM ""` plus type filters, so it works in nested and root layouts.
- Custom folder-scoped queries must use a prefix that matches the layout.

## Folder model

| Folder | Unit of analysis | Purpose |
|---|---|---|
| `00-Product` | Product | Vision, strategy, goals, metrics, scenario |
| `01-Users` | Customer | Personas, JTBD, journey maps, feedback |
| `02-Problems` | Problem | Evidence-backed problems |
| `03-Opportunities` | Opportunity | Opportunity assessments and Discovery Map |
| `04-Research` | Evidence | Market, user, competitor, and data research |
| `05-Decisions` | Decision | Decision records |
| `06-Roadmap` | Product horizon | GO roadmap |
| `07-Delivery` | Delivery | Experiments, PRDs, releases |
| `08-Reviews` | Learning | Goal vs outcome and risk reviews |
| `09-Transformation` | Portfolio | Transformation thesis, capability, value stream, adoption, portfolio roadmap |
| `10-Operating-Model` | Operating model | Product taxonomy, funding, team topology, flow, dependencies, transition |
| `11-Compliance` | Compliance | Tier 1 health-data scope, data inventory, risk, controls, vendors, incidents, review |
| `99-Playbook` | Method | Playbooks, templates, rules, agent brief, architecture, visual standards |

Templates live under `99-Playbook/Templates/`. Template indexes:

- [_Templates](Templates/_Templates.md) — product-lifecycle templates
- [_Operating-Models](Templates/Operating-Models/_Operating-Models.md) — transformation and project-to-product templates
- [_Compliance-Templates](Templates/Compliance/_Compliance-Templates.md) — Tier 1 compliance templates

## Frontmatter is the data layer

Dataview reads YAML frontmatter, not headings:

- `TABLE status, date` renders those frontmatter keys as columns.
- `WHERE type = "decision"` filters on `type:`.
- `SORT date DESC` uses the frontmatter `date:`, not file modification time.
- Missing keys produce blank columns; wrong `type` values make notes invisible to queries.

Copy the template frontmatter, then update `id`, `status`, links, and `updated:`. Never leave example
values in a live artifact. The schema contract is in [_Templates](Templates/_Templates.md).

## Identity and traceability

IDs live in filenames: `PROB-004-your-slug.md`, `OPP-002-your-slug.md`.

- Scan the target folder, take the highest existing numeric ID, add one, and zero-pad to three.
- Never reuse an ID, even if a note was archived.
- Non-standard IDs keep their template form: `REVIEW-2027-02`, `REVIEW-OM-001`.
- `CAND-NNN` IDs are global across Opportunities. Scan every Opportunity’s `Candidate solutions`
  table before allocating one.
- Link canonical artifacts with relative Markdown links that resolve in both Obsidian and GitHub.

Traceability chains:

- Product: canonical in [Discovery to Delivery](Discovery-to-Delivery.md)
- Transformation: `Transformation Thesis → Capability Map → Value-Stream Map → Product Taxonomy → Funding → Portfolio Roadmap → Adoption → Review`
- Project-to-product: `Product Taxonomy → Funding → Team Topology → Flow Baseline → Dependency Map → Transition Roadmap → Review`
- Compliance: `Compliance Scope → Data Inventory → Risk → Controls → Vendor/BAA → Incident Readiness → Review`

`Discovery Map.md` is an Opportunity Solution Tree **view** over Goals, Problems, Opportunities,
solution briefs, and Experiments. It never replaces those notes.

## Git

In the maintainer's deployment, the vault’s `.git` is a pointer file to `~/Documents/pm-vault-git`,
deliberately outside iCloud. A fresh clone uses a normal `.git` directory.

- In the maintainer's setup, never move git internals into iCloud.
- Do not create a nested git repository inside a checkout; that creates diverging history.
- Nested `.obsidian/` remains on disk but is ignored by git as inert machine-local state.
- A remote may be configured; pushing is a separate, intentional action.
- Releases are tagged `vX.Y.Z`; update `VERSION` and `CHANGELOG.md` before tagging. See
  [VERSIONING](../VERSIONING.md).

## Agent write boundaries

[Rules](Rules.md) Rule 21 is authoritative. Do not restate or widen it here. Every material write
updates `updated:` and leaves a reviewable git diff.

## Verification before declaring success

Check programmatically and in Obsidian; visible files alone are not proof.

1. Dataview sources are either `FROM ""` with type filters or use the correct folder prefix.
2. Every queried column exists in the corresponding template schema.
3. `/pm` loads the `product-management` skill with the requested subcommand intact.
4. Check that relative Markdown links resolve, then run `obsidian unresolved vault=<vault-name>` for
   any legacy wikilinks.
5. Open and visually verify the rendered dashboard in Obsidian.
6. Prefilled product templates contain zero `[FILL]`; operating-model and compliance templates may
   contain `[FILL]` by design.
7. If PII, PHI, ePHI, vendors, or health data are involved, require a live `compliance-scope` note
   in `11-Compliance` with status `approved` or `active`, data classification, jurisdiction, and a
   named owner. A template in `99-Playbook/Templates` does not satisfy this.
8. `git status` is clean after an intentional commit.
