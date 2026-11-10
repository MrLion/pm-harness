# Decisions

`DEC-NNN` notes from [DEC-001-Build-Partner-Defer](../99-Playbook/Templates/DEC-001-Build-Partner-Defer.md). A decision that costs more than a week of work, or is hard to
reverse, gets a record. Verbal decisions do not exist — if it isn't written down, it will be
re-litigated in three weeks by someone who wasn't there.

```dataview
TABLE status, date, reversibility, review_date
FROM ""
WHERE type = "decision" AND contains(file.folder, "05-Decisions") AND project = "pm-harness"
SORT date DESC
LIMIT 12
```

## Awaiting outcome

```dataview
TABLE date, review_date, expected_outcome
FROM ""
WHERE type = "decision" AND status = "accepted" AND (actual_outcome = null OR actual_outcome = "Pending") AND contains(file.folder, "05-Decisions") AND project = "pm-harness"
SORT review_date ASC
```

> An accepted decision past its review date with no recorded outcome is the most common defect in a
> PM vault. Every record names a measurable expected outcome and the date you will check it.
