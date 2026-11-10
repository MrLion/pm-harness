# Changelog

All notable changes to this repository are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Repository copy of the agent layer under `agent/`: the `pm` skill, its references and checker, and
  the `pm` bundle template.
- `scripts/validate_vault.py`, a contract validator for Markdown links and anchors, frontmatter, IDs,
  filename/ID consistency, product-template fill markers, open gates, and overdue decisions.
- GitHub Actions validation on every push and pull request.
- `scripts/install_agent_layer.py`, which installs the skill and writes the absolute vault path into
  `pm.yaml`, plus `scripts/requirements.txt` for its PyYAML dependency.
- `examples/vertical-slice/`, a synthetic end-to-end fixture from product to review.
- `LICENSE` (MIT) and `NOTICE` separating MIT from CC BY-SA 4.0 content.

### Changed

- Reworked the HDHP imaging worked example: corrected the problem statement, added a buyer and
  journey-map view, separated coverage from patient outcome, made the release conditional, and
  aligned the compliance scenario across templates.
- Closed the peer-review gaps: labeled the survey-to-segment transfer, separated comprehension from
  prediction, added decision follow-up for non-bookers, and specified 8–10 recent booking journeys
  as the next evidence.
- Kept survey percentages out of the problem statement and defined the prediction capture point:
  expected dollar amount before booking, compared with final responsibility after adjudication.
- Added a synthetic eight-journey interview rehearsal and linked it to the problem, opportunity,
  and decision records without treating it as evidence.
- Added the missing-charge probe to `EXP-001`, so the comprehension test can find whether an
  estimate’s scope is clear enough to be usable.
- Made the README, Agent Manual, and Architecture platform-neutral: documented nested, root, and
  renamed vault layouts, Dataview prefix choices, and normal `.git` behavior outside the maintainer's
  macOS/iCloud setup.
- Hardened the installer: it validates the source bundle before copying, refuses to overwrite an
  existing skill or `pm.yaml`, and requires `--update` for replacement.
- Added a `project: pm-harness` marker to every artifact and constrained all Dashboard queries to it,
  so a shared Obsidian vault cannot leak sibling `type:` notes into the PM tables.
- Extended the validator to reject impossible calendar dates and to require a named owner, data
  classification, and jurisdiction on any `approved` or `active` compliance scope.
- Added the worked example to CI as a second validation step.
- Removed the last folder-scoped `FROM "PM vault/..."` queries from the index pages; they now use
  `FROM ""` with a folder filter and the `project` marker.
- Renamed the skill to `pm`, so `/pm` is one command on both surfaces: the desktop gateway resolves
  the skill, and the classic CLI resolves the bundle.

## [0.1.0] - 2026-11-09

### Added

- Obsidian-based product-management harness with folders `00-Product` through `11-Compliance` and
  `99-Playbook`.
- Four playbooks: Vision-led 0→1, Outcome-led 1→N, Digital Transformation, and Project-to-Product.
- Tier 1 health-data compliance rail with scope, data inventory, risk, controls, vendor/BAA, incident,
  and review templates.
- Product, operating-model, and compliance template sets.
- Canonical discovery-to-delivery chain with transition gates in `99-Playbook/Discovery-to-Delivery.md`.
- Agent setup and operating manual, guided walkthrough, and value estimate.
- Dataview dashboard and folder indexes.
- GitHub-compatible relative Markdown links.

### Changed

- Consolidated the product traceability chain into one canonical document.
- Reduced duplicated gate and permission language across `PM`, `Rules`, and `Architecture`.
- Converted Obsidian wikilinks to relative Markdown links for GitHub rendering.
- Updated the harness value estimate to a 40-hour week with team-count sensitivity.

### Fixed

- Corrected the agent permission ladder so decision records remain human-approved.
- Replaced the blank compliance template gate with a live compliance-scope gate.
- Corrected stale template references and missing source citations.
