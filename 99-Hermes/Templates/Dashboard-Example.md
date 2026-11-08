---
type: dashboard
artifact: dashboard
status: example
example: true
created: 2026-11-08
updated: 2026-11-08
---

# Example Dashboard — pre-filled template data

This dashboard reads `PM vault/99-Hermes/Templates`, so it renders the pre-filled examples instead of empty artifact folders.

To use it on real notes, copy the blocks and change each `FROM` path to the matching canonical folder:

`02-Problems` · `03-Opportunities` · `04-Research` · `05-Decisions` · `07-Delivery` · `08-Reviews`

## Problems

```dataview
TABLE status, confidence, severity, priority
FROM "PM vault/99-Hermes/Templates"
WHERE type = "problem"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

## Opportunities — all

> This table shows every opportunity, including `go`, `defer`, `no-go`, and `Pending`.

```dataview
TABLE status, confidence, recommendation
FROM "PM vault/99-Hermes/Templates"
WHERE type = "opportunity"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

## Opportunities — pending recommendation

> This table is a subset of the first: only opportunities whose recommendation is `Pending`. `defer` and `no-go` are recommendation values, so they do not appear here.

```dataview
TABLE status, confidence, recommendation, review_after
FROM "PM vault/99-Hermes/Templates"
WHERE type = "opportunity" AND recommendation = "Pending"
```

## Decisions

```dataview
TABLE status, date, reversibility, review_date
FROM "PM vault/99-Hermes/Templates"
WHERE type = "decision"
SORT date DESC
```

## PRDs

```dataview
TABLE status, opportunity, updated
FROM "PM vault/99-Hermes/Templates"
WHERE type = "prd"
SORT updated DESC
```

## Experiments

```dataview
TABLE status, opportunity, start, end
FROM "PM vault/99-Hermes/Templates"
WHERE type = "experiment"
SORT start ASC
```

## Research

```dataview
TABLE category, date, reliability
FROM "PM vault/99-Hermes/Templates"
WHERE type = "research"
SORT date DESC
```

## Releases

```dataview
TABLE status, date, goal, metric_result
FROM "PM vault/99-Hermes/Templates"
WHERE type = "release"
SORT date DESC
```

## Reviews

```dataview
LIST
FROM "PM vault/99-Hermes/Templates"
WHERE type = "review"
SORT file.name DESC
```
