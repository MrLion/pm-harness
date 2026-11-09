# Documentation Ownership

Each page in the PM harness has one job. A new page must link to the owner of a rule rather than restate it.

| Page | Owns | Must not |
|---|---|---|
| `README.md` | Human entry and playbook routing | Restate the chain or write boundaries |
| `99-Playbook/PM.md` | Agent routing and read order | Become the rules or the chain |
| `99-Playbook/Rules.md` | Enforceable constraints and write boundaries | Explain the whole product flow |
| `99-Playbook/Architecture.md` | Folder model, IDs, git, verification | Define product gates |
| `99-Playbook/Discovery-to-Delivery.md` | Canonical product chain and transition gates | Become a second rulebook |
| `99-Playbook/Agent-Manual.md` | Installation, command reference, troubleshooting | Teach the sequence as a lab |
| `99-Playbook/Agent-Walkthrough.md` | Guided lab and checkpoints | Define policy or permission boundaries |
| `99-Playbook/Harness-Value.md` | Time-value estimates, assumptions, validation plan | Become a measured benchmark or sales claim |
| `99-Playbook/Playbooks/_Playbooks.md` | Playbook/method lineage and router | Restate the canonical product chain |
| `99-Playbook/Templates/_Templates.md` | Artifact shapes and framework mapping | Restate a competing chain |

## Rules

- Give a new document one job and a named owner for every fact it repeats.
- When a page restates a chain, gate, write boundary, or ID rule, diff it against the owner and delete the copy.
- IDs belong to `Architecture.md`; `PM.md` and `Rules.md` link to its identity section instead of restating allocation.
- `PM.md` owns routing, not stage order: its read order links to `Discovery-to-Delivery` rather than becoming a second chain.
- Simplified permission ladders are the highest drift risk. Mirror `Rules.md` Rule 21 exactly.
- `05-Decisions` is human-approved only. An agent may prepare options, tradeoffs, and a recommendation, but it must not write or accept the decision record.
- A guided lab may repeat prompts and checkpoints; it must not redefine policy.
- When deleting a section, grep for sentences that refer to it. A removed table can leave a dangling explanation of a table that no longer exists.
- Value/ROI numbers are hypotheses, not measurements. Keep the assumptions, confidence, non-benefits, and validation measures with the estimate; do not move a percentage into README, Agent-Manual, or a playbook as a headline claim. Keep one weighted 40-hour roll-up, not a separate per-task table; see `value-estimation.md`.
