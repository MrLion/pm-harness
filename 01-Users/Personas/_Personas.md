# Personas

One note per persona from [PERSONA-001-HDHP-Imaging-Patient](../../99-Playbook/Templates/PERSONA-001-HDHP-Imaging-Patient.md) (Pichler's template). A persona models a real segment; it does
not substitute for talking to one.

```dataview
TABLE status, confidence, evidence_count
FROM ""
WHERE type = "persona" AND contains(file.folder, "01-Users/Personas") AND project = "pm-harness"
SORT evidence_count ASC
```

> `evidence_count: 0` means the persona is a guess. A roadmap built on a guess-shaped persona is a
> guess-shaped roadmap. Per Pichler, keep the evidence base visible in the note itself.
