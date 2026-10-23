# Decisions

`DEC-NNN` notes from [[Decision]]. A decision that costs more than a week of work, or is hard to
reverse, gets a record. Verbal decisions do not exist — if it isn't written down, it will be
re-litigated in three weeks by someone who wasn't there.

```dataview
TABLE status, date, reversibility, review_date
FROM "05-Decisions"
WHERE type = "decision"
SORT date DESC
LIMIT 12
```

## Awaiting outcome

```dataview
TABLE date, review_date, expected_outcome
FROM "05-Decisions"
WHERE type = "decision" AND status = "accepted" AND (actual_outcome = null OR actual_outcome = "Pending")
SORT review_date ASC
```

> An accepted decision past its review date with no recorded outcome is the most common defect in a
> PM vault. Every record names a measurable expected outcome and the date you will check it.
