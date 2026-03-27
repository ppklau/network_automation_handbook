# 12 — Security & Compliance Automation

## Purpose

For regulated industries — financial services, healthcare, critical infrastructure — compliance automation is often where the business case is clearest. This chapter shows how to embed security and compliance into the automation pipeline rather than bolting it on after the fact.

## Audience

- **Primary:** Network Architects, Security Engineers, Compliance Officers
- **Secondary:** Infrastructure Leaders (for regulatory justification)

## Content Outline

### Security Policy as Code
- ACLs, firewall rules, and segmentation policies defined in version control
- Policy definitions as structured data (YAML), not device CLI
- Template-driven policy rendering across multi-vendor environments
- Intent annotations linking every policy to a business or regulatory requirement

### Automated Compliance Checks in CI/CD
- Compliance assertions as pipeline stages
- Example checks: no permit-any ACLs, default-deny enforced, management plane isolated
- SoT-level structural checks (fast, sub-second)
- Batfish-level behavioural checks (reachability, policy enforcement)
- JUnit XML reporting for pipeline integration

### Audit Trail Generation
- Git history as the immutable audit trail
- Pipeline artefacts as compliance evidence
- Every change traceable: who proposed it, what tests passed, who approved it, when it deployed
- No retrospective documentation — the audit trail is a natural by-product of the workflow

### The Traceability Chain
- From business/regulatory requirement → design intent → device configuration
- REQ-SEC-01 (FCA/MiFID II) → INTENT-SEG-01 (VRF segmentation) → nodes.yml → device config
- ACL comments carry requirement IDs into the running configuration
- Machine-readable, queryable, testable at every link
- Extends: Encoding Intent (IBN Part 2)

### Regulatory Alignment Patterns
- Financial services: MiFID II, FCA SYSC, PCI-DSS
- Patterns applicable to any regulated environment
- How to structure requirements.yml for regulatory traceability

### Drift Detection and Compliance Remediation
- Detect when a device configuration diverges from compliant state
- Automated remediation for policy violations
- Compliance drift treated as a security event

## Cross-References

- [06 — Architecture Patterns](../06-architecture-patterns/) — intent-based traceability architecture
- [07 — CI/CD Pipelines](../07-implementation-guides/ci-cd-pipelines/) — pipeline stages for compliance
- [11 — Intent-Based Networking](../11-advanced-topics/intent-based-networking/) — the full traceability model
- [02 — Business Alignment](../02-business-alignment/) — compliance as a business case

## Source Articles

- Encoding Intent (Part 2) — ACL traceability, requirement annotations
- The Self-Provisioning Network (Part 3) — verification pipeline

## Status

`draft` — content to be developed
