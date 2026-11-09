# Feedback

Raw customer signal: support tickets, calls, reviews, churn reasons, feature requests.
Template: [[FB-001-Imaging-Cost-Feedback]]. Copy its frontmatter so `date`, `source` and `sentiment` populate below.

**Verbatim quotes only.** A paraphrase is your interpretation, not evidence. Keep the original
wording, the date, and who said it.

```dataview
TABLE date, source, sentiment
FROM "PM vault/01-Users/Feedback"
WHERE type = "feedback"
SORT date DESC
LIMIT 15
```

## Two rules that matter more than the rest

1. **A feature request is a symptom.** Log it as a problem: who asked, in what situation, what were
   they trying to do. "Add bulk export" is not a problem statement.
2. **Count, don't average.** One loud customer is one data point. Note how many distinct accounts
   raised the same thing — that number is what makes it evidence rather than noise.
