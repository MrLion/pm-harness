---
type: playbook
artifact: playbook
id: PLAYBOOK-002
status: active
updated: 2026-11-08
framework: "Torres + SVPG + Pichler"
---

# Outcome-Led 1→N

Use when the product already exists and the work is to improve an outcome, respond to customer
signal, or decide what to build next. The entry artifact is **signal**: feedback, research, a
metric, or a feature request that must be converted into a problem.

## Flow

| Stage | Question | Artifact |
|---|---|---|
| Signal | What did we observe, and from whom? | [[PM vault/99-Playbook/Templates/FB-001-Imaging-Cost-Feedback\|Feedback]] · [[PM vault/99-Playbook/Templates/RESEARCH-001-Imaging-Cost-Transparency\|Research]] |
| Problem | Who experiences what problem, when, and at what cost? | [[PM vault/99-Playbook/Templates/PROB-001-Imaging-Cost-Problem\|Problem]] |
| Opportunity | Is this worth pursuing, and what are the four risks? | [[PM vault/99-Playbook/Templates/OPP-001-Outpatient-Imaging-Cost\|Opportunity]] |
| Challenge | What would make this a no-go or defer? | [[PM vault/99-Playbook/Templates/OPP-001-Outpatient-Imaging-Cost#Hermes Challenge\|Opportunity challenge]] |
| Experiment | What is the cheapest test that retires the primary risk? | [[PM vault/99-Playbook/Templates/EXP-001-Comprehension-Test\|Experiment]] |
| Decision | Which option do we choose, and why? | [[PM vault/99-Playbook/Templates/DEC-001-Build-Partner-Defer\|Decision]] |
| PRD | What is the smallest coherent solution brief? | [[PM vault/99-Playbook/Templates/PRD-001-Imaging-Estimate\|PRD]] |
| Release | What shipped, and what moved? | [[PM vault/99-Playbook/Templates/REL-001-Imaging-Estimate-Pilot\|Release]] |
| Review | What did we learn, and what risk remains? | [[PM vault/99-Playbook/Templates/REVIEW-2027-02-Imaging-Estimate-Pilot\|Review]] |

The detailed first-run workflow is [[START-HERE]].

## Gates

| Gate | Pass condition |
|---|---|
| Problem quality | The problem contains no embedded solution and names who, when, and what it costs |
| Evidence | Claims link to research, feedback, or data — or are explicitly marked unknown |
| Opportunity | Four risks are assessed: value, usability, feasibility, viability |
| Challenge | A real no-go or defer option was considered |
| Experiment | One primary risk is retired, with success and kill criteria pre-registered |
| Decision | Options, tradeoffs, reversibility, expected outcome, and review date are recorded |
| PRD | The validation gate is met before a solution brief is written |
| Review | Goal vs outcome and risks retired are reported after release |

## What good looks like

- Feature requests are converted into problems before they enter delivery.
- The Discovery Map links canonical notes, not duplicate content.
- The roadmap shows outcomes and one goal per row.
- A shipped release has a measured result, surprises, and follow-up.
