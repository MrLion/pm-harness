# Experiments

`EXP-NNN` notes from [EXP-001-Comprehension-Test](../../99-Playbook/Templates/EXP-001-Comprehension-Test.md). **Each experiment names one primary risk** — value,
usability, feasibility or business viability. Secondary observations can be recorded separately. If
you cannot say which risk is primary, it is a build, not an experiment.

```dataview
TABLE status, risk_type, risk_owner, opportunity, start, end
FROM ""
WHERE type = "experiment" AND status != "completed" AND contains(file.folder, "07-Delivery/Experiments") AND project = "pm-harness"
SORT start ASC
```

## Pre-registration rule

Success, failure and kill criteria are written **before** the data arrives. Criteria chosen after
seeing results are not criteria — they are rationalisation.

| Risk | Typical cheapest test |
|---|---|
| Value | fake door, concierge run, two-week offer pilot |
| Usability | 4–5 person prototype test |
| Feasibility | timeboxed engineering spike |
| Business viability | pricing conversations, contract/legal review |
