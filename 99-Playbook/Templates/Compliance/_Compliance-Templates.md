# Compliance Templates — Tier 1

Baseline health-data compliance for products touching PII, PHI, ePHI, or consumer health data.

> This is not legal advice. Resolve scope with counsel or a qualified compliance owner.

| Template | Use for |
|---|---|
| [[COMP-001-Compliance-Scope\|COMP-001]] | Role, data classification, jurisdictions, obligations |
| [[DATA-001-Data-Inventory\|DATA-001]] | Data elements, purpose, PHI status, retention, vendors |
| [[RISK-001-Privacy-Security-Risk\|RISK-001]] | HIPAA-style privacy and security risk assessment |
| [[CTRL-001-Control-Matrix\|CTRL-001]] | Administrative, physical, and technical safeguards |
| [[VEND-001-Vendor-BAA-Register\|VEND-001]] | Vendor PHI access, BAA status, termination obligations |
| [[INC-001-Incident-Breach-Response\|INC-001]] | Incident, containment, breach assessment, notification |
| [[COMP-002-Compliance-Review\|COMP-002]] | Audit findings, control effectiveness, CAPA |

## Flow

`Scope → Data inventory → Risk assessment → Control matrix → Vendor/BAA → Incident readiness → Review`

Compliance is a rail across every playbook. It is not a fifth product loop.

## Tier boundary

- **Tier 1:** HIPAA / PII / PHI / ePHI / BAAs / security risk / controls / incidents.
- **Tier 2:** medical-device QMS, ISO 13485, ISO 14971, IEC 62304, IEC 62366. Add only when the product is a medical device or SaMD.
