# Repository hardening

Use when the PM harness repository is presented to a fresh user, audited for enforcement, or prepared for release.

## 1. Contract validator

Install once, then run both scopes:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/validate_vault.py
python3 scripts/validate_vault.py examples/vertical-slice
```

The validator checks relative Markdown links and anchors, frontmatter parsing, duplicate IDs,
filename/ID consistency, required artifact fields, `project` markers, product-template `[FILL]`
markers, open compliance gates, overdue accepted decisions, and orphan candidates. It also rejects
impossible calendar dates and requires a named owner, data classification, and jurisdiction on an
`approved` or `active` compliance scope. It exits non-zero on errors; warnings are informational.

Put both commands in CI (`.github/workflows/validate.yml`) as separate steps. The default run skips
`examples/`, so a root-only CI job does not protect the worked slice.

Do not use `check_wikilinks.py` as the link gate after the vault has converted to Markdown links. It
only sees `[[...]]` and will report zero. Keep it only for an Obsidian-only copy that still uses
wikilinks.

## 2. Layout-agnostic and isolated Dashboard

Fresh clones are often opened at the repository root, not inside a parent vault. Do not leave
`FROM "PM vault/..."` in the standard Dashboard.

Use:

```dataview
FROM ""
WHERE type = "problem"
  AND project = "pm-harness"
  AND !contains(file.folder, "99-Playbook")
  AND !contains(file.folder, "agent")
  AND !contains(file.folder, "examples")
```

This works for root, nested, and renamed-folder layouts. A `type:` filter alone does not isolate a
shared Obsidian vault: a sibling project can have a note with the same `type`. `project: pm-harness`
is the project boundary. Every artifact note, including templates, carries it; fixtures use
`pm-harness-example`.

Keep folder exclusions too: exclude `99-Playbook` (templates and docs), `agent` (profile source), and
`examples` (synthetic fixtures) so template examples do not appear as live artifacts. Keep folder
prefixes only in deliberately folder-scoped custom queries.

When adding a live note, copy the marker from the template. A missing `project:` makes the note
invisible to every Dashboard table even when its `type:` is correct.

## 3. Installer, not a placeholder path

Do not ship a bundle whose only setup step is "edit `<absolute path>`". Provide:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/install_agent_layer.py --vault . --hermes-home "$HERMES_HOME"
hermes bundles reload
```

The installer should:

- validate the source bundle before copying anything: YAML parses, exactly one placeholder, the
  `pm` skill is declared, and the instruction points at `99-Playbook/Rules.md`;
- copy the skill and write the bundle with the absolute vault path;
- refuse to run when `99-Playbook/Rules.md` is absent;
- refuse to overwrite an existing skill or `pm.yaml` unless `--update` is passed;
- report the colliding paths and the `--update` remedy.

The placeholder in `agent/skill-bundles/pm.yaml` remains a template input, not the install path.
`PyYAML` is required; `scripts/requirements.txt` is the install source, and a missing dependency
should be reported as an actionable error, not a traceback.

Also remove maintainer-specific paths from `PM.md` (`vault_root`, `git_dir`); use `.` and `.git`, not
iCloud home paths.

## 4. License split

A public harness that contains both original code and Pichler-derived templates needs two explicit layers:

- `LICENSE` — MIT for scripts, agent layer, and original docs.
- `NOTICE` — names the files or sections under CC BY-SA 4.0, the Pichler attribution, and the source URL.

A single `license: MIT` line in a skill does not license Pichler-derived template text. Do not claim one license for the whole repository when the template set has share-alike content.

## 5. Worked vertical slice

A complete synthetic chain in `examples/vertical-slice/` is a fixture, not market evidence. Mark every note `example: true` and `synthetic: true`, link each stage, and keep the live decision unchanged. It exercises the gates and the validator; it does not fill `actual_outcome`.

Use unique IDs or exclude the fixture from live-root validation. If the fixture reuses live IDs, the validator must skip `examples/` when run at the repository root, and Dashboard queries must exclude `examples/`.

## 6. Fresh-clone acceptance check

Before saying a clone works:

- `python3 -m pip install -r scripts/requirements.txt` succeeds.
- `python3 scripts/validate_vault.py` returns 0 errors.
- `python3 scripts/validate_vault.py examples/vertical-slice` returns 0 errors.
- CI runs both validator commands as separate steps.
- The Dashboard has no `PM vault/` hardcoding, and every `WHERE` clause carries `project = "pm-harness"`.
- Every live artifact has `project: pm-harness`; fixtures use `pm-harness-example`.
- `scripts/install_agent_layer.py` refuses an existing skill or bundle without `--update`, preserves
the existing files when it refuses, and writes a bundle without the placeholder when allowed.
- A deliberately invalid approved compliance scope fails: `Unassigned` owner, unknown classification
  or jurisdiction, and an impossible date should each produce an error.
- `PM.md` has no absolute home path.
- `LICENSE` and `NOTICE` both exist.
- The live compliance gate still reports `draft` / `Unassigned` rather than pretending to pass.
