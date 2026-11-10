# Scripts

| Script | Purpose |
|---|---|
| `validate_vault.py` | Validate links, anchors, frontmatter, IDs, template fill markers, and gates |
| `install_agent_layer.py` | Install the skill and write the vault path into `pm.yaml` |

## Validate

```bash
python3 scripts/validate_vault.py
python3 scripts/validate_vault.py examples/vertical-slice
```

Exit code 1 means an error. Warnings do not fail CI.

## Install the agent layer

```bash
export HERMES_HOME="$HOME/.hermes/profiles/pdm"
python3 scripts/install_agent_layer.py --vault . --hermes-home "$HERMES_HOME"
hermes bundles reload
```
