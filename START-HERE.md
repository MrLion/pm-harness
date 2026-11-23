# Start Here

> [!NOTE] For humans
> This is the first-run path for a human operator. It takes you from opening the vault to one real problem note in about 30 minutes. Agents start at [PM](99-Playbook/PM.md) and [Rules](99-Playbook/Rules.md).

**One path, three stages:** see the vault work → see the agent work → produce one real problem note.

The harness does not require a filled product or a finished strategy to begin discovery. An empty vault is a valid starting state; what it will not do is invent evidence to fill it.

## Before you begin

1. Open the folder that contains `99-Playbook/Rules.md` in Obsidian.
2. Enable **Dataview**: Settings → Community plugins.
3. Open [Dashboard](Dashboard.md). Empty tables are expected.

If the problem involves PII, PHI, ePHI, or vendor data, stop and read the live [Compliance Scope](11-Compliance/COMP-003-Compliance-Scope.md). A `draft` scope or `Unassigned` owner blocks health-data work.

---

## Stage 1 — See the vault work — 5 minutes

Open [Dashboard](Dashboard.md).

You should see tables, even if they are empty. That proves Obsidian and Dataview are working. It does not prove the agent is installed.

| What you see | What it means |
|---|---|
| Tables render | Obsidian and Dataview are working |
| Tables are empty | Correct; no live artifacts exist yet |
| Tables show raw query text | Dataview is not enabled |
| Tables show sibling-project notes | The `project: pm-harness` filter is missing |

Then choose your route:

- **I only need the vault** → skip to [Stage 3](#stage-3--produce-one-real-problem-note--15-minutes).
- **I want the `/pm` agent** → continue to Stage 2.

---

## Stage 2 — See the agent work — 10 minutes

The skill is profile-local. The vault does not load it from `agent/` at runtime.

From the repository root:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/install_agent_layer.py --vault . --hermes-home "$HERMES_HOME"
```

Start a **new Hermes chat**, then run:

```text
/pm doctor
/pm status
```

`/pm doctor` checks the vault, skill, Dataview, git, compliance gate, and first-problem state. `/pm status` should return a report, not an error. On an empty vault it should say what is missing.

If `/pm` is unknown, the skill is not installed in this profile. See [Agent Manual](99-Playbook/Agent-Manual.md).

Full setup reference: [Agent Manual](99-Playbook/Agent-Manual.md). Guided lab: [Agent Walkthrough](99-Playbook/Agent-Walkthrough.md).

---

## Stage 3 — Produce one real problem note — 15 minutes

Use `PROB-` for problems, `OPP-` for opportunities, `RESEARCH-` for evidence, `DEC-` for decisions, and `EXP-` for experiments.

### 3.1 Capture the observation

Ask three questions:

1. Is this a new product or an existing one?
2. Who has the problem?
3. What did you observe?

Use an observation, not a feature request:

- Weak: “Add a price estimator.”
- Better: “Adults on HDHP plans cannot tell what an outpatient imaging visit will cost before they book.”

### 3.2 Create the scaffold

With the agent:

```text
/pm start
```

Without the agent:

```bash
python3 scripts/new_artifact.py --vault . --type problem \
  --title "Patients cannot predict imaging cost" \
  --slug imaging-cost
```

Both routes allocate the next `PROB-NNN`, set the filename, `project`, `id`, and dates, and create the section skeleton. They do not invent evidence.

### 3.3 Fill the problem, not the solution

Open the new note and fill:

- **Problem Statement** — who experiences what, when, and at what cost.
- **User / Segment** — the affected group. Link a live persona only if one exists.
- **JTBD** — “When ______, I want ______, so I can ______.”
- **Evidence** — quote the source in the row. If there is no source, write `Evidence unavailable.` and leave `confidence: low`.
- **Next evidence** — the cheapest observation that would change your confidence.
- **Frequency / Severity** — `Unknown` is valid. Do not guess.
- **Buyer** — `Unresolved` is valid.

Do not add a solution column. A problem note is not a PRD.

### 3.4 Check it

```bash
python3 scripts/validate_vault.py
```

Then run:

```text
/pm status
```

The report should now show one live problem. If it does not, check that the note has `project: pm-harness` and `type: problem`.

---

## What “good” looks like

- [ ] The Dashboard renders.
- [ ] `/pm doctor` passes, or every failure has a named next action.
- [ ] One real `PROB-NNN` note exists.
- [ ] The problem contains no embedded solution.
- [ ] Every claim is linked to evidence or marked `Evidence unavailable.`
- [ ] No PRD or decision has been written yet.

The last point is deliberate. A PRD without a baseline, a challenge, and evidence is the failure the harness exists to prevent.

---

## If you get stuck

| Symptom | Fix |
|---|---|
| `/pm` unknown | Install the skill with the command in Stage 2; start a new chat |
| `/pm` appears twice | Remove any bundle named `pm`; keep only the skill |
| Tables render as text | Enable Dataview in the vault that contains the harness |
| Tables are empty | Expected on a fresh vault; create one problem |
| Tables show other projects | Add `project: pm-harness` to the note; check the query |
| Validator fails on a link | Fix the relative Markdown path in the note it names |
| Compliance work blocked | `COMP-003` is `draft` or `Unassigned`; complete it before health data |
| Agent fills product strategy | Stop; `00-Product` is human-approved only |

---

## Where to go next

| Need | Page |
|---|---|
| Setup, commands, troubleshooting | [Agent Manual](99-Playbook/Agent-Manual.md) |
| Guided discovery-to-decision lab | [Agent Walkthrough](99-Playbook/Agent-Walkthrough.md) |
| Canonical chain and gates | [Discovery to Delivery](99-Playbook/Discovery-to-Delivery.md) |
| Choose a playbook | [README](README.md#choose-your-playbook) |
| Product spine | [Product](00-Product/Product.md) |
| Compliance rail | [Compliance Scope](11-Compliance/COMP-003-Compliance-Scope.md) |
