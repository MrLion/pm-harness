# Users

Interviews, observation and support signal. This is where Pichler's NEEDS stop being assumptions,
and where most value risk is actually retired.

## Interview note fields

| Field | Note |
|---|---|
| Who | Role, org size, sites — enough to check representativeness |
| Method | Interview / observation / shadowing; duration |
| What we asked | The questions, so a biased prompt is visible later |
| What they *do* today | Behaviour, not stated preference |
| Verbatim quotes | **Verbatim only.** A paraphrase is not evidence |
| Frequency & severity | How often it happens, what it costs |
| Sampling bias | Who is missing from this sample — the clinics that wouldn't talk to you |

## Rules

- **Ask about the past, not the future.** "Would you use…" produces polite noise; "what did you do
  last time this happened" produces evidence.
- **Never record a belief about a third party as fact.** "My staff would love that" is Dana's
  hypothesis about her staff — the value risk is still untested.
- **State N, and don't generalise past it.** A larger N does not repair a biased sample.
- **Write down the disconfirming interviews.** The clinic that does it differently is often the
  most informative note in the folder.

## Notes

```dataview
TABLE date, reliability, source
FROM "PM vault/04-Research/Users"
WHERE type = "research"
SORT date DESC
```
