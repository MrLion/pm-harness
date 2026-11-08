---
type: persona
artifact: persona
id: PERSONA-000
status: draft
confidence: low
evidence_count: 0
created: YYYY-MM-DD
updated: YYYY-MM-DD
framework: Pichler
source: https://www.romanpichler.com/the-persona-template/
---


# Persona

## Example — US healthcare consumer

> [!example]- Example — cost-conscious HDHP adult
> **Persona:** Patient on employer-sponsored HDHP choosing outpatient imaging.
> **Observed behavior:** They look for provider availability, review scores, and out-of-pocket cost.
> **Why:** They avoid surprise bills and postponed care.

> [!todo] Ambiguous fields — how to fill
> | Field | Meaning | If unsure |
> |---|---|---|
> | evidence_count | number of real sources | 0 = guess, not persona |
> | role | who they are | keep narrow |
> | context | org size / tools / constraints | make actionable |
> | pains | friction source | avoid generic language |




> [!example]- Example — cost-conscious HDHP adult
> **Persona:** Patient on employer-sponsored HDHP choosing outpatient imaging.
> **Observed behavior:** They look for provider availability, review scores, and out-of-pocket cost.
> **Why:** They avoid surprise bills and postponed care.
>
> Sourced example, not product evidence.

> [!todo] Ambiguous fields — how to fill
> | Field | Meaning | If unsure |
> |---|---|---|
> | evidence_count | number of real sources | 0 = guess, not persona |
> | role | who they are | keep narrow |
> | context | org size / tools / constraints | make actionable |
> | pains | friction source | avoid generic language |

> [!warning] Evidence rule
> `evidence_count: 0` means this persona is a guess. A persona is a modelling technique, not a
> substitute for talking to real users. Never let a guess-shaped persona drive a roadmap.

## Profile

| Field | Content |
|---|---|
| Name (representative, not a real person) | [FILL] |
| Role | [FILL] |
| Context (org size, tools, constraints) | [FILL] |
| Goals | [FILL] |
| Pains | [FILL] |
| Observed behaviour (not stated behaviour) | [FILL] |

## Evidence base

| Type | Source | Date | Count |
|---|---|---|---|
| [[RESEARCH-000]] | | | 0 |

## Related

- [[PROB-000]]

---

> [!example]- Worked example — fictional
> **Dana, practice manager.** 14 staff, two sites. Tools: spreadsheet rota, WhatsApp group, desktop
> payroll suite. **Goals:** week's rota published by Thursday; never short-staffed at open.
> **Pains:** covering a sick call takes six calls; no visibility of who is already near 48 hours.
> **Observed:** builds the rota Sunday evening at home, keeps a personal WhatsApp list of people who
> say yes. **Evidence:** 11 interviews — 9 describe the same phone-tree behaviour.
