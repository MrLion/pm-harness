---
type: opportunity
artifact: opportunity-assessment
id: OPP-001
status: discovery
confidence: low
impact: unknown
effort: unknown
strategic_fit: unknown
score: null
recommendation: Pending
risk_type: value
risk_owner: PM
created: 2026-11-08
updated: 2026-11-09
review_after: 2026-12-08
framework: SVPG
source: https://www.svpg.com/assessing-product-opportunities/
example: true
case_id: CASE-001
---

# Opportunity — reduce uncertainty before outpatient imaging

## The ten questions

**1. Exactly what problem will this solve?**
Patients cannot reliably predict their final patient responsibility before booking outpatient imaging.

**2. For whom do we solve that problem?**
Adults on employer-sponsored HDHPs choosing outpatient imaging. Buyer unresolved; see [PERSONA-002](PERSONA-002-Buyer-Payer.md).

**3. How big is the opportunity?**
Unknown. Establish eligible imaging requests and estimate coverage before sizing.

**4. What alternatives are out there?**
Payer estimators, provider-portal estimators, third-party price comparison, cash-price requests, and calling the provider or insurer.

**5. Why are we best suited to pursue this?**
Unknown. The differentiator is a hypothesis: a patient-readable estimate with inclusions, exclusions, and validity explained.

**6. Why now?**
Cost transparency is receiving regulatory and market attention; estimate receipt is rising while perceived accuracy is falling.

**7. How will we get this to market?**
Unknown. Buyer and data owner are unresolved: patient, provider, or payer.

**8. How will we measure success / make money?**
Coverage: share of eligible imaging requests that receive a pre-booking estimate. Accuracy: share of reconciled estimates within $400. Business model unknown.

**9. What factors are critical to success?**
Access to usable estimate data; reconciliation against final patient responsibility; patient comprehension; buyer willingness to pay.

**10. Given the above, what's the recommendation?**
Proceed to discovery, not build. Test comprehension and data access first.

## The four big risks

| Risk | Rating | Load-bearing assumption | How we'll test it | Owner | Status |
|---|---|---|---|---|---|
| Value | unknown | Patients will use an estimate before booking | Interviews on recent decisions; later behavioural pilot | PM | untested |
| Usability | unknown | Patients can understand inclusions, exclusions, and validity | Paper-prototype comprehension test | Design | untested |
| Feasibility | unknown | Estimate data is accurate and accessible | Data-owner and reconciliation review | Eng | untested |
| Business viability | unknown | A buyer will pay for estimate coverage | Buyer and payer interviews | PM | untested |

## Compliance feasibility

| Question | Answer |
|---|---|
| Data classification | Synthetic prototype — no PHI. A pilot uses the live [COMP-003](../../11-Compliance/COMP-003-Compliance-Scope.md); [COMP-001](Compliance/COMP-001-Compliance-Scope.md) is the structure template. |
| PHI / ePHI | None in the synthetic prototype; reassess before any pilot with real patient data |
| Vendor / BAA | Not applicable until a vendor is selected; then [VEND-001](Compliance/VEND-001-Vendor-BAA-Register.md) |
| Risk and controls | [RISK-001](Compliance/RISK-001-Privacy-Security-Risk.md) · [CTRL-001](Compliance/CTRL-001-Control-Matrix.md) |
| Approval needed | Live compliance scope approved and a named owner before pilot |

## Journey

[JOURNEY-001](JOURNEY-001-Imaging-Path.md) — the booking-to-payment path this opportunity changes.

## Hypothesis

> We believe a patient-readable pre-booking estimate will cause more patients to make an informed booking decision, because cost uncertainty is currently unresolved.

## Evidence

### Supporting

| Source | Date | Says what | Strength |
|---|---|---|---|
| [RESEARCH-002](../../04-Research/RESEARCH-002-William-Blair-Consumer-Healthcare-2026.md) | 2026-11-08 | 41% receive estimates; 71% accurate to $400; 43% would likely postpone without an accurate estimate | weak |

### Contradicting

- Patients may want the estimate but still choose on referral, convenience, or urgency.
- Existing payer or provider estimators may already be good enough.

## Candidate solutions

| ID | Status | Candidate | How it addresses the problem | Cheapest test | Next step |
|---|---|---|---|---|---|
| CAND-001 | candidate | Integrate an existing payer/provider estimator | Uses existing data and reconciliation | Data-access review | test |
| CAND-002 | candidate | Assisted estimate request with human review | Handles complex cases without a full build | Concierge test | test |
| CAND-003 | candidate | Narrow self-service estimate for one imaging type | Limits scope and data complexity | Paper prototype + comprehension test | test |

## Adversarial challenge

- What if we are wrong? The load-bearing assumption is that patients act on cost information.
- What evidence contradicts this? Patients may choose on referral, urgency, or convenience.
- Which claims are unsupported? That an accurate estimate reduces postponement.
- Are we solving the right problem, or a symptom? The problem is uncertainty, not necessarily price level.
- What would invalidate the opportunity outright? Patients do not change any decision, or an existing estimator is sufficient.
- What is the cheapest way to find out? 8–10 recent booking journeys, including non-bookers, then a comprehension prototype.

## Smallest experiment

8–10 recent booking journeys, including at least 4 non-bookers, then a paper-prototype comprehension test. Record the information available at the decision point, the action, and the driver. Rehearsal example: [RESEARCH-003](RESEARCH-003-Mock-Booking-Journeys.md), synthetic and not evidence.

## Recommendation

Pending — discovery only; no build until comprehension and data access are proven. [DEC-001](DEC-001-Build-Partner-Defer.md) proposes defer; the recommendation stays Pending until that decision is accepted.

## Related

- [PROB-001](PROB-001-Imaging-Cost-Problem.md) · [DEC-001](DEC-001-Build-Partner-Defer.md) · [EXP-001](EXP-001-Comprehension-Test.md) · [Discovery Map](../../03-Opportunities/Discovery%20Map.md)