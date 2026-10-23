# Reviews

`YYYY-MM.md` per month, from [[Review]]. Two questions, in this order:

1. **Did the goals move?** Pichler's GO metrics: goal, target, actual, met.
2. **Which risks were retired?** value · usability · feasibility · business viability — tested,
   result, still open or closed.

```dataview
LIST
FROM "08-Reviews"
SORT file.name DESC
```

> A goal whose metric was never recorded counts as **not met**, and a review whose "what we got
> wrong" section is empty is a status report, not a review.
