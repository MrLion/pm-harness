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

`PM vault` is a **folder inside the registered iCloud `Documents` Obsidian vault**, not a
standalone vault.

- Dataview is installed and enabled in `Documents/.obsidian/plugins/dataview/`.
- A nested `PM vault/.obsidian/` is ignored by Obsidian and is not tracked in git.
- Every Dataview source includes the folder prefix: `FROM "PM vault/02-Problems"`.
- Do not register the folder as a separate vault merely to fix empty tables. Convert modes only
  deliberately; doing so requires removing the prefix from every query.

## Folder model

| Folder | Unit of analysis | Purpose |
|---|---|---|
| `00-Product` | Product | Vision, strategy, goals, metrics, scenario |
| `01-Users` | Customer | Personas, JTBD, feedback |
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
- Link canonical artifacts with Obsidian internal links.

Traceability chains:

- Product: `Problem → Evidence → Opportunity → Challenge → Experiment or Decision → PRD → Release → Review`
- Transformation: `Transformation Thesis → Capability Map → Value-Stream Map → Product Taxonomy → Funding → Portfolio Roadmap → Adoption → Review`
- Project-to-product: `Product Taxonomy → Funding → Team Topology → Flow Baseline → Dependency Map → Transition Roadmap → Review`
- Compliance: `Compliance Scope → Data Inventory → Risk → Controls → Vendor/BAA → Incident Readiness → Review`

`Discovery Map.md` is an Opportunity Solution Tree **view** over Goals, Problems, Opportunities,
solution briefs, and Experiments. It never replaces those notes.

## Git

The vault’s `.git` is a pointer file to `~/Documents/pm-vault-git`, deliberately outside iCloud.
Notes sync through iCloud; git history remains on the Mac.

- Never move git internals into iCloud.
- Never `git init` or clone in this folder; that creates diverging history.
- Nested `.obsidian/` remains on disk but is ignored by git as inert machine-local state.
- Commits are local unless a remote is explicitly configured.

## Agent write boundaries

[Rules](Rules.md) Rule 21 is authoritative:

**Free to write:** `04-Research`, `02-Problems`, `03-Opportunities`, `07-Delivery/Experiments`,
`08-Reviews`, `99-Playbook/Templates`, `99-Playbook/Playbooks`, `99-Playbook/Future-Problem-Statements.md`.

**Draft only — propose, do not overwrite:** `07-Delivery/PRDs`, `06-Roadmap`,
`09-Transformation`, `10-Operating-Model`, `11-Compliance`.

**Human-approved only:** `00-Product`, `05-Decisions`, `README.md`, `99-Playbook/Rules.md`,
`99-Playbook/PM.md`, `99-Playbook/Visual-Standards.md`.

Every material write updates `updated:` and leaves a reviewable git diff.

## Verification before declaring success

Check programmatically and in Obsidian; visible files alone are not proof.

1. All Dataview sources have the correct `PM vault/` prefix.
2. Every queried column exists in the corresponding template schema.
3. `/pm` loads the `product-management` skill with the requested subcommand intact.
4. Run the `product-management` skill audit script `scripts/check_wikilinks.py` and
   `obsidian unresolved vault=Documents`.
5. Open and visually verify the rendered dashboard in Obsidian.
6. Prefilled product templates contain zero `[FILL]`; operating-model and compliance templates may
   contain `[FILL]` by design.
7. If PII, PHI, ePHI, vendors, or health data are involved, require a live `compliance-scope` note
   in `11-Compliance` with status `approved` or `active`, data classification, jurisdiction, and a
   named owner. A template in `99-Playbook/Templates` does not satisfy this.
8. `git status` is clean after an intentional commit.
