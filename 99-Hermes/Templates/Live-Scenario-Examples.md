---
type: examples
artifact: live-scenario-pack
updated: 2026-11-08
---

# Live scenario examples

These are **illustrative, source-backed scenarios**, not product evidence. Do not copy them into
real notes, and do not treat them as user evidence. The fictional product ("Lantern") remains
fictional; the public sources are real and cited.

## Problem → JTBD → persona

**Problem statement.** Rota administrators in extended access / community-clinic services lose
time hunting last-minute cover across spreadsheets and informal messaging. Policy requires a
compliant rota with daily and weekly rest periods that **cannot** be opted out of, yet informal
WhatsApp is explicitly disallowed for sickness reporting.

**JTBD.** When a clinician calls in sick just before a session, I want to identify qualified,
legally eligible staff and fill the shift safely without breaking rest rules or relying on
WhatsApp, so I can keep the service running without a manual phone tree.

**Persona sketch (sourced from public documents).** A rota administrator in an extended-access or
outpatient clinic service is typically the first point of contact for rota issues. They maintain
clinical and admin rotas, manage short-notice changes, and escalate compliance issues.

### Sources

- NHS job advert B0297-25-0006: [*Rota Administrator (Extended Access)*](https://beta.jobs.nhs.uk/candidate/jobadvert/B0297-25-0006)
- CPFT policy HR91: [*On-call and Planned and Unplanned hours*](https://www.cpft.nhs.uk/download/hr91-oncall-and-planned-and-unplanned-hours-policy.pdf?ver=21954)
- NHS Scotland sick leave guidance: [*WhatsApp should not be used to alert us of sickness*](https://www.med.scot.nhs.uk/trainee-doctors/specialties/acute-medicine/rie/admin-team/sick-leave)

## Opportunity → candidate solutions

**Why now.** Same-day clinical staffing is a recurring operational and compliance problem, not a
nice-to-have. Public rota roles now advertise **proactive gap management** and **daily compliance
checks** as ordinary duties, and policy requires cover for unplanned absence while preserving
non-optable rest rules.

**Candidate solutions (illustrative).**

| ID | Alternative | How it addresses the problem | Cheapest test |
|---|---|---|---|
| CAND-001 | Ranked auto-offer to eligible staff | Removes the phone tree and ranks by actual eligibility | Manual 2-week pilot on one small team |
| CAND-002 | Broadcast offer to all staff | Fast but low trust and high noise | Fake-door offer only |
| CAND-003 | Concierge service / rota assistant | Validate the job, not the automation | 5 interviews + manual service trial |

**Four risks (illustrative).**

| Risk | Rating | Load-bearing assumption | Test |
|---|---|---|---|
| Value | high | staff would accept an offer without a manager call | manual offer pilot |
| Usability | medium | a two-tap accept flow works mid-shift | prototype test |
| Feasibility | low | eligibility ranking can be built from existing rota data | engineering spike |
| Business viability | medium | a small clinic will pay for this without a sales team | pricing conversations |

### Sources

- CPFT policy HR91: mandatory cover for unplanned absence, daily/weekly rest, non-optable rest periods
- NHS job advert B0297-25-0006: "safe, compliant rotas", "proactively managing gaps", "escalate compliance issues"
- Skills for Care 2024/25 workforce data: [*Latest social care sector and workforce data*](https://skillsforcare.org.uk/news-and-events/news/latest-social-care-sector-and-workforce-data-published)

## Experiment → decision

**Cheapest test.** Do not build the automation first. Run a manual, two-week pilot with one small
team: when a gap appears, send a ranked offer manually from an existing contact list, and record
whether the first eligible respondent accepts. The success criterion is whether ranked offers beat
the informal phone tree within the same staff pool.

**Decision framing.** If ranked manual offers do not materially change the time-to-fill or
compliance burden, then the automation is a convenience, not a validated solution. It should be
parked or re-framed.

### Sources

- CPFT policy HR91: compliance/rest-period constraints cannot be traded away
- NHS job advert B0297-25-0006: "proactively managing gaps", "complete daily compliance checks"

## PRD / roadmap framing

**Solution brief (illustrative).** Use a ranked-offer flow with a built-in rest-rule guardrail.
The guardrail must be present in the first release, not later. A future release can reduce the
manual compliance effort, but not defer a legal constraint.

### Sources

- CPFT policy HR91: daily and weekly rest cannot be opted out
- NHS job advert B0297-25-0006: daily compliance checks

## Market context

Skills for Care reported **111,000 vacant posts** and a **7% vacancy rate** in adult social care in
2024/25, a 12.4% decrease on the previous year. This is *adjacent workforce context*, not target
market data for Lantern. Use it to show where the commercial risk sits: staffing and service
continuity pressures are real, but pricing and purchasing power remain untested.

### Source

- [*Latest social care sector and workforce data published*](https://skillsforcare.org.uk/news-and-events/news/latest-social-care-sector-and-workforce-data-published)

---

This document is deliberately **not** a substitute for a real user interview, real pricing data,
or a real product decision. It exists to show how to use the templates without inventing evidence.