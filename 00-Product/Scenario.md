# Scenario

> Pre-filled templates: [[PM vault/99-Hermes/Templates/_Templates|Templates]]

## Main scenario

**Who:** Adults on employer-sponsored high-deductible health plans.
**Situation:** Choosing outpatient imaging.
**Decision moment:** Deciding whether to book, where to book, and whether the expected out-of-pocket cost is tolerable.
**Uncertainty:** They do not have a reliable out-of-pocket estimate before booking.

## Why the uncertainty matters

- Cost uncertainty can lead to:
  - postponed or skipped care,
  - surprise bills,
  - reduced trust in the provider,
  - switching to another provider.
- We should not assume estimation itself reduces postponement. It may.
  It can also simply reveal that the care is unaffordable at that moment.

## Evidence we can use

| Evidence | What it says | What it does not prove |
|---|---|---|
| William Blair *Consumer-Centric Healthcare 2026* | Patients receiving more estimates still report declining accuracy. | Not observed behavior change. |
| Experian Health *2025 State of Patient Access* | 43% of patients say they will likely postpone care without an accurate estimate. | Stated intent, not observed cancellation. |
| Robert Wood Johnson Foundation, reported by William Blair (Jan 2026) | Among patients carrying medical debt, 66.1% already had a bill in collections. | Not a measure of estimation effect. |

## Learning sequence

1. Investigate recent patient decisions on outpatient imaging.
2. Test estimate comprehension with a prototype.
3. Check what data the buyer, provider, and payer would allow us to use.
4. Test whether a usable estimate changes booking behavior.

## What we need to learn

1. How patients actually make the booking decision today.
2. What information they already have and where they look.
3. Whether an accurate estimate changes their decision.
4. What estimate scope and data access are needed to make an estimate usable.

## The estimate itself must be defined

An estimate is not usable unless we specify:

- which services and charges it includes,
- assumptions, exclusions, and validity period,
- how it is reconciled against final patient responsibility,
- acceptable error, especially underestimation,
- how changed services and unresolved bills are handled.

## Decision gate

Before committing to build, we need to know:

- who owns the estimate data,
- whether the patient, provider, or payer is the buyer,
- whether an existing estimator can be integrated instead of built.

## What this is not

- **Not product evidence.** This is an illustrative scenario.
- Not proof that one estimate will reduce postponed care.
- Not a substitute for data with the buyer, the provider, or the payer.

## Sources
- William Blair *Consumer-Centric Healthcare 2026*
- Experian Health *2025 State of Patient Access*
- Robert Wood Johnson Foundation, reported by William Blair, Jan 2026
