# Agent layer

> [!NOTE] For humans
> This folder is the source for the agent layer. It is not loaded automatically from the repository. Run the installer once to copy it into your Hermes profile and write the vault path.

## What is here

| Path | Purpose |
|---|---|
| `skills/productivity/product-management/` | PM skill: procedures, references, and the wikilink checker |
| `skill-bundles/pm.yaml` | `/pm` command routing |

## Install

From the repository root:

```bash
export HERMES_HOME="$HOME/.hermes/profiles/pdm"
python3 -m pip install -r scripts/requirements.txt
python3 scripts/install_agent_layer.py --vault . --hermes-home "$HERMES_HOME"
```

The installer copies the skill and writes `pm.yaml` with the absolute vault path. It validates the
source bundle first, refuses to run if the target does not contain `99-Playbook/Rules.md`, and refuses
to overwrite an existing skill or `pm.yaml` unless you pass `--update`.

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
