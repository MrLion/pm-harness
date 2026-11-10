# Worked vertical slice

> [!WARNING] Synthetic fixture
> This is one complete artifact chain built from the synthetic imaging case. It exercises the
> harness, not the market. It is not live evidence and must not be cited as research.

## Chain

| Stage | Artifact |
|---|---|
| Product spine | [Product](00-Product/PRODUCT-001-Transparent-Imaging.md) |
| Problem | [PROB-001](02-Problems/PROB-001-Imaging-Cost-Problem.md) |
| Opportunity | [OPP-001](03-Opportunities/OPP-001-Outpatient-Imaging-Cost.md) |
| Decision | [DEC-001](05-Decisions/DEC-001-Build-Partner-Defer.md) |
| PRD | [PRD-001](07-Delivery/PRDs/PRD-001-Imaging-Estimate.md) |
| Experiment | [EXP-001](07-Delivery/Experiments/EXP-001-Comprehension-Test.md) |
| Release | [REL-001](07-Delivery/Releases/REL-001-Imaging-Estimate-Pilot.md) |
| Review | [REVIEW-2027-02](08-Reviews/REVIEW-2027-02-Imaging-Estimate-Pilot.md) |

## What this proves

- The IDs link from problem to review.
- The decision gates the PRD and release.
- The release is conditional and the review is simulated.
- The validator can check the chain without a live product.

Run:

```bash
python3 scripts/validate_vault.py examples/vertical-slice
```

## What this does not prove

- That the problem is real in this segment.
- That the buyer or data access exists.
- That the estimate changes behaviour.
- That any live gate has passed.
