---
type: research
artifact: research
id: RESEARCH-003
category: user
status: synthetic
confidence: none
synthetic: true
reliability: none
updated: 2026-11-09
framework: none
example: true
case_id: CASE-001
---

# Mock interview results — outpatient imaging cost estimates

> [!WARNING] Synthetic example
> All eight journeys and findings below are invented. Use them to rehearse analysis and decision-making. Keep the live research and decision outcomes marked pending until actual interviews are completed.

## Research question

What did adults on employer-sponsored high-deductible plans know about their out-of-pocket cost when they decided whether and where to book elective outpatient imaging?

## Journeys

| Journey | Estimate seen before decision? | Information at the decision point | Action | Main driver | Role of the estimate |
|---|---|---|---|---|---|
| J-01 | Yes | Two in-network sites gave estimates for the same scan. Both had acceptable appointment times. | Booked the lower-estimate site. | Expected cost | Patient reported that the estimate changed **where** they booked. |
| J-02 | Yes | Provider gave a range and explained which charges it covered. | Booked the originally referred site. | Referral and timing | Helped the patient budget. No reported change in provider or timing. |
| J-03 | No | The scheduler could offer an appointment but couldn’t give a cost estimate during the call. | Booked the first available slot. | Timing | No estimate was available when the patient decided. |
| J-04 | Yes | The portal showed a low estimate, but the patient couldn’t tell whether it included the radiologist’s fee. | Booked the referred site. | Trust in the referral | Saw the estimate but didn’t rely on it because its scope was unclear. |
| J-05 | No | Provider referred the patient to the insurer. The insurer requested details the patient didn’t have. | Deferred without booking. | Cost uncertainty | The handoff prevented the patient from getting an estimate. What they would have done with one is unknown. |
| J-06 | Yes | The patient understood the estimated amount and said it exceeded what they could pay. | Deferred without booking. | Affordability | The estimate informed the decision by revealing the cost. The patient reported no confusion about it. |
| J-07 | No | A portal estimate became available after the patient had already decided to wait. | Remained unbooked. | Cost uncertainty at the decision point | Arrived too late to inform the original decision. |
| J-08 | No | The patient couldn’t confirm whether the site was in-network. | Did not book while seeking confirmation. | Network uncertainty | The immediate barrier was network status. The effect of an estimate is unknown. |

## Mock synthesis

- Four of eight patients saw an estimate before deciding. One reported changing **where** they booked. Another used it to budget without changing the booking. A third deferred because the expected cost exceeded their budget. The fourth saw a number but didn’t trust its scope.
- Four patients remained unbooked. Two lacked timely cost information, one understood the estimate but couldn’t afford it, and one lacked network confirmation.
- The interviews would give the team distinct problems to investigate: getting an estimate in time, understanding what it covers, and affording the amount. Each points to a different next step.
- This small, deliberately mixed sample would help identify failure modes. It would give little basis for estimating how common they are or whether an estimator reduces postponement.

## Mock decision update

| Finding | Evidence | Decision effect |
|---|---|---|
| Two unbooked journeys involved missing or late estimates. The other two had different barriers. | J-05–J-08 | **Continue discovery.** Narrow the next test to whether one clinic can deliver a scoped estimate before patients decide whether to book one imaging type. |
| Patients can use an estimate for provider choice or budgeting, but unclear inclusions can make it unusable. | J-01, J-02, J-04 | Keep the comprehension test. Ask participants to identify the amount, explain what it covers, and name a charge that could still be missing. |
| The journeys provide no evidence that the team can access and reconcile the necessary data or that a buyer will fund the service. | No buyer or data-owner interviews in this mock sample | Keep the build deferred. Investigate an existing estimator and a human-assisted workflow before committing to self-service. |

## Next decision

Can an existing tool or a human-assisted process deliver a scoped estimate before booking for one imaging type? If it can, compare that path with building. If it can’t, identify the missing input and who controls it before committing to a pilot.

## What this does not prove

- That the eight journeys represent the segment.
- That an estimate changes booking behaviour.
- That a buyer will fund the service.
- That the data can be accessed and reconciled.

## Related

- [PROB-001](PROB-001-Imaging-Cost-Problem.md)
- [OPP-001](OPP-001-Outpatient-Imaging-Cost.md)
- [DEC-001](DEC-001-Build-Partner-Defer.md)
- [EXP-001](EXP-001-Comprehension-Test.md)
