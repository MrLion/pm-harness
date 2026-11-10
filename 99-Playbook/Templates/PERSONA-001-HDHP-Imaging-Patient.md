---
type: persona
project: pm-harness
artifact: persona
id: PERSONA-001
status: draft
confidence: low
evidence_count: 0
created: 2026-11-08
updated: 2026-11-09
framework: Pichler
source: https://www.romanpichler.com/the-persona-template/
example: true
case_id: CASE-001
---

# Persona — cost-conscious HDHP adult choosing imaging

> Evidence rule: `evidence_count: 0` means this is a modelled persona, not a real person.

## Profile

| Field | Content |
|---|---|
| Name (representative, not a real person) | Maya |
| Role | Adult on an employer-sponsored high-deductible health plan |
| Context | Needs outpatient imaging; comparing providers and expected out-of-pocket cost before booking |
| Goals | Avoid surprise bills; know what the visit will cost; choose a provider without delaying care |
| Pains | Opaque estimates; repeated calls; unclear inclusions and exclusions |
| Observed behaviour (not stated behaviour) | Unknown — no direct observation or interview data yet |

## Segment variables

| Variable | This case | Why it matters |
|---|---|---|
| Deductible status | Not met — hypothesis | Full-price exposure makes the estimate decision live |
| Urgency | Elective | There is time to compare providers and delay |
| Network | In-network preferred | Out-of-network changes both price and data |
| Procedure count | Single procedure at start | Keeps the first estimate scoped |
| Estimate received | Unknown | The problem is reliability, not universal absence |

## Evidence base

| Type | Source | Date | Count |
|---|---|---|---|
| secondary survey | [RESEARCH-002](../../04-Research/RESEARCH-002-William-Blair-Consumer-Healthcare-2026.md) | 2026-11-08 | 0 direct observations |

## Related

- [PROB-001](PROB-001-Imaging-Cost-Problem.md)
- [JTBD-001](JTBD-001-Know-Cost-Before-Booking.md)
- [JOURNEY-001](JOURNEY-001-Imaging-Path.md)