---
type: dashboard
project: pm-harness
artifact: dashboard
status: example
example: true
created: 2026-11-08
updated: 2026-11-08
---

# Example Dashboard — pre-filled template data

This dashboard reads `99-Playbook/Templates` with `FROM ""` plus a folder filter, so it works in a nested or root vault.

To use it on real notes, copy the blocks and change each `FROM` path to the matching canonical folder:

`02-Problems` · `03-Opportunities` · `04-Research` · `05-Decisions` · `07-Delivery` · `08-Reviews`

## Problems

```dataview
TABLE status, confidence, severity, priority
FROM ""
WHERE type = "problem" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

## Opportunities — all

> This table shows every opportunity, including `go`, `defer`, `no-go`, and `Pending`.

```dataview
TABLE status, confidence, recommendation
FROM ""
WHERE type = "opportunity" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

## Opportunities — pending recommendation

> This table is a subset of the first: only opportunities whose recommendation is `Pending`. `defer` and `no-go` are recommendation values, so they do not appear here.

```dataview
TABLE status, confidence, recommendation, review_after
FROM ""
WHERE type = "opportunity" AND recommendation = "Pending" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
```

## Decisions

```dataview
TABLE status, date, reversibility, review_date
FROM ""
WHERE type = "decision" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT date DESC
```

## PRDs

```dataview
TABLE status, opportunity, updated
FROM ""
WHERE type = "prd" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT updated DESC
```

## Experiments

```dataview
TABLE status, opportunity, start, end
FROM ""
WHERE type = "experiment" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT start ASC
```

## Research

```dataview
TABLE category, date, reliability
FROM ""
WHERE type = "research" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT date DESC
```

## Releases

```dataview
TABLE status, date, goal, metric_result
FROM ""
WHERE type = "release" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT date DESC
```

## Reviews

```dataview
LIST
FROM ""
WHERE type = "review" AND contains(file.folder, "99-Playbook/Templates") AND project = "pm-harness"
SORT file.name DESC
```
