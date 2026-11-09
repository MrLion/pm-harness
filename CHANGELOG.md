# Changelog

All notable changes to this repository are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Repository copy of the agent layer under `agent/`: the `product-management` skill, its references
  and checker, and the `pm` bundle template.

### Changed

- Reworked the HDHP imaging worked example: corrected the problem statement, added a buyer and
  journey-map view, separated coverage from patient outcome, made the release conditional, and
  aligned the compliance scenario across templates.
- Closed the peer-review gaps: labeled the survey-to-segment transfer, separated comprehension from
  prediction, added decision follow-up for non-bookers, and specified 8–10 recent booking journeys
  as the next evidence.
- Kept survey percentages out of the problem statement and defined the prediction capture point:
  expected dollar amount before booking, compared with final responsibility after adjudication.
- Made the README, Agent Manual, and Architecture platform-neutral: documented nested, root, and
  renamed vault layouts, Dataview prefix choices, and normal `.git` behavior outside the maintainer's
  macOS/iCloud setup.

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
