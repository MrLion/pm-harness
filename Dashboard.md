---
type: dashboard
---

# Hermes PM Dashboard

Start · [[START-HERE]]

Product · [[Product]] · [[PM vault/00-Product/Vision|Vision]] · [[PM vault/00-Product/Strategy|Strategy]] · [[PM vault/00-Product/Goals|Goals]] · [[PM vault/00-Product/Metrics|Metrics]]
Roadmap · [[Now]] · [[Next]] · [[Later]]
Discovery · [[Discovery Map]]
Transformation · [[_Transformation]] · Operating model · [[_Operating-Model]] · Compliance · [[_Compliance]]
Operating · [[PM]] · [[Rules]]

---

## Problems

```dataview
TABLE status, confidence, severity, priority
FROM "PM vault/02-Problems"
WHERE type = "problem" AND status != "closed"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC,
     choice(severity = "low", 0, choice(severity = "medium", 1, 2)) DESC
```

## Opportunities

```dataview
TABLE status, confidence, recommendation
FROM "PM vault/03-Opportunities"
WHERE type = "opportunity" AND status != "closed"
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

## Opportunities with no recommendation

```dataview
TABLE confidence, review_after
FROM "PM vault/03-Opportunities"
WHERE type = "opportunity" AND status != "closed" AND (recommendation = null OR recommendation = "Pending")
```

## Decisions

```dataview
TABLE status, date, reversibility, review_date
FROM "PM vault/05-Decisions"
WHERE type = "decision"
SORT date DESC
LIMIT 12
```

## Decisions awaiting outcome

```dataview
TABLE date, review_date, reversibility
FROM "PM vault/05-Decisions"
WHERE type = "decision" AND status = "accepted" AND (actual_outcome = null OR actual_outcome = "Pending")
SORT review_date ASC
```

## PRDs

```dataview
TABLE status, opportunity, updated
FROM "PM vault/07-Delivery/PRDs"
WHERE type = "prd"
SORT updated DESC
```

## Experiments

```dataview
TABLE status, opportunity, start, end
FROM "PM vault/07-Delivery/Experiments"
WHERE type = "experiment" AND status != "completed"
SORT start ASC
```

## Research

```dataview
TABLE category, date, reliability
FROM "PM vault/04-Research"
WHERE type = "research"
SORT date DESC
LIMIT 15
```

## Transformation

```dataview
TABLE status, confidence, owner, updated
FROM "PM vault/09-Transformation"
WHERE type != null AND type != "transformation-index"
SORT updated DESC
```

## Operating model

```dataview
TABLE status, confidence, owner, updated
FROM "PM vault/10-Operating-Model"
WHERE type != null AND type != "operating-model-index"
SORT updated DESC
```

## Compliance

```dataview
TABLE status, confidence, owner, updated
FROM "PM vault/11-Compliance"
WHERE type != null AND type != "compliance-index"
SORT updated DESC
```

## Maintenance — missing dates

```dataview
TABLE type, status
FROM "PM vault/00-Product" OR "PM vault/01-Users" OR "PM vault/02-Problems" OR "PM vault/03-Opportunities" OR "PM vault/05-Decisions" OR "PM vault/07-Delivery" OR "PM vault/04-Research" OR "PM vault/06-Roadmap" OR "PM vault/08-Reviews" OR "PM vault/09-Transformation" OR "PM vault/10-Operating-Model" OR "PM vault/11-Compliance"
WHERE type != null AND (updated = null OR updated = "" OR updated = "YYYY-MM-DD")
SORT file.name ASC
```

## Maintenance — not updated in 30 days

```dataview
TABLE type, updated
FROM "PM vault/00-Product" OR "PM vault/01-Users" OR "PM vault/02-Problems" OR "PM vault/03-Opportunities" OR "PM vault/05-Decisions" OR "PM vault/07-Delivery" OR "PM vault/04-Research" OR "PM vault/06-Roadmap" OR "PM vault/08-Reviews" OR "PM vault/09-Transformation" OR "PM vault/10-Operating-Model" OR "PM vault/11-Compliance"
WHERE type != null AND (updated != null AND updated != "") AND date(updated) < date(today) - dur(30 days)
SORT updated ASC
```

## Maintenance — opportunity review overdue

```dataview
TABLE status, confidence, review_after
FROM "PM vault/03-Opportunities"
WHERE type = "opportunity" AND status != "closed" AND review_after != null AND date(review_after) <= date(today)
SORT review_after ASC
```

## Maintenance — decision outcome review overdue

```dataview
TABLE status, review_date, reversibility
FROM "PM vault/05-Decisions"
WHERE type = "decision" AND status = "accepted" AND (actual_outcome = null OR actual_outcome = "Pending") AND review_date != null AND date(review_date) <= date(today)
SORT review_date ASC
```

## Maintenance — review deadlines missing

### Open opportunities

```dataview
TABLE status, confidence, updated
FROM "PM vault/03-Opportunities"
WHERE type = "opportunity" AND status != "closed"
      AND (review_after = null OR review_after = "" OR review_after = "YYYY-MM-DD")
SORT file.name ASC
```

### Accepted decisions awaiting outcome

```dataview
TABLE status, actual_outcome, updated
FROM "PM vault/05-Decisions"
WHERE type = "decision" AND status = "accepted"
      AND (actual_outcome = null OR actual_outcome = "Pending")
      AND (review_date = null OR review_date = "" OR review_date = "YYYY-MM-DD")
SORT file.name ASC
```

## Maintenance — cadence overdue

```dataview
TABLE type, updated, review_cadence_days
FROM "PM vault/00-Product" OR "PM vault/01-Users" OR "PM vault/06-Roadmap" OR "PM vault/08-Reviews"
WHERE review_cadence_days != null AND (updated != null AND updated != "" AND updated != "YYYY-MM-DD") AND date(updated) < date(today) - dur(review_cadence_days + " days")
SORT updated ASC
```

## Reviews

```dataview
LIST
FROM "PM vault/08-Reviews"
WHERE type = "review"
SORT file.name DESC
```
