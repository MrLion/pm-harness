# Agent layer

> [!NOTE] For humans
> This folder is the source for the agent layer. It is not loaded automatically from the repository. Run the installer once to copy it into your Hermes profile.

## What is here

| Path | Purpose |
|---|---|
| `skills/productivity/pm/` | PM skill: procedures, references, and the wikilink checker |

## Install

From the repository root:

```bash
export HERMES_HOME="$HOME/.hermes/profiles/pdm"
python3 -m pip install -r scripts/requirements.txt
python3 scripts/install_agent_layer.py --vault . --hermes-home "$HERMES_HOME"
```

The installer copies the skill, refuses to run if the target does not contain
`99-Playbook/Rules.md`, and refuses to overwrite an existing skill unless you pass `--update`.

Start a new Hermes chat and run:

```text
/pm status
```

Expected result: a read-only status report, not an error.

## Notes

- The skill is profile-local; it is not read from `agent/` at runtime.
- If you update the repository copy, run the installer again with `--update`, then start a new chat.
- Do not copy `.obsidian/` or git internals into the skill folder.
- The skill supports both root and nested vault layouts; set the Dataview prefix to match the layout.
