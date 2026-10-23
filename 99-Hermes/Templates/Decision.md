---
type: template
artifact: decision
framework: none
note: decision records are not part of either framework; this structure is kept because it works
---

# Decision

## Question
<One sentence. If it contains "and", split it into two decisions.>

## Context
<What is true now that forces this.>

## Options
### A — <name>
### B — <name>
### C — do nothing / defer

## Tradeoffs
| Dimension | A | B | C |
|---|---|---|---|
| User impact | | | |
| Business impact | | | |
| Effort | | | |
| Risk | | | |
| Strategic fit | | | |
| Reversibility | | | |

## Decision
<Chosen option.>

## Rationale
<Why — including what we are knowingly giving up.>

## Assumptions
- <If wrong, revisit.>

## Reversibility
High / Medium / Low, and the actual cost of reversal.

## Expected outcome
<Measurable. "X moves from A to B by DATE.">

## Review date
YYYY-MM-DD

## Actual outcome
Pending

---

> [!example]- Worked example — fictional
> **Question:** do we ship gap-filling first, or the full rota builder?
> **Context:** pilots ask for gap-filling; the rota builder is 3× the build.
> **Options:** A gap-filling only · B full rota builder · C do nothing, keep the spreadsheet.
> **Decision:** A. **Rationale:** retires value risk for the whole thesis in 4 weeks instead of 14;
> knowingly gives up switching cost — clinics still keep the spreadsheet for planning.
> **Reversibility:** high — the rota builder can follow without re-architecting.
> **Expected:** gaps filled without a manager call 22% → 60% by 31 Mar. **Review:** 2026-03-31.
