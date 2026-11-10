# Harness Audit

Use for `/pm review`, any static vault audit, or before declaring a harness change complete.

## 1. Inventory

- Compare `rglob("*.md")` with `git ls-files`; the live tree must contain no untracked unexpected files.
- Check `git remote -v`, branch state, and working tree before claiming a change was committed or shared.
- Distinguish **artifact notes** (instantiated copies), **templates**, and **index notes** (`_*`) in every count.
- Count non-index artifact notes per live folder; report scaffold-only folders separately from operational ones.
- Treat narrative claims on index pages (`_Templates`, `Dashboard-Example`) as assertions to verify against actual files: worked-example scenario, `[!example]` instruction, and stated `FROM` count. Never hardcode a `FROM` count in a guide; say "every `FROM` clause" because the count drifts.
- Include `09-Transformation/`, `10-Operating-Model/`, and `11-Compliance/` in vault audits; they are operating-model and compliance destinations, not product artifacts.

## 2. Frontmatter contract

- Parse every template's frontmatter as YAML; require a dict with the real artifact `type`.
- Require standard enums: confidence `none → low → medium → high`; research reliability
  `weak → medium → strong`; primary risk `value / usability / feasibility / viability`.
- Require `updated:` on typed artifact templates. Missing maintenance dates are a finding.
- After a bulk edit, update `updated:` on every touched typed artifact; correct content with yesterday's date is still a stale note.
- Content pages outside templates (`Scenario`, future-problem list) still need `type`, `status`, `updated:` when they are live; a missing `type` hides them from Dataview and freshness checks.
- Decision frontmatter `expected_outcome:` must match the body's measurable outcome; `TBD` beside a populated body is a contradiction.
- Operating-model templates also require `scope: portfolio | product | value-stream | team` and a named `owner`; do not score them with the product templates' Pichler/SVPG schema.
- Verify referenced traceability is a quoted link where resolution is expected: a relative Markdown
  link in the GitHub-published vault, or `opportunity: "[[OPP-000]]"` in an Obsidian-only copy — not
  a plain ID.

## 3. Dataview reliability

- Check every `FROM` uses the current folder-mode prefix.
- Check every typed artifact folder (and index note) query filters on `type`; otherwise index notes and unrelated notes become rows.
- For every `TABLE` column, compare against the matching template schema; a column without a schema key renders blank.
- Sort confidence/severity/reliability by rank, not alphabetically. A nested choice is a working pattern:

```dataview
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

- Report freshness as three separate classes: overdue, missing date, and current.

## 4. Links and naming

- **All layouts:** run `python3 scripts/validate_vault.py` from the repository root. It checks relative
  Markdown targets, heading anchors, frontmatter, ID uniqueness, filename/ID consistency, and
  product-template fill markers. It is the link and contract gate.
- **Obsidian-only legacy links:** run `python scripts/check_wikilinks.py` only when the vault still
  contains `[[...]]`. It will report zero after conversion; do not present that as a link audit.
- Use `obsidian unresolved` as a second target index. If an image is reported, confirm the asset
  exists and trust Obsidian's verdict.
- `obsidian orphans` scans the whole parent vault; filter output to `PM vault/`. A root page such as
  `Dashboard` or `Scenario` with no incoming wikilink is a navigation gap even if reachable by path.
  Index notes (`_*`) and non-Markdown assets are expected orphans; report content pages first.
- Then run `obsidian unresolved vault=Documents` for Obsidian's own file-target index, and
  `obsidian links path="..."` on the note to see the resolved target paths.
- Do not treat `obsidian unresolved` as a complete correctness check: it does not validate anchors
  or semantic target. A link that opens a template when the map should open a canonical artifact is
  defective even though it resolves.
- For an operational Discovery Map, count links against the open/deferred opportunity set; an
  open/deferred opportunity with no link is a missing map branch.
- Grep for bare names when templates and artifacts share a stem (`Goals`, `Strategy`, `Metrics`).
- Use relative Markdown links with display aliases for colliding basenames, for example
  `[Goals](00-Product/Goals.md)` versus `[Goals template](99-Playbook/Templates/Goals.md)`. In an
  Obsidian-only copy, the equivalent is `[[PM vault/00-Product/Goals|Goals]]` versus
  `[[99-Playbook/Templates/Goals|Goals template]]`.
- Do not leave `PROB-000`/`OPP-000` placeholders in an operational note. In a template they are
  scaffolding; in `02-Problems/`, `03-Opportunities/`, or a map they are broken references.
- A template example link to `00-Product/*` that opens a `[FILL]` note is semantically broken even
  though it resolves; point it at the prefilled template or mark it illustrative.
- Check prefilled example filenames against their `id:`; artifact examples should lead with the ID. Exclude `99-Playbook/Playbooks/` from this check: `PLAYBOOK-NNN` is a playbook identifier, not a filename-encoded artifact ID.
- For README or playbook audits, verify the visible body contains every mode/loop the router promises. A router link is not proof that the main document explains the path.
- For playbook audits, parse every `## Flow` table and require a relative Markdown link in the
  Artifact cell of every row (`[...](...)`). A bare artifact label is incomplete even when the target
  template exists. If no exact template exists, require a template section anchor or a new template.
- After a bulk wikilink rewrite, scan for duplicated aliases (`PROB-001PROB-001`, `NOWNOW`) and collapse them before committing; naive target replacement can append the alias twice.
- After a folder or template rename, grep for the old token in prose, code paths, Dataview `FROM`
  clauses, and link targets; the Markdown checker will not catch stale plain-text paths or prose
  claims.
- Also grep the `/pm` bundle (`~/.hermes/profiles/pdm/skill-bundles/pm.yaml`) for the old folder path; `hermes bundles list` proves registration only, not that the instruction points at an existing `Rules.md`.

## 5. Workflow gates

- No solution brief before: evidence table, challenge run, risks with owners, and a primary-metric baseline.
- Pre-validation solution candidates live in the Opportunity's `Candidate solutions`, not a PRD.
- Experiments name one **primary** risk; secondary observations are not decision evidence unless pre-registered.
- Reviews distinguish measured miss, unknown, and not measured.
- A Review must not claim a risk was tested when the linked Experiment is still `status: planned`.
- A planned or future-dated Review must not report compliance checks as completed. Use `Pending — pilot not run` or `Not assessed — example`; `None`, `Reviewed`, and `No findings` imply work that has not happened.
- The compliance gate is the **live** `11-Compliance` scope, not the `COMP-001` template. Require `status: approved` or `active`, resolved data classification and jurisdiction, and a named owner; `draft` or `Unassigned` is a stop condition.
- Cross-check metric direction words (under/over a threshold) across Metrics, PRD and Goals; a
  reversed guardrail is a material defect.

## 6. Rendering hygiene

- No raw `<...>` placeholders; use `[FILL: ...]`.
- The zero-`[FILL]` check applies only to the prefilled **product-lifecycle** template set. Operating-model templates under `99-Playbook/Templates/Operating-Models/` and compliance templates under `99-Playbook/Templates/Compliance/` are structure-only and intentionally keep `[FILL]` prompts.
- Cross-cutting sections added after the initial prefill (compliance, data handling) can regrow `[FILL]` in product templates; fill them with example-specific values or explicit "not assessed in example" text, then rerun the zero-FILL check.
- Verify prose claims about counts and zero-`[FILL]` against actual files; `Architecture` and `_Templates` claims drift after bulk edits.
- Closing frontmatter delimiter must be on its own line; parse YAML after bulk edits.
- Headings need blank lines before and after, including before tables.
- Read the rendered file back and rerun link/schema checks; disk success alone proves nothing.

## 7. Page-level audits

For README, START-HERE, PM, Rules, Architecture, Visual-Standards, Future-Problem-Statements, and Agent-Manual audits:

- Treat the product chain as a single-source-of-truth artifact. `99-Playbook/Discovery-to-Delivery.md`
  owns it; README, Agent-Manual, Architecture, Rules, and `_Templates` must link to it, not restate it.
  Grep for chain phrases (`Signal → Problem`, `Problem → Evidence`, `Solution brief → Release`) and
  reconcile divergent wording before adding another chain.

- Require an audience callout: README/START-HERE **For humans**; PM/Rules/Architecture **For AI
  agents only**; Visual-Standards, Future-Problem-Statements, and Agent-Manual **For humans and agents**.
- README must state the agent layer is external: skill path, bundle path, `/pm status` smoke test,
  and expected output. A vault that renders without `/pm` is not broken; a README that omits the
  prerequisite is incomplete.
- Grep the page and its headings for `Hermes`; vault naming is `PM Playbook`, `PM Rules`, `PM Dashboard`, not the old brand.
- Cross-check every named Rules section against the current numbering; do not trust `§18` or other
  stale section references.
- Check the page's write boundaries against `Rules.md` Rule 21: templates/playbooks and the future-problem reference writable; PRDs/Roadmap/transformation/operating-model/compliance draft-only; Product, Decisions, README, Rules, PM, and Visual-Standards human-approved only.
- Check entry paths: README routes; START-HERE is outcome-led only; vision-led work starts at
  `Vision-Led-0-to-1`; transformation and project-to-product use their own playbooks.
- For a report named in a template, require a live `04-Research/` note with `source:` and a link
  from each evidence row. A name-only citation is a provenance gap.
- When creating that live research note from a template, allocate a new live ID (`RESEARCH-002` when the template is `RESEARCH-001`) and repoint evidence rows to it; do not duplicate the template's ID.
- Audit every Evidence/Sources table cell: require a direct URL or a wikilink to a live research
  note in the Source cell. A named publisher is not enough, even when the same report is linked in
  frontmatter, a bottom Sources list, or another row.
- When a source appears in several artifacts, fix all locations together: frontmatter `source`,
  evidence rows, quote attributions, scenario evidence tables and source lists, decision S-tables,
  and future-problem source lists. Re-grep the publisher name and confirm each visible citation has
  a link.
- Audit the template index and example dashboard as pages: their stated worked-example scenario, placeholder instructions, and query counts must match the current templates.
- When the user reports a missing reference, inspect and fix the page they are reading first. A
  correct citation in a different template does not answer the complaint.

## 8. Audit output

Group findings, cite file and concrete gap, and end with the highest-leverage fixes plus proposed edits.
Do not make edits unless the user asks.