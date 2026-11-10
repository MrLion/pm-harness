---
type: compliance-scope
project: pm-harness
artifact: compliance-scope
id: COMP-003
scope: product
status: draft
confidence: none
data_classification: unsure
jurisdiction: unsure
owner: Unassigned
updated: 2026-11-09
framework: "HIPAA + privacy/security compliance"
source: "https://www.hhs.gov/hipaa/for-professionals/covered-entities"
related:
  - "[DATA-001](../99-Playbook/Templates/Compliance/DATA-001-Data-Inventory.md)"
  - "[RISK-001](../99-Playbook/Templates/Compliance/RISK-001-Privacy-Security-Risk.md)"
---

# Compliance Scope — live

> [!WARNING] Gate open
> This scope is not decided. Do not handle PII, PHI, ePHI, or vendor data until the classification is resolved and a named owner signs off.

## 1. Product and role

| Field | Answer |
|---|---|
| Product | Unknown — product definition not supplied |
| Business unit | Unknown — unresolved |
| Are we a covered entity? | unsure |
| Are we a business associate? | unsure |
| Who is the covered entity or customer? | Unknown — unresolved |
| Who is the compliance owner? | Unassigned |

## 2. Data classification

| Data type | In scope? | Evidence |
|---|---|---|
| PII | unsure | No data inventory yet |
| PHI | unsure | No data inventory yet |
| ePHI | unsure | No data inventory yet |
| De-identified data | unsure | No method selected |
| Limited data set | unsure | No method selected |
| Consumer health data outside HIPAA | unsure | No jurisdiction analysis |

## 3. Regulatory classification

| Question | Answer |
|---|---|
| Is the product a medical device or SaMD? | unsure |
| Does ISO 13485 / QMS apply? | unsure |
| Which jurisdictions apply? | Unknown — unresolved |
| Which state privacy laws apply? | Unknown — unresolved |
| Which contractual obligations apply? | Unknown — unresolved |

## 4. Obligations

| Obligation | Applies? | Owner | Evidence |
|---|---|---|---|
| BAA required | unsure | Unassigned | No vendor register |
| HIPAA risk analysis required | unsure | Unassigned | No risk assessment |
| Privacy notice or authorization | unsure | Unassigned | No privacy review |
| Breach notification process | unsure | Unassigned | No incident plan |
| De-identification method | unsure | Unassigned | No method selected |
| Data retention / destruction | unsure | Unassigned | No retention policy |
| Device QMS / design controls | unsure | Unassigned | No classification |

## 5. Decision

**Stop and escalate.** Do not proceed with health-data handling until the role, data classification,
jurisdictions, and a named compliance owner are resolved.

## Checklist

- [ ] Role and data classification are explicit
- [ ] BAA need is resolved
- [ ] Medical-device classification is resolved
- [ ] Jurisdictions and state laws are listed
- [ ] Every obligation has an owner
- [ ] Unknowns are marked `unsure`, not guessed
