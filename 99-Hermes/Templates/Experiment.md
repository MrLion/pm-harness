---
type: experiment
artifact: experiment
id: EXP-000
status: planned
risk_type: value
risk_owner: PM
opportunity: "[[OPP-000]]"
start: YYYY-MM-DD
end: YYYY-MM-DD
cost: unknown
created: YYYY-MM-DD
framework: SVPG
source: https://www.svpg.com/four-big-risks/
updated: YYYY-MM-DD
---

# Experiment

An experiment exists to retire **one primary named risk**. If you cannot name which of the four
risks it targets (value, usability, feasibility or viability), it is not an experiment — it is a
build. Secondary observations may be recorded, but they do not redefine the experiment.

> [!quote] Why experiments before builds
> Product discovery retires value and business risk early, while the cost of being wrong is
> still a prototype rather than a shipped feature.

## Risk being retired

| Field | Content |
|---|---|
| Risk type | value / usability / feasibility / business viability |
| Assumption | [FILL] |
| Opportunity | [[OPP-000]] |

## Hypothesis

> We believe **[FILL: change]** will cause **[FILL: measured effect]** for **[FILL: population]**, measured by **[FILL: metric]**.

## Design

[FILL: Fake door / concierge / prototype test / A/B / 5 interviews. State the cheapest version that works.]

| Field | Content |
|---|---|
| Population | |
| Duration | [FILL: and why that is long enough to see signal] |
| Cost | |

## Pre-registered criteria

| Success | Failure | Kill |
|---|---|---|
| [FILL: decide now, before data] | | |

## Result

Pending

## Secondary observations

- [FILL: observations outside the primary risk; not decision evidence unless pre-registered]

## What we learned

Pending

## Decision

Pending — link the resulting [[DEC-000]] or updated [[OPP-000]].

---

> [!example]- Worked example — fictional
> **Risk:** value — will staff accept a shift offer without being phoned?
> **Hypothesis:** an offer sent to eligible staff will be accepted within 10 minutes in ≥50% of
> gaps, for 2 pilot clinics over 2 weeks, measured by offer-acceptance rate.
> **Design:** fake-door offer in the existing WhatsApp flow, one staff group, no app build.
> **Success:** ≥50% acceptance in 10 min. **Failure:** <20%. **Kill:** <10% after week 1.
> **Cost:** 2 days of build, no new infrastructure.
