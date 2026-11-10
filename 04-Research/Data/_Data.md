# Data

Queries, metric values and instrumentation. Feeds Cagan's Q8 (*how will we measure success?*) and
gives GO Roadmap rows their metrics a baseline.

## Note fields

| Field | Note |
|---|---|
| Question | One question. "How do people use the product" is a fishing trip |
| Source | Warehouse · product analytics · billing · support system |
| Query | The actual query or a link to it — otherwise the number is unreproducible |
| Result | Value **and** the window it covers |
| Definition | What counts as an event; exclusions |
| Caveats | Instrumentation gaps, seasonality, small N |
| Run date | Numbers without a date are decoration |

## Rules

- **A number with no definition is not a metric.** "60% retention" means nothing until you say what
  active means and over what window.
- **Baseline before target.** Every goal needs a starting value; if none exists, the honest entry
  is `unknown` plus an instrument-by date.
- **Log instrumentation gaps here** as findings, not as excuses — a metric you cannot measure is a
  decision you cannot make.

## Notes

```dataview
TABLE date, reliability, source
FROM ""
WHERE type = "research" AND contains(file.folder, "04-Research/Data") AND project = "pm-harness"
SORT date DESC
```
