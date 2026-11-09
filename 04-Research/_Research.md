# Research

The evidence layer. Both frameworks depend on it: Pichler's NEEDS are unvalidated assumptions until
research backs them, and Cagan's four risks are retired by research, not by opinion.

**Everything here is a note about a source.** No source, no note. Write `Evidence unavailable.`
rather than reasoning from plausibility.

## What goes where

| Folder | Holds | Answers |
|---|---|---|
| [[_Market]] | market size, segmentation, timing, regulation | How big, and why now? (Cagan Q3, Q6) |
| [[_Competitors]] | teardowns, pricing, positioning | What alternatives exist, where do they fail our group? (Cagan Q4) |
| [[_Users]] | interviews, observation, support signal | Who hurts, how often, what do they do today? |
| [[_Data]] | queries, metrics, instrumentation | What do the numbers actually say? |

## Evidence ladder

Confidence in a problem or opportunity can never exceed the strength of its weakest
load-bearing evidence.

`reliability` values are: `weak` · `medium` · `strong`.

| Strength | Example | Can carry a roadmap? |
|---|---|---|
| **strong** | behavioural data you can reproduce; a consistent pattern across an appropriate sample | yes |
| **medium** | a well-conducted small study; support-ticket volume; one customer's own data | with a stated caveat |
| **weak** | one conversation; a manager's belief about their staff; an undated competitor page | no |

> Counts do not establish representativeness. Method quality, sample selection, bias and the limits
> of the source can raise or lower the rating independently of N.

> The common trap: **second-hand belief.** A manager saying "my staff would love that" is someone's
> guess about a third party. Mark it weak, and do not treat it as retiring value risk.

## Notes by category

```dataview
TABLE category, date, reliability
FROM "PM vault/04-Research"
WHERE type = "research"
SORT date DESC
```

## Weak or unrated evidence

```dataview
TABLE category, reliability
FROM "PM vault/04-Research"
WHERE type = "research" AND (reliability = "weak" OR reliability = null)
```

## Intake checklist for every research note

- [ ] The question this note answers, stated first
- [ ] Method, sample and N — plus how the sample was recruited
- [ ] Verbatim quotes, not paraphrases
- [ ] Reliability rating from the ladder above, with method quality considered
- [ ] **What this does NOT tell us** — mandatory section
- [ ] Links to the `PROB` / `OPP` it supports or weakens

Template: `99-Playbook/Templates/RESEARCH-001-Imaging-Cost-Transparency.md`. Set `category:` in frontmatter so the tables work.
