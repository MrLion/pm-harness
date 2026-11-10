---
type: journey-map
project: pm-harness
artifact: journey-map
id: JOURNEY-001
status: draft
confidence: low
updated: 2026-11-09
framework: "Journey mapping"
example: true
case_id: CASE-001
---

# Journey — outpatient imaging cost path

> [!NOTE] Synthesis view, not evidence
> This map organizes the case. Each pain point must name its source or `Evidence unavailable.` It does not replace the Problem or Opportunity notes.

## Scope

| Field | Content |
|---|---|
| Person | Adult on an employer-sponsored HDHP |
| Job | Choose and complete elective outpatient imaging without an unmanageable cost surprise |
| Start | Symptom, referral, or clinician order |
| End | Final patient responsibility paid or resolved |
| Out of scope | Clinical diagnosis, emergency imaging, post-acute care |

## Stages

| Stage | Actor | Action | Touchpoint | Pain or uncertainty | Evidence | Links |
|---|---|---|---|---|---|---|
| 1. Trigger | Patient / clinician | Receives a referral or order for imaging | Clinic visit, portal, phone | Does not know whether imaging is covered or what it will cost | Hypothesis from scenario; no direct observation | [PROB-001](PROB-001-Imaging-Cost-Problem.md) |
| 2. Provider search | Patient | Looks for an in-network imaging provider | Payer directory, provider site, referral | Network status and location are easier to compare than cost | Hypothesis | [PROB-001](PROB-001-Imaging-Cost-Problem.md) |
| 3. Scheduling | Patient / scheduler | Books a date and location | Phone, portal, front desk | Cost is often unavailable at the moment of booking | Hypothesis | [PROB-001](PROB-001-Imaging-Cost-Problem.md) |
| 4. Pre-service estimate | Patient / provider staff / payer tool | Requests or receives an estimate | Portal, phone, paper, app | Inclusions, exclusions, validity, and final responsibility are unclear | Secondary survey only; see [RESEARCH-002](../../04-Research/RESEARCH-002-William-Blair-Consumer-Healthcare-2026.md) | [OPP-001](OPP-001-Outpatient-Imaging-Cost.md) |
| 5. Check-in | Patient / front desk | Confirms identity, coverage, and payment responsibility | Front desk, kiosk, phone | Estimate may not match the service actually performed | Hypothesis | [OPP-001](OPP-001-Outpatient-Imaging-Cost.md) |
| 6. Imaging | Patient / technologist | Receives the service | Imaging center | Order changes can change the price | Hypothesis | [OPP-001](OPP-001-Outpatient-Imaging-Cost.md) |
| 7. Claim and EOB | Payer / patient | Claim is adjudicated; patient receives an explanation of benefits | Payer portal, mail | Final responsibility differs from the estimate | Source needed | [OPP-001](OPP-001-Outpatient-Imaging-Cost.md) |
| 8. Payment | Patient / billing office | Pays or resolves the balance | Bill, portal, collections | Surprise balance damages trust | Hypothesis; medical-debt context only | [PROB-001](PROB-001-Imaging-Cost-Problem.md) |

## Moments of truth

| Moment | What must be true | Why it matters |
|---|---|---|
| Before booking | The patient can see a range and the assumptions behind it | The decision is made here |
| At check-in | Coverage and order are still valid | The estimate can go stale |
| After the claim | Estimate and final responsibility reconcile | Trust depends on the gap |

## Frontstage and backstage

| Layer | Actors | What they need |
|---|---|---|
| Frontstage | Patient, scheduler, front desk | A readable estimate and a clear next step |
| Backstage | Provider finance, payer, billing, data vendor | Access to eligibility, benefit, and allowed-amount data |
| Systems | Scheduling, eligibility, price transparency files, claims, billing | A shared way to reconcile the estimate |

## What this map does not prove

- That patients will change a booking decision after seeing an estimate.
- That an estimate can be produced accurately for every plan and procedure.
- That the buyer will fund the experience.
- That the estimate reduces total cost or postponed care.

## Related

- [PROB-001](PROB-001-Imaging-Cost-Problem.md)
- [OPP-001](OPP-001-Outpatient-Imaging-Cost.md)
- [PERSONA-001](PERSONA-001-HDHP-Imaging-Patient.md)
- [PERSONA-002](PERSONA-002-Buyer-Payer.md)
- [Discovery Map](Discovery-Map.md)
