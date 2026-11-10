# Market

Answers Cagan's Q3 (*how big is the opportunity?*) and Q6 (*why now?*). Sizing here exists to stop
bad bets, not to decorate a deck.

> **Cagan**
> "Assessing the size of the opportunity… remember to be conservative and realize that not every
> opportunity needs to be a billion-dollar market."

## What to capture

| Field | Note |
|---|---|
| Segment definition | Who is in, who is out — the same specificity Pichler requires of TARGET GROUP |
| TAM / SAM / SOM | Show the arithmetic. A single number with no derivation is unusable |
| Basis | Analyst report · trade association · bottom-up count · finance staff |
| Market window | What changed recently that makes *now* different (regulation, technology, cost) |
| Structural constraints | Procurement cycles, licensing, incumbents' lock-in |
| Source + date | Mandatory. Undated market numbers rot silently |

## Rules

- **Bottom-up beats top-down.** "18,000 UK clinics × £29/month" is checkable; "a £2bn market" is not.
- **Undated numbers are not evidence.** If the source has no date, mark `reliability: weak`.
- **State the falsifier.** What would have to be true for this market to be too small?

## Notes

```dataview
TABLE date, reliability, source
FROM ""
WHERE type = "research" AND contains(file.folder, "04-Research/Market") AND project = "pm-harness"
SORT date DESC
```
