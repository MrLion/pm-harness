# Problems

`PROB-NNN` notes from [[PROB-001-Imaging-Cost-Problem]] template. **Problem ≠ feature request** — convert "we need X"
into "what problem would X solve" before anything is written.

```dataview
TABLE status, confidence, frequency, severity
FROM "PM vault/02-Problems"
WHERE type = "problem" AND status != "closed"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

## Rule
An empty evidence table means the problem is a **hypothesis**. Set `confidence: low` and say so
out loud — do not let it into the roadmap.
