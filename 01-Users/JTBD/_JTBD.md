# Jobs to be done

One note per job, from [JTBD-001-Know-Cost-Before-Booking](../../99-Playbook/Templates/JTBD-001-Know-Cost-Before-Booking.md). Supporting lens for [PROB-001-Imaging-Cost-Problem](../../99-Playbook/Templates/PROB-001-Imaging-Cost-Problem.md) and [PERSONA-001-HDHP-Imaging-Patient](../../99-Playbook/Templates/PERSONA-001-HDHP-Imaging-Patient.md) — not a Pichler or
SVPG artifact, but the clearest way to state what a user is actually trying to accomplish.

```dataview
TABLE status, confidence
FROM ""
WHERE type = "jtbd" AND contains(file.folder, "01-Users/JTBD") AND project = "pm-harness"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

> When writing one, the **anxiety** and **habit** forces are the ones that decide whether a
> validated opportunity lands. A job with no anxiety named is usually under-analysed.
