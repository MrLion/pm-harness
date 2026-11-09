# Agent layer

> [!NOTE] For humans
> This folder is the source for the agent layer. It is not loaded automatically from the repository. Copy it into your Hermes profile once, then edit the vault path.

## What is here

| Path | Purpose |
|---|---|
| `skills/productivity/product-management/` | PM skill: procedures, references, and the wikilink checker |
| `skill-bundles/pm.yaml` | `/pm` command routing |

## Install

Set `HERMES_HOME` to the profile that should own the agent. On this machine that is
`~/.hermes/profiles/pdm`.

```bash
export HERMES_HOME="$HOME/.hermes/profiles/pdm"

mkdir -p "$HERMES_HOME/skills/productivity" "$HERMES_HOME/skill-bundles"
cp -R agent/skills/productivity/product-management "$HERMES_HOME/skills/productivity/"
cp agent/skill-bundles/pm.yaml "$HERMES_HOME/skill-bundles/pm.yaml"
```

Edit `pm.yaml` and replace:

```text
Vault root: <absolute path to the vault root>
```

with the absolute path that contains `99-Playbook/Rules.md`.

Then reload and verify:

```bash
hermes bundles list
hermes bundles show pm
hermes bundles reload
```

Start Hermes and run:

```text
/pm status
```

Expected result: a read-only status report, not an error.

## Notes

- The skill is profile-local; it is not read from `agent/` at runtime.
- If you update the repository copy, copy it into `$HERMES_HOME` again and reload.
- The bundle is a template. Do not leave the placeholder path in place.
- Do not copy `.obsidian/` or git internals into the skill folder.
- The skill supports both root and nested vault layouts; set the Dataview prefix to match the layout.
