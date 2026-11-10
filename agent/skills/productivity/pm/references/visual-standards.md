# Playbook Visual Standards

Use when creating or revising PM-playbook infographics, decks, one-pagers, or per-playbook graphics.
The approved infographic is the canonical visual language; do not treat it as a starting mood board.

## What the visual must say

At a glance:

- There are two legitimate starting paths: vision-led `0→1` and outcome-led `1→N`.
- Both converge on one evidence question: **Do we know enough to commit?**
- Evidence produces three honest outcomes: run the next test, proceed to delivery and review, or stop/defer.
- The harness and operating model are support conditions, not extra steps in the main flow.

## Locked composition

1. **Two token-pill rows** in slim outline containers:
   - Vision-led `0→1`: Vision → Thesis → Concept test, copper.
   - Outcome-led `1→N`: Signal → Problem & evidence → Challenge, teal.
2. **One shared Evidence-gate box** in navy: “Do we know enough to commit?” Both rows feed it from the right margin.
3. **One fan-out to three outcome cards**:
   - Uncertain → Run the next test.
   - Proceed → Deliver → Review.
   - No-go → Defer or stop.
4. **Demoted footer strip**: harness (`Obsidian · Evidence`, `/pm · Reasoning`, `Git · Audit trail`) and operating model (`Digital transformation vs Project-to-product`).

## Discipline

- Keep the main flow at roughly twelve elements maximum.
- All text stays inside containers; nothing floats.
- No crossing lines.
- If a variant needs more detail, extend the footer. Do not add elements to the main flow.
- Do not generate dense labels or links with an image model; use deterministic SVG/HTML layout and reserve image generation for non-textual art.

## Production route

The approved asset set lives in `99-Playbook/Visuals/`:

- `playbook_v8.png` — approved render
- `playbook_v8.svg` — editable source
- `playbook_min_source.svg` — build-name source
- `build_infographic_min.py` — deterministic SVG generator

Future variants are token swaps in the generator, not redraws. Preserve the hierarchy: two starting paths → shared evidence gate → three outcomes → demoted footer.
