# Experiments

`EXP-NNN` notes from [[Experiment]]. **Each experiment retires exactly one named risk** — value,
usability, feasibility or business viability. If you cannot say which, it is a build, not an
experiment.

```dataview
TABLE status, risk_type, opportunity, start, end
FROM "07-Delivery/Experiments"
WHERE status != "completed"
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
