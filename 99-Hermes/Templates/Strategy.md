---
type: strategy
artifact: strategy
status: draft
confidence: low
updated: 2026-11-08
review_cadence_days: 90
framework: Pichler
source: https://romanpichler.com/blog/my-product-strategy-model/
example: true
---

# Strategy — cost transparency in outpatient imaging

## Strategy elements

| Element | Current position | Evidence | Confidence |
|---|---|---|---|
| Target group | Adults on employer-sponsored HDHPs choosing outpatient imaging | [[RESEARCH-001-Imaging-Cost-Transparency\|RESEARCH-001]] | low |
| Needs | Know expected cost and understand inclusions/exclusions | [[RESEARCH-001-Imaging-Cost-Transparency\|RESEARCH-001]] | low |
| Business goals | Increase estimate coverage and reconciled accuracy | unknown | low |
| Stand-out features | Patient-readable estimate + reconciliation | hypothesis | low |

## Differentiation

| Alternative | What it does well | Where it fails our target group | Our answer |
|---|---|---|---|
| Payer estimator | Uses claims and benefit data | May be hard to interpret before booking | Explain inclusions and validity |
| Provider-portal estimator | Local price data | Limited to one provider | Start with one imaging type |
| Third-party price comparison | Broad comparison | Narrow accuracy and network context | Pair with reconciliation |
| Human-assisted estimate | Handles complexity | Does not scale | Use for discovery and edge cases |

## Deliberately not doing

- Provider matching in the first pilot
- Appointment scheduling
- Claims adjudication
- Multi-service bundles

## Priority thesis

> If we show a patient-readable estimate before booking, then more eligible patients will have the information they need to make a booking decision, because current estimates are hard to interpret and reconcile.

## What would invalidate this strategy

- Patients do not change any decision after seeing an estimate.
- Existing estimators are already sufficient.
- Estimate data cannot be reconciled.
- No buyer will pay for coverage.