---
type: problem
project: pm-harness
artifact: problem
id: PROB-002
status: discovery
priority: high
confidence: low
frequency: unknown
severity: unknown
created: 2026-11-10
updated: 2026-11-10
framework: none
---

# Problem — most imaging patients do not know their out-of-pocket cost before booking

## Problem Statement

Adults scheduled for or completing outpatient advanced imaging often decide whether and where to book without knowing their likely out-of-pocket cost. In one U.S. academic imaging system, only 15.4% of 532 surveyed patients reported having that knowledge before their appointment. Whether the same gap exists among employer-sponsored HDHP members, and how often it changes a booking decision, is unknown.

## User / Segment

The live target group is unresolved: [Product](../00-Product/Product.md) is `confidence: none` and its TARGET GROUP is `[FILL]`.

The working segment for this discovery pass is the illustrative HDHP imaging case in [Scenario](../00-Product/Scenario.md). That scenario is illustrative, not product evidence.

## JTBD

No live JTBD note exists. Hypothesis: when facing a shoppable imaging appointment, I want to know my likely out-of-pocket cost before I commit, so I can decide whether and where to book without a financial surprise.

## Evidence

| Type | Source | Date | Says what | Strength |
|---|---|---|---|---|
| study | [Grant et al., JACR](https://www.jacr.org/article/S1546-1440(24)00831-7/fulltext) | 2024-10-15 | 15.4% (82/532) reported pre-imaging out-of-pocket cost knowledge before their appointment | medium for this system; low for the segment |
| study | [Grant et al., JACR](https://www.jacr.org/article/S1546-1440(24)00831-7/fulltext) | 2024-10-15 | Among those aware, 23.4% asked the insurer directly; 18.5% knew from benefit design; 17.3% received the cost from the imaging center without asking | medium |
| contradicting study | [Mitchell et al., PubMed record](https://pubmed.ncbi.nlm.nih.gov/39950202/) | 2025 | No evidence of an association between prospective out-of-pocket cost exposure and cancellation or no-show; 21.9% of canceled patients knew their cost versus 11.9% of completed patients | medium for this sample |
| synthesis | [RESEARCH-004](../04-Research/RESEARCH-004-Imaging-Cost-Transparency-Evidence-2024-2025.md) | 2026-11-10 | Combines the JACR findings with imaging price-variation evidence | medium |

> **Contradiction:** knowing the cost did not predict completing the exam. Cost knowledge may be a necessary condition for an informed choice without being sufficient to change behavior. Do not claim that an estimate alone reduces cancellations.

## Next evidence

Run 8–10 recent imaging decisions, including at least 4 non-bookers. For each, capture:

- what the patient knew about out-of-pocket cost before booking;
- where that information came from;
- whether they saw an estimate before or after choosing a site;
- what they did next: booked, switched site, delayed, or abandoned;
- the stated driver: uncertainty, affordability, network, urgency, or something else.

Do not ask for recall after the bill. Capture the decision at the point it happens.

## Journey

No live journey map exists. The illustrative path is [JOURNEY-001](../99-Playbook/Templates/JOURNEY-001-Imaging-Path.md), which is a template, not evidence.

## Frequency

Unknown. The JACR study reports a single academic system and does not report frequency for employer-sponsored HDHP members.

## Severity

Unknown. The study measures knowledge, not delayed care, surprise bills, site switching, or abandoned imaging.

## Current workaround

Patients call the insurer or imaging center, use a portal price tool, ask for a cash price, compare online, or delay the decision.

## Business impact

Evidence unavailable. Candidate effects to measure: delayed bookings, call-center volume, surprise-bill complaints, site leakage, and trust.

## Assumptions / Unknowns

- Employer-sponsored HDHP members behave like the JACR sample. This is unproven.
- The patient is the person deciding whether and where to book. The buyer is unresolved.
- Cost knowledge is actionable; the JACR result suggests it may not be sufficient.
- The patient can obtain an estimate before booking without exposing themselves to a misleading price.

## Related Opportunities

[Discovery Map](../03-Opportunities/Discovery%20Map.md) — no opportunity assessment exists yet.

## Buyer

Unresolved. Candidates: employer benefits lead, payer product lead, or provider finance/access lead.
