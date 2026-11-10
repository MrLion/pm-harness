# Scenario sourcing for template examples

Use when the user gives a research document, report, URL, or dataset and asks for examples or
scenarios to populate templates.

## Workflow

1. Extract candidate problems first; do not touch templates yet.
2. Grep the source for pain-point nouns — cost, wait, confusion, friction, debt, avoidance,
   switching, paperwork, authorization, coordination, self-service.
3. For each candidate problem, capture:
   - *Who experiences it* — narrow segment, not "consumers"
   - *What breaks* — the observable failure or friction
   - *Evidence* — exact number, quote, or direct claim with source/date
   - *Why it matters* — the consequence if it persists
4. Present the candidates as a numbered menu. The user chooses before any template is filled.
5. If the user asks for **one coherent scenario across all templates**, use the chosen candidate as
   the single running example throughout the artifact chain. Put the unchosen candidates on a
   separate future-problems page, not inside the templates.
6. Fill only the chosen paths, one artifact at a time.

## Example placement rule

- Keep the **primary chosen scenario** consistently represented in each relevant artifact template
  when the user asks for one scenario across the set.
- Keep **uncandidate scenarios** on a separate future-problems page. Do not cram each template with
  multiple examples or generic filler.
- Use **one artifact-specific example per template**, built from the same coherent scenario, and
  pair it with a short field-by-field guide only for that artifact's genuinely ambiguous fields.
- Do **not** paste a generic "ambiguous fields" table into every template — that turns the example
  set into filler rather than a coherent case.
- Label the example as illustrative, never as product evidence.
- Do not paste research numbers into real artifact notes unless they are the product's own data or
  explicitly cited as external context.
- Before committing the scenario, verify that the chain is coherent: the problem, the evidence, the
  experiment, the metric and the decision must point at the same journey, not a generic market fact.

## Case spine and completeness

- Give the worked example one `case_id` (for example `CASE-001`) in `00-Product/Scenario.md` and in
every prefilled product template. `_Templates.md` names the case spine. A template with an example
but no `case_id` is an orphaned fragment, not part of the case.
- When the buyer is unresolved, add a buyer/payer persona marked `confidence: none` and
  `evidence_count: 0`. Do not let the PRD, roadmap, or release imply a buyer that the decision
  record has not named.
- For any booking, payment, or service case, add a journey map under `01-Users/Journey-Maps/`. It is
  a view: stages, actor, touchpoint, pain, evidence, and links to Problems and Opportunities. It is
  not evidence and must not be the only place a problem exists.
- Put a short glossary in the scenario for role terms that drift: patient, member, buyer, user,
  estimate, patient responsibility. Use those terms consistently across templates.

## Pre-filled templates vs example callouts

- "Pre-fill the templates" means fill the template body: replace every `[FILL]` with scenario data.
  An example callout above a blank template is not a pre-filled template.
- Fill the real templates in `99-Playbook/Templates/` in place. Do not create a separate
  `Pre-filled/` folder — the user expects the templates themselves to change.
- Keep each template's frontmatter `type:` and section headings unchanged so it still renders and
  remains query-compatible.
- Verify with `grep -RIn '\[FILL' 99-Playbook/Templates`; expect zero hits in the prefilled product-lifecycle set. Operating-model and compliance templates intentionally keep `[FILL]` prompts and are excluded from that check.
- Run the wikilink audit after pre-filling. Every `[[ID]]` link, including frontmatter links, must
  resolve to an existing note inside the vault; unresolved links create empty notes in Obsidian.

## Source handling

- Prefer sources local to the user's market or geography. In the Americas, use US-centred sources
  by default; do not substitute another country's scenario unless the user asks.
- Distinguish **source of problem** (research, report, user signal) from **product artifact**
  (problem note, opportunity note, experiment, PRD). Research content belongs in research and
  examples, not in product artifacts.
- If a claim has no number, quote, or direct observation behind it, mark it as an assumption.
- A report cited only inside a template is not a source in the live vault. Create a
  `04-Research/RESEARCH-NNN-<slug>.md` note with the `source:` URL, reliability, and `updated:` date,
  then link it from every evidence row that uses it. A publisher name alone is a provenance gap,
  not a citation.

## Propagation and consistency checklist

After the central scenario is written, make every template example obey it. A correct scenario page
plus a contradictory example is still a failed example pass.

- **Evidence wording:** copy the exact claim and preserve its status. If the source says respondents
  *would consider* postponing, do not write that they *do postpone*; label stated intent separately
  from observed behaviour. Attach population, denominator, date, and source to every number.
- **Provenance labels:** a paraphrase is never `Verbatim`. A single illustrative account is not a
  recurring complaint; do not claim frequency without a count and source trail.
- **Experiment scope:** the hypothesis, design, success/failure criteria and what the experiment
  does *not* test must match. Comprehension interviews cannot prove reduced postponement; call the
  behavioural pilot a separate experiment. Make success and failure criteria exhaustive, so no
  outcome is left unclassified.
- **Metric definition:** define the unit (patients vs events), eligibility, window, source of truth,
  reconciliation rule, and error tolerance. Do not define a North Star as a count of actions when the
  claimed value is a better patient decision. A guardrail needs a threshold, not just a direction.
- **Decision honesty:** an example may show a gate, not a foregone build. Compare build, partner and
  defer when data ownership, buyer, estimate accuracy or implementation cost are unresolved.
- **Evidence-to-problem wording:** if the source says a share of users already receive the artifact,
  do not write that users "cannot" get it. Write the precise failure — coverage and accuracy are
  uneven — and split the segment by whether they received it and whether it was accurate.
- **Coverage vs outcome:** a coverage metric is a leading metric, not a North Star. Pair it with an
  outcome metric (for example, whether the patient can predict final responsibility within tolerance)
  and propagate both through Goals, PRD, roadmap, release, and review. A coverage metric can rise
  while the customer outcome does not move.
- **Release status follows the decision:** if the decision is `defer`/`no-go`, or the buyer is
  unresolved, the release record is `conditional`, not `planned`. Add the gate, named owners, and a
  simulated/pending review. Do not imply a scheduled launch behind an open gate.
- **Decision options include status quo:** compare build, partner, defer, and do-nothing. Status quo
  is the baseline the other options must beat, not a neutral default.
- **Scope consistency:** use one journey and one procedure name across the chain (for example, avoid
  switching from outpatient imaging to colonoscopy). A capability deferred in Release must not appear
  in the initial roadmap release; align PRD, Roadmap and Release feature scope explicitly.
- **Final sweep:** grep the templates for the old claim, the old procedure name, the old metric, and
  the old release scope. Fix every hit before committing or reporting completion.

## Worked-case review: measurement and rehearsal traps

Run these checks before calling a multi-template case coherent. A case can be internally consistent
and still measure the wrong population or the wrong outcome.

1. **Survey-to-segment transfer.** If the source surveys a broad consumer or patient population and
the case names a narrower segment, label the transfer explicitly. State that the figures are a reason
to investigate, not a segment estimate, and that frequency and accuracy in the segment are unknown.
   Close the gap with recent journeys from that segment, including people who did not complete the
   action — for a booking case, 8–10 journeys with at least 4 non-bookers. Record the information
   available at the decision point, the action taken, whether the artifact changed the choice, and
   the driver (uncertainty, affordability, network, urgency, or another reason). Do not present the
   broader survey as segment evidence.

2. **Comprehension vs prediction.** A comprehension test asks whether someone can explain
   inclusions, exclusions, and validity. Prediction asks whether they can forecast the final amount.
   A patient can understand an estimate perfectly and still receive a materially different bill.
   Keep comprehension as the prototype result; measure prediction in a pilot with reconciled bills.
   In the review, label the prediction row as a pilot metric and state that the formative test did
   not measure it. Do not set a four-of-five prediction target on a five-person comprehension study.

3. **Denominator bias against non-bookers.** Coverage counts who saw the estimate; reconciliation
   counts people who eventually received a bill. Both miss people who switched, deferred, or never
   booked. Add a short decision follow-up for everyone who received an estimate, reported separately
   from reconciliation: action taken, whether the estimate informed the choice, and what drove it.
   State the denominator explicitly: prediction accuracy is among reconciled estimates; decision
   follow-up is among all estimate recipients. Without that split, the case can look successful while
   the people most affected are invisible.

4. **Prediction capture timing.** Record the patient's expected dollar amount before booking, after
   the estimate is shown, and before any bill or EOB is visible. Compare it with final responsibility
   after claim adjudication. Do not ask after the bill; that measures recall, not prediction. State
   the capture point in the metric, PRD, and review so the pilot cannot drift.

5. **Synthetic rehearsal.** A mock interview set is a rehearsal, not evidence. Keep it in
   `99-Playbook/Templates/`, mark it `synthetic` with `confidence: none`, link it to the capture form,
   and keep the live decision `Pending` or `defer`. Use it to expose failure modes and derive the exact
   next-test prompt. For example, if participants cannot tell what an estimate covers, add a
   missing-charge probe to the comprehension test. Never let the rehearsal update `actual_outcome` or
   change the decision.
