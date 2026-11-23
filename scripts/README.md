# Scripts

| Script | Purpose |
|---|---|
| `doctor.py` | Check vault wiring, skill install, Dataview, git, and the first-problem state |
| `new_artifact.py` | Allocate the next `PROB-NNN` and create a blank problem scaffold |
| `validate_vault.py` | Validate links, anchors, frontmatter, IDs, template fill markers, gates, and template-as-evidence citations |
| `install_agent_layer.py` | Install the `pm` skill into a Hermes profile |

## Doctor

```bash
python3 scripts/doctor.py --vault . --hermes-home "$HERMES_HOME"
```

Exit code 1 means a blocking check failed. Warnings do not block the vault.

## Create a problem scaffold

```bash
python3 scripts/new_artifact.py --vault . --type problem \
  --title "Patients cannot predict imaging cost" --slug imaging-cost
```

The script allocates the next `PROB-NNN`, creates the file in `02-Problems/`, and leaves the body
sections for the operator to fill. It does not invent evidence.

## Validate

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/validate_vault.py
python3 scripts/validate_vault.py examples/vertical-slice
```

Exit code 1 means an error. Warnings do not fail CI.

## Install the agent layer

```bash
export HERMES_HOME="$HOME/.hermes/profiles/pdm"
python3 scripts/install_agent_layer.py --vault . --hermes-home "$HERMES_HOME"
```

Use `--update` to replace an existing skill. Without it, the installer refuses to overwrite the
target.
