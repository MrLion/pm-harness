# Problems

`PROB-NNN` notes from [[Problem]] template. **Problem ≠ feature request** — convert "we need X"
into "what problem would X solve" before anything is written.

```dataview
TABLE status, confidence, frequency, severity
FROM "02-Problems"
WHERE type = "problem" AND status != "closed"
SORT confidence ASC
```

## Rule
An empty evidence table means the problem is a **hypothesis**. Set `confidence: low` and say so
out loud — do not let it into the roadmap.
