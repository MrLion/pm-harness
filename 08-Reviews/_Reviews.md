# Reviews

`YYYY-MM.md` per month, from [REVIEW-2027-02-Imaging-Estimate-Pilot](../99-Playbook/Templates/REVIEW-2027-02-Imaging-Estimate-Pilot.md). Two questions, in this order:

1. **Did the goals move?** Pichler's GO metrics: goal, target, actual, met.
2. **Which risks were retired?** value · usability · feasibility · business viability — tested,
   result, still open or closed.

```dataview
LIST
FROM ""
WHERE type = "review" AND contains(file.folder, "08-Reviews") AND project = "pm-harness"
SORT file.name DESC
```

> A **measured miss**, **unknown**, and **not measured** are distinct findings. A review whose
> "what we got wrong" section is empty is a status report, not a review.
