# Jobs to be done

One note per job, from [[JTBD-001-Know-Cost-Before-Booking]]. Supporting lens for [[PROB-001-Imaging-Cost-Problem]] and [[PERSONA-001-HDHP-Imaging-Patient]] — not a Pichler or
SVPG artifact, but the clearest way to state what a user is actually trying to accomplish.

```dataview
TABLE status, confidence
FROM "PM vault/01-Users/JTBD"
WHERE type = "jtbd"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

> When writing one, the **anxiety** and **habit** forces are the ones that decide whether a
> validated opportunity lands. A job with no anxiety named is usually under-analysed.
