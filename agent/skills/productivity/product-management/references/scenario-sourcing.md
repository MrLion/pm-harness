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
- **Scope consistency:** use one journey and one procedure name across the chain (for example, avoid
  switching from outpatient imaging to colonoscopy). A capability deferred in Release must not appear
  in the initial roadmap release; align PRD, Roadmap and Release feature scope explicitly.
- **Final sweep:** grep the templates for the old claim, the old procedure name, the old metric, and
  the old release scope. Fix every hit before committing or reporting completion.
