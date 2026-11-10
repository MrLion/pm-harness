# Releases

What shipped, when, and what happened afterwards. Template: [REL-001-Imaging-Estimate-Pilot](../../99-Playbook/Templates/REL-001-Imaging-Estimate-Pilot.md), with frontmatter
`date`, `goal` and `metric_result` feeding the table below.

```dataview
TABLE date, goal, metric_result
FROM ""
WHERE type = "release" AND contains(file.folder, "07-Delivery/Releases") AND project = "pm-harness"
SORT date DESC
```

## Per release, record

| Field | Why |
|---|---|
| Date and contents | The factual record |
| GOAL it was meant to move | Matches the roadmap row — per Pichler, a release without a goal shouldn't ship |
| Metric before / after | With the window, so the comparison is honest |
| What surprised us | The most valuable line in the note, six months later |
| Unexpected cost | Support load, incident, debt taken on |

> A release note with no metric movement recorded is a delivery log, not a learning artifact.
