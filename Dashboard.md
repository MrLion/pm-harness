---
type: dashboard
updated: 2026-11-09
---

# PM Dashboard

Start · [START-HERE](START-HERE.md) · Manual · [Agent-Manual](99-Playbook/Agent-Manual.md) · Chain · [Discovery-to-Delivery](99-Playbook/Discovery-to-Delivery.md) · Walkthrough · [Agent-Walkthrough](99-Playbook/Agent-Walkthrough.md) · Value · [Harness-Value](99-Playbook/Harness-Value.md)

Product · [Product](00-Product/Product.md) · [Scenario](00-Product/Scenario.md) · [Vision](00-Product/Vision.md) · [Strategy](00-Product/Strategy.md) · [Goals](00-Product/Goals.md) · [Metrics](00-Product/Metrics.md)
Roadmap · [Now](06-Roadmap/Now.md) · [Next](06-Roadmap/Next.md) · [Later](06-Roadmap/Later.md)
Discovery · [Discovery Map](03-Opportunities/Discovery%20Map.md)
Transformation · [_Transformation](09-Transformation/_Transformation.md) · Operating model · [_Operating-Model](10-Operating-Model/_Operating-Model.md) · Compliance · [_Compliance](11-Compliance/_Compliance.md)
Operating · [PM](99-Playbook/PM.md) · [Rules](99-Playbook/Rules.md)

---

## Problems

```dataview
TABLE status, confidence, severity, priority
FROM ""
WHERE type = "problem" AND status != "closed" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC,
     choice(severity = "low", 0, choice(severity = "medium", 1, 2)) DESC
```

## Opportunities

```dataview
TABLE status, confidence, recommendation
FROM ""
WHERE type = "opportunity" AND status != "closed" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT choice(confidence = "none", 0, choice(confidence = "low", 1, choice(confidence = "medium", 2, 3))) ASC
```

## Opportunities with no recommendation

```dataview
TABLE confidence, review_after
FROM ""
WHERE type = "opportunity" AND status != "closed" AND (recommendation = null OR recommendation = "Pending") AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
```

## Decisions

```dataview
TABLE status, date, reversibility, review_date
FROM ""
WHERE type = "decision" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT date DESC
LIMIT 12
```

## Decisions awaiting outcome

```dataview
TABLE date, review_date, reversibility
FROM ""
WHERE type = "decision" AND status = "accepted" AND (actual_outcome = null OR actual_outcome = "Pending") AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT review_date ASC
```

## PRDs

```dataview
TABLE status, opportunity, updated
FROM ""
WHERE type = "prd" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT updated DESC
```

## Experiments

```dataview
TABLE status, opportunity, start, end
FROM ""
WHERE type = "experiment" AND status != "completed" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT start ASC
```

## Research

```dataview
TABLE category, date, reliability
FROM ""
WHERE type = "research" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT date DESC
LIMIT 15
```

## Transformation

```dataview
TABLE status, confidence, owner, updated
FROM ""
WHERE contains(file.folder, "09-Transformation") AND type != null AND type != "transformation-index" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT updated DESC
```

## Operating model

```dataview
TABLE status, confidence, owner, updated
FROM ""
WHERE contains(file.folder, "10-Operating-Model") AND type != null AND type != "operating-model-index" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT updated DESC
```

## Compliance

```dataview
TABLE status, confidence, owner, updated
FROM ""
WHERE contains(file.folder, "11-Compliance") AND type != null AND type != "compliance-index" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT updated DESC
```

## Maintenance — missing dates

```dataview
TABLE type, status
FROM ""
WHERE type != null AND (updated = null OR updated = "" OR updated = "YYYY-MM-DD") AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT file.name ASC
```

## Maintenance — not updated in 30 days

```dataview
TABLE type, updated
FROM ""
WHERE type != null AND (updated != null AND updated != "") AND date(updated) < date(today) - dur(30 days) AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT updated ASC
```

## Maintenance — opportunity review overdue

```dataview
TABLE status, confidence, review_after
FROM ""
WHERE type = "opportunity" AND status != "closed" AND review_after != null AND date(review_after) <= date(today) AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT review_after ASC
```

## Maintenance — decision outcome review overdue

```dataview
TABLE status, review_date, reversibility
FROM ""
WHERE type = "decision" AND status = "accepted" AND (actual_outcome = null OR actual_outcome = "Pending") AND review_date != null AND date(review_date) <= date(today) AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT review_date ASC
```

## Maintenance — review deadlines missing

### Open opportunities

```dataview
TABLE status, confidence, updated
FROM ""
WHERE type = "opportunity" AND status != "closed" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
      AND (review_after = null OR review_after = "" OR review_after = "YYYY-MM-DD")
SORT file.name ASC
```

### Accepted decisions awaiting outcome

```dataview
TABLE status, actual_outcome, updated
FROM ""
WHERE type = "decision" AND status = "accepted" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
      AND (actual_outcome = null OR actual_outcome = "Pending")
      AND (review_date = null OR review_date = "" OR review_date = "YYYY-MM-DD")
SORT file.name ASC
```

## Maintenance — cadence overdue

```dataview
TABLE type, updated, review_cadence_days
FROM ""
WHERE review_cadence_days != null AND (updated != null AND updated != "" AND updated != "YYYY-MM-DD") AND date(updated) < date(today) - dur(review_cadence_days + " days") AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT updated ASC
```

## Reviews

```dataview
LIST
FROM ""
WHERE type = "review" AND !contains(file.folder, "99-Playbook") AND !contains(file.folder, "agent") AND !contains(file.folder, "examples")
SORT file.name DESC
```
