# Competitors

Feeds Cagan's Q4 (*what alternatives are out there?*) and Pichler's differentiation. The output is
not a feature grid — it is **where each alternative fails our target group**.

> Alternatives include "a spreadsheet and a WhatsApp group". Doing nothing is always a competitor.

## Teardown fields

| Field | Note |
|---|---|
| Alternative | Product, or the workaround it replaces |
| What it does well | Be fair. Dismissive teardowns produce useless strategy |
| Where it fails our target group | Specific and behavioural, not "hard to use" |
| Pricing model | And what a 12-person team actually pays |
| Onboarding cost | Time-to-first-value — often the real differentiator |
| Evidence | Screenshot, pricing page, trial notes — with a **date** |

## Rules

- **No claims from memory.** A competitor's pricing changes quarterly; an undated claim is a guess.
- **Don't quote marketing as capability.** A positioning page is evidence of positioning, nothing more.
- **Record the workaround.** If clinics use a personal WhatsApp list, that is the incumbent to beat.

## Notes

```dataview
TABLE date, reliability, source
FROM "PM vault/04-Research/Competitors"
WHERE type = "research"
SORT date DESC
```
