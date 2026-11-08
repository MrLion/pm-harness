---
type: opportunity
artifact: opportunity-assessment
id: OPP-003
status: closed
confidence: low
impact: unknown
effort: unknown
strategic_fit: unknown
score: null
recommendation: no-go
risk_type: viability
risk_owner: PM
created: 2026-11-08
updated: 2026-11-08
review_after: null
framework: SVPG
source: https://www.svpg.com/assessing-product-opportunities/
example: true
---

# Opportunity — resolve prior-authorization friction

## The ten questions

**1. Exactly what problem will this solve?**
Authorization rules create uncertainty and administrative overhead before treatment decisions.

**2. For whom do we solve that problem?**
Patients and provider staff dealing with prior authorization for elective care.

**3. How big is the opportunity?**
Unknown. The workflow is payer- and provider-specific.

**4. What alternatives are out there?**
Payer portals, provider authorization teams, third-party authorization services, and manual phone follow-up.

**5. Why are we best suited to pursue this?**
We are not. The current product has no payer workflow ownership or authorization data access.

**6. Why now?**
Not now. This is outside the estimate-first scope and would require a different buyer and data model.

**7. How will we get this to market?**
Unknown. It would require payer or provider workflow integration.

**8. How will we measure success / make money?**
Unknown. The buyer and reimbursement model are unresolved.

**9. What factors are critical to success?**
Payer connectivity, authorization rule coverage, provider adoption, and a separate business model.

**10. Given the above, what's the recommendation?**
No-go for this product horizon. Record the reason and revisit only if the product moves into payer or provider workflow tooling.

## Four big risks

| Risk | Rating | Load-bearing assumption | How we'll test it | Owner | Status |
|---|---|---|---|---|---|
| Value | unknown | Patients or providers would use a separate authorization tool | Buyer interviews | PM | not tested |
| Usability | unknown | The workflow can be simplified without payer integration | Workflow review | Design | not tested |
| Feasibility | high | Payer rules and status are accessible | Data-access review | Eng | failed — no access |
| Business viability | high | A buyer exists outside payer/provider systems | Market review | PM | failed — no buyer in scope |

## Recommendation

No-go for the current product horizon. The data-access and buyer assumptions fail before an experiment is justified.

## Related

- [[PM vault/00-Product/Future-Problem-Statements|Future problem statements]]
- [[OPP-001-Outpatient-Imaging-Cost|OPP-001]]
