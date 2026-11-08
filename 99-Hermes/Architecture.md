# Architecture

Technical reference for agents and advanced users. Start with `README.md` or [[START-HERE]] for
ordinary use.

## Vault mode

`PM vault` is a **folder inside the registered iCloud `Documents` Obsidian vault**, not a
standalone vault.

- Dataview is installed and enabled in `Documents/.obsidian/plugins/dataview/`.
- A nested `PM vault/.obsidian/` is ignored by Obsidian and is not tracked in git.
- Every Dataview source includes the folder prefix: `FROM "PM vault/02-Problems"`.
- Do not register the folder as a separate vault merely to fix empty tables. Convert modes only
  deliberately; doing so requires removing the prefix from every query.

## Frontmatter is the data layer

Dataview reads YAML frontmatter, not headings:

- `TABLE status, date` renders those frontmatter keys as columns.
- `WHERE type = "decision"` filters on `type:`.
- `SORT date DESC` uses the frontmatter `date:`, not file modification time.
- Missing keys produce blank columns; wrong `type` values make notes invisible to queries.

Copy template frontmatter verbatim. The schema contract is in [[_Templates]].

## Identity and traceability

Allocate IDs by scanning the target folder, taking the highest existing number, adding one and
zero-padding to three. Never reuse an ID. Link canonical artifacts with Obsidian internal links.

`Discovery Map.md` is an Opportunity Solution Tree **view** over Goals, Problems, Opportunities,
solution briefs and Experiments. It never replaces those notes.

## Git

The vault's `.git` is a pointer file to `~/Documents/pm-vault-git`, deliberately outside iCloud.
Notes sync through iCloud; git history remains on the Mac.

- Never move git internals into iCloud.
- Never `git init` or clone in this folder; that creates diverging history.
- Nested `.obsidian/` remains on disk but is ignored by git as inert machine-local state.
- Commits are local unless a remote is explicitly configured.

## Agent write boundaries

[[Rules]] §18 is authoritative:

- Free to write: Research, Problems, Opportunities, Experiments, Reviews, `99-Hermes/`.
- Draft only: solution briefs and Roadmap.
- Propose for human approval: Product strategy and Decisions.

Every material write updates `updated:` and leaves a reviewable git diff.

## Verification before declaring success

Check programmatically rather than relying on visible files:

1. All query sources have the correct `PM vault/` prefix.
2. Every queried column exists in the corresponding template schema.
3. `/pm` loads the `product-management` skill with the requested subcommand intact.
4. Wikilinks resolve, except documented placeholders.
5. `git status` is clean after an intentional commit.
