---
type: manual
status: active
updated: 2026-11-09
---

# Agent Setup and Harness Manual

> [!NOTE] For humans and agents
> This is the practical setup and operating manual: install the agent layer, wire the vault, run the first chain, and use `/pm` without inventing evidence. It is not legal advice and it does not define the product.

## 1. What you are setting up

| Layer | What it is | Where it lives |
|---|---|---|
| Vault | Product brain: notes, templates, evidence, decisions | `PM vault` in any Obsidian vault |
| Agent skill | PM procedures and gates | `$HERMES_HOME/skills/productivity/product-management/` |
| Bundle | Turns `/pm` into the PM command | `$HERMES_HOME/skill-bundles/pm.yaml` |
| Git | Local audit trail | `.git` in the repo; the maintainer uses an external git directory |
| Compliance rail | Health-data gate | `11-Compliance/` |

The vault works without the agent layer. `/pm` commands do not.

> [!NOTE] Platform
> The paths below show the maintainer's macOS + iCloud deployment. The harness is platform-neutral.
> On Windows or Linux, use your own folder and a normal `.git`; keep the Dataview prefix aligned with
> the vault layout in [README](../README.md#platform-and-vault-layout).

## 2. Prerequisites

- Obsidian installed.
- The parent `Documents` vault opened in Obsidian — not `PM vault` as a separate vault.
- Dataview enabled in the parent vault: Settings → Community plugins.
- Hermes installed for `/pm` commands.
- Git available for local audit.

Verify Obsidian first:

1. Open `Documents`.
2. Open `PM vault/Dashboard.md`.
3. Confirm the Dataview tables render as tables, even if empty.

## 3. Install the agent layer

The skill and bundle are profile-local. They are not part of the vault repo.

### 3.1 Install the skill

Copy the skill folder from this repository:

`agent/skills/productivity/product-management/` → `$HERMES_HOME/skills/productivity/product-management/`

It must contain `SKILL.md` and its `references/` and `scripts/` folders.

### 3.2 Install the bundle

Copy `agent/skill-bundles/pm.yaml` to:

`$HERMES_HOME/skill-bundles/pm.yaml`

Edit its `Vault root:` line to the absolute path of your vault. The bundle must point at the skill
and at `99-Playbook/Rules.md`.

### 3.3 Reload and verify

```bash
hermes bundles list
hermes bundles show pm
hermes bundles reload
```

Then start Hermes and run:

```text
/pm status
```

Expected result: product health, top problems and opportunities, stale artifacts, and one recommended
next action. On an empty vault, it should say what is missing rather than inventing a product.

If `/pm` is unknown, the bundle is not registered. If it loads but reads the wrong rules file, fix
`pm.yaml`.

## 4. Wire the vault

### 4.1 Folder mode

`PM vault` can be a nested folder or the vault root.

| Layout | Dataview source |
|---|---|
| Nested folder | `FROM "PM vault/02-Problems"` |
| Repository root | `FROM "02-Problems"` |
| Renamed folder | `FROM "<folder>/02-Problems"` |

Choose one layout and apply the same prefix to every query. Do not mix nested and root queries.

### 4.2 Git

```bash
cd "<path to PM vault>"
git status
git log -1 --oneline
```

On this machine `.git` points to `~/Documents/pm-vault-git`. A fresh clone uses a normal `.git`
directory. Never move git internals into a synced folder if that causes conflicts.

### 4.3 Verify links and rendering

```bash
python3 "$HERMES_HOME/skills/productivity/product-management/scripts/check_wikilinks.py" \
  "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/PM vault"
obsidian unresolved vault=Documents
```

Then open `Dashboard.md` and confirm the tables render.

## 5. First run

### 5.1 Decide what is real

The vault starts as a scaffold. `00-Product/Product.md` may be `confidence: none`.

That blocks strategy, roadmap, decisions, and PRDs. It does **not** block research, problems,
opportunities, experiments, challenges, or compliance work.

### 5.2 Fill the product spine

In order:

1. `00-Product/Product.md` — vision, target group, needs, product, business goals.
2. `00-Product/Strategy.md` — target group, needs, business goals, differentiation.
3. `00-Product/Goals.md` — one objective, measurable KRs.
4. `00-Product/Metrics.md` — one North Star, inputs, guardrails.

Use the templates as shape, not as evidence.

### 5.3 Open the compliance gate if health data is involved

If the work touches PII, PHI, ePHI, vendors, or health data:

1. Open the live scope: `11-Compliance/COMP-003-Compliance-Scope.md`.
2. Resolve role, data classification, jurisdictions, obligations, and a named owner.
3. Set `status: approved` or `active` only when resolved.
4. If the status is `draft` or the owner is `Unassigned`, stop.

`COMP-001` is the structure template. It is not a live gate.

### 5.4 Run the smoke test

```text
/pm status
```

Then open `Dashboard.md` and confirm the tables render.

## 6. Daily use

| Command | Use it when | It produces |
|---|---|---|
| `/pm status` | You need the current health and next action | Read-only report |
| `/pm discover <area>` | You have signal but no problem note | Problems, opportunities, map links |
| `/pm analyze <OPP-ID>` | You need an evidence and risk audit | Analysis with gaps |
| `/pm challenge <OPP-ID>` | You need a go/no-go challenge | Adversarial challenge |
| `/pm prd <OPP-ID>` | The opportunity has passed its gate | Solution brief |
| `/pm decide <question>` | A consequential choice needs a record | Proposed decision |
| `/pm review` | You need a vault-wide audit | Findings and proposed fixes |

### 6.1 `/pm status`

Read-only. Expect:

- product objective and priority thesis
- top problems and opportunities
- roadmap items and whether evidence exists
- open decisions
- experiments in flight
- stale artifacts
- one recommended next action

### 6.2 `/pm discover`

Use when you have an observation, interview, support signal, or market source.

Rules:

- Quote sources with URLs and dates.
- Write problems, not feature requests.
- Mark unsourced claims `confidence: low`.
- Put unchosen candidate problems on `99-Playbook/Future-Problem-Statements.md`.

### 6.3 `/pm analyze` and `/pm challenge`

`analyze` asks whether the evidence supports the opportunity.

`challenge` asks what would kill it. A challenge that validates everything has failed. It can
recommend `no-go`, `defer`, or `Pending`; `Pending` is a valid discovery verdict.

### 6.4 `/pm prd`

This is gated. It should refuse when:

- the opportunity has no evidence table
- the challenge has not run
- the primary metric has no baseline
- the value risk is still untested

When refused, run the experiment that would unblock it.

### 6.5 `/pm decide`

A decision record is required when the choice:

- costs more than a week
- is hard to reverse
- changes regulatory posture or data handling
- changes a vendor or BAA
- changes funding, team topology, or governance

The agent proposes; the human accepts.

## 7. The artifact chain

The canonical product chain, stage questions, artifacts, and transition gates live in
[Discovery to Delivery](Discovery-to-Delivery.md). This manual does not restate them.

## 8. Write boundaries

| Boundary | Paths |
|---|---|
| Free to write | `04-Research`, `02-Problems`, `03-Opportunities`, `07-Delivery/Experiments`, `08-Reviews`, `99-Playbook/Templates`, `99-Playbook/Playbooks`, `99-Playbook/Future-Problem-Statements.md` |
| Draft only | `07-Delivery/PRDs`, `06-Roadmap`, `09-Transformation`, `10-Operating-Model`, `11-Compliance` |
| Human-approved only | `00-Product`, `05-Decisions`, `README.md`, `99-Playbook/Rules.md`, `99-Playbook/PM.md`, `99-Playbook/Visual-Standards.md` |

## 9. Working with multiple agents

Use one PM writer per vault.

| Agent role | Writes | Does not write |
|---|---|---|
| PM agent | `02-Problems`, `03-Opportunities`, `07-Delivery/Experiments`, `08-Reviews` | Final product strategy or accepted decisions |
| Research agent | `04-Research` | Opportunity verdicts |
| Delivery agent | `07-Delivery/Experiments` | Roadmap or product strategy |
| Compliance agent | `11-Compliance` drafts | Approval on the human’s behalf |

When another agent produces research, have it hand back the source, date, and evidence. The PM agent
integrates it. Do not let two agents write the same artifact folder concurrently.

## 10. Troubleshooting

| Symptom | Check | Fix |
|---|---|---|
| `/pm` unknown | `hermes bundles list` | Register or reload `pm.yaml` |
| `/pm` reads old rules | `pm.yaml` path | Point to `99-Playbook/Rules.md` |
| Tables empty | Parent vault and Dataview | Open `Documents`, enable Dataview |
| Tables still empty | `FROM` prefix | Use `FROM "PM vault/<folder>"` |
| Links unresolved | `obsidian unresolved` | Fix target or parent-vault registration |
| Product strategy blocked | `00-Product/Product.md` | Fill the product spine |
| PRD refused | Evidence, challenge, baseline | Run the missing experiment |
| Compliance work blocked | `COMP-003` status/owner | Complete scope and assign owner |
| Markdown link broken | Open the target; GitHub shows 404 | Fix the relative path or anchor |
| `check_wikilinks.py` fails | Script output | Fix file target or anchor; this is a legacy wikilink check |
| Agent writes too much | Write boundary | Check `Rules.md` Rule 21 |

## 11. Verification checklist

Before saying the harness works:

- [ ] `hermes bundles list` shows `/pm`
- [ ] `/pm status` returns a report, not an error
- [ ] Dashboard tables render in Obsidian
- [ ] Relative Markdown links resolve on GitHub: open the README and click the main links
- [ ] `obsidian unresolved` reports no unresolved legacy wikilinks
- [ ] `check_wikilinks.py` reports no unresolved wikilinks (legacy check; Markdown links are checked above)
- [ ] `00-Product/Product.md` is filled or explicitly marked `confidence: none`
- [ ] Live compliance scope is completed when health data is involved
- [ ] `VERSION` matches the latest changelog entry and release tag
- [ ] `git status` is clean after an intentional commit

## Related

- [README](../README.md) — human entry point
- [START-HERE](../START-HERE.md) — outcome-led walkthrough
- [PM](PM.md) — agent brief
- [Rules](Rules.md) — operating law
- [Architecture](Architecture.md) — technical contract
- [Discovery to Delivery](Discovery-to-Delivery.md) — canonical product chain
- [Agent Walkthrough](Agent-Walkthrough.md) — guided lab
- [Harness Value](Harness-Value.md) — time-value estimate
- [_Playbooks](Playbooks/_Playbooks.md) — playbook router
