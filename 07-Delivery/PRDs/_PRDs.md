# Solution briefs (PRDs)

`PRD-NNN` notes from [[PRD]] — a Pichler canvas plus acceptance criteria that **links a prototype**,
because Cagan's position is that the prototype is the spec.

```dataview
TABLE status, opportunity, updated, primary_metric
FROM "07-Delivery/PRDs"
SORT updated DESC
```

## Validation gate

Do not write one of these until:

- [ ] The opportunity has an evidence table with at least one source
- [ ] `/pm challenge` has been run and its objections answered
- [ ] The primary metric has a **baseline**

An ungated brief is a draft for discussion, not a delivery document. Empty PRDs in this folder are a
sign the gate is being skipped.
