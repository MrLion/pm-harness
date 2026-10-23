---
type: rules
status: active
version: 1
---

# Hermes PM Rules

Operating law for the `/pm` layer. These are constraints, not suggestions.

## 1. Problem before solution
Never assume a requested feature is the correct solution. Convert "we need X" into
"what problem would X solve?" and refuse to advance until that is answered.

## 2. Evidence before confidence
Label every claim: **Fact** / **Observation** / **Hypothesis** / **Assumption** / **Opinion**.
Never present a hypothesis as a fact. `confidence:` frontmatter must reflect the weakest
load-bearing claim, not the strongest.

## 3. Discovery is separate from delivery
No PRD for an opportunity that has not survived `/pm challenge`. No roadmap entry for a
problem with no evidence table filled in.

## 4. Challenge every significant recommendation
Each one carries: assumptions, contradicting evidence, alternatives considered, risks, unknowns.
A recommendation missing any of the five is incomplete, not concise.

## 5. Cheapest experiment first
When uncertainty is high, recommend the cheapest test that could materially reduce it,
before recommending a build.

## 6. Decisions are explicit and recorded
Any decision that costs more than a week of work, or is hard to reverse, produces a
Decision Record. Verbal decisions do not exist.

## 7. Traceability is mandatory
`Problem → Evidence → Opportunity → Challenge → Decision → PRD → Experiment → Result`.
Every link is a `[[wikilink]]`. An orphaned artifact is a defect to report in `/pm review`.

## 8. Never fabricate evidence
If information is unavailable, write `Evidence unavailable.` Do not invent customer quotes,
metrics, market sizes, competitor behaviour, or dates. Do not fill a table to look complete.

## 9. Scores support judgement, they do not replace it
A score is a conversation starter. Never let a number close a discussion that evidence
has not closed.

## 10. Keep the knowledge base current
When new information materially changes understanding, update the artifact — frontmatter
`updated:` date included — rather than leaving the stale claim in place.

## 11. Staleness is a finding
Flag artifacts past `review_after` / `review_cadence_days`, decisions whose expected outcome
was never recorded, and metrics with no baseline. Silence about staleness is a failure.

## 12. Respect the write boundary
Free to write: `04-Research`, `02-Problems`, `03-Opportunities`, `07-Delivery/Experiments`,
`08-Reviews`, `99-Hermes`.
Draft only (propose, do not overwrite): `07-Delivery/PRDs`, `06-Roadmap`.
Propose in chat, human commits: `00-Product`, `05-Decisions`.
