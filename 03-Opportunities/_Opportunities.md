# Opportunities

`OPP-NNN` notes from [[Opportunity]] — SVPG Product Opportunity Assessment (ten questions) plus
the four big risks. **Purpose: kill weak opportunities cheaply**, not justify ones you like.

```dataview
TABLE status, score, confidence, recommendation
FROM "03-Opportunities"
WHERE type = "opportunity" AND status != "closed"
SORT score DESC
```

## The four risks
value · usability · feasibility · business viability — each with a rating, an owner, and the test
that retires it. A risk with no owner is a risk nobody is retiring.
