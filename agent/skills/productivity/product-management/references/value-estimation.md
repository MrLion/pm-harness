# Value Estimation

Use when the user asks for time savings, ROI, throughput, or the harness's business value.

## Rules

- Never present an estimate as a measured benchmark. State assumptions, confidence, and the validation plan.
- Use the user's stated workweek. Default to 40 hours. A different workweek changes absolute hours, not the percentage range.
- Build a weighted roll-up: `activity share of the week × realistic reduction`, then apply an overlap/adoption haircut. Do not add independent per-task savings as if they stack.
- Keep one weighted roll-up table. Do not keep a separate per-task savings table beside it; the two drift and imply additive savings.
- Include non-benefits: interviews, stakeholder alignment, legal/compliance approval, build, and politics are largely unchanged.
- A senior PM already has context and writing speed. The tool's larger value is consistency, recall, traceability, and preventing unsupported work.
- Do not use the page as a sales claim. It is a set of hypotheses until the user's own baseline replaces it.

## 40-hour roll-up pattern

| Activity | Share | Time | Reduction used | Saved |
|---|---:|---:|---:|---:|
| Docs, status, reporting | 18% | 7.2 hrs | 40% | 2.9 hrs |
| Discovery synthesis | 18% | 7.2 hrs | 30% | 2.2 hrs |
| PRD, decision, review | 18% | 7.2 hrs | 25% | 1.8 hrs |
| Meetings and alignment | 31% | 12.4 hrs | 5% | 0.6 hrs |
| Delivery and operations | 16% | 6.4 hrs | 0% | 0 hrs |
| **Total** | | **40 hrs** | | **7.5 hrs — 18.7%** |

Apply a 20–25% overlap/adoption haircut for a central estimate near **5.6 hours — 14%**. Keep the range at **10–20% of total PM time** unless the user supplies a baseline.

## Validation

Baseline four weeks of:

- hours from opportunity decision to reviewable PRD
- minutes to prepare weekly status
- share of artifacts returned for missing evidence, metrics, or compliance
- days from accepted decision to release record

Replace the estimate with those measurements. Do not keep quoting the model after a real baseline exists.

## Team-count sensitivity

The percentage does not scale linearly with team count. More teams increase coordination time, which
the harness only partly reduces.

| Scenario | Central saving | Range | Main constraint |
|---|---:|---:|---|
| PM with 1–2 teams | **5.6 hrs — 14%** | 10–20% | Documentation is a larger share of the week |
| One PM across 5 teams | **5.0 hrs — 12.6%** | 10–15% | Coordination is about 40% of the week and barely reduced |
| Group PM over 5 PMs | **6.9 hrs — 17.2%** | 15–20% | Portfolio status and cross-team synthesis are larger |

One PM across five teams saves **less** than a PM with one or two teams: the tool compresses
documentation, recall, and traceability — not escalation, alignment, or dependency meetings. Do not
promise linear savings from team count.
