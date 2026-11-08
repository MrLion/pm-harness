---
type: discovery-map
artifact: discovery-map
framework: Torres
outcome: TBD
updated: YYYY-MM-DD
source: https://www.producttalk.org/opportunity-solution-trees/
---

# Discovery Map — Opportunity Solution Tree

A **view of existing artifacts**, not another source of truth. Link `GOAL`, `PROB`, `OPP`, solution
briefs and `EXP` notes rather than copying their contents. Torres's "opportunity" maps to this
vault's problem plus its assessment; do not create a third opportunity category.

## Desired outcome

[[PM vault/00-Product/Goals|Goals]] — [FILL]

## Tree

- **[Problem]** [[PROB-000]]
  - **[Opportunity assessment]** [[OPP-000]]
    - **CAND-000** — [FILL] · [[OPP-000#Candidate solutions|OPP-000 · CAND-000]]
      - **Assumption test** [[EXP-000]]
    - **CAND-001** — [FILL] · [[OPP-000#Candidate solutions|OPP-000 · CAND-001]]
    - **CAND-002** — [FILL] · [[OPP-000#Candidate solutions|OPP-000 · CAND-002]]
      - **Solution brief after validation** [[PRD-000]]

## Coverage check

- [ ] Every branch starts from a desired outcome
- [ ] Every opportunity links evidence-backed problems
- [ ] More than one **stable `CAND-` row** was considered where uncertainty is high
- [ ] Each candidate branch names its riskiest assumption and cheapest test
- [ ] No candidate appears here without a matching `CAND-` row in its Opportunity
- [ ] A validated candidate links the solution brief that replaced it

---

> [!example]- Worked example — fictional
> **Desired outcome:** 60% of gaps filled without a manager call by 31 March.
> - **PROB-001:** managers lose 3–6 hours a week phoning staff to cover gaps.
> - **OPP-001:** automatically offer gaps to eligible staff.
>     - **CAND-001:** ranked auto-offer → EXP-001 fake-door offer pilot
>     - **CAND-002:** broadcast offer to all staff → rejected until value risk is tested
>     - **CAND-003:** manager-curated shortlist → concierge test if CAND-001 fails
> - **PROB-004:** managers do not trust eligibility decisions.
>   - **OPP-004:** show why each staff member is eligible.
>     - **CAND-004:** one-line eligibility explanation → EXP-004 prototype comprehension test
>
> The tree shows alternatives before commitment. It does not authorize any solution by itself.
