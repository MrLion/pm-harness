---
type: template
artifact: opportunity-assessment
framework: SVPG
source: https://www.svpg.com/assessing-product-opportunities/ + https://www.svpg.com/four-big-risks/
---

# Opportunity (SVPG Product Opportunity Assessment)

Ten questions, then the four risks. **The purpose is to kill weak opportunities cheaply**, not to
justify ones you already want to build.

> [!quote] Cagan, on the hardest question
> "Ask most product managers what problem their product is intended to solve, and you usually get
> a rambling list of features and capabilities, rather than a crisp, clear and compelling statement
> of exactly the problem that's solved."

## The ten questions

**1. Exactly what problem will this solve? (value proposition)**
[FILL]

**2. For whom do we solve that problem? (target market)**
[FILL]

**3. How big is the opportunity? (market size)**
[FILL] — be conservative; not every opportunity needs to be a billion-dollar market.

**4. What alternatives are out there? (competitive landscape)**
[FILL]

**5. Why are we best suited to pursue this? (our differentiator)**
[FILL]

**6. Why now? (market window)**
[FILL]

**7. How will we get this to market? (go-to-market strategy)**
[FILL]

**8. How will we measure success / make money? (metrics / revenue)**
[FILL]

**9. What factors are critical to success? (solution requirements)**
[FILL]

**10. Given the above, what's the recommendation? (go / no-go)**
[FILL — **no-go is a valid and frequent answer**]

---

## The four big risks

> [!quote] Cagan's four risks
> **Value** — will customers buy it or users choose to use it?
> **Usability** — can users figure out how to use it?
> **Feasibility** — can our engineers build it with the time, skills and technology we have?
> **Business viability** — does it work for go-to-market, contracts, legal, acquisition cost,
> monetisation and brand promise?

| Risk | Rating | Load-bearing assumption | How we'll test it | Owner | Status |
|---|---|---|---|---|---|
| Value | unknown | | | PM | untested |
| Usability | unknown | | | Design | untested |
| Feasibility | unknown | | | Eng | untested |
| Business viability | unknown | | | PM | untested |

> The PM owns value and viability and is accountable for the **outcome**. Design owns usability.
> Engineering owns feasibility. A risk with no owner is a risk nobody is retiring.

## Hypothesis
> We believe **<change>** will cause **<measurable outcome>** because **<reason/evidence>**.

## Evidence
### Supporting
| Source | Date | Says what | Strength |
|---|---|---|---|
| | | | weak |

### Contradicting
- <Empty means you have not looked.>

## Smallest experiment
<The cheapest test that retires the highest-rated risk. If you cannot name one, this is not ready.>

## Recommendation
Pending

## Related
- [[PROB-000]] · [[DEC-000]] · [[EXP-000]]

---

> [!example]- Worked example — fictional
> **1. Problem:** managers cannot fill a gap without a serial phone tree, so gaps stay open for hours.
> **2. For whom:** practice managers, 5–20-staff outpatient clinics, 1–3 sites.
> **3. Size:** ~18,000 such UK clinics; 41% still on spreadsheets. Conservative SAM: 7,000.
> **4. Alternatives:** Deputy (full suite), Planday, spreadsheets, WhatsApp.
> **5. Differentiator:** two-field setup plus an eligibility guardrail; rivals need weeks of onboarding.
> **6. Why now:** 2024 rest-period rules turned manual assignment into an audit risk.
> **7. GTM:** clinic-manager communities and accountant referrals; no sales team.
> **8. Success:** median time-to-fill under 15 min; churn under 4%.
> **9. Critical factors:** eligibility ranking must be explainable; managers must trust the guardrail.
> **10. Recommendation:** **go**, gated on retiring value risk first.
>
> | Risk | Rating | Assumption | Test | Owner |
> |---|---|---|---|---|
> | Value | high | staff accept an offer without a call | fake-door offer, 2 clinics, 2 weeks | PM |
> | Usability | medium | two-tap accept works mid-shift | prototype with 4 staff | Design |
> | Feasibility | low | ranking needs only existing rota data | 2-day eng spike | Eng |
> | Viability | medium | £29/month accepted without a sales call | 8 pricing conversations | PM |
