# Compliance Layer — Tier 1 and Tier 2

Use when the playbook or a product artifact touches PII, PHI, ePHI, vendor data, or a regulated medical device. This is scoping guidance, not legal advice.

## Core boundary

- **HIPAA applies by role and data**, not by product category. Covered entities are health plans, clearinghouses, and qualifying providers; business associates are vendors acting for them. A consumer app outside those roles may still face FTC or state health-privacy rules.
- **PII** is a broad term with no single federal definition. **PHI** is individually identifiable health information held or transmitted by a covered entity or business associate. **ePHI** is electronic PHI.
- **BAA** is required before a vendor creates, receives, maintains, or transmits PHI for a covered entity or another business associate. Cloud vendors are business associates even when they cannot decrypt the data.
- **HIPAA Security Rule:** documented risk analysis and risk management; administrative, physical, and technical safeguards; incident procedures; contingency planning; evaluation; six-year documentation retention.
- **De-identification:** Safe Harbor removes all 18 identifier categories; Expert Determination requires a qualified expert and documented methods. A limited data set remains PHI and requires a data use agreement.
- **ISO 13485** is a medical-device QMS standard, not a privacy standard. FDA's QMSR became effective February 2, 2026 and incorporates ISO 13485:2016. For a device or SaMD, also consider ISO 14971, IEC 62304, IEC 62366, and FDA software/cybersecurity guidance.
- **Do not apply ISO 13485 to a non-device product** merely because it is health-related. Classify first.

## Tier 1 — baseline health-data compliance

Live folder: `11-Compliance/`

Templates: `99-Playbook/Templates/Compliance/`

| Template | Purpose |
|---|---|
| `COMP-001-Compliance-Scope` | Role, data classification, jurisdictions, obligations, owners |
| `DATA-001-Data-Inventory` | Data elements, purpose, PHI status, minimum necessary, retention, vendors |
| `RISK-001-Privacy-Security-Risk` | HIPAA-style privacy and security risk assessment |
| `CTRL-001-Control-Matrix` | Administrative, physical, and technical safeguards |
| `VEND-001-Vendor-BAA-Register` | Vendor PHI access, BAA status, termination obligations |
| `INC-001-Incident-Breach-Response` | Incident, containment, breach assessment, notification |
| `COMP-002-Compliance-Review` | Audit findings, control effectiveness, CAPA |

Flow: `Scope → Data inventory → Risk → Controls → Vendor/BAA → Incident readiness → Review`.

Compliance is a rail across every playbook, not a fifth product loop. Start with the **live**
compliance scope in `11-Compliance/` before discovery if the work touches PHI/PII. `COMP-001` in
`99-Playbook/Templates/Compliance/` is the structure-only template; do not use it as the gate.

## The gate is a live note

A compliance scope passes only when `11-Compliance/` contains a product-specific scope with:

- `status: approved` or `active`
- resolved PII / PHI / ePHI / de-identified status
- resolved covered-entity or business-associate role
- listed jurisdictions and state privacy laws
- a named compliance owner

`draft`, `owner: Unassigned`, `unsure` classification, or an unfilled decision is a stop condition:
do not handle PII/PHI/ePHI or vendor data. Allocate the next live `COMP-NNN` rather than reusing the
template's `COMP-001` ID.

A template-presence check is not a gate. Architecture verification must inspect the live note's
status, classification, jurisdiction, and owner.

## Where to integrate

- **START-HERE:** add the compliance-scope gate before problem capture when PII/PHI/ePHI or vendor data is involved.
- **Opportunity:** add compliance feasibility separately from the four SVPG risks.
- **PRD:** compliance impact, data used, PHI status, controls, approvals, retention.
- **Experiment:** real PHI vs synthetic/de-identified data, BAA, storage, retention, destruction.
- **Decision:** regulatory/compliance risk as an explicit criterion.
- **Release:** compliance sign-off and incident readiness.
- **Review:** incidents, audit findings, access reviews, vendor/BAA status, corrective actions.
- **Dashboard/Rules/Architecture:** include `11-Compliance` in navigation, maintenance queries, and write boundaries.

## Tier 2 — medical-device QMS overlay

Only after the scope gate confirms a medical device or SaMD.

Add design-control traceability, ISO 14971 risk-management file, IEC 62304 software lifecycle evidence, IEC 62366 usability evidence, and CAPA/post-market review. Do not mix Tier 2 artifacts into Tier 1 templates.

## Sources

- HHS covered entities: https://www.hhs.gov/hipaa/for-professionals/covered-entities
- HHS business associates: https://hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates
- HHS Security Rule: https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html
- HHS risk analysis: https://www.hhs.gov/hipaa/for-professionals/security/guidance/guidance-risk-analysis/index.html
- De-identification: https://ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514
- FDA QMSR: https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr
- ISO 13485: https://www.iso.org/standard/13485
- ISO 14971: https://www.iso.org/standard/72704.html
- FDA SaMD: https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd
