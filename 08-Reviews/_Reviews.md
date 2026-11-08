# Reviews

`YYYY-MM.md` per month, from [[Review]]. Two questions, in this order:

1. **Did the goals move?** Pichler's GO metrics: goal, target, actual, met.
2. **Which risks were retired?** value · usability · feasibility · business viability — tested,
   result, still open or closed.

```dataview
LIST
FROM "PM vault/08-Reviews"
WHERE type = "review"
SORT file.name DESC
```

> A **measured miss**, **unknown**, and **not measured** are distinct findings. A review whose
> "what we got wrong" section is empty is a status report, not a review.
