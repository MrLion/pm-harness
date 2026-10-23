---
type: dashboard
---

# Hermes PM Dashboard

Product · [[Product]] [[Vision]] [[Strategy]] [[Goals]] [[Metrics]]
Roadmap · [[Now]] [[Next]] [[Later]]
Operating · [[PM]] [[Rules]]

---

## Problems
```dataview
TABLE status, confidence, severity, priority
FROM "PM vault/02-Problems"
WHERE type = "problem" AND status != "closed"
SORT confidence ASC, severity DESC
```

## Opportunities
```dataview
TABLE status, confidence, recommendation
FROM "PM vault/03-Opportunities"
WHERE type = "opportunity" AND status != "closed"
SORT confidence ASC
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
SORT updated DESC
```

## Experiments
```dataview
TABLE status, opportunity, start, end
FROM "PM vault/07-Delivery/Experiments"
WHERE status != "completed"
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

## Stale (not touched in 30+ days)
```dataview
TABLE updated, status
FROM "PM vault/00-Product" OR "PM vault/02-Problems" OR "PM vault/03-Opportunities" OR "PM vault/05-Decisions"
WHERE updated AND date(updated) < date(today) - dur(30 days)
SORT updated ASC
```

---

## Reviews
```dataview
LIST
FROM "PM vault/08-Reviews"
SORT file.name DESC
```