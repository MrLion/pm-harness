---
type: discovery-map
artifact: discovery-map
framework: Torres
outcome: Reduce out-of-pocket cost uncertainty before outpatient imaging
updated: 2026-11-08
source: https://www.producttalk.org/opportunity-solution-trees/
example: true
---

# Discovery Map — imaging cost uncertainty

## Desired outcome

[[PM vault/00-Product/Goals|Goals]] — reduce out-of-pocket cost uncertainty before elective outpatient imaging.

## Tree

- **[Problem]** [[99-Hermes/Templates/Problem|PROB-001]]
  - **[Opportunity assessment]** [[99-Hermes/Templates/Opportunity|OPP-001]]
    - **CAND-001** — integrate an existing payer/provider estimator · [[99-Hermes/Templates/Opportunity#Candidate solutions|OPP-001 · CAND-001]]
    - **CAND-002** — assisted estimate request with human review · [[99-Hermes/Templates/Opportunity#Candidate solutions|OPP-001 · CAND-002]]
    - **CAND-003** — narrowly scoped self-service estimate · [[99-Hermes/Templates/Opportunity#Candidate solutions|OPP-001 · CAND-003]]
      - **Assumption test** [[99-Hermes/Templates/Experiment|EXP-001]]

## Coverage check

- [x] Every branch starts from a desired outcome
- [x] Every opportunity links evidence-backed problems
- [x] More than one stable `CAND-` row considered
- [x] Each candidate branch names its riskiest assumption and cheapest test
- [x] No candidate appears without a matching `CAND-` row in the Opportunity
- [ ] A validated candidate links a solution brief — not yet validated
