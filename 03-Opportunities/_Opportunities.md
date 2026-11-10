# Opportunities

See [Discovery Map](Discovery%20Map.md) for the Opportunity Solution Tree linking goals, problems, opportunities,
alternative solutions and experiments.

`OPP-NNN` notes from [OPP-001-Outpatient-Imaging-Cost](../99-Playbook/Templates/OPP-001-Outpatient-Imaging-Cost.md) — SVPG Product Opportunity Assessment (ten questions) plus
the four big risks. **Purpose: kill weak opportunities cheaply**, not justify ones you like.

```dataview
TABLE status, score, confidence, recommendation
FROM ""
WHERE type = "opportunity" AND status != "closed" AND contains(file.folder, "03-Opportunities") AND project = "pm-harness"
SORT score DESC
```

## The four risks
value · usability · feasibility · business viability — each with a rating, an owner, and the test
that retires it. A risk with no owner is a risk nobody is retiring.
