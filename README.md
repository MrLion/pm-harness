# Hermes-PM

The product brain, in plain Markdown. Obsidian is the UI, Hermes is the reasoning layer,
git is the audit trail.

## Structure

```
00-Product/      the current truth about the product (scaffold until filled)
01-Users/        personas, jobs-to-be-done, raw feedback
02-Problems/     PROB-NNN — who hurts, how often, what it costs
03-Opportunities/ OPP-NNN + Discovery Map — assessments and the Opportunity Solution Tree
04-Research/     market · competitors · users · data
05-Decisions/    DEC-NNN — options, tradeoffs, outcome, review date
06-Roadmap/      Now / Next / Later
07-Delivery/     PRDs · Experiments · Releases
08-Reviews/      YYYY-MM — what we said, what happened, what we learned
99-Hermes/       Rules.md (the law) · PM.md (agent brief) · Templates/
Dashboard.md     live cockpit (Dataview)
```

## Commands

| Command | Does |
|---|---|
| `/pm status` | health, top problems/opportunities, stale items, one recommended action |
| `/pm discover [query]` | find problems from vault + web + GitHub, write PROB notes |
| `/pm analyze <ID>` | evidence audit, impact, alternatives, risks, unknown, cheapest experiment |
| `/pm challenge <ID>` | adversarial review, written into the note |
| `/pm prd <ID>` | PRD draft — refuses if validation gate unmet |
| `/pm decide <question>` | decision record, proposed not accepted |
| `/pm review` | vault-wide audit: stale, orphaned, unsupported, contradictions, unrecorded outcomes |

## Where this vault sits

`PM vault` is a **folder inside the iCloud `Documents` Obsidian vault**, not a vault of its own.
That matters for Dataview:

- The plugin is installed and enabled in the **parent** vault (`Documents/.obsidian/plugins/dataview/`).
- Every query therefore references the folder path: `FROM "PM vault/02-Problems"`.
- `PM vault/.obsidian/` is inert — Obsidian ignores a nested folder's config. It stays on disk for
  possible future standalone use but is **not tracked in git**. If you convert modes, every `FROM`
  must lose its `PM vault/` prefix again.

Trade-off accepted: one vault, one plugin install, one trust prompt — at the cost of PM notes
sharing a graph and search index with whatever else lives in `Documents`.

## Frameworks

Templates are not invented. Each quotes a published method's structure and checklist, with attribution:

| Layer | Method | Artifacts |
|---|---|---|
| What we're building, and how we plan it | **Roman Pichler** (*Strategize*) | Product Vision Board · strategy elements · goal-setting · KPI selection · **GO Product Roadmap** · persona · Product Canvas |
| Should we build it, and what will kill it | **SVPG / Marty Cagan** (*Inspired*) | **Product Opportunity Assessment** (ten questions) · **four big risks** (value, usability, feasibility, business viability) · prototype over PRD |

Pichler alone assumes the opportunity is sound. Cagan alone refuses to plan. The vault uses
Pichler for artifacts that survive quarters, SVPG for the gate that stops you building the wrong
thing. Every template carries a collapsible fictional worked example ("Lantern", a clinic
scheduling tool) so the shape is obvious.

Additional layers: **Opportunity Solution Trees** link goals → problems → opportunities →
solutions → experiments; **Impact Mapping** makes goal → actor → behaviour change → deliverable
explicit; **OKRs** give each horizon one Objective with measurable Key Results; **North Star**
adds one customer-value metric with inputs and guardrails.

Pichler material is quoted under **CC BY-SA 4.0** — see `99-Hermes/Templates/_Templates.md`.

## The loop

```
discover → problem → evidence → opportunity → challenge
                                   ├── uncertain → experiment ──┐
                                   └── confident → decision ───┤
                                                               ▼
                                       PRD → delivery → metrics → learn → review ↺
```
No step is skippable. `99-Hermes/Rules.md` §3 and §7 enforce it.

## First run

1. Open the parent iCloud `Documents` vault in Obsidian — `PM vault` stays a folder inside it.
2. Settings → Community plugins → enable **Dataview** in that parent vault.
3. Open `PM vault/Dashboard.md` — the tables populate from frontmatter as notes land.
4. Fill `00-Product/Product.md`. While `confidence: none`, `/pm` blocks strategic recommendations,
   roadmap commitments, decisions and PRDs, but still permits research, discovery, opportunity
   drafts, experiments and challenge reviews.

## Git

Every artifact is a diff. `git log -p 00-Product/` answers "what changed in my strategy, and when".
Agent writes are reviewable, revertable, and attributable.

**The git directory lives outside iCloud** — at `~/Documents/pm-vault-git`. `.git` in this folder is a
one-line pointer file. This is deliberate: iCloud syncing git internals across devices corrupts
object databases and collides indexes. Notes sync via iCloud; history stays on the Mac, safe.

Never `git init` here again, never move the git dir into iCloud, and never clone this vault —
it would create a second, diverging history.
