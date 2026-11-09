# Versioning

This repository uses semantic versioning: `MAJOR.MINOR.PATCH`.

## What changes the version

| Change | Version |
|---|---|
| Breaking change to the folder model, frontmatter schema, ID contract, command surface, or artifact contract | **MAJOR** |
| New playbook, template set, command, dashboard, or operating guide | **MINOR** |
| Correction, link fix, wording change, or data refresh that does not change the contract | **PATCH** |

Before `1.0.0`, breaking changes may ship in a **MINOR** release. The changelog must say so.

## Release process

1. Update `VERSION`.
2. Move the relevant entries from `[Unreleased]` to the new version in `CHANGELOG.md`.
3. Commit both files.
4. Tag the commit:

   ```bash
   git tag -a vX.Y.Z -m "vX.Y.Z"
   git push origin main --tags
   ```

5. Create the GitHub release:

   ```bash
   gh release create vX.Y.Z --title "vX.Y.Z" --notes-file CHANGELOG.md
   ```

## Rules

- A tag is immutable. Never move or reuse a release tag.
- `VERSION` and the latest changelog entry must match.
- A release note must say what changed and what the reader must do.
- Do not tag uncommitted work.
- Do not version a single file change as a release; it is a commit until it changes the contract or ships a coherent slice.
