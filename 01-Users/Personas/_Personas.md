# Personas

One note per persona from [[PERSONA-001-HDHP-Imaging-Patient]] (Pichler's template). A persona models a real segment; it does
not substitute for talking to one.

```dataview
TABLE status, confidence, evidence_count
FROM "PM vault/01-Users/Personas"
WHERE type = "persona"
SORT evidence_count ASC
```

> `evidence_count: 0` means the persona is a guess. A roadmap built on a guess-shaped persona is a
> guess-shaped roadmap. Per Pichler, keep the evidence base visible in the note itself.
